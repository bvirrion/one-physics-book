"""Book 1 -- fr. Curation only; the rules live in tools/termlink/.

Young-book register, French edition. The traps are not the English ones:
French carries one word where English has two ("lampe" is both the bulb and
the lamp, "milieu" both the sound-carrying medium and the middle of
anything), and its commonest determiner, "son", is spelled exactly like the
noun for sound. Every entry below was read in context before being kept,
stopped or dropped.

Terms are spelled as the bodies spell them: raw UTF-8 accents, no TeX
escapes.
"""

# French translation of the default NOT_A_TERM keywords (the English defaults
# would let French result-names through and over-link).
NOT_A_TERM = ("théorème", "lemme", "inégalité", "formule", "critère",
              "principe", "identité", "règle", "loi de", "loi des",
              "paradoxe", "problème")

# Kept out of the global vocabulary, still linked inside the chapter that
# defines them: honest terms there, ordinary French everywhere else.
STOP = {
    # "observer que", "on observe alors" -- the ordinary verb of every
    # experiment; the noun is no better ("cette observation", "nos
    # observations")
    "observation", "observer", "Observer",
    # the circuit-diagram symbol in its chapter; "le symbole $\\Omega$" and
    # every unit symbol elsewhere
    "symbole",
    # the lunar phase in its chapter; "la première phase", "les deux phases
    # de la chute" elsewhere ("phases" stays: almost always lunar)
    "phase",
    # the magnet's pole in its chapter; the Earth's geographic poles and the
    # "pôle nord"/"pôle sud" compounds (which keep their own links) elsewhere
    "pôle", "pôles",
    # French says "milieu" both for the substance a sound crosses (g7) and
    # for the middle of anything -- and the last chapter stands the reader
    # "au milieu" of the ladder of scales on nearly every line
    "milieu",
    # one French word for the English pair bulb/lamp: the component in its
    # own chapter, the ordinary household lamp in six hundred other places
    # (streetlamp, desk lamp, "la lampe s'allume"). Linked everywhere it
    # would paint the book blue.
    "lampe",
    # the see-saw's balance in its chapter; "l'équilibre des comptes", "les
    # forces s'équilibrent", "en équilibre sur un pied" elsewhere
    "équilibre", "en équilibre",
    # the waxing and waning Moon in its chapter; "des écarts croissants",
    # "une suite décroissante" in the motion chapters
    "croissant", "croissante", "décroissante",
}

NO_CAPITAL = {
    # capitalized, these name the physicists, not the units
    "newton", "joule", "watt", "volt", "ampère", "ohm", "hertz",
}

EXTRA = {}            # manual {term: label}; overrides every rule

DROP = {
    # ordinary adjectives of the gentle grade-1/2 register
    "chaud", "Chaud", "froid",
    # "les cinq sens" is a chapter; "dans le même sens", "le sens du
    # courant", "en ce sens" is the whole of grades 6--9. The three
    # unambiguous senses (ouïe, odorat, goût) keep their links.
    "sens", "vue", "toucher",
    # ordinal and ordinary ("la seconde lampe", "en une seconde"); the unit
    # survives through the prose of its own chapter
    "seconde",
    # "à cet instant", "un instant plus tard" -- ordinary time word
    "instant",
    # bare adjectives; "circuit ouvert", "circuit fermé", "trajectoire
    # rectiligne", "trajectoire circulaire", "mouvement uniforme",
    # "mouvement varié" all survive as phrases of their own
    "ouvert", "fermé", "rectiligne", "circulaire", "uniforme", "varié",
    # "cette année", "l'an dernier", "neuf années" -- ordinary everywhere;
    # "année-lumière" and "saison" keep their links
    "année",
    # ordinary time-of-day words used on every page; "lever du Soleil" and
    # "coucher du Soleil" keep their links
    "jour", "nuit",
    # "fond" is the third person of *fondre* (it melts) and, far more often,
    # the bottom of a glass, the back wall, "au fond", "le fond de scène".
    # "fondre", "gèle" and "geler" keep their links.
    "fond",
    # sentence-initial imperative of a method step, not the defined noun
    "Mesurer",
}

DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"   # a spiral curriculum re-defines its terms
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40

# Spans no link may enter. NB: every space is \s+ -- the sources wrap at 72
# columns, and a phrase split across two lines must still be protected.
EXTRA_PROTECT = [
    # "son" is both the sound of grade 3 and the possessive determiner, which
    # a physics book writes on nearly every page ("son unité", "son écho",
    # "calculer son énergie"). The noun always follows a determiner, the
    # determiner never does, so protect every occurrence that no determiner
    # introduces. The plural "sons" is always the noun and is left alone.
    r"(?<!\ble\s)(?<!\bLe\s)(?<!\bdu\s)(?<!\bDu\s)(?<!\bun\s)(?<!\bUn\s)"
    r"(?<!\bce\s)(?<!\bCe\s)(?<!\bau\s)(?<!\bAu\s)(?<!\bdes\s)(?<!\bDes\s)"
    r"(?<!\bles\s)(?<!\bLes\s)(?<!\baux\s)(?<!\bAux\s)\b[Ss]on\b",
    # mathematics' powers of ten, not the electrical quantity P = U I
    r'\bpuissances?\s+de\s+dix\b',
    # mechanics' drag, not the electrical quantity R = U/I
    r'\brésistances?\s+de\s+l[\'’]air\b',
    # loudness, not the current's intensity
    r'\bintensités?\s+sonores?\b',
    # headphone loudness and the books of the series, not the space a body
    # occupies
    r'\bplein\s+volume\b',
    r'\bvolumes?\s+de\s+lycée\b',
    r'\bce\s+volume\b',
    # the fuels, not the state of matter
    r'\bcharbon\s+ou\s+(?:du\s+)?gaz\b',
    # the apple's branch, not the parallel branch of a circuit
    r'\bsa\s+branche\b',
    # "pile" as the adverb ("la valeur moderne pile"), not the battery
    r'\bmoderne\s+pile\b',
    # the sports-field model's marble, not the state of matter
    r'\bbille\s+de\s+verre\b',
    # the eye's flicker-fusion rate, not the melting of ice
    r'\b(?:taux|seuil)\s+de\s+fusion\b',
    r'\bfusion\s+de\s+l[\'’]œil\b',
    # the frames of a film, not the picture a mirror or lens makes
    r'\bimages?\s+par\s+(?:seconde|image)\b',
    r'\bimage\s+par\s+image\b',
    r'\bimages?\s+du\s+cinéma\b',
    r'\bimages?\s+de\s+(?:la\s+)?vidéo\b',
    r'\bimages?\s+de\s+la\s+caméra\b',
    r'\bpar\s+images?\b',
    r'\bd[\'’]une\s+image\s+à\b',
    r'\b(?:parcourir|filmer)\s+les\s+images\b',
    # "une caméra à $25$ images": a lookbehind, never a consumed $ (see the
    # warning at the top of tools/termlink/protect.py)
    r'(?<=\$)\s+images\b',
    # the combustion engine and the probe's cold rocket engines, not the
    # little electric motor of the circuits chapter
    r'\bmoteurs?\s+(?:de|d[\'’]une)\s+voiture\b',
    r'\bmoteurs?\s+froids?\b',
]
