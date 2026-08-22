"""Book 4 -- pt (Brazilian Portuguese). Curation only; the rules live in
tools/termlink/.

Every key is optional: anything left out falls back to the defaults in
tools/link_defined_terms.py (empty sets, AMBIG_POLICY "drop").

Curated 2026-08-22 from the harvested list (`--terms`) of the translated
31-chapter book, against the English curation (`book4_en.py`) and the
Portuguese one of Book 3 (`book3_pt.py`).  Regenerate with:

    python3 tools/link_defined_terms.py --book 4 --lang pt --unwrap --apply
    python3 tools/link_defined_terms.py --book 4 --lang pt --apply

This is a curation, not a translation of `book4_en.py`: the two languages cut
the vocabulary in different places.  It replaces the Book 3 seed that was
copied here on 2026-08-22; what survives of that seed is only what Book 4
actually harvests (checked entry by entry against `--terms`).

What Book 4 pt does NOT need, although Book 3 pt did:
  * the whole *tensão* apparatus.  Book 3 had to protect twenty mechanical
    sites so the electrical sense could keep its links; Book 4 never harvests
    bare *tensão* at all -- the only terms are *tensão superficial* and
    *tensão de cisalhamento* -- so no link can land on either sense and
    EXTRA_PROTECT is empty, exactly as in `book4_en.py`.  (Both senses are in
    this volume: the rope tension of ch. 1 and the voltage of chs. 8--10.
    Neither is linkable, in either language.)
  * *sinal*, *casca*, *núcleo*, *fluxo*, *momento*, *imagem*, *foco*, *ganho*,
    *unidade*, *dimensão*, *transformação*, *bar*: none of them is a Book 4
    term.  Book 4's bare-noun terms are a different, much shorter set.
  * `resistência do ar` / `potências de dez`: bare *resistência* and bare
    *potência* are not Book 4 terms either, so the two Book 3 protections are
    inert here and are dropped.
  * the Book 3 EXTRA entry for *comprimento de onda de De Broglie*.  It points
    at `thm:b1:quantum-introduction:debroglie`, a **Book 3 label**: kept here
    it would wrap a term on a target that does not exist in this volume and
    put an undefined reference in the log.  Book 4 states de Broglie's
    relation in ch. 30 without an \\omterm target of its own, exactly as the
    English edition does.
"""

# See the long note in book3_pt.py: the shared default is the English wording
# of the same idea, and a named RESULT is not a term.  It must be translated
# or the filter is inert and Portuguese harvests index entries English never
# linked -- but NOT word for word.  harvest.py tests plain substring
# containment, so a bare keyword fires whatever the word order ("Archimedes'
# theorem" / "teorema de Arquimedes").  The trap is the one PHRASE in the
# default, "law of": it is position-dependent and never fires on English's own
# possessive ("Ohm's law"), whereas Portuguese puts the keyword first ("lei de
# Ohm"), so a literal "lei de" would delete every named-law link with no gate
# complaint.  It is deliberately absent.  "método" and "enunciado" are absent
# for the same reason: the English default carries neither.
NOT_A_TERM = ("teorema", "lema", "desigualdade", "fórmula", "critério",
              "princípio", "identidade", "regra", "paradoxo", "problema")

# Ordinary language in this register, or a word whose sense elsewhere in the
# book is not the sense its definition gives it.  (A STOPped word is still
# linked inside the chapter that defines it.)  One for one with book4_en.py.
STOP = {
    # "laser" is named in every optics chapter long before ch. 23 defines it
    # (chs. 18--22 all use it); a link on each occurrence would be noise.
    "laser",
    # the laser threshold of ch. 23 vs the hearing threshold of ch. 6, the
    # perception threshold of ch. 24 and "acima do limiar" everywhere.
    # ("limiar de audição" survives as a term of its own.)
    "limiar",
    # English stops "steady" (the steady flow of ch. 27).  Portuguese has to
    # stop it twice over: *estacionário* is both "steady" (regime/escoamento
    # estacionário, chs. 2--5, 25, 27) and "stationary" (estado estacionário,
    # chs. 30--31), so the bare adjective is on nearly every page of two
    # different halves of the book.  "estado estacionário" and "escoamento
    # estacionário" survive as terms.
    "estacionário",
    # cycle and turbine efficiency (chs. 23, 27) vs fin efficiency (ch. 25),
    # luminous efficiency (ch. 26), quantum efficiency.  "eficiência de uma
    # aleta" survives.
    "eficiência",
    # absorption of light (ch. 23) vs absorption of sound (ch. 6), of heat
    # (chs. 25--26), of a diffusing species (ch. 24).
    "absorção",
}

NO_CAPITAL = {
    # capitalized, these are the physicists, not the units -- and unlike
    # Spanish (julio, voltio, culombio, ohmio), Portuguese spells the two
    # alike.  The book writes "lei de Ampère", "efeito Joule", "leis de
    # Newton".  Same list as book4_en.py.
    "newton", "joule", "watt", "pascal", "kelvin", "tesla", "hertz",
    "coulomb", "volt", "ampère", "ohm", "henry", "farad", "weber",
}

EXTRA = {
    # the devices of ch. 27 are introduced capitalised at the head of an
    # \item, so the harvester only ever sees the capitalised form; link the
    # lowercase nouns too, exactly as book4_en.py does for throttle/nozzle.
    "bocal": "prop:b2:open-systems:devices",
    "estrangulamento": "prop:b2:open-systems:devices",
    "trocador de calor": "prop:b2:open-systems:devices",
    # two phrases the harvester cannot keep, both linked in English:
    #   * "rotação em torno de um eixo fixo" is SIX words (English's
    #     "rotation about a fixed axis" is five), one over MAX_TERM_WORDS;
    #   * "espectroscopia por transformada de Fourier" is 41 characters
    #     (English's "Fourier transform spectroscopy" is 30), one over
    #     MAX_TERM_CHARS.
    # EXTRA is subject to neither cap, so both recover the English link
    # rather than raising the caps for the whole book.
    "rotação em torno de um eixo fixo": "rem:b2:rigid-body-mechanics:motions",
    "espectroscopia por transformada de Fourier": "prop:b2:michelson:measure",
}

DROP = {
    # bare adjectives and harvest artefacts, one for one with book4_en.py
    # ("quantised", "Eulerian", and the titles cut at a line break).
    # Portuguese harvests the participle "quantizadas" from
    # \emph{quantizadas} in ch. 31 and the adjective "euleriana" from
    # \emph{descrição euleriana}; "descrição euleriana" survives as a term.
    "quantizadas", "euleriana",
    # English DROPs the bare adjectives "three-level" and "four-level"; the
    # Portuguese \emph{} carries the same two, and left in they link nine
    # ordinary occurrences of "três/quatro níveis" in ch. 23 that English
    # never links.  "laser de três níveis" / "laser de quatro níveis" stay
    # as terms (they occur only in \index{}, exactly as in English).
    "três níveis", "quatro níveis",
    # the itemize head of ch. 27 is a list of three devices, not a term; the
    # three nouns are reached through EXTRA above.  (English harvests the
    # same artefact, "Compressor, pump, turbine".)
    "Compressor, bomba, turbina",
}

# Irregular plurals only.  lang_pt.py sets TAIL_ON_EVERY_WORD = True, so the
# regular Portuguese plural of a phrase is generated by the rule itself
# ("linha de campo" -> "linhas de campo", "coeficiente de reflexão" ->
# "coeficientes de reflexão").  What the per-word tail "(?:e?s)?" cannot
# produce is the stem-changing plural: "-ão" -> "-ões", "-al" -> "-ais",
# "-m" -> "-ns".  Every entry below was generated from the Book 4 harvest and
# then checked to occur, with word boundaries, in this edition's own corpus;
# a plural the book never writes is not listed, because the harvester would
# drop it anyway.
DERIVED = {
    "bocal": ("bocais",),
    "corrente superficial": ("correntes superficiais",),
    # "decibel" -> "decibéis": the tail rule offers "decibels"/"decibeles",
    # neither of which the book writes.  Without this the pt edition linked
    # the word once against English's seven.
    "decibel": ("decibéis",),
    "equação de Euler": ("equações de Euler",),
    "escoamento irrotacional": ("escoamentos irrotacionais",),
    "frequência espacial": ("frequências espaciais",),
    "função de onda": ("funções de onda",),
    "mancal": ("mancais",),
    "máximo principal": ("máximos principais",),
    "onda longitudinal": ("ondas longitudinais",),
    "polarização circular": ("polarizações circulares",),
    "polarização retilínea": ("polarizações retilíneas",),
    "potencial químico": ("potenciais químicos",),
    "potencial vetor": ("potenciais vetores",),
    "realimentação": ("realimentações",),
    "reação normal": ("reações normais",),
    "relação de dispersão": ("relações de dispersão",),
    "trem de ondas": ("trens de ondas",),
    "velocidade terminal": ("velocidades terminais",),
}

PRIMARY_OK = set()

# Empty, like book4_en.py: this volume has no Portuguese homograph that a
# link can land on.  See the header for why the Book 3 *tensão* block does
# not carry over.  If one is ever added, remember the two rules at the top of
# tools/termlink/protect.py: never consume a `$` (match it with a lookahead),
# and never write a literal space (always `\s+`).
# NOT added, deliberately: "divergência" as an alternate of "divergente".
# Portuguese splits what English spells one way -- *divergente* is the vector
# operator of ch. 11, *divergência* is the angular spread of a laser beam in
# ch. 23 -- and the English canon, having a single word, links nine ch. 23
# beam divergences to `def:b2:maxwell-equations:operators`.  Listing the
# second form here would faithfully reproduce an English mis-link; leaving it
# out is why this edition shows 37 links on that target against English's 44.

EXTRA_PROTECT = []

AMBIG_POLICY = "drop"          # the university convention (books 3, 4, 5)
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40
