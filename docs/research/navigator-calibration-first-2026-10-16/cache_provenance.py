import os
from pathlib import Path
"""Bind private signal caches to raw inputs, extraction code and payload digest."""
import hashlib, json

def _metadata(path):
    return path.with_suffix(path.suffix + '.provenance.json')

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def cache_valid(path, expected):
    try:
        meta = json.loads(_metadata(path).read_text())
        return meta['inputs'] == expected and meta['payload_sha256'] == digest(path)
    except (OSError, ValueError, KeyError, TypeError):
        return False

def seal_cache(path, expected):
    target = _metadata(path)
    temporary = target.with_suffix(target.suffix + '.tmp')
    temporary.write_text(json.dumps({'inputs': expected, 'payload_sha256': digest(path)}, indent=2) + '\n')
    temporary.replace(target)

def validate_staging(folder, files):
    expected = {f'segment-{i:03}' for i in range(len(files))}
    if {x.name for x in folder.iterdir()} != expected:
        raise ValueError('staging has unexpected segments')
    for i, source in enumerate(files):
        directory = folder / f'segment-{i:03}'
        target = directory / 'rlog.zst'
        if {x.name for x in directory.iterdir()} != {'rlog.zst'} or not target.is_symlink() or target.resolve() != source.resolve():
            raise ValueError('staging is not an exact expected raw link')
