"""Book 3 -- id (Indonesian). Curation only; the rules live in tools/termlink/.

Curated 2026-08-21 against the translated tree, then audited by diffing the
PER-TARGET link counts against English: target-set parity alone hides
wrong-sense links (indonesian_style_card.md 4b.8).

Indonesian costs this book the same curation problems as Book 2, plus two
that are specific to a university physics volume:

* `hukum` is NOT in NOT_A_TERM here, unlike book2_id.  English's default
  list blocks "law of X" but not "X's law", so English harvests "Ampère's
  law", "Gauss's law", "Faraday's law", ... from their `\\index{}` keys.
  Indonesian writes all of them "hukum X"; blocking `hukum` made fourteen
  named results unreachable and cost the edition fourteen link targets.
  Dropping it from NOT_A_TERM reproduces the English behaviour exactly and
  needs no EXTRA entry.  (Book 2's school register never needed it, because
  its law names are also `\\emph{}` defined terms.)
* homographs English keeps apart with two words: `inti` is the core of an
  optical fibre (ch. 2), the nucleus of an atom (ch. 30), the core of the
  Earth, of a transformer and of the Sun, and `intinya` = "essentially";
  `bayangan` is the optical image and any figurative shadow; `gaya` is
  force and manner; `usaha` is work and an effort; `momen` is the moment of
  a force and any instant.
* unit names spelled exactly like the physicists they honour: Indonesian,
  like Portuguese, has no julio/voltio spelling to escape with, so every
  one goes in NO_CAPITAL.

Two divergences from English are deliberate and are NOT defects:

* `lintasan` covers English's *path* (never linked) and *trajectory*
  (linked), so its target carries more links than English's; `jam` is
  clock, hour and watch in one word.  Recorded, not "fixed"
  (indonesian_style_card.md 4c.4).
* `tegangan` is voltage far more often than it is the tension of a rope or
  a surface, so it is masked rather than stoplisted (4c.3).
"""

# Heads of Indonesian result-names. `hukum` is deliberately absent -- see
# the docstring; the English default blocks only "law of", not "X's law".
NOT_A_TERM = ("teorema", "lema", "ketaksamaan", "rumus", "kriteria",
              "prinsip", "asas", "aturan", "identitas", "paradoks", "soal")

# A STOPped word is still linked inside the chapter that defines it, which
# is what these need. CAPITALIZED forms are a separate harvest entry and
# bypass STOP (4b.1), so every word is listed in both cases.
STOP = {
    # the ubiquitous bare nouns of mechanics and thermodynamics: from
    # ch. 12 on, a link on every occurrence is noise. Exactly English's
    # "force, mass, velocity, acceleration, momentum, pressure,
    # temperature, heat, work".
    "gaya", "Gaya", "massa", "Massa",
    "kecepatan", "Kecepatan", "percepatan", "Percepatan",
    "momentum", "Momentum", "tekanan", "Tekanan",
    "suhu", "Suhu", "kalor", "Kalor", "usaha", "Usaha",
    # the bar (unit, kinetic theory) against the sliding bar of the
    # Laplace rails -- and `bar` is also the English word the prose gate
    # ungates, so it is on every page of chs. 21--25.
    "bar", "Bar",
    # the moment of a force (ch. 15) against "pada momen itu"
    "momen", "Momen",
    # the optical image (ch. 3) against every figurative shadow
    "bayangan", "Bayangan",
    # op-amp / filter gain against the ordinary verb
    "penguatan", "Penguatan",
    # fibre core (ch. 2), atomic nucleus (ch. 30), the Earth's core, the
    # transformer core, "intinya" = essentially. 119 links, 8 right, in
    # the Book 2 audit.
    "inti", "Inti",
    # electric flux (ch. 26) against magnetic flux (ch. 29)
    "fluks", "Fluks",
    # the SI unit (ch. 1) against "vektor satuan", "tiap satuan panjang"
    "satuan", "Satuan",
    # physical dimension (ch. 1) against "dimensi ruangan", "satu dimensi"
    "dimensi", "Dimensi",
    # thermodynamic transformation (ch. 22) against ordinary usage
    "transformasi", "Transformasi",
    # one Indonesian word for English's *gravity* (never linked) and
    # *gravitation* (linked); 78 links against English's 14 in Book 2.
    "gravitasi", "Gravitasi",
    # English never links "wavelength" at all: it is defined twice (ch. 5
    # and the de Broglie wavelength of ch. 30) and the ambiguity policy
    # drops it. Indonesian spells the two differently, so "panjang
    # gelombang" survived and generated 38 links English does not have.
    # Stoplisted for parity; chapter-local links survive.
    "panjang gelombang", "Panjang gelombang",
    # the electrical ground point (ch. 6) against the sub-satellite
    # "titik tanah" of the ground track (ch. 16).
    "titik tanah", "Titik tanah",
    # the cladding of an optical fibre (ch. 2) -- and the *envelope* of a
    # damped oscillation (chs. 5, 7), of a beat, of a hot-air balloon
    # (chs. 20, 21) and the sheath of a coaxial cable (ch. 26). Fifteen of
    # twenty links were the wrong sense; English links "cladding" four
    # times. Chapter-local links survive.
    "selubung", "Selubung",
}

NO_CAPITAL = {
    # capitalized these are the physicists, not the units, and Indonesian
    # spells the two alike: "hukum Newton", "efek Joule", "hukum Ohm",
    # "penghalang Coulomb". "Newton" alone shipped 23 wrong links in Book 2.
    "newton", "joule", "watt", "pascal", "kelvin", "tesla", "hertz",
    "coulomb", "volt", "ampere", "ohm", "henry", "farad", "weber",
    "becquerel", "sievert", "curie",
}

EXTRA = {
    # English harvests "eyepiece" (32 links) and "objective" (23) as terms
    # in their own right; the Indonesian definition spells them "lensa
    # okuler" and "lensa objektif", and the prose then uses the bare heads
    # 47 and 28 times, reaching nothing. Both words occur only in the two
    # optics chapters, so there is no other sense to protect.
    "okuler": "def:b1:optical-instruments:microscope",
    "objektif": "def:b1:optical-instruments:microscope",
}

DROP = {
    # bare adjectives harvested from definitions that merely use them --
    # English drops "ideal", "ideally", "linear", "central".
    "ideal", "linear", "sentral",
}

DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"          # university register
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40

# Two rules hold for EVERY pattern below:
#   * NEVER consume a `$` -- match it with a lookahead. Eating an opening $
#     leaves the inline-math rule pairing the closing $ with the next
#     formula's opening one and the mask runs to end of file: no error, the
#     links simply vanish (tools/termlink/protect.py).
#   * NEVER write a literal space -- always `\s+`; the list is compiled
#     with re.S and real prose wraps.
EXTRA_PROTECT = [
    # Rope, wire and material tension, not the voltage of a circuit
    # (4c.3): stoplisting `tegangan` would cost 145 right links to save 27
    # wrong ones. Every pattern below was read off a per-target audit of
    # the mechanics chapters (12, 13, 15, 18, 19, 21), where the word is
    # never electrical -- and checked against chapters 6--10, 14, 17, 26,
    # 27, 29, where it always is.
    r'\\emph\{tegangan\}',
    r'[Tt]egangan(?:nya)?\s+(?:tali|kawat|kabel|benang|dawai|senar|permukaan|tekan|luluh|geser)\w*',
    r'[Tt]egangan\s+maksimumnya',
    r'[Tt]egangan\s+rata-rata\s+selama',
    r'[Tt]egangan\s+sebuah\s+tali',
    r'percepatan(?:nya)?\s+dan\s+(?:kedua\s+)?tegangannya',
    r'periodenya\s+dan\s+tegangannya',
    r'tegangannya\s+diteruskan',
    r'dan\s+tegangan\s+(?=\$-T)',
    r'berapa\s+tegangannya\s+di\s+sana',
    r'menuliskan\s+tegangannya',
    r'[Tt]egangannya\s+(?:memotong|sentral|memang\s+radial|melalui\s+porosnya'
    r'|bekerja\s+pada\s+titik|lebih\s+besar\s+atau|dapat\s+berusaha)',
    r'[Tt]egangannya:\s*tak\s+bermomen',
    r'[Tt]egangannya:\s*(?=\$T\s)',
    r'[Tt]egangan\s+(?=\$T\$\s+ke\s+atas)',
    r'sudut\s+dan\s+tegangan\s+yang\s+sama',
    r'Hanya\s+tegangannya\s+yang',
    r'dan\s+tegangannya;',
]
