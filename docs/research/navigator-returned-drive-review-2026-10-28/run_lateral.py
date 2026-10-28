import os
from pathlib import Path
from pathlib import Path
import json, hashlib, subprocess
P = Path(__file__).resolve().parent
receipt = json.loads((P / 'acquisition-provenance.json').read_text())
B = Path(receipt['private_backup'])
manifest = json.loads((P / 'input-manifest.json').read_text())
V = str(Path(os.environ['OPENPILOT_ROOT']) / '.venv/bin/python')
assert receipt['segment_hashes_verified']
for drive in sorted({s['drive'] for s in manifest}):
    for s in [s for s in manifest if s['drive'] == drive]:
        f = B / 'recordings' / drive / f"segment-{s['segment']:03d}" / 'rlog.zst'
        with f.open('rb') as stream:
            assert hashlib.file_digest(stream, 'sha256').hexdigest() == s['sha256']
    subprocess.run([V, str(P / 'lateral/extract.py'), str(B / 'recordings' / drive), drive, str(P / 'lateral' / (drive + '-signals.json.zst'))], check=True)
subprocess.run([V, str(P / 'lateral/analyze.py')], check=True)
