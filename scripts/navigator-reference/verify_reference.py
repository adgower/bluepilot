"""Verify the public reference export without device access or private inputs."""
from pathlib import Path
import argparse,hashlib,json,re,subprocess,sys
from urllib.parse import unquote
ROOT=Path(__file__).resolve().parents[2]
META=ROOT/'docs/navigator-reference'
PATTERNS={
 'owner_home':r'/Users/[A-Za-z0-9_.-]+/',
 'private_host':r'\b(?:192\.168\.\d{1,3}\.\d{1,3}|10\.\d{1,3}\.\d{1,3}\.\d{1,3}|172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3})\b',
 'raw_route':r'\b[0-9a-f]{8}--[0-9a-f]{10}--\d+\b',
 'vehicle_id':r'\b(?=[A-HJ-NPR-Z0-9]{17}\b)(?=[A-HJ-NPR-Z0-9]*[A-HJ-NPR-Z])(?=[A-HJ-NPR-Z0-9]*\d)[A-HJ-NPR-Z0-9]{17}\b',
 'private_key':r'-----BEGIN (?:OPENSSH |RSA |EC |DSA )?PRIVATE KEY-----',
 'access_token':r'\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9_-]{20,})\b',
 'signed_token':r'eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{10,}',
 'private_chat':r'codex://threads/[0-9a-f]{8}-',
 'email_address':r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
 'precise_wall_timestamp':r'\b20\d{2}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}',
}
BANNED={'.npz','.pkl','.zst','.bundle','.so','.os','.o','.a','.mp4','.hevc','.png','.jpg','.jpeg','.tar','.gz','.jsonl','.csv','.xml','.pyc'}

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def git(*args):return subprocess.check_output(['git','-C',str(ROOT),*args],text=True).strip()
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--openpilot-root',type=Path);ap.add_argument('--staged',action='store_true');args=ap.parse_args()
 manifest=json.loads((META/'export-manifest.json').read_text());entries=manifest['files'];paths={e['path'] for e in entries}
 assert len(paths)==len(entries),'duplicate manifest path'
 errors=[];links=0;compiled=0
 for e in entries:
  rel=e['path'];p=ROOT/rel
  if not p.is_file():errors.append([rel,'missing']);continue
  if digest(p)!=e['published_sha256']:errors.append([rel,'hash mismatch'])
  if p.suffix in BANNED or p.stat().st_size>2_000_000:errors.append([rel,'excluded binary/data/large file'])
  try:text=p.read_text()
  except UnicodeDecodeError:errors.append([rel,'not UTF-8 text']);continue
  for reason,pattern in PATTERNS.items():
   if re.search(pattern,text):errors.append([rel,reason])
  if p.suffix=='.py':
   compile(text,rel,'exec');compiled+=1
  if p.suffix=='.md':
   for target in re.findall(r'\]\(([^)\n]+)\)',text):
    target=target.strip('<>')
    if target.startswith(('https://','http://','mailto:','#')):continue
    base=unquote(target.split('#',1)[0])
    if not base:continue
    if not (p.parent/base).exists():errors.append([rel,'missing local link: '+base])
    links+=1
 # The manifest itself is metadata, not a source/published self-hash cycle.
 allowed=paths|{'docs/navigator-reference/export-manifest.json'}
 changed=git('diff','--name-only','--cached' if args.staged else 'HEAD').splitlines()
 if args.staged:
  # Check actual index blobs, not only matching working-tree files.
  staged={}
  for record in subprocess.check_output(['git','-C',str(ROOT),'ls-files','--stage','-z']).split(b'\0'):
   if not record:continue
   metadata,path=record.split(b'\t',1);mode,oid,stage=metadata.decode().split()
   if stage=='0':staged[path.decode()]=(mode,oid)
  algorithm=git('rev-parse','--show-object-format')
  for rel in sorted(allowed):
   data=(ROOT/rel).read_bytes();blob=hashlib.new(algorithm,b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
   if rel not in staged or staged[rel][1]!=blob or staged[rel][0] not in ['100644','100755']:
    errors.append([rel,'staged blob/mode differs from reviewed file'])
 unknown=set(changed)-allowed
 if unknown:errors.extend([[p,'change outside curated manifest'] for p in sorted(unknown)])
 source_checked=False
 if args.openpilot_root:
  r=args.openpilot_root.resolve();rebuild=json.loads((META/'rebuild-manifest.json').read_text())
  for path,expected in [(r,rebuild['parent']['commit']),(r/'opendbc_repo',rebuild['opendbc']['commit'])]:
   actual=subprocess.check_output(['git','-C',str(path),'rev-parse','HEAD'],text=True).strip()
   if actual!=expected:errors.append(['source pair','commit mismatch'])
  for rel,h in rebuild['source_file_sha256'].items():
   if not (r/rel).is_file() or digest(r/rel)!=h:errors.append(['source pin',rel])
  source_checked=True
 result={'checks_passed':not errors,'curated_files':len(entries),'compiled_python_helpers':compiled,'local_links_checked':links,'source_pins_checked':source_checked,'errors':errors,'device_access':False,'scope':'Manifest, explicit privacy-pattern and link/source checks; not a controller build, replay, sanitizer or road-validation result.'}
 print(json.dumps(result,indent=2));raise SystemExit(0 if not errors else 1)

if __name__=='__main__':main()
