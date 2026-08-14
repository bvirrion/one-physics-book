"""Book 1 -- nl. Curation only; the rules live in tools/termlink/.

Young-book register (cf. the English book1 config): most of the defined
vocabulary is also ordinary Dutch, so a word earns a link only if it
means the defined thing in nearly all of its uses. Dutch writes its
compounds solid, so the word boundary already refuses to link "licht"
inside "daglicht" or "kracht" inside "zwaartekracht"; what needs
guarding here is the everyday adjective and the everyday verb.
"""

STOP = {
    # honest in its chapter ("de waarneming van de klas"), ordinary
    # emphasis elsewhere ("let op dat", "we nemen waar dat")
    "waarnemen", "waarneming",
    # magnet sense in its chapters; the battery's terminals, the
    # Earth's geographic poles and the flagpole elsewhere
    "pool", "polen",
    # circuit-diagram sense in its chapter; "het symbool \\unit{A}"
    # elsewhere
    "symbool",
}
# NB "seconde" is deliberately NOT stopped: unlike English "second" it
# is never the ordinal, so every use is the SI unit and links honestly,
# exactly as "meter", "gram" and "kilogram" do.

NO_CAPITAL = {
    # capitalized, these are the physicists, not the units
    "newton", "joule", "watt", "volt", "ampère", "ohm", "hertz",
    # sentence-initial these are instructions ("Meet de gaten", "Neem
    # waar dat"), not the defined nouns
    "meten", "waarnemen",
}

# Manual {term: label}; overrides every rule. "weerstand" is defined
# twice in one chapter -- the quantity and the component -- so the
# harvester drops it as ambiguous; both senses are the same physics
# here, and the quantity's definition is the honest target.
EXTRA = {
    "weerstand": "def:g8:ohms-law:resistance",
    "weerstanden": "def:g8:ohms-law:resistor",
}

DROP = {
    # ordinary adjectives/verbs of the register, harvested from the
    # gentle grade-1/2 definitions; linking them everywhere is noise
    "warm", "Warm", "koud",
    # the five senses as everyday verbs: "je ziet", "we horen", "voel
    # de warmte". The noun "zintuig" keeps its link.
    "zien", "horen", "ruiken", "proeven", "voelen",
    # bare adjectives; "eenparige beweging", "veranderlijke beweging",
    # "rechtlijnige baan", "cirkelvormige baan" and "gesloten
    # stroomkring" survive as phrases
    "eenparig", "veranderlijk", "rechtlijnig", "cirkelvormig",
    "gesloten",
    # "dit jaar", "vorig jaar", "negen jaar": ordinary everywhere; the
    # season words keep their links
    "jaar",
    # ordinary time-of-day words used constantly in prose; "zonsopgang"
    # and "zonsondergang" keep their links
    "dag", "Dag", "nacht", "Nacht",
    # the verb and the everyday adjective ("open de lus", "de open
    # ruimte", "een open vraag"); "gesloten stroomkring" survives as a
    # phrase
    "open", "Open",
}

DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"   # a spiral curriculum re-defines its terms
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40

# NOTE: multi-word patterns use \s+ between words -- a phrase wrapped
# across a source line break must still be protected.
EXTRA_PROTECT = [
    # the adjective "licht" ("licht overbelast", "licht gekromde
    # lenzen"), not the phenomenon
    r'\blicht\s+(?:overbelast|gekromde?|hellend|verlicht|gebogen)\b',
    # the fuel, not the state of matter
    r'\bkolen\s+of\s+gas\b',
    # headphone loudness, not the space a body occupies
    r'\bvol\s+volume\b',
    # a dynamometer's axis of use, not the Earth's spin axis
    r'\bas\s+van\s+het\s+instrument\b',
    # the everyday verb ("de schakelaar aan-/uitzetten"), not the
    # component
    r'\bschakel(?:aar)?\s+(?:hem|het|de\s+kring)\s+(?:aan|uit)\b',
    # the apple's branch on the tree, not the branch of a circuit
    r'\bzijn\s+tak\s+los\b',
    # the separable verb "aandrijven" ("de batterij drijft de mars
    # aan", "stoomstralen drijven de turbine aan"), not the floating of
    # the grade-1 chapter
    r'\bdrij(?:ft|ven)\b(?:\s+\S+){0,6}\s+aan\b',
]
