import os
from pathlib import Path
"""Catalog existing Markdown evidence only; never runs research/device scripts."""
from pathlib import Path
import argparse, datetime, hashlib, json, os, re
from urllib.parse import quote, unquote
from zoneinfo import ZoneInfo
ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'docs/research/NAVIGATOR_RESEARCH_INDEX.md'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--as-of', default=datetime.datetime.now(ZoneInfo('America/Chicago')).date().isoformat())
    args = parser.parse_args()
    date = datetime.date.fromisoformat(args.as_of)
    areas = [('Research evidence', ROOT / 'docs/research'), ('Designs and implementation plans', ROOT / 'docs/superpowers')]
    entries = []
    lines = ['# Navigator research and workflow catalog', '', f'Generated for {date.isoformat()}. This catalogs **all Markdown files currently present** under `docs/research` and `docs/superpowers`, excluding this generated index. It includes historical, rejected and superseded work; a catalog entry is not current acceptance, installation or physical validation.', '', '[Start with the tuning/workflow guide](../../NAVIGATOR_TUNING_GUIDE.md) · [Roadmap](../../NAVIGATOR_ROADMAP.md) · [Feature inventory](navigator-branch-feature-list.md) · [Documentation audit](../../NAVIGATOR_DOCUMENTATION_AUDIT.md)', '', 'The linked study folders also contain their available JSON receipts, manifests, hashes, scripts, tests and logs. Private originals/archives/caches are referenced by receipts and are not copied into this catalog. Public GitHub claims in old reports retain their original research date.', '', 'Refresh locally with `python3 docs/research/build_navigator_research_index.py`. This generator reads Markdown and writes only this index and its dated coverage manifest. It performs no SSH, imports of research modules, ECU/CAN access, Git publication or installation.']
    counts = {}
    for label, base in areas:
        files = sorted((f for f in base.rglob('*.md') if f.resolve() != OUT.resolve()))
        counts[label] = len(files)
        lines += ['', f'## {label} — {len(files)} documents', '']
        previous = None
        for f in files:
            group = f.parent.relative_to(base).as_posix()
            if group != previous:
                lines += ['', f"### {(group if group != '.' else 'Top-level references')}", '']
                previous = group
            title = next((line.lstrip('#').strip() for line in f.read_text(errors='replace').splitlines() if line.startswith('# ')), f.stem)
            title = title.replace('[', '\\[').replace(']', '\\]')
            relative = Path(os.path.relpath(f, OUT.parent)).as_posix()
            link = quote(relative, safe='/._-')
            assert (OUT.parent / unquote(link)).resolve() == f.resolve()
            lines.append(f'- [{title}]({link})')
            entries.append({'path': f.relative_to(ROOT).as_posix(), 'sha256': sha(f), 'area': label})
    lines += ['', '## Coverage limits', '', 'This is a file-completeness catalog, not a completeness proof for every chat message, unrecorded experiment, historical device preference or physical claim. Read the documentation audit for known limits. Snapshot verification may require private originals and the exact source pair; local-only documents and artifacts are not automatically backed up to GitHub.', '']
    OUT.write_text('\n'.join(lines))
    for link in re.findall('\\]\\(([^)]+)\\)', OUT.read_text()):
        if not link.startswith(('https://', 'http://', '#')):
            assert (OUT.parent / unquote(link.split('#')[0])).exists(), link
    root_refs = ['NAVIGATOR_TUNING_GUIDE.md', 'NAVIGATOR_DOCUMENTATION_AUDIT.md', 'NAVIGATOR_ROADMAP.md', 'README.md']
    result = {'as_of': date.isoformat(), 'scope': 'All existing Markdown in the two named evidence areas, not all conversation content or physical validation', 'counts': counts, 'documents': len(entries), 'generated_index': OUT.relative_to(ROOT).as_posix(), 'generated_links_resolve': True, 'entries': entries, 'entrypoint_sha256': {n: sha(ROOT / n) for n in root_refs if (ROOT / n).exists()}}
    receipt = OUT.parent / f'navigator-documentation-coverage-{date.isoformat()}.json'
    receipt.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k not in ['entries', 'entrypoint_sha256']}, indent=2))
if __name__ == '__main__':
    main()
