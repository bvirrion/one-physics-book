"""Book 5 -- pt (Brazilian Portuguese). Curation only; the rules live in
tools/termlink/.

Curated 2026-09-03 from the harvested list (`--terms`) of the translated
27-chapter book, against the English curation (`book5_en.py`).  Regenerate
with:

    python3 tools/link_defined_terms.py --book 5 --lang pt --unwrap --apply
    python3 tools/link_defined_terms.py --book 5 --lang pt --apply

This replaces the `book4_pt.py` seed that was copied here by the coordinator
of the Book 5 translation run.  Every entry of that seed was re-tested against
Book 5's own harvest; what survives is only what Book 5 actually needs.

Audit of the seed (the trap the seed's own docstring warns about is a STOP
entry that silently DELETES a term this book does define):

  * `STOP` carried five Book 4 words -- *absorção*, *eficiência*,
    *estacionário*, *laser*, *limiar*.  Re-running the harvest with STOP
    emptied shows that Book 5 defines **none** of them, so all five were inert
    rather than masking; they are dropped as noise.  The four that do change
    the harvest are kept below.
  * the seed also carried *buraco* and *lacuna* as the Portuguese of English's
    STOPped "hole".  With STOP emptied neither is harvested: the semiconductor
    hole of ch. 24 is `\emph{lacuna}` in two different definitions
    (`def:...:classes` and `def:...:doping`), so AMBIG_POLICY "drop" already
    removes it, and *buraco* only ever occurs inside *buraco negro*, which is
    a term of its own.  Both are dropped, with no change to the link set.
  * `EXTRA` stays empty, and this was checked rather than assumed: the
    Portuguese harvest reaches every target the English harvest reaches (and
    nine more), so there is no English link this edition cannot make.  A
    seeded `b2:` label would have shipped as an undefined reference.
  * `MAX_TERM_WORDS` / `MAX_TERM_CHARS` are deliberately NOT set.  Book 4 set
    5/40 because `book4_en.py` did; `book5_en.py` sets neither, and adding a
    cap here would drop Portuguese terms the English edition keeps.
"""

# The shared default is the English wording of the same idea; left untranslated
# it is inert, and Portuguese then harvests named results English never linked.
# NOT word for word, though: harvest.py tests plain substring containment, so a
# bare keyword fires whatever the word order ("Archimedes' theorem" / "teorema
# de Arquimedes").  The trap is the one PHRASE in the default, "law of": it is
# position-dependent and never fires on English's own possessive ("Ohm's law"),
# whereas Portuguese puts the keyword first ("lei de Ohm"), so a literal
# "lei de" would delete every named-law link of this book -- Planck's, Bragg's,
# Hubble's, Hooke's, Curie--Weiss -- with no gate complaint.  Deliberately
# absent.
NOT_A_TERM = ("teorema", "lema", "desigualdade", "fórmula", "critério",
              "princípio", "identidade", "regra", "paradoxo", "problema")

# Ordinary language in this register, or a word whose sense elsewhere in the
# book is not the sense its definition gives it.  (A STOPped word is still
# linked inside the chapter that defines it.)  These four are exactly the
# Book 5 English STOP set minus "hole", which has no bare Portuguese
# counterpart that harvests -- see the audit note in the header.
STOP = {
    # o spin quântico do cap. 12 contra "a estrela gira", "período de
    # rotação", "aceleração de rotação" dos caps. 25--27
    "spin",
    # o metal da teoria de bandas (cap. 24) contra o ferro-velho, o metal
    # precioso e as panelas de metal dos caps. 22--23
    "metal",
    # o evento do espaço-tempo (cap. 4) contra a contagem de eventos em
    # detectores e em estatística (caps. 16, 26)
    "evento",
    # o observável hermitiano (cap. 8) contra o adjetivo ("universo
    # observável", "efeitos observáveis")
    "observável",
    # A dilatação volumétrica do cap. 3 (`def:...:strain`) contra a dilatação
    # DO TEMPO dos caps. 4--5 e a dilatação TÉRMICA do cap. 16.  Inglês tem
    # três palavras separadas -- strain, dilation, expansion -- e nunca liga
    # "dilatation" ao alvo da deformação; o português usa uma só, e o
    # morfologizador ligava as três acepções ao alvo do cap. 3 (nove links
    # contra os três do inglês, dos quais três eram simplesmente da acepção
    # errada).  STOP mantém os links dentro do capítulo que define o termo,
    # de modo que os do cap. 3 sobrevivem; "dilatação do tempo" é um termo
    # distinto, com alvo próprio, e não é afetado (verificado, não suposto).
    "dilatação",
}

NO_CAPITAL = {
    # capitalized these are the physicists, not the units; Portuguese spells
    # the two alike (unlike Spanish julio/voltio/ohmio).  The book writes
    # "lei de Ampère", "efeito Joule", "constante de Boltzmann".
    "ampère", "coulomb", "farad", "henry", "hertz", "joule", "kelvin",
    "newton", "ohm", "pascal", "tesla", "volt", "watt", "weber",
}

# Checked, not assumed: `--terms` for pt reaches every target `--terms` for en
# reaches.  Nothing to recover.
EXTRA = {}

DROP = set()

# Irregular plurals only.  lang_pt.py sets TAIL_ON_EVERY_WORD = True, so the
# regular Portuguese plural of a phrase is generated by the rule itself
# ("nível de energia" -> "níveis"? no: "-el/-al/-ão/-m" is exactly what the
# per-word tail "(?:e?s)?" cannot produce).  Every entry below was generated
# from this edition's own harvest and then checked to occur, with word
# boundaries, in this edition's own corpus; a plural the book never writes is
# not listed, because the harvester would drop it anyway.
DERIVED = {
    "cristal": ("cristais",),
    "interação forte": ("interações fortes",),
    "oscilação de Rabi": ("oscilações de Rabi",),
    "polarização": ("polarizações",),
    "potencial químico": ("potenciais químicos",),
    "referencial inercial": ("referenciais inerciais",),
    "seção de choque": ("seções de choque",),
    "transição de fase": ("transições de fase",),
    "tração": ("trações",),
}

PRIMARY_OK = set()

# Two Portuguese collocations that English cannot produce, both of them a
# term of this book used in an ordinary sense.  See the two rules at the top
# of tools/termlink/protect.py: never consume a `$`, never write a literal
# space (always `\s+`).
EXTRA_PROTECT = [
    # "polarizacao direta/reversa" is diode BIASING, not the P field of a
    # dielectric. English cannot collide here: it writes "forward bias" and
    # "reverse bias", and the word "polarisation" does not occur anywhere in
    # its chapter 24. Three links in ch. 24 pointed at
    # def:b3:electromagnetism-in-matter:polarisation (bound charges,
    # dielectrics) before this mask. Live in all three Romance editions;
    # absent from nl (doorlaatrichting) and id (panjar maju).
    r"[Pp]olarização\s+(?:direta|reversa|inversa)",
    # "ação" is the action of ch. 1 (def:b3:lagrangian-mechanics:action) and
    # English links "action" too -- but the English canon writes "at work"
    # where this edition writes "em ação" (eleven sites, chs. 5--26, none of
    # them the Lagrangian action).  Without this the pt edition would carry
    # eleven links English does not have.
    r'em\s+ação',
    # "rede" is the crystal lattice of ch. 23; the diffraction grating of
    # ch. 23's own solutions ("rede de cinco fendas") is the other sense, and
    # it sits in the defining chapter, where a STOP would not protect it.
    r'rede\s+de\s+cinco\s+fendas',
]

AMBIG_POLICY = "drop"          # the university convention (books 3, 4, 5)
