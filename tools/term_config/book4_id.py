"""Book 4 -- id. Curation only; the rules live in tools/termlink/.

Curated 2026-08-22 against Book 4's own Indonesian harvest
(`python3 tools/link_defined_terms.py --book 4 --lang id --terms`), then
audited by diffing the PER-TARGET link counts against English: target-set
parity alone hides wrong-sense links (indonesian_style_card.md 4b.8).

This file started as a verbatim copy of `book3_id.py`, whose curation was
written for a different book -- optics of instruments, electrostatics,
Newtonian mechanics.  Everything that Book 4 does not define has been
pruned rather than left as dead weight, because a stale `STOP` entry is
invisible until it silently costs links, and a stale `EXTRA_PROTECT`
pattern is worse: Book 3's

    [Tt]egangan(?:nya)?\\s+(?:tali|...|permukaan|tekan|luluh|geser)\\w*

masked exactly the two Book 4 terms *tegangan permukaan* and *tegangan
geser*, which are multi-word here and therefore need no masking at all.

The English curation for this book is `book4_en.py`; its five STOP words
(laser, threshold, steady, efficiency, absorption) are reproduced below in
Indonesian, and its two `EXTRA` entries (throttle, nozzle) become one,
because Indonesian's *katup cekik* is harvested in both cases and only
*nosel* is not.

Regenerate with:
    python3 tools/link_defined_terms.py --book 4 --lang id --unwrap --apply
    python3 tools/link_defined_terms.py --book 4 --lang id --apply
"""

# Heads of Indonesian result-names. `hukum` is deliberately absent: the
# English default blocks only "law of X", not "X's law", and Indonesian
# writes every one of them "hukum X" (hukum Curie, hukum Malus, hukum
# Stokes, hukum Snellius--Descartes, hukum Hooke, hukum Ohm, hukum Joule).
# Blocking it would cost this book eight named results.
NOT_A_TERM = ("teorema", "lema", "ketaksamaan", "rumus", "kriteria",
              "prinsip", "asas", "aturan", "identitas", "paradoks", "soal")

# A STOPped word is still linked inside the chapter that defines it, which
# is what these need. CAPITALIZED forms are a separate harvest entry and
# bypass STOP (4b.1), so every word is listed in both cases.
STOP = {
    # English's five, in Indonesian.
    # "laser" is named in every optics chapter (16, 18, 19, 20, 22, 30)
    # long before ch. 23 defines it; a link on each occurrence is noise.
    "laser", "Laser",
    # the laser threshold (ch. 23) against the hearing threshold of ch. 7,
    # the perception threshold of ch. 24 and "di atas ambangnya".
    "ambang", "Ambang",
    # the steady flow of ch. 27 against the adjective, which qualifies
    # every regime in chapters 2--5, 10, 24 and 25.
    "tunak", "Tunak",
    # cycle and turbine efficiency (ch. 27) against fin efficiency
    # (ch. 25), luminous efficiency (ch. 26), quantum efficiency.
    "efisiensi", "Efisiensi",
    # absorption of light (ch. 23) against the absorption of sound
    # (ch. 7), of heat (ch. 24) and of infrared (ch. 26).
    "serapan", "Serapan",
}

NO_CAPITAL = {
    # capitalized these are the physicists, not the units, and Indonesian
    # spells the two alike: "hukum Ohm", "efek Joule", "hukum Curie".
    # "Newton" alone shipped 23 wrong links in Book 2.
    "newton", "joule", "watt", "pascal", "kelvin", "tesla", "hertz",
    "coulomb", "volt", "ampere", "ohm", "henry", "farad", "weber",
    "curie",
}

EXTRA = {
    # ch. 27 introduces its five devices in an itemize whose items are
    # capitalised; Indonesian harvests "Nosel" but never the lowercase
    # noun the prose then uses 11 times.  (English needs the same entry
    # for "nozzle", plus one for "throttle"; Indonesian's "katup cekik"
    # is harvested in both cases already.)
    "nosel": "prop:b2:open-systems:devices",
    # ch. 27 defines the enthalpy of a flow as "\\emph{Entalpi}" at the head
    # of a sentence, so only the capitalised form is harvested; the prose
    # then writes the bare noun 17 times and reached nothing, against
    # English's 9 links on "enthalpy".  "entalpi bebas" (ch. 28) is a
    # longer match and keeps its own target.
    "entalpi": "thm:b2:open-systems:firstlaw",
}

DROP = {
    # bare adjectives and harvest artefacts, term for term with English's
    # {"quantised", "four-level", "three-level", "rotation about a fixed",
    #  "power of forces on"} -- except that English's last two entries are
    # titles truncated at a line break, and Indonesian harvests them whole:
    # "rotasi terhadap sumbu tetap" is kept, because English links
    # "rotation about a fixed axis" twice from the full title.
    "terkuantumkan",
    "tiga aras", "empat aras",
    "daya gaya pada benda tegar",
    # the itemize head of ch. 27's device list, harvested whole
    "Kompresor, pompa, turbin",
}

DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"          # university register
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40

# Book 3 needed a long mask for `tegangan` because it linked the bare
# word.  Book 4 defines only "tegangan geser" and "tegangan permukaan",
# both multi-word, so the bare noun is never a link target and nothing
# needs masking.  Two rules hold for any pattern added later:
#   * NEVER consume a `$` -- match it with a lookahead.  Eating an opening
#     $ leaves the inline-math rule pairing the closing $ with the next
#     formula's opening one and the mask runs to end of file: no error,
#     the links simply vanish (tools/termlink/protect.py).
#   * NEVER write a literal space -- always `\s+`; the list is compiled
#     with re.S and real prose wraps.
EXTRA_PROTECT = []
