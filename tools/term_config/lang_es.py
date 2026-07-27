"""Spanish morphology for One Physics Book term linking.

Spanish inflects every word of a noun phrase (onda estacionaria -> ondas
estacionarias), as French does, so the tail goes on each word and not only the
last -- see the sibling one-math-book config for the full note.
"""
WORD_TAIL = r'(?:e?s)?'
TAIL_ON_EVERY_WORD = True
HEAD = r'(?:[^\W\d_]+-)?'
DERIVE = False
