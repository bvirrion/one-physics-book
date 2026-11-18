import re,sys
known=set()
for b in sys.argv[1].split(','):
    for l in open(f'sources/GLOSSARY_BOOK_{b}_ZH.md'):
        m=re.match(r'\d\d \| (.*?) \| ',l)
        if m: known|={f.strip().lower() for f in m.group(1).split(' / ')}
for y in sys.argv[2:]:
    out=[]
    for l in open(f'draft/zh/terms-{y}.txt'):
        ch,t=l.rstrip('\n').split(' | ',1)
        if t.lower() not in known: out.append(f'{ch}:{t}'); known.add(t.lower())
    print(f'## {y} ({len(out)}): '+'; '.join(out))
