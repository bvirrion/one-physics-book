"""Book 5 -- fr. Curation only; the rules live in tools/termlink/.

Audited 2026-09-03 against Book 5's own French harvest
(`python3 tools/link_defined_terms.py --book 5 --lang fr --terms`), after
all 54 chapter and solution files had landed. What the audit changed with
respect to the coordinator's seed (which came from `book4_fr.py`):

  * `STOP` -- the five words carried from Book 4 (*absorption*, *efficacité*,
    *laser*, *permanent*, *seuil*) were removed: none of them is a harvested
    term of this book, so each was a dead entry that could only ever silence
    a term a later edit introduced. What remains is exactly the French
    rendering of `book5_en.py`'s five, and all five fire (the harvest reports
    "dropped (stoplist): 5"): *spin* (ch. 12's quantum spin against a star
    spinning in chs. 25--27), *métal* (ch. 24's band-theory metal against the
    scrap and cookware metal of chs. 22--23), *événement* (ch. 4's spacetime
    event against counted events in chs. 16 and 26), *observable* (ch. 8's
    Hermitian observable against the adjective), *trou* (ch. 24's
    semiconductor hole against ch. 27's black hole -- the multi-word "trou
    noir" is a term of its own and still links).
    The unaccented spelling "evenement" was dropped: this edition writes
    "événement" everywhere.
  * `EXTRA` -- stays empty. Diffing this edition's reachable target set
    against `en_omterm_targets.txt` leaves nothing on the English side:
    all 100 English targets are reached by French terms, so there is no
    target that needs a hand-written alias.
  * `EXTRA_PROTECT` -- emptied. Neither carried mask matched anything in this
    book (`résistance de l'air` and `série de Fourier` occur nowhere in
    `parts/bachelor-3/fr/`), and neither "résistance" nor "série" is a bare
    linkable term here; keeping dead masks is exactly the hazard the seed
    warned about.
  * `DROP` -- stays empty; the harvest drops nothing as defined twice.

`NO_CAPITAL` is kept: French lowercases unit names derived from physicists'
names, and it costs nothing where the words do not occur.

The `"law of"` entry of the shared `NOT_A_TERM` default is deliberately NOT
translated: it never fires on English, but a literal French rendering would
swallow every named law in the book.
"""

STOP = {
    # book5_en.py's five, rendered in French. All five fire.
    "spin",         # ch. 12 quantum spin vs a spinning star (chs. 25-27)
    "métal",        # ch. 24 band-theory metal vs scrap/cookware metal
    "événement",    # ch. 4 spacetime event vs counted detector events
    "observable",   # ch. 8 Hermitian observable vs the adjective
    "trou",         # ch. 24 semiconductor hole vs ch. 27 black hole
    # French-only homograph collisions, found by comparing this edition's
    # \omterm surface-form frequency table against English's (see the module
    # note below). English needs none of these: it has a distinct word for
    # each sense, so its harvest never collides.
    "contrainte",   # ch. 1 Lagrangian *constraint* vs ch. 3 elastic *stress*
    "dilatation",   # ch. 3 elastic *dilatation* vs *dilatation du temps*
                    # (ch. 4) and *dilatation thermique* (chs. 16, 23)
    "bra",          # French pluralises in -s: *bra* -> *bras*, the ordinary
                    # word for the spiral *arms* of a galaxy (chs. 12, 27)
                    # and for *bras de fer* (ch. 14)
}

NO_CAPITAL = {
    "ampère", "coulomb", "farad", "henry", "hertz", "joule", "kelvin",
    "newton", "ohm", "pascal", "tesla", "volt", "watt", "weber",
}

EXTRA = {}

DROP = set()

EXTRA_PROTECT = [
    # Fourth French homograph collision, found by the coordinator's
    # complementary census (a target linked in a chapter where English never
    # links it) -- the ratio test is blind to it, because these three wrong
    # links landed on a target English links 11 times elsewhere.
    #
    # *polarisation directe* / *polarisation inverse* is the standard French
    # for a diode's forward / reverse BIAS (ch. 24). The harvested term
    # *polarisation* is the P field of a dielectric (ch. 22,
    # def:b3:electromagnetism-in-matter:polarisation). English cannot
    # collide: it writes "forward bias" / "reverse bias", and the word
    # "polarisation" appears nowhere in its chapter 24.
    #
    # Masking only the two collocations leaves every dielectric-sense
    # occurrence in chapters 22-23 linkable.
    r"[Pp]olarisation\s+(?:directe|inverse)",
]

AMBIG_POLICY = "drop"          # the university convention (books 3, 4, 5)
