"""Book 2 -- en. Curation only; the rules live in tools/termlink/.

Every key is optional: anything left out falls back to the defaults in
tools/link_defined_terms.py (empty sets, AMBIG_POLICY "drop").

Placeholder config: the chapters are not written yet. Curate the vocabulary
(STOP / NO_CAPITAL / EXTRA / EXTRA_PROTECT / DROP) as content lands, then
generate links with:  python3 tools/link_defined_terms.py --book 2 --apply
"""

STOP = set()
NO_CAPITAL = set()
EXTRA = {}
DROP = set()
EXTRA_PROTECT = []
AMBIG_POLICY = "nearest-preceding"
