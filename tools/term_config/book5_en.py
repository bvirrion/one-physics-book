"""Book 5 -- en. Curation only; the rules live in tools/termlink/.

Every key is optional: anything left out falls back to the defaults in
tools/link_defined_terms.py (empty sets, AMBIG_POLICY "drop").

Curated 2026-08-27 from the harvested list (`--terms`) of the written
27-chapter book.  Regenerate with:
    python3 tools/link_defined_terms.py --book 5 --unwrap --apply
    python3 tools/link_defined_terms.py --book 5 --apply
"""

# Ordinary language in this register, or a word whose sense elsewhere in
# the book is not the sense its definition gives it. (A STOPped word is
# still linked inside the chapter that defines it.)
STOP = {
    # quantum spin (ch. 12) vs "the star spins", "spin period", "spin-up"
    # in the rotation sense throughout chs. 25-27
    "spin",
    # the band-theory metal (ch. 24) vs scrap metal, precious metal,
    # metal pans in chs. 22-23 problems
    "metal",
    # the spacetime event (ch. 4) vs counting events in detectors and
    # statistics (chs. 16, 26)
    "event",
    # the Hermitian observable (ch. 8) vs the adjective ("observable
    # universe", "observable effects")
    "observable",
    # the semiconductor hole (ch. 24) vs the black hole of ch. 27
    "hole",
}

NO_CAPITAL = set()

EXTRA = {}

DROP = set()

EXTRA_PROTECT = []

AMBIG_POLICY = "drop"
