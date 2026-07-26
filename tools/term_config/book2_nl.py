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

# Dutch writes as one solid word what English writes as two ("RC circuit" ->
# "RC-kring", "time dilation" -> "tijddilatatie"). An \index entry attached to
# a statement is only harvested when it contains a space (harvest.py), so every
# such compound is lost here while its English twin is linked. Restored by
# hand, one entry per English link target.
EXTRA = {
    "RC-kring": "thm:g12:rc-rl-circuits:charging",
    "RL-kring": "prop:g12:rc-rl-circuits:rl",
    "LC-kring": "prop:g12:rlc-oscillations:equation",
    "tijddilatatie": "thm:g12:special-relativity:dilation",
    "lengtecontractie": "prop:g12:special-relativity:contraction",
    "ijzerpiek": "prop:g12:nuclear-energy:ironpeak",
    "veeroscillator": "prop:g12:oscillators-and-time:spring-period",
    "tijdschakelingen": "rem:g12:rc-rl-circuits:applications",
}
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
