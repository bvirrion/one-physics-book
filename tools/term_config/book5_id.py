"""Book 5 -- id. Curation only; the rules live in tools/termlink/.

Curated 2026-09-03 against Book 5's own Indonesian harvest
(`python3 tools/link_defined_terms.py --book 5 --lang id --terms`), from the
seed the coordinator built out of `book4_id.py`. Regenerate the links with:

    python3 tools/link_defined_terms.py --book 5 --lang id --unwrap --apply
    python3 tools/link_defined_terms.py --book 5 --lang id --apply

What the audit found, and what it changed.

`NOT_A_TERM` (added). The shared default is English-only, and `harvest.py`
matches it as a SUBSTRING anywhere in the display, so English's "theorem",
"formula", "principle" and "rule" silently block *Noether's theorem*,
*the Sackur--Tetrode formula*, *Hamilton's principle* and *the Born rule*.
Indonesian writes every one of those with the result-name in FRONT
("teorema Noether", "rumus Sackur--Tetrode", "asas Hamilton", "kaidah Born"),
so without an Indonesian list this edition would have linked fourteen result
names English deliberately does not. Two heads that look like obvious members
are deliberately absent:

  * `hukum` -- the English default blocks only "law of X", never "X's law",
    so English KEEPS Bragg's, Hooke's, Hubble's, Planck's, Dulong--Petit's
    and the radioactive decay law. Indonesian writes all six "hukum X";
    blocking the head would cost this book those six links.
  * `lema` and `aturan` -- both are substrings of ordinary Book 5 terms
    ("interaksi le-ma-h", "parameter keter-atura-n"). With a substring
    matcher they are not conservative, they are destructive.

`STOP` (pruned). The seed carried five Book 4 words (Ambang, Efisiensi,
Laser, Serapan, Tunak, and their lowercase twins). None of them is a defined
term anywhere in Book 5 -- the harvest drops exactly four entries, all of
them Book 5's own -- so every one was inert and has been removed. What
remains is Book 5's own STOP set (`book5_en.py`) in this edition's actual
spellings, each listed in both cases because a capitalised display is a
separate harvest entry and bypasses STOP.

English STOPs five words; Indonesian drops four, and the difference is
correct, not a miss: English's *observable* is the bare noun, while this
edition writes the defined term as "besaran teramati", which is multi-word
and therefore never matched by the bare `teramati`.

`EXTRA` (stays empty, and this was checked, not assumed). Diffing this
edition's target set against English's found every English target reached:
`comm -23 en_targets id_targets` is empty, and the Indonesian harvest reaches
133 targets against English's 124. There is nothing for `EXTRA` to repair.

`EXTRA_PROTECT` (stays empty, and this was checked too). Indonesian
morphology can invent a homograph -- `lang_nl.py` inflected *ket* into the
ordinary Dutch word for *chain* and produced 38 wrong links -- so the
generated `\omterm` surface forms were counted and their frequency table
compared against English's. No Indonesian term came out implausibly ahead of
its English twin, so no mask is needed. Any pattern added later must obey the
two standing rules: never consume a `$` (match it with a lookahead, or the
inline-math rule pairs the wrong delimiters and the links vanish silently),
and never write a literal space -- always `\s+`, because the list is compiled
with `re.S` and real prose wraps.
"""

# Heads of Indonesian result-names. See the module docstring for why `hukum`,
# `lema` and `aturan` are deliberately absent.
NOT_A_TERM = ("teorema", "rumus", "asas", "prinsip", "kaidah",
              "ketaksamaan", "kriteria", "identitas", "paradoks", "soal")

# A STOPped word is still linked inside the chapter that defines it.
# CAPITALISED forms are a separate harvest entry and bypass STOP, so every
# word is listed in both cases.
STOP = {
    # quantum spin (ch. 12) vs a star spinning in chs. 25-27
    "spin", "Spin",
    # the band-theory metal (ch. 24) vs scrap metal in chs. 22-23
    "logam", "Logam",
    # the spacetime event (ch. 4) vs counting events in chs. 16 and 26
    "peristiwa", "Peristiwa", "kejadian", "Kejadian",
    # the Hermitian observable (ch. 8) vs the adjective
    "teramati", "Teramati",
    # the semiconductor hole (ch. 24) vs the black hole of ch. 27
    "lubang", "Lubang",
}

NO_CAPITAL = {
    # unit names: never capitalised mid-sentence in Indonesian either.
    "ampere", "coulomb", "curie", "farad", "henry", "hertz", "joule",
    "kelvin", "newton", "ohm", "pascal", "tesla", "volt", "watt", "weber",
}

EXTRA = {}

DROP = set()

DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"          # the university convention (books 3, 4, 5)
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40

EXTRA_PROTECT = []
