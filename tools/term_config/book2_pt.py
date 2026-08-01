"""Book 2 -- pt. Curation only; the rules live in tools/termlink/.

Every key is optional: anything left out falls back to the defaults in
tools/link_defined_terms.py (empty sets, AMBIG_POLICY "drop").

Brazilian Portuguese costs this book four curation problems English does
not have:

* homographs the English text keeps apart with two different words
  ("tension" and "voltage" are both *tensão*; "pitch" and "height" are
  both *altura*; "power" and "power of ten" are both *potência*; the
  focus of a lens and the focus of an ellipse are both *foco*);
* one term that collides with an ordinary function word: *nós* is both
  the nodes of a standing wave and the pronoun "we/us";
* unit names spelled exactly like the physicists they honour --- Newton,
  Joule, Coulomb, Ohm, Watt, Henry, Becquerel are the men when
  capitalized and the units when not (Spanish escapes this with
  julio/voltio/culombio, Portuguese does not);
* multiword terms whose plural agrees on every word (*linha de campo* ->
  *linhas de campo*), which the shared morphology file does not yet
  generate for pt -- see DERIVED below.
"""

NOT_A_TERM = ()

# Words that name something else in ordinary prose, or whose sense in the
# book is not the sense the definition gives them. (A STOPped word is still
# linked inside the chapter that defines it.)
STOP = {
    # THE Portuguese homograph: rope tension (g10 inertia) and electrical
    # voltage (g11 circuits) share one word, so no chapter ordering can
    # place it right -- every mechanics chapter of grade 12 would link to
    # the voltage definition. Linked only inside its two defining chapters.
    "tensão",
    # pitch of a sound (g12 sound); "altura" is also the ordinary height of
    # a drop, a tower, a satellite -- hundreds of mechanical uses. The
    # phrase "altura (do som)" survives.
    "altura",
    # the focus of a lens (g11) and the focus of an ellipse (g12) are one
    # word, and the plural tail makes the two indistinguishable. Each links
    # inside its own chapter; "foco imagem" and "focos" survive.
    "foco",
    # standing-wave nodes (g12 sound) -- and the pronoun "we/us", which the
    # book uses a dozen times ("a luz que chega até nós").
    "nós", "nó",
    # radiation sense (g11 nucleus) is right in the nuclear chapters and
    # wrong in the relativity chapter, where prose "gama" names the
    # dilation factor. "radiação gama" survives as a phrase.
    "gama",
    # the fundamental of a note (g12 sound); elsewhere the adjective is
    # ordinary -- and "interação fundamental", "estado fundamental" are
    # terms of their own.
    "fundamental",
    # harvested from "trabalho motor" (g11); bare "motor" is the engine,
    # from the rocket's to the clock's driving weight. The phrase survives.
    "motor",
    # oscilloscope gain (g10 signals); "ganho" is also the ordinary gain of
    # anything -- resolution, energy, speed.
    "ganho",
    # ordinary words of the register, never harvested bare in the current
    # text but kept here as a guard if a later edit defines them alone.
    # ("força", "energia", "trabalho", "campo" and "onda" are deliberately
    # NOT here: they are unambiguous in Portuguese and English links them
    # book-wide.)
    "real", "normal", "uniforme", "velocidade",
}

NO_CAPITAL = {
    # capitalized, these are the physicists, not the units -- and in
    # Portuguese the two are spelled alike. The book writes "leis de
    # Newton", "efeito Joule", "barreira de Coulomb", "lei de Ohm".
    "newton", "joule", "coulomb", "ohm", "watt", "henry", "becquerel",
    "pascal", "kelvin", "tesla", "volt", "ampère", "hertz", "farad",
    "sievert", "curie",
}

EXTRA = {}            # manual {term: label}; overrides every rule

DROP = {
    # bare feminine adjective harvested from the diving method ("pressão
    # absoluta"); it also opens "temperatura absoluta" and "incerteza
    # absoluta", where a link to the pressure method would be wrong. All
    # three full phrases survive as terms of their own.
    "absoluta",
    # display form with math in it; never matches prose. The dilation
    # theorem is reachable through "dilatação do tempo".
    "fator $\\gamma$ (gama)",
    # bare adjective from "lente delgada"; "lâmina delgada", "casca
    # delgada" have nothing to do with optics. The lens phrases survive.
    "delgada",
    # bare adjectives from the equilibrium proposition; "núcleo instável",
    # "chumbo estável", "órbita estável" are everywhere. "equilíbrio
    # estável" and "equilíbrio instável" survive.
    "estável", "instável",
    # ordinary words of the register, harvested from definitions that
    # merely use them: "vertical" (from the weight definition), "segundo"
    # (from the SI-unit definition -- but "o segundo postulado", "o segundo
    # máximo" are ordinals), "em repouso" (from the reference-frame
    # definition, though the phrase means "motionless" everywhere),
    # "escapa" (the ordinary verb: argon escapes the lava, the rocket
    # escapes the Earth).
    "vertical",
    "segundo",
    "em repouso", "repouso",
    "escapa",
}

# Irregular plurals only. lang_pt.py now sets TAIL_ON_EVERY_WORD = True, so
# the regular Portuguese plural of a phrase is generated by the rule itself
# ("linha de campo" -> "linhas de campo", "força conservativa" -> "forças
# conservativas"). What "(?:e?s)?" per word still cannot produce is the
# stem-changing plural: "-ão" -> "-ões", "-al" -> "-ais", "-m" -> "-ns".
# These six phrases are the ones the book actually uses in the plural.
# ("referencial inercial" -> "referenciais inerciais" would belong here too,
# but its base is an ambiguous term resolved by AMBIG_POLICY, and DERIVED
# only extends the unambiguous map -- the entry would be inert, so the one
# plural use in g12 ch06 stays unlinked.)
DERIVED = {
    "ordem de grandeza": ("ordens de grandeza",),
    "interação fundamental": ("interações fundamentais",),
    "reflexão total": ("reflexões totais",),
    "pressão absoluta": ("pressões absolutas",),
    "força gravitacional": ("forças gravitacionais",),
    "energia potencial": ("energias potenciais",),
    "distância focal": ("distâncias focais",),
}

PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"   # a spiral curriculum re-defines its terms
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40

# Two rules hold for EVERY pattern below, not only for the ones that have
# already been caught failing:
#   * NEVER consume a `$` -- match it with a lookahead. The list is one
#     alternation scanned left to right, so eating an opening $ leaves the
#     inline-math rule pairing the closing $ with the next formula's opening
#     one, and the mask runs inside out to end of file. It reports nothing;
#     the links just vanish (see tools/termlink/protect.py, and the errata in
#     translation_scores/book_2/pt/translation_score.md: 270 links).
#   * NEVER write a literal space -- always `\s+`. The list is compiled with
#     re.S and real prose wraps: "potências de\ndez", "de mesmo\nsinal". A
#     pattern that matches today is one reflow away from silently missing.
EXTRA_PROTECT = [
    # mechanics' drag, not the electrical quantity
    r'resistência\s+do\s+ar',
    # "potência" is both power and a mathematical power
    r'potências?\s+de\s+(?:dez|dois)',
    # the spring's compression, not the acoustic one
    r'compressão\s+máxima',
    # "núcleo" is the core of a fibre (g10), the nucleus of an atom (g11)
    # and, in these phrases, neither: the iron core of an electromagnet or
    # of a planet, and the burning core of a star.
    r'núcleos?\s+de\s+ferro(?:\s+fundido)?',
    r'(?:sem|com\s+o)\s+núcleo',
    r'núcleo\s+d[oa]\s+(?:Sol|Terra)',
    r'núcleos?\s+atômicos?',
    # "sinal" is a signal (g10) and, in these phrases, the algebraic sign
    # of a charge, of a cosine, of a work. The "de $" branch matches the
    # opening $ with a LOOKAHEAD and never consumes it: consuming it would
    # leave the inline-math rule pairing the closing $ of that formula with
    # the next formula's opening one, masking the rest of the file inside
    # out and silently dropping every link after it (see the warning at the
    # top of tools/termlink/protect.py).
    # \s+ and not a literal space: the list is compiled with re.S and the
    # phrase may straddle a line break ("de mesmo\nsinal" in g11 ch04 did,
    # and that link survived the first audit because of it).
    r'(?:mesmo|único)\s+sinal',
    r'sinais?\s+(?:opostos?|iguais)',
    r'sinal\s+(?:de\s+(?=\$)|de\s+\\cos|compara)',
    r'(?:significado|troca|mudança)\s+d[eo]s?\s+sinal',
    r'muda(?:ria)?\s+de\s+sinal',
    r'sinais,\s+casos-limite',
    r'com\s+sinal',        # "todos números com sinal" -- signed numbers
    r'sinal\s*&',          # the "sign" row of the gravity/electricity table
    # complementary ANGLES (g12 projectile range), not complementary colours;
    # English does not link its bare "complementary" at all. The four honest
    # uses in the colour chapter («amarelo e azul são complementares») keep
    # their link.
    r'(?:ângulos?|par)\s+complementar(?:es)?',
]
