"""Book 3 -- pt (Brazilian Portuguese). Curation only; the rules live in
tools/termlink/.

Every key is optional: anything left out falls back to the defaults in
tools/link_defined_terms.py (empty sets, AMBIG_POLICY "drop").

Curated 2026-08-21 from the harvested list (`--terms`) of the translated
30-chapter book, against the English curation (`book3_en.py`) and the
Portuguese one of Book 2 (`book2_pt.py`).  This is a curation, not a
translation of `book3_en.py`: the two languages cut the vocabulary in
different places.

What Portuguese does NOT need, although English stops it:
  * "objective" is stopped in English because it is also an adjective;
    the Brazilian *objetiva* is only ever the lens of ch. 4 here, so it
    keeps its 30-odd links.
  * "câmara"/"câmera" -- Spanish had to stop *cámara* (camera and cold
    chamber are one word); Portuguese spells the chamber *câmara* and the
    camera *câmera*, so no stop is needed.
  * *torque* is the Brazilian word for the moment of a force, so the
    Spanish clash on *par* ("a pair of") does not arise.
  * *capacitância* is not *capacidade*, so the Spanish clash on
    *capacidad* does not arise either.
  * the French edition had to stop *solide*; Portuguese names the rigid body
    *corpo rígido*, so bare *sólido* is never harvested as a term at all and
    its two dozen ordinary uses ("estado sólido", "esfera sólida", "ângulo
    sólido") cannot be mislinked. The label def:b1:systems-of-points:solid is
    reached through *corpo rígido* four times, against English's three.
  * the French edition had to DROP *centrale* (the power station); the
    Brazilian power station is a *usina*, and bare *central* is dropped here
    only as a stray adjective -- see DROP below.

What Portuguese needs and English does not:
  * *sinal* is both the signal of ch. 5 and the algebraic sign of a charge,
    of a work, of a determinant -- roughly half of its 98 occurrences.
  * *casca* is both the cladding of an optical fibre (ch. 2) and the
    spherical/cylindrical shell of chs. 21, 26, 27.
  * *tensão* is both the rope's tension and the circuit's voltage.  Unlike
    Spanish, this file does NOT stop it: the mechanical sense is confined
    to about twenty enumerable sites in chs. 12--15, 21 and 25, which
    EXTRA_PROTECT masks one by one, so the 100-odd electrical uses keep the
    links English gives its "voltage".
"""

# The shared default is the English wording of the same idea ("theorem",
# "lemma", "principle", ...): a named RESULT is not a term, the point being to
# link definitions. It must be translated, or the filter is inert and
# Portuguese harvests two dozen "teorema de ...", "princípio de ..." index
# entries that English never linked (English has no single \omterm on a
# "theorem", "principle", "rule", "formula", "inequality", "criterion" or
# "identity" display -- verified, all zero).
#
# BUT IT CANNOT BE TRANSLATED WORD FOR WORD. The test in harvest.py is plain
# substring containment, not position, so a bare keyword fires in both
# languages whatever the word order: English "Archimedes' theorem" and
# Portuguese "teorema de Arquimedes" are both caught by their keyword, and the
# two editions stay symmetric. The trap is the one PHRASE in the default,
# "law of", which is position-dependent and therefore never fires on English's
# own possessive form ("Ohm's law", "Gauss's law"): English links 70 named-law
# displays. Portuguese puts the keyword FIRST -- "lei de Ohm" -- so a literal
# "lei de" would fire on every one of them and delete the lot, with no gate
# complaint from any of the eight checks. It is deliberately absent, and this
# edition ships 77 named-law links against English's 70.
#
# The same reasoning keeps "método" and "enunciado" out: the English default
# carries neither "method" nor "statement", so English links "Bessel's method"
# and harvests the Clausius/Kelvin statements, and Portuguese must keep
# "método de Bessel", "método de Silbermann", "enunciado de Clausius" and
# "enunciado de Kelvin" linkable too. (The French edition of this same book
# lost 88 links and 5 target labels outright by translating the list
# literally; the Portuguese one loses 32 links and, verified label by label,
# ZERO targets -- every label the filter suppresses here is either equally
# unreachable in English, because English's own filter suppresses the same
# class, or still reached through another term at a count at or above
# English's.)
#
# NOT_A_TERM is also SUBJECT- and LEVEL-specific: book2_pt.py, the school
# book, leaves it empty and is right to, because a spiral curriculum links its
# result names on purpose. Check, do not copy.
NOT_A_TERM = ("teorema", "lema", "desigualdade", "fórmula", "critério",
              "princípio", "identidade", "regra", "paradoxo", "problema")

# Ordinary language in this register, or a word whose sense elsewhere in the
# book is not the sense its definition gives it. (A STOPped word is still
# linked inside the chapter that defines it.)
STOP = {
    # the bare nouns of mechanics and thermodynamics: from chapter 12 on they
    # are on every page, and a link on each is noise. Every compound
    # ("força central", "velocidade angular", "pressão cinética", "trabalho
    # perdido", "calor latente", "centro de massa", ...) survives as a term
    # of its own.
    "força", "massa", "velocidade", "aceleração",
    "pressão", "temperatura", "calor", "Calor", "trabalho",
    # the Portuguese for "momentum", stopped in English for the same reason;
    # "conservação da quantidade de movimento" survives.
    "quantidade de movimento",
    # the unit (kinetic theory, ch. 20). English stops it for the sliding bar
    # of the Laplace rails -- which Portuguese calls *barra*, so the reason
    # here is only density: chs. 21--25 write \qty{}{bar} on nearly every
    # page. Linked inside ch. 20, exactly as in English.
    "bar",
    # moment of a force (ch. 15) vs "no momento em que", "por um momento".
    # "momento angular", "momento de inércia", "momento dipolar", "momento
    # magnético", "momento de uma força" all survive.
    "momento",
    # the optical image (ch. 3) vs "imagem especular" in the symmetry
    # chapters and "a imagem ondulatória" in ch. 30. "imagem real",
    # "imagem virtual", "foco imagem" survive.
    "imagem",
    # the focus of a mirror or a lens (ch. 3) vs "o foco de uma fonte", and
    # the verb-like uses. "distância focal", "foco imagem", "plano focal"
    # are unaffected.
    "foco",
    # op-amp gain (ch. 10) vs the ordinary "ganho" of anything --- energia,
    # resolução, velocidade. "ganho em malha aberta" and "produto
    # ganho--largura de banda" survive.
    "ganho",
    # the fibre core (ch. 2) vs the Earth's core (ch. 26), the coaxial core
    # (ch. 28), the iron core of a coil and the atomic nucleus (chs. 26--30)
    # --- all "núcleo" in Portuguese.
    "núcleo",
    # the cladding of a fibre (ch. 2) vs the spherical shell of ch. 26
    # ("teorema das cascas", "casca esférica espessa"), the cylindrical
    # shell of ch. 21 and the "casca por casca" of ch. 27.
    "casca",
    # the flux of the electric field (ch. 26) vs the magnetic flux (ch. 29);
    # "fluxo do campo elétrico", "fluxo magnético" and "conservação do fluxo
    # (magnético)" survive.
    "fluxo",
    # the SI unit (ch. 1) vs "vetor unitário", "por unidade de comprimento",
    # "unidade de massa". "unidade de base" and "unidade derivada" survive.
    "unidade",
    # the physical dimension (ch. 1) vs "as dimensões da sala", "em uma
    # dimensão", "de dimensão dois".
    "dimensão",
    # the thermodynamic transformation (ch. 22) vs ordinary usage elsewhere;
    # "transformação adiabática", "transformação reversível", ... survive.
    "transformação",
    # THE Portuguese trap of this book: *sinal* is the signal of ch. 5 and,
    # about as often, the algebraic sign ("convenção de sinais", "cargas de
    # mesmo sinal", "o sinal de menos", "verifique o sinal"). No pattern
    # list separates "o sinal de teste" from "o sinal de $q$" reliably, so
    # the word is linked only inside ch. 5; "sinal senoidal" survives
    # everywhere, and so does every other term of the chapter (amplitude,
    # fase, celeridade, comprimento de onda, ...).
    "sinal",
}

NO_CAPITAL = {
    # capitalized, these are the physicists, not the units --- and unlike
    # Spanish (julio, voltio, culombio, ohmio, faradio, henrio, amperio),
    # Portuguese spells the two alike. The book writes "leis de Newton",
    # "efeito Joule", "lei de Coulomb", "lei de Ohm", "lei de Ampère".
    "newton", "joule", "watt", "pascal", "kelvin", "tesla", "hertz",
    "coulomb", "volt", "ampère", "ohm", "henry", "farad", "weber",
    "siemens", "gauss", "becquerel", "curie", "sievert",
}

EXTRA = {
    # English harvests "de Broglie wavelength" (three words) and links it in
    # ch. 30; the Portuguese phrase is six words, one over MAX_TERM_WORDS, so
    # the harvester drops it and the inner "comprimento de onda" links to the
    # sinusoidal wave of ch. 5 instead -- right notion, wrong statement. EXTRA
    # is not subject to the length cap, and wrap_file matches the longest term
    # first, so the whole phrase wins wherever it occurs.
    "comprimento de onda de De Broglie":
        "thm:b1:quantum-introduction:debroglie",
}

DROP = {
    # bare adjectives harvested from definitions that merely use them. The
    # phrases they came from --- "gás ideal", "amplificador operacional
    # ideal", "circuito linear", "regime linear", "sistema linear de segunda
    # ordem", "força central", "força conservativa" --- all survive as terms
    # of their own.
    "ideal", "linear", "central", "conservativa",
    # harvested from "\emph{central conservativa}": a two-word adjective
    # phrase, never a noun phrase in prose.
    "central conservativa",
}

# Irregular plurals only. lang_pt.py sets TAIL_ON_EVERY_WORD = True, so the
# regular Portuguese plural of a phrase is generated by the rule itself
# ("linha de campo" -> "linhas de campo", "força conservativa" -> "forças
# conservativas"). What the per-word tail "(?:e?s)?" cannot produce is the
# stem-changing plural: "-ão" -> "-ões", "-al" -> "-ais", "-ar" -> "-ares",
# "-r" -> "-res", "-m" -> "-ns". The entries below are the ones this book
# actually writes in the plural (checked against the corpus; a form that
# does not occur is dropped by the harvester anyway).
DERIVED = {
    "força central": ("forças centrais",),
    "ponto material": ("pontos materiais",),
    "momento angular": ("momentos angulares",),
    "velocidade angular": ("velocidades angulares",),
    "frequência angular": ("frequências angulares",),
    "função de transferência": ("funções de transferência",),
    "função de onda": ("funções de onda",),
    "transformação adiabática": ("transformações adiabáticas",),
    "transformação reversível": ("transformações reversíveis",),
    "transformação irreversível": ("transformações irreversíveis",),
    "transformação isotérmica": ("transformações isotérmicas",),
    "transformação quase-estática": ("transformações quase-estáticas",),
    "reflexão total": ("reflexões totais",),
    "ordem de grandeza": ("ordens de grandeza",),
    "referencial inercial": ("referenciais inerciais",),
    "gás ideal": ("gases ideais",),
    "gás perfeito": ("gases perfeitos",),
    "potencial elétrico": ("potenciais elétricos",),
    "superfície equipotencial": ("superfícies equipotenciais",),
    "energia potencial": ("energias potenciais",),
    "condição inicial": ("condições iniciais",),
    "linha de campo": ("linhas de campo",),
    "máquina térmica": ("máquinas térmicas",),
    "nível de energia": ("níveis de energia",),
    "dipolo linear": ("dipolos lineares",),
    "resolução angular": ("resoluções angulares",),
    "onda progressiva": ("ondas progressivas",),
    "onda estacionária": ("ondas estacionárias",),
}

PRIMARY_OK = set()

# Two rules hold for EVERY pattern below, not only for the ones already caught
# failing (the warnings at the top of tools/termlink/protect.py and of
# tools/term_config/book2_pt.py):
#   * NEVER consume a `$` -- match it with a lookahead. The list is one
#     alternation scanned left to right, so eating an opening $ leaves the
#     inline-math rule pairing the closing $ with the next formula's opening
#     one, and the mask runs inside out to end of file, silently dropping
#     every link after it.
#   * NEVER write a literal space -- always `\s+`. The list is compiled with
#     re.S and real prose wraps.
EXTRA_PROTECT = [
    # --- *tensão*: the rope's tension, not the circuit's voltage. -------
    # Every mechanical site of chs. 12--15, 21 and 25, enumerated against the
    # corpus; the electrical uses of chs. 5--10, 17 and 26--29 stay linked.
    r'\\emph\{tensão\}',
    r'tens(?:ão|ões)\s+d[eoa]s?\s+(?:um\s+|uma\s+)?(?:fio|corda|cabo|haste)',
    r'tens(?:ão|ões)\s+(?:é|são)\s+(?:transmitida|central|radial|a\s+mesma)',
    r'tensão\s+(?:máxima|superficial)',
    r'tensão\s+de\s+compressão',
    r'tensão\s+encontra\s+o\s+eixo',
    r'(?:escrever|Deduza)\s+a\s+tensão',
    r'tensão\s+consegue',
    r'duas\s+tensões',
    r'linha\s+de\s+ação\s+da\s+tensão',
    r'tensão\s+ali\b',
    r'tensão\s+no\s+ponto\s+mais',
    r'[Tt]ensão:\s*(?:momento|(?=\$))',
    r'(?:aceleração|período)\s+e\s+a\s+tensão',
    r'e\s+tensão\s+(?=\$)',
    # --- other Portuguese homographs the term list cannot see -----------
    # mechanics' drag of the air, not the electrical quantity
    r'resistência\s+d[oe]\s+ar',
    # a mathematical power, not the physical one
    r'potências?\s+de\s+(?:dez|dois)',
]

AMBIG_POLICY = "drop"          # the university convention (books 3, 4, 5)
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40
