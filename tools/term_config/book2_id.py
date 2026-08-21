"""Book 2 -- id (Indonesian). Curation only; the rules live in tools/termlink/.

Curated against the translated tree, then audited by diffing the PER-TARGET
link counts against English (target-set parity alone hides wrong-sense links).

Indonesian costs this book five curation problems English does not have:

* homographs English keeps apart with two different words. "tegangan" is
  both the voltage of a circuit and the tension of a rope; "berat" is both
  the weight of a body and the adjective "heavy"; "inti" is the core of an
  optical fibre and the nucleus of an atom; "hambatan" is electrical
  resistance and aerodynamic drag; "gravitasi" is both English "gravity"
  (never linked) and "gravitation" (linked);
* ordinary words of the register harvested from a definition that merely
  uses them: "diam" (at rest), "mantap" (stable / steady), "seragam" (uniform field / marching in step), "lolos"
  (escape speed / any escaping), "mutlak" (absolute pressure / any absolute);
* unit names spelled exactly like the physicists they honour -- newton,
  joule, coulomb, ohm, watt, henry, becquerel, tesla, pascal, kelvin are
  the men when capitalized and the units when not, and Indonesian, like
  Portuguese, has no julio/voltio spelling to escape with;
* named results whose head word sits in NOT_A_TERM ("hukum Snell", "hukum
  Ohm", "hukum Boyle", "hukum kedua Newton") are unreachable unless they
  are declared in EXTRA -- English reaches them through "Snell's law";
* one term the English text links book-wide under a word the Indonesian
  definition does not use bare: English "friction" (123 links) against an
  Indonesian definition that reads "gaya gesek". Declared in EXTRA so that
  the ordinary Indonesian word "gesekan" reaches the same definition.

Two Indonesian/English divergences are deliberate and are NOT bugs:

* "sekon" is stoplisted although it is never ambiguous. English does not
  link "second" at all (the ordinal would fire); linking every one of the
  137 Indonesian occurrences would put a fifth of the book's links on one
  unit definition. Chapter-local links survive.
* "daya" (power) is defined once in the Indonesian tree (g10) where English
  defines "power" twice (g10 and g11), so the 124 power links all land on
  the g10 definition instead of splitting 61/59. Every link is right in
  sense; only the split differs.
"""

# Heads of Indonesian result-names: "hukum Newton", "asas Archimedes",
# "aturan tangan kanan" are named results, not defined terms.
NOT_A_TERM = ("teorema", "lema", "sifat", "kaidah", "rumus", "kriteria",
              "asas", "aturan", "hukum", "prinsip", "ketaksamaan", "soal")

# A STOPped word is still linked inside the chapter that defines it, which
# is what these need: each one is right there and wrong everywhere else.
# CAPITALIZED forms are a separate harvest entry and bypass STOP, so every
# word is listed in both cases (the seed's warning, confirmed in the audit:
# "Newton" alone shipped 23 wrong links before NO_CAPITAL).
STOP = {
    # THE Indonesian homograph, exactly as "tensão" is for pt: the tension
    # of a rope (g10 inertia) and the voltage of a circuit (g11 circuits).
    # NOT stoplisted -- the electrical sense is by far the commoner one and
    # stoplisting would cost 55 right links to save 17 wrong ones; the
    # mechanical phrases are masked in EXTRA_PROTECT below instead. Left
    # here as a note so the next editor does not "fix" it the wrong way.
    #
    # core of an optical fibre (g10 refraction) -- and the atomic nucleus,
    # the core of the Sun, the core of an electromagnet, "intinya" meaning
    # "essentially". 119 links, 8 of them right.
    "inti", "Inti",
    # "at rest", harvested from the reference-frame definition (g10). The
    # ordinary adjective is on every other page: 102 links, ~15 right.
    "diam", "Diam",
    # English writes "gravity" (never linked) and "gravitation" (linked);
    # Indonesian has one word, and it is defined twice on top of that.
    # 78 links against English's 14. "gaya gravitasi" and "interaksi
    # gravitasi" survive as terms of their own.
    "gravitasi", "Gravitasi",
    # unambiguous, but see the docstring: 137 links on one unit definition.
    "sekon", "Sekon",
    # uniform field (g11) -- against soldiers marching in step, which is
    # exactly where the wrong links landed.
    "seragam", "Seragam",
    # stable equilibrium (g12) -- and "mantap" is the ordinary adjective
    # for a steady current, a steady thrust, a steady gigawatt.
    "mantap", "Mantap",
    # escape speed (g12) -- and the ordinary verb: neutrons escape the
    # lump, argon escapes the lava, the ball escapes the hand.
    "lolos", "Lolos",
    # absolute pressure (g10 diving method) -- and "batas mutlak", "nol
    # mutlak", "kebenaran mutlak".
    "mutlak", "Mutlak",
}

NO_CAPITAL = {
    # Capitalized these are the physicists, not the units, and Indonesian
    # spells the two alike: the book writes "hukum Newton", "efek Joule",
    # "hukum Ohm", "penghalang Coulomb". "Newton" alone was 23 wrong links.
    "newton", "joule", "coulomb", "ohm", "watt", "henry", "becquerel",
    "pascal", "kelvin", "tesla", "volt", "ampere", "hertz", "farad",
    "sievert", "curie", "gauss",
}

# Manual entries; they win over every rule above, and may point at a
# theorem or a proposition, not only at a definition.
EXTRA = {
    # Head word in NOT_A_TERM, hence unreachable without this: these are
    # the four named results English links through "X's law".
    "hukum Snell": "thm:g10:refraction:snell",
    "hukum Ohm": "prop:g11:circuits-and-power:ohm",
    "hukum Boyle": "prop:g10:pressure:boyle",
    "hukum kedua Newton": "thm:g12:newtons-laws:second",
    "hukum ketiga Newton": "thm:g12:newtons-laws:third",
    # The proposition names the motion in an \index line, not in an \emph,
    # so nothing was harvested; English links "uniformly accelerated".
    "gerak lurus berubah beraturan": "prop:g12:kinematics-2d:uarm",
    # English links "friction" 123 times to the force-inventory definition.
    # The Indonesian definition spells the term "gaya gesek", so the word
    # the rest of the book actually uses reached nothing.
    "gesekan": "def:g10:inertia:inventory",
}

DROP = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"   # school book: a term may be re-defined by year
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40

# Two rules hold for EVERY pattern below:
#   * NEVER consume a `$` -- match it with a lookahead. Eating an opening $
#     leaves the inline-math rule pairing the closing $ with the next
#     formula's opening one, and the mask runs inside out to end of file:
#     no error, the links simply vanish (see tools/termlink/protect.py).
#   * NEVER write a literal space -- always `\s+`. The list is compiled with
#     re.S and real prose wraps.
EXTRA_PROTECT = [
    # "tipis" is the thin lens of g11 -- English links its "thin" 17 times,
    # so the term stays; these are its non-optical uses.
    r'udara\s+(?:yang\s+)?tipis',
    r'dengung\s+tipis',
    r'penyekat\s+yang\s+tipis',
    r'matahari\s+gunung\s+yang\s+tipis',
    # mechanics' drag, not the electrical quantity (20 wrong links)
    r'[Hh]ambatan(?:nya)?\s+udara',
    r'[Gg]aya\s+hambatan(?:nya)?',
    r'hambatannya\s+(?:mengimbangi|memangkas|melawannya)',
    r'menurunkan\s+hambatannya',
    r'tanpa\s+udara:\s+hambatannya',
    # rope/cable tension, not voltage. The "$" branch uses a LOOKAHEAD.
    r'[Tt]egangan(?:nya)?\s+(?=\$)',
    r'[Tt]egangan(?:nya)?\s+(?:penghela|tali|kawat|kabel|kerja)\w*',
    r'[Tt]egangannya\s+tegak\s+lurus',
    r'[Tt]egangannya\s+harus\s+keluar',
    r'percepatan\s+dan\s+[Tt]egangannya',
    r'tambahan\s+[Tt]egangan',
    r'[Tt]egangan\s+terbesar\s+yang\s+ditemui',
    r'[Tt]egangan\s+dan\s+lajunya',
    r'Hitunglah\s+[Tt]egangannya',
    # "berat" the adjective (heavy), not the weight of a body
    r'(?:yang|lebih|paling|amat|sangat|terlalu)\s+berat',
    r'kendur\s+dan\s+berat',
    r',\s*berat;',
]
