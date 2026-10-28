"""Create a public reference export from local Navigator notes; no device access.
The original workspace is read-only. Exported text is deliberately redacted and
is not a byte-identical copy of frozen research evidence.
"""
from pathlib import Path
import argparse,ast,collections,hashlib,json,os,re
from urllib.parse import unquote,quote,urlsplit

ROOT_DOCS=['NAVIGATOR_TUNING_GUIDE.md','NAVIGATOR_DOCUMENTATION_AUDIT.md','NAVIGATOR_ROADMAP.md']
OFFLINE=[
 'navigator-returned-drive-review-2026-10-28/health_scan.py',
 'navigator-returned-drive-review-2026-10-28/launch_rpm_audit.py',
 'navigator-returned-drive-review-2026-10-28/run_lateral.py',
 'navigator-returned-drive-review-2026-10-28/longitudinal/extract.py',
 'navigator-returned-drive-review-2026-10-28/longitudinal/analyze.py',
 'navigator-returned-drive-review-2026-10-28/lateral/extract.py',
 'navigator-returned-drive-review-2026-10-28/lateral/analyze.py',
 'navigator-calibration-first-2026-10-16/normalize.py',
 'navigator-calibration-first-2026-10-16/dataset.py',
 'navigator-calibration-first-2026-10-16/estimator.py',
 'navigator-calibration-first-2026-10-16/cache_provenance.py',
 'navigator-postclear-rebraking-2026-10-28/policy.py',
 'navigator-postclear-rebraking-2026-10-28/prototype.py',
 'navigator-postclear-rebraking-2026-10-28/test_policy.py',
 'navigator-postclear-rebraking-2026-10-28/test_prototype.py',
 'navigator-postclear-rebraking-2026-10-28/braking_compare.py',
 'navigator-postclear-rebraking-2026-10-28/comparison_contract.py',
 'build_navigator_research_index.py',
]
VIN=r'\b(?=[A-HJ-NPR-Z0-9]{17}\b)(?=[A-HJ-NPR-Z0-9]*[A-HJ-NPR-Z])(?=[A-HJ-NPR-Z0-9]*\d)[A-HJ-NPR-Z0-9]{17}\b'
RULES=[
 ('private_key',r'-----BEGIN [A-Z ]*PRIVATE KEY-----[\s\S]*?-----END [A-Z ]*PRIVATE KEY-----','<redacted private key>'),
 ('credential',r'\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9_-]{20,})\b','<redacted token>'),
 ('jwt',r'eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{10,}','<redacted token>'),
 ('vehicle_identifier',VIN,'<redacted vehicle identifier>'),
 ('route_identifier',r'\b[0-9a-f]{8}--[0-9a-f]{10}--\d+\b','<private recording>'),
 ('chat_reference',r'codex://[^\s)>]+','<private chat reference>'),
 ('private_uuid',r'\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b','<private identifier>'),
 ('private_host',r'\b(?:192\.168\.\d{1,3}\.\d{1,3}|10\.\d{1,3}\.\d{1,3}\.\d{1,3}|172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3})\b','<private host>'),
 ('email',r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b','<redacted email>'),
 ('private_home',r'/Users/[^/\s`\"\x27)]+','${USER_HOME}'),
 ('private_cache',r'/private/(?:tmp|var/folders)/[^\s`\"\x27)<>]+','${PRIVATE_CACHE}'),
 ('wall_timestamp',r'\b20\d{2}-\d{2}-\d{2}[T ]\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?(?:Z|[+-]\d{2}:\d{2})?','<private wall-clock timestamp>'),
 ('clock_time',r'(?<![\w:])(?:[01]?\d|2[0-3]):[0-5]\d(?::[0-5]\d(?:\.\d+)?)?(?:\s?(?:a\.m\.|p\.m\.|AM|PM))?(?!\w)','<private clock time>'),
 ('identity_assignment',r'(?im)((?:dongle.?id|serial(?:.?number)?|ssid|password|access.?token|api.?key)\s*[=:]\s*)[\"\x27]?[A-Za-z0-9_+./=-]{8,}[\"\x27]?',r'\1<redacted>'),
 ('coordinate_assignment',r'(?i)((?:latitude|longitude|gps_lat|gps_lon)\s*[=:]\s*)-?\d+(?:\.\d+)?',r'\1<redacted>'),
 ('wall_clock_assignment',r'(?i)((?:wallTimeNanos|wall_time_ns|wall_time_nanos)\s*[=:]\s*)\d{10,}',r'\1<redacted>'),
]

def sha(data):return hashlib.sha256(data).hexdigest()
def sanitize(text,clocks=True):
 counts=collections.Counter()
 for name,pattern,replacement in RULES:
  if not clocks and name in ['clock_time','wall_timestamp']:continue
  text,n=re.subn(pattern,replacement,text);counts[name]+=n
 return text,{k:v for k,v in counts.items() if v}

def public_summary(value):
 # Keep only outcome scalars, never arbitrary traces, identities or private paths.
 out={}
 for k,v in value.items():
  if re.search(r'private|path|serial|vin|dongle|host|password|token|gps|latitude|longitude|wall|archive|backup|sha256|files',k,re.I):continue
  if isinstance(v,(bool,int,float)) or v is None:out[k]=v
  elif isinstance(v,str) and len(v)<500:out[k]=sanitize(v)[0]
 return {'curation_notice':'Selected scalar outcomes from the local verification receipt; not the full original artifact/hash manifest. Private originals and inputs are intentionally omitted.','outcomes':out}

class PortablePaths(ast.NodeTransformer):
 def visit_Constant(self,node):
  if not isinstance(node.value,str):return node
  value=node.value
  marker='/Apps/openpilot/.navigator-master-integration-20261014'
  if value.startswith('/Users/') and marker in value:
   suffix=value.split(marker,1)[1].lstrip('/')
   expr="str(Path(os.environ['OPENPILOT_ROOT'])"+(" / "+repr(suffix) if suffix else '')+")"
   return ast.copy_location(ast.parse(expr,mode='eval').body,node)
  if value.startswith('/Users/') and '/Apps/bluepilot' in value:
   suffix=value.split('/Apps/bluepilot',1)[1].lstrip('/')
   expr="str(Path(os.environ['BLUEPILOT_ROOT'])"+(" / "+repr(suffix) if suffix else '')+")"
   return ast.copy_location(ast.parse(expr,mode='eval').body,node)
  if value.startswith('/private/tmp/'):
   suffix=Path(value).name
   return ast.copy_location(ast.parse("str(Path(os.environ['NAVIGATOR_PRIVATE_CACHE']) / "+repr(suffix)+")",mode='eval').body,node)
  cleaned=sanitize(value,clocks=False)[0]
  return ast.copy_location(ast.Constant(cleaned),node)

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--source',type=Path,required=True);ap.add_argument('--destination',type=Path,required=True);a=ap.parse_args()
 src,dst=a.source.resolve(),a.destination.resolve();assert src!=dst and (dst/'.git').exists()
 documents=[src/n for n in ROOT_DOCS]+sorted((src/'docs/research').rglob('*.md'))+sorted((src/'docs/superpowers').rglob('*.md'))
 selected={p.relative_to(src).as_posix():p for p in documents}
 selected.update({'docs/research/'+name:src/'docs/research'/name for name in OFFLINE})
 summary_paths={}
 for f in sorted((src/'docs/research').rglob('VERIFICATION.json')):
  if f.stat().st_size>131072:continue
  try:value=json.loads(f.read_text())
  except (ValueError,UnicodeDecodeError):continue
  if not isinstance(value,dict):continue
  dest=f.parent.relative_to(src)/'PUBLIC_VERIFICATION.json';summary_paths[dest.as_posix()]=(f,public_summary(value))
 included=set(selected)|set(summary_paths)
 notice=dst/'docs/navigator-reference/PRIVATE_ARTIFACTS.md'
 entries=[];omitted_links=0
 for rel,p in selected.items():
  data=p.read_bytes();text=data.decode('utf-8');redactions={};link_changes=0
  if p.suffix=='.py':
   tree=PortablePaths().visit(ast.parse(text));ast.fix_missing_locations(tree)
   text=ast.unparse(tree)+'\n'
   # Path adapters use only explicit environment roots; do not connect anywhere.
   text='import os\nfrom pathlib import Path\n'+text
   compile(text,rel,'exec')
  else:
   text,redactions=sanitize(text)
   def replace(match):
    nonlocal link_changes,omitted_links
    label,target=match.group(1),match.group(2);image=label.startswith('!')
    original=target;target=target.strip('<>');base_target=unquote(target.split('#',1)[0])
    if target.startswith(('https://','http://','mailto:')):
     if '<' not in target and 'redacted' not in target and 'private' not in target:return match.group(0)
    elif not base_target:return match.group(0)
    else:
     resolved=(dst/rel).parent/base_target
     try:target_rel=resolved.resolve().relative_to(dst).as_posix()
     except ValueError:target_rel=None
     if target_rel in included:
      return match.group(0)
     if target_rel and target_rel.endswith('/VERIFICATION.json'):
      summary=target_rel.removesuffix('/VERIFICATION.json')+'/PUBLIC_VERIFICATION.json'
      if summary in included:
       link_changes+=1;return label+'('+quote(os.path.relpath(dst/summary,(dst/rel).parent),safe='/._-')+')'
     if target_rel and (dst/target_rel).is_file() and not target_rel.startswith(('docs/research/','docs/superpowers/')):return match.group(0)
    omitted_links+=1;link_changes+=1
    relative=quote(os.path.relpath(notice,(dst/rel).parent),safe='/._-')
    if image:return '[Private/local visualization omitted]('+relative+')'
    return label+'('+relative+')'
   # Include optional leading ! in the matched label for omitted images.
   text=re.sub(r'(!?\[[^\]\n]*\])\(([^)\n]+)\)',replace,text)
   text='<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->\n'+text
  out=dst/rel;out.parent.mkdir(parents=True,exist_ok=True);out.write_text(text)
  entries.append({'path':rel,'source_sha256':sha(data),'published_sha256':sha(text.encode()),'kind':'offline_helper' if p.suffix=='.py' else 'document','redactions':redactions,'artifact_link_rewrites':link_changes})
 for rel,(source,value) in summary_paths.items():
  out=dst/rel;out.parent.mkdir(parents=True,exist_ok=True);data=(json.dumps(value,indent=2)+'\n').encode();out.write_bytes(data)
  entries.append({'path':rel,'source_sha256':sha(source.read_bytes()),'published_sha256':sha(data),'kind':'curated_verification_summary'})
 provenance={'schema':1,'reference_date':'2026-10-28','scope':'Public, curated reference export. Source workspace remains unchanged. Redacted exports do not inherit original byte hashes or acceptance proofs.','counts':dict(collections.Counter(e['kind'] for e in entries)),'omitted_artifact_links':omitted_links,'excluded':'Original recordings, GPS/identity mappings, full parameter backups, credentials, raw traces/caches, datasets, binary/model/build/firmware artifacts, Git bundles, private archive paths, live SSH/activation/install scripts and bulk JSON/logs.','files':entries}
 out=dst/'docs/navigator-reference/export-manifest.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(provenance,indent=2)+'\n')
 print(json.dumps({k:v for k,v in provenance.items() if k!='files'},indent=2))

if __name__=='__main__':main()
