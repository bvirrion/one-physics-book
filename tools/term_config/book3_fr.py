"""Book 3 -- fr. Curation only; the rules live in tools/termlink/.

Curated 2026-08-21 against the English curation (`book3_en.py`), which this
file follows term for term wherever the two languages agree, plus the
homographs French makes on its own.

The French bodies (parts/bachelor-1/fr) write their accents as raw UTF-8, so
the terms below are spelled the same way. `lang_fr.py` sets
TAIL_ON_EVERY_WORD with WORD_TAIL "(?:e?s)?", so "force centrale" already
matches "forces centrales" and no plural has to be declared here.

The French-only traps, each read in context before being kept or dropped:

* *tension* is the pull of a rope (chs. 12--19) and the electrical quantity
  English calls voltage (chs. 6--10, 27). One word, two definitions, no
  chapter order that can place it right.
* *couple* is the torque of chapter 15 and "un couple de forces",
  "le couple électron--trou", "un couple de valeurs".
* *capacité* is the capacitance of chapter 27 and the ordinary capacity of a
  reservoir, a battery, a compressor -- and the head of "capacité thermique",
  which survives as a term of its own.
* *solide* is the rigid body of chapter 19, the state of matter of
  chapters 20--25, and the ordinary adjective.
* *foyer* is the focal point of chapters 3--4 and the hearth of a boiler.
* *cœur* is the core of an optical fibre (ch. 2) and the core of the Earth,
  of a coaxial cable, of a transformer.
* *masse* would be the same clash English has between mass and electrical
  ground, but the book never defines it bare, so no rule is needed.
"""

# French translation of the default NOT_A_TERM keywords (the English defaults
# would let French result-names through and over-link).
#
# "loi", "lois", "énoncé" and "méthode" are deliberately NOT here, although
# the English default carries "law of": English writes "Gauss's law",
# "Bessel's method", "Clausius statement", so its filter never fires on a
# named law and it links two dozen of them -- French writes "loi de Gauss",
# "méthode de Bessel", "énoncé de Clausius", and translating the default word
# for word would silently delete every one. "théorème" stays, exactly as
# English's "theorem" does: neither edition links "théorème de Millman" /
# "Millman's theorem". The one asymmetry it costs is "théorème de Gauss" and
# "théorème d'Ampère", which English calls laws and links; the French bodies
# carry those two notions on "flux du champ électrique" and "circulation"
# instead.
NOT_A_TERM = ("théorème", "lemme", "inégalité", "formule", "critère",
              "principe", "identité", "règle", "paradoxe", "problème")

# Ordinary language in this register, or a word whose sense elsewhere in the
# book is not the sense its definition gives it. (A STOPped word is still
# linked inside the chapter that defines it.)
STOP = {
    # the bare nouns of mechanics and thermodynamics: from chapter 12 on they
    # are on every page and a link on each is noise. Every compound
    # ("force centrale", "vitesse angulaire", "pression cinétique",
    # "travail perdu", "chaleur latente", ...) survives as a term of its own.
    "force", "vitesse", "accélération",
    "pression", "température", "chaleur", "travail",
    # the French for "momentum", stopped in English for the same reason;
    # "conservation de la quantité de mouvement" survives.
    "quantité de mouvement",
    # the unit (kinetic theory) vs the sliding bar of the Laplace rails
    "bar",
    # moment of a force (ch. 15) vs "au moment où", "pour le moment"
    "moment",
    # the optical image (ch. 3) vs "l'image ondulatoire", "à l'image de"
    "image",
    # the focal point of chs. 3--4 vs the hearth of a boiler (ch. 24)
    "foyer",
    # op-amp gain (ch. 10) vs the ordinary gain of anything
    "gain",
    # the fibre core (ch. 2) vs the Earth's core, the coaxial core, the
    # transformer core
    "cœur",
    # flux of the electric field (ch. 26) vs the magnetic flux (ch. 29)
    "flux",
    # the SI unit (ch. 1) vs "vecteur unité", "par unité de longueur"
    "unité",
    # physical dimension (ch. 1) vs "les dimensions de la salle", "à une
    # dimension"
    "dimension",
    # thermodynamic transformation (ch. 22) vs ordinary usage elsewhere
    "transformation",
    # the objective of an instrument (ch. 4) vs the adjective
    "objectif",
    # THE French homograph: the rope's tension and the circuit's voltage are
    # one word. "diviseur de tension", "tension de saturation", "tension
    # accélératrice" survive.
    "tension",
    # torque (ch. 15) vs "un couple de forces", "le couple électron--trou"
    "couple",
    # capacitance (ch. 27) vs the ordinary capacity of a reservoir or a
    # battery. "capacité thermique à volume constant" survives.
    "capacité",
    # the rigid body (ch. 19) vs the state of matter (chs. 20--25) vs the
    # adjective. "frottement solide", "équilibre d'un solide" survive.
    "solide",
}

NO_CAPITAL = {
    # capitalized, these are the physicists, not the units
    "newton", "joule", "watt", "pascal", "kelvin", "tesla", "hertz",
    "coulomb", "volt", "ampère", "ohm", "henry", "farad", "weber",
}

EXTRA = {
    # NOT_A_TERM's "théorème" is right for "théorème de Millman" and its
    # dozen siblings, which English does not link either -- but two of the
    # notions English calls *laws* and links heavily are *théorèmes* in
    # French. Restored by hand so the two editions carry the same links.
    "théorème de Gauss": "thm:b1:electrostatics-gauss:gauss",
    "théorème d'Ampère": "thm:b1:magnetostatics:ampere",
}

DROP = {
    # bare adjectives harvested from definitions that merely use them; the
    # phrases they came from ("gaz idéal", "amplificateur opérationnel
    # idéal", "circuit linéaire", "régime linéaire", "force centrale",
    # "force conservative") all survive as terms of their own.
    "idéal", "linéaire", "conservative",
    # "centrale" is the feminine of the adjective, harvested from "force
    # centrale conservative"; on its own French reads it as a power station,
    # which chapter 24 mentions on every other page.
    "centrale", "centrale conservative",
}

DERIVED = {}
PRIMARY_OK = set()

EXTRA_PROTECT = [
    # the drag of the air, not the electrical component
    r"résistance\s+de\s+l['’]air",
    # "à couple constant" is stopped anyway, but the ordinary "en série" and
    # "en dérivation" of chapter 6 are not the Fourier series nor the
    # derivative
    r'\bsérie\s+de\s+Fourier\b',
]

AMBIG_POLICY = "drop"          # the university convention (books 3, 4, 5)
