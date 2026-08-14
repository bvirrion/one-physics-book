"""Book 1 -- en. Curation only; the rules live in tools/termlink/.

Young-book register (cf. the math book1 config): most defined vocabulary
is also ordinary English, so a word earns a link only if it means the
defined thing in nearly all of its uses. Everyday furniture words are
DROPped (their compound phrases survive as terms of their own); words
that are honest terms inside their own chapter but ordinary language
elsewhere are STOPped.
"""

STOP = {
    # honest in its chapter, ordinary emphasis elsewhere ("observe that")
    "observation", "observe",
    # equilibrium sense in its chapter; "the books balance(d)" elsewhere
    "balanced",
    # moon sense in its chapter; "first phase", "partial phases" of any
    # process elsewhere ("phases" stays linked -- almost always lunar)
    "phase",
    # magnet sense in its chapters; the Earth's geographic poles, the
    # tightrope walker's pole and the flagpole elsewhere
    "pole", "poles",
    # circuit-diagram sense in its chapter; "the symbol \\unit{A}" and
    # math symbols elsewhere
    "symbol",
}

NO_CAPITAL = {
    # capitalized, these are the physicists, not the units
    "newton", "joule", "watt", "volt", "ampere", "ohm", "hertz",
    # sentence-initial these are imperatives ("Measure a filament
    # lamp's portrait"), not the defined nouns
    "measure", "observe",
}

EXTRA = {}            # manual {term: label}; overrides every rule

DROP = {
    # ordinary adjectives/verbs of the register, harvested from the
    # gentle grade-1/2 definitions; linking them everywhere is noise
    "hot", "Hot", "cold",
    "sense", "senses", "sight", "touch", "smell", "taste",
    # ordinal "second" everywhere; the unit survives via "per second"
    # prose and the SI chapter's own text
    "second", "seconds",
    # "at that moment" -- ordinary time word
    "moment",
    # bare adjectives; "open circuit", "closed circuit", "straight
    # trajectory", "uniform motion", "varied motion" survive as phrases
    "open", "closed", "straight", "circular", "uniform", "varied",
    # "this year", "last year", "nine years": ordinary everywhere
    "year",
    # derived verb forms: "lights a lamp", "heats as the current
    # grows" -- the bare nouns "light" and "heat" keep their links
    "lights", "heats",
    # ordinary time-of-day words used constantly in prose; "sunrise",
    # "sunset" and the astronomy phrases keep their links
    "night", "Night", "daytime", "Daytime",
}

DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"   # a spiral curriculum re-defines its terms
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40

# NOTE: multi-word patterns use \s+ between words -- a phrase wrapped
# across a source line break must still be protected.
EXTRA_PROTECT = [
    # mechanics' drag (g9 parachutist), not the electrical quantity
    r'\bair\s+resistance\b',
    # mathematics' powers, not electric power
    r'\bpowers?\s+of\s+ten\b',
    # the buildings, not the quantity P = UI
    r'\bpower\s+(?:plant|station)s?\b',
    # the childhood toy, not the wind
    r'\bwind-up\b',
    # the kitchen sink (float-test method), not the verb of the
    # floating rule
    r'\bor\s+the\s+sink\b',
    # a firm handshake, not the state of matter
    r'\bsolid\s+handshake\b',
    # the fuel, not the state of matter
    r'\bcoal\s+or\s+gas\b',
    # still water "mirrors" the mountains -- the verb, not the object
    r'\bmirrors\s+the\s+mountains\b',
    # a dynamometer's axis of use, not the Earth's spin axis
    r"\binstrument's\s+axis\b",
    # headphone loudness, not the space a body occupies
    r'\bfull\s+volume\b',
    # a book of the series, not the space a body occupies
    r'\b(?:High\s+School|Year\s+\w+|this)\s+volume\b',
    # the adjective ("a light paper cup"), not the phenomenon
    r'\blight\s+paper\s+cup\b',
    # the verb ("switch on/off"), not the component
    r'\bswitch(?:ed|es)?\s+(?:it\s+)?(?:on|off)\b',
    r'\bswitch\s+the\s+circuit\s+off\b',
]
