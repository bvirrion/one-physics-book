"""Merge sources/GLOSSARY_BOOK_{1..N}_ZH.md into one file for glossary.py split: a later book's line replaces every
earlier line that shares one of its English forms (case-insensitive). Usage: merge_glossary.py N out.md"""
import re, sys
n, out = int(sys.argv[1]), sys.argv[2]
LINE = re.compile(r'^(\d\d) \| (.*?) \| (.*)$')
lines = []                                   # (forms, raw)
for b in range(1, n + 1):
    for raw in open(f'sources/GLOSSARY_BOOK_{b}_ZH.md', encoding='utf-8'):
        m = LINE.match(raw.strip())
        if not m:
            continue
        forms = {f.strip().lower() for f in m.group(2).split(' / ')}
        lines = [(f, r) for f, r in lines if not (f & forms)]
        lines.append((forms, raw.strip()))
hdr = open(f'sources/GLOSSARY_BOOK_{n}_ZH.md', encoding='utf-8').read().split('\n00 |')[0].rstrip()
open(out, 'w', encoding='utf-8').write(hdr + f'\n\n(Merged Books 1–{n}; generated, do not edit.)\n\n' + '\n'.join(r for _, r in lines) + '\n')
print(f'book {n}: {len(lines)} lines')
