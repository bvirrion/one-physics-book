"""Brazilian Portuguese morphology for One Physics Book term linking.

Portuguese agrees every word of a noun phrase (onda estacionaria -> ondas
estacionarias, forca conservativa -> forcas conservativas), as Spanish and
French do, so the tail goes on each word and not only the last. The tail is
optional per word, so head-only plurals still match: "linha de campo" ->
"linhas de campo" pluralises the head and leaves the prepositional tail
alone.

This flag was False until 2026-07-31; with the tail on the last word alone
the regex asked for "onda estacionarias" and every plural of a compound term
went unlinked. Book 2 worked around it with a hand-measured DERIVED table in
book2_pt.py -- the same workaround the Spanish books carried before their own
flag was corrected. That table is now trimmed to the genuinely irregular
plurals ("-ao" -> "-oes", "-al" -> "-ais", "-r" -> "-res") that the tail
"(?:e?s)?" cannot produce.
"""
WORD_TAIL = r'(?:e?s)?'
TAIL_ON_EVERY_WORD = True
HEAD = r'(?:[^\W\d_]+-)?'
DERIVE = False
