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
    # French genders and pluralises; the entries above translate the English
    # stoplist word for word, but each harvested inflection is a term of its
    # own and has to be named. "réelle" is the feminine of "réel": an image
    # réelle in g11 lenses, ordinary "actual" everywhere else.
    "réelle", "réelles",
    # French says "hauteur" both for the pitch of a note (g12 acoustics) and
    # for a height: half the mechanics of grade 12 measures a "hauteur" in
    # metres. English has two words and needs no rule here.
    "hauteur", "hauteurs",
    # likewise "tension": the pull of a rope (g10 inertia) and the electrical
    # quantity English calls voltage (g11 circuits). Under
    # AMBIG_POLICY = "nearest-preceding" every mechanics chapter after g11
    # circuits sent its rope tensions to the electrical definition. Stopped,
    # the word links in its two defining chapters and nowhere else.
    "tension", "tensions",
    # "foyer" is the focal point of g11 optics, the focus of an ellipse in g12
    # astronomy, a household in every energy chapter, and a hearth in the
    # carbon-dating example. Only the first two are defined here.
    "foyer", "foyers",
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
    # feminines of the two entries above: "absolue" is harvested from the
    # diving method ("pression absolue") but also opens "température absolue",
    # "limite absolue"; "verticale" is harvested from the weight definition
    # (the direction) but is above all the ordinary adjective (composante
    # verticale, boucle verticale). The full phrases survive as terms.
    "absolue",
    "verticale", "verticales",
    # bare adjective harvested from "pression relative"; in French it is the
    # ordinary adjective everywhere else (incertitude relative, vitesse
    # relative, dérive relative). "pression relative" survives.
    "relative", "relatives",
    # harvested from "lentille mince"; on its own it is ordinary "thin"
    # (fil mince, fibre mince, isolant mince). "lentille mince" survives.
    "mince", "minces",
    # harvested from "travail moteur"; on its own it is the engine, which this
    # book mentions a dozen times (le moteur du treuil, les moteurs d'une
    # fusée). "travail moteur" survives.
    "moteur", "moteurs",
    # harvested from "équilibre stable / instable"; on their own they describe
    # a nuclide (plomb-206 stable, noyaux instables) or a steady power. The
    # two full phrases survive, and the solutions that needed them say them.
    "stable", "stables",
    "instable", "instables",
}

DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40

EXTRA_PROTECT = [
    r'\brésistance\s+de\s+l.air\b',
    r'\bfonctionne\b',
    # "son" is both the sound of grade 10 and the possessive determiner, which
    # a physics book writes on nearly every page ("son unité", "son écho",
    # "calculer son énergie"). The noun always follows a determiner, the
    # determiner never does, so protect every occurrence that no determiner
    # introduces. The plural "sons" is always the noun and is left alone.
    # Without this rule the sound definition collected 263 links where English
    # has 43, and all but a few dozen were the possessive.
    r"(?<!\ble\s)(?<!\bLe\s)(?<!\bdu\s)(?<!\bDu\s)(?<!\bun\s)(?<!\bUn\s)"
    r"(?<!\bce\s)(?<!\bCe\s)(?<!\bau\s)(?<!\bAu\s)(?<!\bdes\s)(?<!\bDes\s)"
    r"(?<!\bles\s)(?<!\bLes\s)(?<!\baux\s)(?<!\bAux\s)\b[Ss]on\b",
    # "poussée" is the thrust of the force inventory (g10 inertia) and the
    # feminine past participle of "pousser" ("la caisse est poussée de 4 m").
    # Only the participle takes an auxiliary or an instrumental complement.
    r"\b(?:est|sont|était|étaient|été|a|ont|l['’]a|l['’]ont|les\s+a)"
    r"\s+poussées?\b",
    r"\bpoussées?\s+(?:avec|à\s+des)\b",
    # "complémentaire" is stoplisted, but its plural is harvested separately
    # and the only occurrence outside the colour chapter is geometric (the
    # complementary launch angles of g12 projectile motion).
    r'\bangles?\s+complémentaires?\b',
]
