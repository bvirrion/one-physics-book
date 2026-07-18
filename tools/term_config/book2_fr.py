"""Book 2 -- fr. Curation only; the rules live in tools/termlink/.

The French bodies (parts/grade-10..12/fr) write their accents as raw UTF-8, so
the terms below are spelled the same way.
"""

# French translation of the default NOT_A_TERM keywords (English defaults would
# let French result-names through and over-link).
NOT_A_TERM = ("théorème", "lemme", "inégalité", "formule", "critère",
              "principe", "identité", "règle", "loi de", "loi des",
              "paradoxe", "problème")

# Ordinary French, or a word whose sense in the book is not the definition's.
# A STOPped word is still linked inside the chapter that defines it.
STOP = {
    # ordinary language that happens to be harvested from definitions
    "réel",
    "normale",
    "cœur",
    "nœud",
    "gain",
    "repos",
    "uniforme",
    "complémentaire",
    "tige",
    "tiges",
    "gamma",
    "cœur",
    "vitesse",  # everywhere from grade 10; vector definition is later
}

NO_CAPITAL = {
    # capitalized, these are the physicists, not the units
    "newton", "joule", "watt", "pascal", "kelvin", "tesla", "hertz",
    "coulomb", "volt", "ampère", "ohm", "becquerel", "henry", "farad",
}

EXTRA = {}
DROP = {
    "absolu",
    "vertical",
    "seconde",
    "secondes",
    "au repos",
}

DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40

EXTRA_PROTECT = [
    r'\brésistance\s+de\s+l.air\b',
    r'\bfonctionne\b',
]
