"""Book 5 -- es. Curation only; the rules live in tools/termlink/.

SEED, not a finished curation. Written 2026-09-02 by the coordinator of the
Book 5 translation run, from `book4_es.py`. What carries over between books
of one language is the language's own judgement -- its homographs, its
capitalisation traps, its protect patterns -- and that is all that was
copied. What does NOT carry over was deliberately emptied:

  * `EXTRA` -- every Book 4 value was a `b2:` label. A seeded `EXTRA` pointing
    at the previous book's labels ships as an undefined reference and nothing
    warns you (the audit across eight Book 4 configs found `nl` with 67 such
    entries, `ar` with 23). Rebuild it against Book 5's own labels, by diffing
    this edition's target set against English's:
        python3 tools/link_defined_terms.py --book 5 --lang es --terms
    then `awk '{print $NF}' | sort -u` both sides and `comm` them. One entry
    per target the English harvest reaches and this language cannot.
  * `DROP` -- Book 4 harvest artefacts, meaningless here.

`STOP` and `EXTRA_PROTECT` below are the seed's real content and are NOT
neutral: a protect pattern written to stop one book's collocation from
linking will, in a book where that collocation is the only surviving sense,
silently DELETE the links you wanted (Book 3's Indonesian `tegangan` mask
killed Book 4's only two `tegangan` terms). Audit both against Book 5's own
harvest before the first link pass.

Book 5's English curation (`book5_en.py`) STOPs five words, each for a reason
that survives translation: *spin* (the quantum spin of ch. 12 against a star
spinning in chs. 25--27), *metal* (the band-theory metal of ch. 24 against
scrap metal in chs. 22--23), *event* (the spacetime event of ch. 4 against
counting events in chs. 16 and 26), *observable* (the Hermitian observable of
ch. 8 against the adjective, "observable universe"), and *hole* (the
semiconductor hole of ch. 24 against the black hole of ch. 27). Their Spanish
renderings are listed at the end of `STOP`; prune them to the spellings this
edition actually uses.

Do not translate the `"law of"` entry of the shared `NOT_A_TERM` default: it
never fires on English, but its literal translation swallows every named law
in the book.
"""

STOP = {
    # Carried from book4_es.py and AUDITED against Book 5's own es harvest
    # (2026-09-03): all thirteen occur in Book 5 as ordinary vocabulary and
    # none of them is an `\emph{x}\index{x}` definition pair here, so
    # stopping them costs no target. `momento` (103 hits), `núcleo` (85) and
    # `tensión` (51) are the dangerous ones -- each is Book 5's everyday word
    # for momentum, atomic/stellar core and voltage/stress respectively.
    "absorción", "estacionario", "flujo estacionario", "foco", "ganancia",
    "imagen", "láser", "momento", "núcleo", "rendimiento", "tensión",
    "trayectoria", "umbral",
    # Book 5's own STOP set (book5_en.py), rendered in this language.
    # `evento` was pruned: this edition renders the spacetime event as
    # `suceso` throughout and `evento` occurs zero times.
    "espín", "spin", "metal", "suceso", "observable", "hueco",
    "agujero",
}

NO_CAPITAL = {
    # carried from book4_es.py.
    "kelvin", "newton", "pascal", "tesla", "weber",
}

# AUDITED 2026-09-03 and deliberately left empty. The target sets were
# diffed as the docstring prescribes (`--terms` for en and es, targets
# compared): this edition reaches every target the English harvest reaches,
# and nine more (Noether, Liouville, Ehrenfest, equipartición, regla de oro
# de Fermi, principio de exclusión de Pauli, espín--estadística,
# Sackur--Tetrode, Breit--Wigner). Nothing is missing, so nothing to add.
EXTRA = {}

DROP = set()

# AUDITED 2026-09-03. Book 4's only mask, r"resistencia del aire", matches
# nothing in Book 5's Spanish (zero occurrences), so it was dropped rather
# than carried as a dead pattern that could mask a future term.
#
# `en acción` is this edition's own collision, found by comparing the
# per-target link counts against English (the method the Dutch `keten` case
# established). Spanish renders "at work" / "in action" as *en acción*, which
# collides with *acción* = the mechanical action $S$ of
# `def:b3:lagrangian-mechanics:action`: twelve chapter and exercise openers
# ("Clausius--Clapeyron en acción", "cuatro fuerzas en acción") were linking
# to Lagrangian action. The mask leaves "la acción $S$", "variable de
# acción", "integral de acción" and "el cuanto de acción" linked.
EXTRA_PROTECT = [
    r"en acción",
    # The fourth collision, and the one a frequency ratio cannot see: it lands
    # on a heavily-linked target, so the count barely moves. Spanish names
    # diode biasing *polarización directa* / *polarización inversa*, which
    # collides with *polarización* = the P field of a dielectric
    # (`def:b3:electromagnetism-in-matter:polarisation`, ch. 22). English
    # cannot collide: it writes "forward bias" / "reverse bias", and the word
    # *polarisation* does not occur in its chapter 24 at all. Found by the
    # chapter-set census (a target linked in a chapter where English never
    # links it). `\s+` because one of the two sites breaks across a line.
    # Consumes no `$`, per this module's warning.
    r"polarización\s+(?:directa|inversa)",
]

AMBIG_POLICY = "drop"          # the university convention (books 3, 4, 5)
