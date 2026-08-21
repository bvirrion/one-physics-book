"""Book 3 -- hi. Curation only; the rules live in tools/termlink/.

Curated 2026-08-21 from the harvested list (`--terms`) of the written
30-chapter Hindi edition.  Regenerate with:
    python3 tools/link_defined_terms.py --book 3 --lang hi --unwrap --apply
    python3 tools/link_defined_terms.py --book 3 --lang hi --apply

University register, so ``AMBIG_POLICY = "drop"`` as in ``book3_en``.

Hindi-specific notes (see also ``book2_hi.py``):

* **Compounds are written apart**, so the bare head of a compound term is
  also an ordinary noun on nearly every page.  The heads that the harvest
  picked up bare sit in ``STOP`` (still linked inside the chapter that
  defines them) while the full phrases keep linking everywhere.
* **``NO_CAPITAL`` is inert**: Devanagari has no letter case, so the man and
  the unit are the same string.  The unit-vs-surname split is done with
  ``EXTRA_PROTECT`` instead.
* ``बार`` is the SI-adjacent unit *and* the ordinary Hindi word for
  "time(s)" (एक बार, दो बार): it must be stopped, not merely dropped.
"""

# Ordinary language in this register, or a word whose sense elsewhere in the
# book is not the sense its definition gives it.  (A STOPped word is still
# linked inside the chapter that defines it.)
STOP = {
    # ubiquitous bare nouns of mechanics and thermodynamics
    "बल", "द्रव्यमान", "वेग", "त्वरण", "संवेग",
    "दाब", "ताप", "ऊष्मा", "कार्य", "शक्ति",
    # "बार" the unit vs "एक बार", "दो बार" (once, twice)
    "बार",
    # moment of a force (ch. 15) vs "उस क्षण" prose and the many compounds
    "आघूर्ण",
    # the optical image vs "दर्पण-प्रतिबिंब" in the symmetry chapters
    "प्रतिबिंब",
    # optical focus vs the verb sense
    "फोकस",
    # fibre core (ch. 2) vs the Earth's core, the coaxial core, the transformer core
    "क्रोड",
    # flux of the electric field (ch. 26) vs the magnetic flux (ch. 29)
    "अभिवाह",
    # SI unit (ch. 1) vs "एकांक"-free prose: मात्रक heads a dozen compounds
    "मात्रक",
    # physical dimension (ch. 1) vs the dimensions of a room
    "विमा",
    # thermodynamic transformation (ch. 22) vs ordinary usage elsewhere
    "रूपांतरण",
    # the signal of ch. 5 vs "संकेत करता है" (points, indicates), everywhere
    "संकेत",
    # fibre cladding (ch. 2) vs the cable sheath (ch. 28) and the balloon envelope
    "आवरण",
    # electrical ground vs the ground under a thundercloud
    "भूसंपर्क",
}

# Structurally inert in Devanagari (no letter case); kept empty on purpose,
# the unit-vs-surname split lives in EXTRA_PROTECT below.
NO_CAPITAL = set()

EXTRA = {}            # manual {term: label}; overrides every rule

DROP = {
    # bare adjectives harvested from definitions that merely use them
    "आदर्श", "रैखिक", "केंद्रीय", "संरक्षी",
}

# Spans masked before linking: the unit names that are also the physicists'
# surnames.  Never consume a `$` (use a lookahead) and never write a literal
# space (prose wraps): see the header of tools/termlink/protect.py.
EXTRA_PROTECT = [
    r"पास्कल\s+का\s+सिद्धांत",
    r"पास्कल\s+के\s+सिद्धांत",
    r"ऐंपियर-फेर",
    r"ऐंपियर\s+की\s+परिभाषा",
]

AMBIG_POLICY = "drop"
