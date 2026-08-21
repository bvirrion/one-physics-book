"""Book 1 -- id (Indonesian). Curation only; the rules live in tools/termlink/.

Curated against the translated tree (2026-08-21), taking book1_en.py as the
editorial model: this is a young book whose defined vocabulary is also
ordinary Indonesian, so a word earns a link only when it means the defined
thing in nearly all of its uses.

Two Indonesian-specific pressures shaped the lists below.

  * ``WORD_TAIL`` matches the enclitic ``-nya``, and this edition marks
    definiteness with ``-nya`` on almost every noun ("gayanya", "lampunya").
    Every term therefore matches roughly twice as often as its English twin.
    That is honest density, not wrong sense -- but it makes the DROP list
    matter far more than in English: an ordinary word left in the harvest
    links hundreds of times.
  * Indonesian definitions naturally OPEN with the term ("Tegangan $U$ ...").
    A capitalised display is a SEPARATE harvest entry, so such a definition
    can leave a term reachable only in its capitalised form. Two of them were
    repaired in the sources instead of here (g7 "massa jenis", g9
    "osiloskop"); the capitalised entries that remain are proper nouns
    (Bulan, Bima Sakti, Tata Surya, Bintang Utara) or duplicate an existing
    lowercase entry harmlessly.

Physics homographs that needed care (see ../indonesian_style_card.md):
"tegangan" (voltage / rope tension), "kutub" (magnetic pole / battery
terminal -- bare "kutub" is deliberately not a term here, only "kutub utara"
and "kutub selatan" are), "berat" (weight / heavy), "gaya" (force / style),
"daya" (power / capacity), "jam" (clock / hour -- see the note in DROP),
"air" (Indonesian for WATER; English "air" is "udara" and the two never
meet in this tree).
"""

# Heads of Indonesian result-names: "hukum Newton", "asas Archimedes",
# "aturan tangan kanan" are named results, not defined terms.
NOT_A_TERM = ("teorema", "lema", "sifat", "kaidah", "rumus", "kriteria",
              "asas", "aturan", "hukum", "prinsip", "ketaksamaan", "soal")

STOP = {
    # honest in its own chapter, ordinary prose elsewhere: this edition
    # says "amatilah", "perhatikan bahwa", "pengamatannya" constantly
    # (mirrors en: "observation", "observe")
    "pengamatan", "Pengamatan", "mengamati", "Mengamati",
    # equilibrium sense in its chapter; "seimbang" is the everyday word
    # for any balanced budget, force pair or ledger elsewhere
    "seimbang", "Seimbang",
    # circuit-diagram sense in its chapter; "lambang" is used for every
    # unit symbol, Greek letter and algebraic letter in the later years
    "lambang", "Lambang",
    # magnet sense in its chapter; from grade 5 on, bare "kutub" is
    # overwhelmingly the BATTERY TERMINAL (English says "terminal"
    # there, a different word). "kutub utara" and "kutub selatan"
    # survive as terms of their own -- exactly as en stops "pole"
    # and "poles" while keeping "north pole" / "south pole".
    "kutub", "Kutub",
}

NO_CAPITAL = {
    # capitalised, these name the physicists, not the units
    "newton", "joule", "watt", "volt", "ampere", "ohm", "hertz",
    # sentence-initial these are imperatives ("Ukurlah ...", "Amatilah ...")
    "ukur", "mengukur",
}

EXTRA = {}            # manual {term: label}; overrides every rule

DROP = {
    # --- ordinary words of the register (the en DROP list, translated) ---
    # "hot"/"cold": bare adjectives used on every page of nine years
    "panas", "Panas", "dingin", "Dingin",
    # "second": "sekon" is the unit AND the ordinary word for the moment;
    # the unit survives in \qty{}{s} and in the SI chapter's own prose
    "sekon", "Sekon",
    # "moment": "saat" is "when/at the moment that" throughout
    "saat", "Saat",
    # "year": "tahun ini", "tahun lalu", "bertahun-tahun" everywhere
    "tahun", "Tahun",
    # "night"/"daytime": ordinary time-of-day words; "matahari terbit"
    # and "matahari terbenam" keep the day-and-night links
    "malam", "Malam", "siang", "Siang",
    # bare adjectives: the phrases "rangkaian terbuka", "rangkaian
    # tertutup", "lintasan lurus", "lintasan lingkaran", "gerak
    # beraturan", "gerak berubah" survive as terms of their own
    "terbuka", "Terbuka", "tertutup", "Tertutup",
    "lurus", "Lurus", "melingkar", "Melingkar",
    "beraturan", "Beraturan", "berubah", "Berubah",
    # the five senses: "penglihatan", "perabaan", "penciuman",
    # "pengecapan" and "indra" are ordinary vocabulary here, exactly as
    # en drops sight/touch/smell/taste/sense; "pendengaran" is kept,
    # as en keeps "hearing"
    "indra", "Indra", "penglihatan", "Penglihatan",
    "perabaan", "Perabaan", "penciuman", "Penciuman",
    "pengecapan", "Pengecapan",
    # --- Indonesian homographs with no English counterpart ---
    # "menarik" is BOTH "attracts" and "interesting", and in this book
    # it is mostly neither: it draws a current, hauls a rope, pulls a
    # lever. Harvested from the grade-1 magnet definition, it produced
    # 86 wrong-sense links to "magnet" (en's "attract" links 8 times).
    "menarik", "Menarik",
}

DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"   # a spiral curriculum re-defines its terms
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40

# NOTE: multi-word patterns use \s+ between words -- a phrase wrapped across a
# source line break must still be protected. Count with whitespace collapsed
# when auditing them, or the census undercounts.
EXTRA_PROTECT = [
    # "berat" as the everyday adjective (heavy), not the force
    r'\b(?:lebih|paling|sangat|amat|terlalu|makin|begitu|cukup)\s+berat\b',
    r'\bberat\s+(?:badan|sebelah)\b',
    r'\bpekerja\s+yang\s+lebih\s+berat\b',
    # "gaya" as manner/style ("jatuh dengan gaya"), not the force
    r'\bdengan\s+gaya\b',
    # rope/mechanical tension and the everyday "tense", not the voltage
    r'\btegangan\s+permukaan\b',
    # mathematics' powers of ten, not electric power
    r'\bpangkat\s+sepuluh\b',
    # the buildings, not the quantity P = U I
    r'\bpembangkit\s+(?:listrik|tenaga)\b',
    # headphone loudness, not the space a body occupies
    r'\bsuara\s+penuh\b',
    # a book of the series, not the space a body occupies
    r'\bjilid\s+(?:Sekolah\s+Menengah|\w+)\b',
    # the verb ("dinyalakan/dipadamkan"), not the component
    r'\bsakelarnya\s+(?:dinyalakan|dipadamkan|ditekan)\b',
    # the ordinary "in parallel with" of prose, not the wiring
    r'\bsejajar\s+dengan\s+tangan\b',
    # "for hours" as an adverb, not the clock
    r'\bberjam-jam\b',
    # inside the kilowatt-hour definition itself, where the term cannot
    # self-link and bare "jam" would otherwise claim the compound
    r'\bkilowatt-jam\s+secara\s+langsung\b',
]
