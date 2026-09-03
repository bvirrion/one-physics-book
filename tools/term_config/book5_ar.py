"""Book 5 -- ar. Curation only; the rules live in tools/termlink/.

SEED, not a finished curation. Written 2026-09-02 by the coordinator of the
Book 5 translation run, from `book4_ar.py`. What carries over between books
of one language is the language's own judgement -- its homographs, its
capitalisation traps, its protect patterns -- and that is all that was
copied. What does NOT carry over was deliberately emptied:

  * `EXTRA` -- every Book 4 value was a `b2:` label. A seeded `EXTRA` pointing
    at the previous book's labels ships as an undefined reference and nothing
    warns you (the audit across eight Book 4 configs found `nl` with 67 such
    entries, `ar` with 23). Rebuild it against Book 5's own labels, by diffing
    this edition's target set against English's:
        python3 tools/link_defined_terms.py --book 5 --lang ar --terms
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
semiconductor hole of ch. 24 against the black hole of ch. 27). Their Arabic
renderings are listed at the end of `STOP`; prune them to the spellings this
edition actually uses.

Do not translate the `"law of"` entry of the shared `NOT_A_TERM` default: it
never fires on English, but its literal translation swallows every named law
in the book.
"""

STOP = {
    # AUDITED 2026-09-03 against Book 5 ar's own harvest (tools/
    # link_defined_terms.py --book 5 --lang ar --terms, run with STOP
    # emptied and diffed): these five and only these five fire, and each
    # is the spelling this edition actually uses.
    #   سبين     quantum spin (ch. 12) vs a star spinning (chs. 25--27)
    #   فلز      band-theory metal (ch. 24) vs scrap metal (chs. 22--23)
    #   حدث      spacetime event (ch. 4) vs counting events (chs. 16, 26)
    #   مرصودة   Hermitian observable (ch. 8) vs the adjective
    #   ثقب      semiconductor hole (ch. 24) vs the black hole (ch. 27)
    # The seed's other ten entries (the seven book4_ar.py carry-overs
    # "الامتصاص العتبة الليزر ليزر جسم صلب مردودها مستقر" and the three
    # alternate spellings "اللف المغزلي" "معدن" "فجوة") matched nothing in
    # this book's harvest and were pruned: an inert STOP entry is a
    # standing invitation to delete a future term silently.
    "سبين", "فلز", "حدث", "مرصودة", "ثقب",
    # Article-bearing canonical forms harvested from the definition bodies
    # (the linker harvests \emph{} phrases as well as \index{} entries, and
    # "الحدث" reached the harvest past the bare "حدث"): the chapter-set
    # census caught \omterm{...event}{الحدث} in chs. 05 and 18, where
    # English -- which STOPs *event* -- links nothing.
    "الحدث", "الثقب", "الفلز", "السبين", "المرصودة",
    # "قابل" is the semiconductor *acceptor* of ch. 24 and also the ordinary
    # Arabic adjective ("قابل للاحتراق", "قابلًا للتوجيه"): the chapter-set
    # census found it linking doping in ch. 25. "مانح" (donor) and "التطعيم"
    # carry that definition's links instead.
    "قابل",
}

NO_CAPITAL = set()

# AUDITED 2026-09-03 and deliberately left empty. `comm -23` of the English
# target set against this edition's found no target the English harvest
# reaches and the Arabic one cannot (English 124 distinct targets, Arabic
# 136, English's a subset), so there is nothing for EXTRA to repair.
EXTRA = {}

DROP = set()

# AUDITED 2026-09-03: empty. Arabic's proclitics are handled by
# tools/termlink/morphology.py, not by protect patterns; the seed carried
# none, and Book 5 ar needs none.
EXTRA_PROTECT = []

AMBIG_POLICY = "drop"          # the university convention (books 3, 4, 5)
