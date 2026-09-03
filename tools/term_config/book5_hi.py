"""Book 5 -- hi. Curation only; the rules live in tools/termlink/.

SEED, not a finished curation. Written 2026-09-02 by the coordinator of the
Book 5 translation run, from `book4_hi.py`. What carries over between books
of one language is the language's own judgement -- its homographs, its
capitalisation traps, its protect patterns -- and that is all that was
copied. What does NOT carry over was deliberately emptied:

  * `EXTRA` -- every Book 4 value was a `b2:` label. A seeded `EXTRA` pointing
    at the previous book's labels ships as an undefined reference and nothing
    warns you (the audit across eight Book 4 configs found `nl` with 67 such
    entries, `ar` with 23). Rebuild it against Book 5's own labels, by diffing
    this edition's target set against English's:
        python3 tools/link_defined_terms.py --book 5 --lang hi --terms
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
semiconductor hole of ch. 24 against the black hole of ch. 27). Their Hindi
renderings are listed at the end of `STOP`; prune them to the spellings this
edition actually uses.

Do not translate the `"law of"` entry of the shared `NOT_A_TERM` default: it
never fires on English, but its literal translation swallows every named law
in the book.
"""

# AUDITED 2026-09-03 against Book 5's own hi harvest (see the score file).
# The five Book-5 entries each suppress a real homograph collision, verified
# by re-running the harvest with STOP emptied: without them the linker adds
# 65 links on five targets whose Hindi surface is an ordinary word
# (घटना/def:...:event, चक्रण/def:...:spin, धातु/def:...:classes,
# प्रेक्ष्य/def:...:observable, विवर/def:...:doping). The four Book-4
# carry-overs suppress nothing in this edition and are kept only as
# defensive vocabulary guards; "स्पिन" and "छिद्र" were pruned because this
# edition never uses those spellings.
STOP = {
    # carried from book4_hi.py -- this language's ordinary vocabulary.
    # Audited: none of these is a Book 5 defined-term surface.
    "अवशोषण", "दक्षता", "देहली", "स्थायी",
    # Book 5's own STOP set (book5_en.py), in this edition's spellings.
    # चक्रण  = quantum spin (ch. 12) vs a star spinning (chs. 25--27)
    # धातु   = band-theory metal (ch. 24) vs scrap metal (chs. 22--23)
    # घटना   = spacetime event (ch. 4) vs counting events (chs. 16, 26)
    # प्रेक्ष्य = Hermitian observable (ch. 8) vs the adjective
    # विवर   = semiconductor hole (ch. 24) vs कृष्ण विवर, black hole (ch. 27)
    "चक्रण", "धातु", "घटना", "प्रेक्ष्य", "विवर",
}

NO_CAPITAL = set()

# REBUILT 2026-09-03 against Book 5's own labels, by diffing this edition's
# harvested target set against English's (131 en / 139 hi targets). The hi
# harvest reaches nine targets English cannot and misses exactly one:
# velocity composition, whose Hindi index key "वेग-संयोजन" is hyphenated and
# so never matched the running text's own spelling. One entry, one target.
EXTRA = {
    "वेग-संयोजन": "prop:b3:relativistic-kinematics:addition",
}

# AUDITED 2026-09-03: empty. No harvest artefact to drop in this edition.
DROP = set()

# AUDITED 2026-09-03: empty on purpose. Book 5 hi needs no protect pattern --
# the harvest was re-run with STOP emptied and no collocation was found whose
# masking would be needed, and an empty list cannot delete a wanted link.
EXTRA_PROTECT = []

AMBIG_POLICY = "drop"          # the university convention (books 3, 4, 5)
