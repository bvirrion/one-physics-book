"""Book 4 -- fr. Curation only; the rules live in tools/termlink/.

Curated 2026-08-22 against the English curation (`book4_en.py`), which this
file follows term for term wherever the two languages agree, plus the
homographs French makes on its own. It replaces the Book 3 seed that was
copied here on the same day: Book 4 is a different book -- rigid bodies,
fluids, Maxwell's equations, physical optics, diffusion, thermal radiation,
thermodynamic potentials and quantum mechanics -- and most of Book 3's
homograph traps (tension/voltage, couple, capacité, foyer, cœur, solide,
image, ...) are dead weight here because Book 4 never *defines* those bare
words. What survives of the seed is the part that is about the French
language rather than about Book 3: NOT_A_TERM, NO_CAPITAL, and the two
`théorème` restorations.

Regenerate with:
    python3 tools/link_defined_terms.py --book 4 --lang fr --unwrap --apply
    python3 tools/link_defined_terms.py --book 4 --lang fr --apply

The French bodies (parts/bachelor-2/fr) write their accents as raw UTF-8, so
the terms below are spelled the same way. `lang_fr.py` sets
TAIL_ON_EVERY_WORD with WORD_TAIL "(?:e?s)?", so "onde plane" already matches
"ondes planes" and no plural has to be declared here.
"""

# French translation of the default NOT_A_TERM keywords (the English defaults
# would let French result-names through and over-link).
#
# "loi", "lois", "énoncé" and "méthode" are deliberately NOT here, although
# the English default carries "law of": English writes "Gauss's law",
# "Fourier's law", "Fick's law", so its filter never fires on a named law and
# it links them -- French writes "loi de Fourier", "loi de Fick", and
# translating the default word for word would silently delete every one.
# "théorème" stays, exactly as English's "theorem" does.
NOT_A_TERM = ("théorème", "lemme", "inégalité", "formule", "critère",
              "principe", "identité", "règle", "paradoxe", "problème")

# Ordinary language in this register, or a word whose sense elsewhere in the
# book is not the sense its definition gives it. (A STOPped word is still
# linked inside the chapter that defines it.) These are book4_en.py's five
# stops, in French.
STOP = {
    # "laser" is named in every optics chapter long before ch. 23 defines
    # it; a link on each occurrence would be noise
    "laser",
    # the laser threshold (ch. 23) vs the hearing threshold (ch. 7), a
    # threshold of detection, "au-dessus du seuil". "seuil d'audition"
    # survives as a term of its own.
    "seuil",
    # absorption of light (ch. 23) vs absorption of sound, of heat, of a
    # photon; "absorption (de la lumière)" is the index entry, the bare noun
    # is ordinary language here
    "absorption",
    # cycle and turbine efficiency (ch. 27) vs fin efficiency (ch. 25),
    # luminous efficiency (ch. 26), the efficiency of anything. Both
    # "rendement isentropique" and "efficacité d'ailette" survive.
    "efficacité",
    # the steady flow of ch. 27: the adjective is on every page of chapters
    # 2--5 and 27. "régime permanent (écoulement)" survives.
    "permanent",
}

NO_CAPITAL = {
    # capitalized, these are the physicists, not the units
    "newton", "joule", "watt", "pascal", "kelvin", "tesla", "hertz",
    "coulomb", "volt", "ampère", "ohm", "henry", "farad", "weber",
}

EXTRA = {
    # NOT_A_TERM's "théorème" costs French the two notions English calls
    # *laws* -- "théorème de Gauss", "théorème d'Ampère". Book 3's fr config
    # restores them by hand; Book 4 must NOT, because the two statements live
    # in Book 3 (`thm:b1:...`) and this volume has no such labels: a link
    # would be an undefined reference. Chapter 10 names both in passing and
    # leaves them unlinked, exactly as book4_en.py does.
    #
    # the devices of ch. 27 are introduced capitalised in an itemize, exactly
    # as in English; link the lowercase nouns too (book4_en.py does the same
    # for "throttle" and "nozzle")
    "détendeur": "prop:b2:open-systems:devices",
    "tuyère": "prop:b2:open-systems:devices",
}

DROP = {
    # bare adjectives and harvest artefacts, term for term with book4_en.py's
    # "quantised", "four-level", "three-level", "Eulerian"
    "quantifiées", "quatre niveaux", "trois niveaux", "eulérienne",
    # THE homograph English does not have, and the reason this file is not a
    # translation of book4_en.py. English defines "rigid body" -- two words,
    # a term of art that its own prose then avoids, so book4_en links it
    # exactly once in the whole volume. French defines \emph{solide}, which
    # is also the state of matter of chs. 6, 25 and 29, the ordinary
    # adjective, and the head of "le son dans les solides". Kept as a term it
    # linked 57 times, 29 of them in chapter 1 alone, where the word is on
    # every line; STOP does not help, because STOP still links inside the
    # defining chapter. Dropped outright, for parity with English's one link.
    # "champ des vitesses (solide)", "moment cinétique (solide)" and
    # "énergie cinétique (solide)" survive as terms of their own.
    "solide",
    # the itemize head of prop:b2:open-systems:devices, harvested whole; the
    # three nouns are linked individually (EXTRA above, and "turbine" from
    # its own \index entry)
    "Compresseur, pompe, turbine",
}

DERIVED = {}
PRIMARY_OK = set()

EXTRA_PROTECT = [
    # the drag of the air, not the electrical component (ch. 4)
    r"résistance\s+de\s+l['’]air",
    # the Fourier series and the Fourier transform are not the "série"
    # nor the "transformée" of anything defined here
    r'\bsérie\s+de\s+Fourier\b',
]

AMBIG_POLICY = "drop"          # the university convention (books 3, 4, 5)
