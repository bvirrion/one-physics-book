"""Book 2 -- nl. Curation only; the rules live in tools/termlink/.

The Dutch bodies (parts/grade-10..12/nl) write their accents as raw UTF-8, so
the terms below are spelled the same way. Dutch writes its compounds solid
and the shared rule refuses to link a component inside a compound.
"""

# Dutch translation of the default NOT_A_TERM keywords.
NOT_A_TERM = ("stelling", "lemma", "ongelijkheid", "formule", "criterium",
              "principe", "identiteit", "regel", "wet van", "paradox",
              "probleem")

# Ordinary Dutch, or a word whose sense in the book is not the definition's.
# A STOPped word is still linked inside the chapter that defines it.
STOP = {
    "reëel",
    "normaal",
    "kern",
    "knoop",
    "versterking",
    "rust",
    "uniform",
    "complementair",
    "staaf",
    "staven",
    "gamma",
    "snelheid",
}

NO_CAPITAL = {
    # capitalized, these are the physicists, not the units
    "newton", "joule", "watt", "pascal", "kelvin", "tesla", "hertz",
    "coulomb", "volt", "ampère", "ohm", "becquerel", "henry", "farad",
}

EXTRA = {}
DROP = {
    "absoluut",
    "verticaal",
    "seconde",
    "seconden",
    "in rust",
}

DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40

EXTRA_PROTECT = [
    r'\bluchtweerstand\b',
    r'\bwerkt\b',
]
