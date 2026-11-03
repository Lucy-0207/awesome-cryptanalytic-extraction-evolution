from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
rows=json.loads((root/'data/papers.json').read_text(encoding='utf-8'))
rel=json.loads((root/'data/relations.json').read_text(encoding='utf-8'))
ids=[p['id'] for p in rows]
assert len(ids)==len(set(ids)), 'duplicate paper ID'
assert len({p['url'] for p in rows})==len(rows), 'duplicate URL'
for x in rel:
    assert x['source'] in ids and x['target'] in ids
    assert x['source'] != x['target']
print(f'OK: {len(rows)} papers; {len(rel)} curated relations')
