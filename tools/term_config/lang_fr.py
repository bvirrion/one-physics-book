"""French morphology.

French pluralises every word of a phrase (grandeur physique -> grandeurs
physiques), so the tail goes on each word, not only the last. The English
suffix derivations mean nothing here and are off; real variants are declared
term by term in EXTRA.
"""
WORD_TAIL = r'(?:e?s)?'
TAIL_ON_EVERY_WORD = True
HEAD = r'(?:[^\W\d_]+-)?'
DERIVE = False
