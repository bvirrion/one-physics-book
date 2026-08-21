#!/usr/bin/env python3
"""Indonesian-specific hygiene gate for a translated tree.

check_translation.sh proves *structure*: same files, same labels, same
environment census. Its prose gates prove almost nothing here -- gate 6 looks
for TeX accent escapes, which Indonesian never writes (the orthography is
plain ASCII), and the drafty-"..." gate is script-agnostic. So an Indonesian
tree can pass every existing gate and still be half English.

**Indonesian is the hard case, and it is hard for the opposite reason to
Hindi.** The Devanagari and Arabic gates can flag *any* Latin word in visible
text, because in those editions Latin script is itself the defect. Indonesian
is written in the same alphabet as the English source, so a forgotten
sentence, a forgotten TikZ node or a forgotten \\text{...} is invisible to
that rule. The only safe detector is the inverse: a **curated list of English
words that are not also Indonesian words**, plus a density heuristic for
sentences that were never touched at all.

This is the One Physics Book copy. It is the math book's gate plus a
physics block in each list (marked "physics" below): the subject changes
which English words a forgotten sentence leaves behind, and it changes which
words are ordinary Indonesian. The loudest example is "air", which is
Indonesian for WATER and appears on nearly every page of Book 1 -- gating the
English word "air" would make the gate unusable here.

Every entry in ENGLISH_WORDS below was checked against Indonesian. Words that
are spelled identically in both languages are deliberately absent and listed
in NOT_GATED with the reason -- "data", "total", "real", "ring", "limit",
"integral", "unit", "area", "set", "median", "mode" are ordinary Indonesian
and flagging them would make the gate unusable.

Failure classes this script detects:

  1. `english`      -- a listed English word in visible text: prose, TikZ node
                       text, \\text{...} inside math, chapter/section titles,
                       environment optional titles, \\index keys.
  2. `untranslated` -- a long visible sentence containing not one of the
                       commonest Indonesian function words. An Indonesian
                       sentence of eight words essentially always contains a
                       "yang", "dan", "di", "dari", "untuk", "adalah", ...;
                       one that does not was never translated.
  3. `math-space`   -- MT-injected spaces inside inline math ("$P $ dan $ Q $"),
                       detected by the shared reduction.
  4. `redup-space`  -- plural reduplication written with spaces around the
                       hyphen ("bilangan - bilangan"). Invisible in print,
                       fatal to the term linker's word boundaries.
  5. `enclitic`     -- the enclitic -nya written as a separate word
                       ("turunan nya"), which is not Indonesian and again
                       breaks term matching.
  6. `split-number` -- a thin space splitting a word from a thousands group
                       ("bilangan\\,000"), the class that damaged Hindi when
                       MT moved a number out of "Numbers up to 10\\,000".

The LaTeX reduction is imported from tools/check_hindi_prose.py rather than
copied: it is language-independent (it drops technical macro arguments, keeps
\\text{...} inside math, pulls visible strings out of tikz/pgfplots drawing
code) and one implementation is better than three.

Usage:
    python3 tools/check_indonesian_prose.py parts/grade-3/id parts/grade-3/solutions/id
    python3 tools/check_indonesian_prose.py --quiet <dir> ...

Exit status is 1 if anything was flagged. Called by check_translation.sh for
lang == id; safe to run by hand on a single directory while translating.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

from check_hindi_prose import (  # noqa: E402  -- shared, language-independent
    LATIN_WORD,
    _locate,
    strip_comments,
    visible_text,
)

# ---------------------------------------------------------------------------
# 1. Residual English.
# ---------------------------------------------------------------------------
# Grammar words. None of these is a word in Indonesian in any spelling, so the
# match is case-insensitive: "The" at the head of a forgotten sentence and
# "the" mid-line are the same defect.
ENGLISH_FUNCTION = {
    "the", "a", "an", "and", "or", "but", "if", "then", "else", "so", "thus",
    "hence", "therefore", "because", "since", "while", "when", "where",
    "which", "whose", "that", "this", "these", "those", "there", "here",
    "of", "to", "in", "on", "at", "by", "for", "from", "into", "onto",
    "with", "without", "within", "about", "above", "below", "under", "over",
    "between", "among", "through", "during", "after", "before", "until",
    "we", "us", "our", "you", "your", "they", "them", "their", "it", "its",
    "he", "she", "him", "her", "his", "who", "what", "how", "why",
    "is", "are", "was", "were", "be", "been", "being", "am",
    "has", "have", "had", "do", "does", "did", "can", "cannot", "could",
    "will", "would", "shall", "should", "must", "might", "may",
    "no", "yes", "all", "any", "both", "each", "every", "some",
    "many", "much", "more", "most", "less", "least", "few", "several",
    "same", "other", "another", "such", "only", "also", "even", "still",
    "first", "second", "third", "last", "next", "previous", "then",
    "let", "given", "using", "note", "recall", "suppose", "assume",
    "consider", "observe", "indeed", "conversely", "moreover", "however",
    "again", "always", "never", "often", "sometimes", "now", "once",
    "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
    # Appended for Book 3 (University Year 1). A university book argues, so it
    # leans on a wider set of connectives and relational words than the school
    # books did; each of these was checked against KBBI. "as" is deliberately
    # ABSENT -- see NOT_GATED.
    "than", "along", "inside", "outside", "against", "across", "toward",
    "towards", "apart", "away", "out", "off", "alone", "own", "itself",
    "behind", "around", "beyond", "instead", "just", "too", "almost",
    "together", "whatever", "nothing", "well", "way", "like", "part",
    # "new" is NOT here: the set is matched case-insensitively and it fired on
    # "New York" in the shipped grade-10 id chapter on optical fibre.
    "whether", "unless", "whereas", "throughout", "everywhere", "anywhere",
    "twice", "once", "enough", "rather", "quite", "very", "already",
}
# "no" is kept out of the short-token pass below, because "No." for "nomor"
# is ordinary Indonesian in a table head; it is listed here and screened by
# NUMBER_ABBREV instead.

# Content words a maths translation leaves behind. Every one was checked not to
# be Indonesian (see NOT_GATED for the ones that are).
ENGLISH_CONTENT = {
    # book furniture
    "chapter", "section", "page", "pages", "exercise", "exercises",
    "problem", "problems", "solution", "solutions", "proof", "proofs",
    "theorem", "theorems", "definition", "definitions", "proposition",
    "lemma", "corollary", "example", "examples", "remark", "remarks",
    "method", "notation", "figure", "table", "answer", "answers", "hint",
    # arithmetic and number
    "number", "numbers", "integer", "integers",
    "fraction", "fractions", "decimal", "decimals", "sum", "difference",
    "product", "quotient", "remainder", "divisor", "multiple", "prime",
    "even", "odd", "add", "adds", "subtract", "multiply", "divide",
    "addition", "subtraction", "multiplication", "division", "count",
    "half", "quarter", "third", "double", "rounding", "round",
    "percentage", "percent", "average", "power", "powers", "root", "roots",
    "square", "cube", "squared", "negative", "positive",
    # geometry and measure
    "line", "lines", "point", "points", "segment", "angle", "angles",
    "circle", "triangle", "rectangle", "polygon", "shape", "shapes",
    "side", "sides", "vertex", "edge", "face", "faces", "length", "width",
    "height", "depth", "surface", "distance",
    "perpendicular", "symmetry", "rotation", "translation",
    "left", "right", "middle", "centre", "center", "scale",
    # algebra and analysis
    "equation", "equations", "inequality", "unknown", "variable",
    "function", "functions", "graph", "slope", "coefficient", "polynomial",
    "sequence", "series", "convergent", "convergence", "divergent",
    "continuous", "continuity", "derivative", "differentiable", "bounded",
    "increasing", "decreasing", "maximum",
    "neighbourhood", "neighborhood", "subset",
    "mapping", "matrix", "matrices", "vector", "vectors",
    "dimension", "kernel", "image", "eigenvalue", "eigenvector",
    "subspace", "orthogonal", "invertible", "determinant",
    "measure", "measurable", "probability", "random", "outcome", "event",
    "expectation", "variance", "distribution", "sample",
    # environment optional titles -- the class that shipped green (see
    # ENGLISH_SUFFIX_CAP and the `title` class below)
    "property", "properties", "characterization", "linearization",
    "invertibility", "expansion", "cofactor", "system", "systems",
    "isometry", "isometries", "plane", "case", "cases", "converse",
    "uniqueness", "existence", "criterion", "criteria",
    # place-value furniture, the commonest leftover in TikZ node text
    "thousand", "hundred", "tens", "ones", "metres", "meters",
    # verbs an exercise stem uses
    "compute", "calculate", "find", "show", "prove", "deduce", "explain",
    "justify", "draw", "write", "read", "complete", "check", "state",
    "simplify", "expand", "factor", "factorise", "factorize", "solve",
    "compare", "estimate", "measure", "order", "sort", "list", "give",
    # ---- physics -----------------------------------------------------------
    # Quantities and their names. Indonesian spells each of these differently
    # (gaya, massa, berat, kelajuan, kecepatan, energi, kalor, gelombang, ...),
    # so the English form in visible text is always a defect. Words ending in
    # -tion/-ght (motion, friction, reflection, refraction, acceleration,
    # radiation, light, weight, height, bright, night) are already caught by
    # ENGLISH_SUFFIX and are deliberately not repeated here.
    "force", "forces", "mass", "weight", "speed", "velocity", "energy",
    "heat", "work", "wave", "waves", "wavelength", "frequency", "amplitude",
    "period", "sound", "mirror", "mirrors", "lens", "lenses", "ray", "rays",
    "beam", "shadow", "shadows", "rainbow", "eclipse", "spectrum",
    "current", "voltage", "charge", "charges", "circuit", "circuits",
    "battery", "bulb", "lamp", "switch", "wire", "wires", "coil", "magnetic",
    "electric", "electron", "electrons", "photon", "photons", "nucleus",
    "nuclear", "radioactive", "isotope", "molecule", "molecules", "crystal",
    "vacuum", "pressure", "temperature", "density", "gravity", "inertia",
    "spring", "string", "rope", "pulley", "lever", "ramp", "block",
    "ball", "screen", "source", "object", "objects", "compass", "diode",
    "capacitor", "transformer", "turbine", "satellite", "comet",
    "quantum", "relativity", "efficiency", "resonance", "diffraction",
    "capacitance", "conductor", "insulator", "prism", "focus",
    # Sight/hearing/... : the five-senses chapter, and single-word TikZ node
    # labels generally -- a node text is too short for the sentence-density
    # class, so a word list is the only thing that sees it.
    "sight", "hearing", "touch", "smell", "taste", "eye", "eyes", "ear",
    "ears", "nose", "tongue", "skin", "hot", "cold", "warm", "cool",
    "north", "south", "east", "west", "up", "down", "top", "bottom",
    "front", "back", "near", "far", "fast", "slow", "heavy", "big",
    "small", "start", "stop", "time", "times", "sun", "moon", "earth",
    "star", "stars", "water", "ice", "steam", "glass", "wood", "metal",
    "iron", "copper", "sand", "stone", "float", "sink", "melt", "freeze",
    "boil", "push", "pull", "axis", "pole", "poles",
    # English plurals of nouns spelled the SAME in both languages. Indonesian
    # pluralises by reduplication (magnet-magnet), never with -s, so the plural
    # is unambiguously English even though the singular is unambiguously not.
    # The -s/-es stem rule cannot reach them: their stems are in NOT_GATED.
    "magnets", "gases", "atoms", "ions", "protons", "neutrons", "orbits",
    "planets", "lasers", "motors", "radios", "resistors", "meteors",
    # ---- university physics (Book 3) ---------------------------------------
    # Harvested from the English bodies of parts/bachelor-1 and filtered
    # against KBBI: the Indonesian of each of these is a DIFFERENT string
    # (medan, hukum, tetapan, fase, entropi, momen, torsi, ...), so the
    # English form in visible text is always a defect. Words already caught
    # by ENGLISH_SUFFIX (-tion, -ance, -ence, -ous, -ly, -ght, -th: friction,
    # resistance, impedance, difference, continuous, length, ...) are not
    # repeated here, and neither are the ones Indonesian spells identically
    # (see NOT_GATED -- radius, uniform, loop, model, input, output, ...).
    "field", "fields", "law", "laws", "constant", "constants", "phase",
    "entropy", "enthalpy", "potential", "flux", "torque", "dipole",
    "moment", "moments", "cycle", "cycles", "frame", "frames", "value",
    "values", "ratio", "signal", "signals", "body", "bodies", "ground",
    "rest", "mean", "liquid", "vapour", "vapor", "fluid", "fluids",
    "particle", "particles", "displacement", "equilibrium", "magnitude",
    "oscillator", "oscillators", "pendulum-bob", "damping", "harmonic",
    "harmonics", "adiabatic", "reversible", "irreversible", "engine",
    "engines", "pump", "sphere", "spheres", "cylinder", "cylinders",
    "plate", "plates", "coil", "coils", "wall", "walls", "tube", "cable",
    "wheel", "wheels", "rod", "rods", "bar-magnet", "hull", "vessel",
    "bottle", "floor", "road", "car", "cars", "machine", "machines",
    "refrigerator", "thermostat", "telescope", "microscope", "eyepiece",
    "objective", "antenna", "receiver", "transmitter",
    "amplitude-gain", "cyclotron", "buoyancy", "curvature", "latitude",
    "tangent", "element", "elements", "index", "rule", "rules", "beat",
    "beats", "mole", "hydrogen", "atmosphere", "steel", "fuel", "sea",
    "bridge", "branch", "threshold", "peak", "gap", "drop", "drops",
    "load", "rate", "sign", "curve", "core", "thin", "turn", "turns",
    "zero", "size", "single", "free", "full", "change", "changes",
    "equal", "equals", "red", "blue", "green", "black", "white",
    "electricity", "uncertainty", "weekend", "week", "day", "year",
    "room", "house",
    # adjectives and adverbs: Indonesian writes kinetik, listrik, mekanis,
    # optis, relatif, sentral, vertikal, sirkular, aksial -- never these.
    "kinetic", "electrical", "mechanical", "optical", "inertial",
    "relative", "central", "vertical", "circular", "cylindrical",
    "spherical", "axial", "external", "independent", "infinite", "finite",
    "visible", "negligible", "dimensionless", "conservative", "critical",
    "steady", "maximal", "minimal", "partial", "extra", "little",
    "quadratic", "symmetric", "local", "initial", "stable", "unstable",
    "simple", "perfect", "common", "open", "closed", "opposite",
    "downward", "upward", "outward", "inward", "clockwise",
    # -ing and -ed forms. ENGLISH_SUFFIX deliberately gates neither ending
    # (penting, masing-masing; and -ed would fire on surnames), so the ones
    # a physics figure label actually uses are listed by hand.
    "boiling", "melting", "freezing", "cooling", "heating", "converging",
    "diverging", "falling", "sliding", "rolling", "charged", "closed-loop",
}

ENGLISH_WORDS = ENGLISH_FUNCTION | ENGLISH_CONTENT

# Deliberately NOT gated -- identical or near-identical in Indonesian, so a
# hit would be a false alarm on correct prose. Kept as a list so the next
# agent does not "helpfully" add them.
NOT_GATED = {
    "data", "total", "real", "ring", "grup", "limit", "integral", "unit",
    "area", "set", "median", "modus", "mode", "faktor", "vektor", "matriks",
    "normal", "positif", "negatif", "final", "modul", "ideal", "kernel",
    "domain", "kompleks", "abstrak", "aljabar", "analisis", "geometri",
    # spelled identically in both languages -- KBBI has all of these. Each one
    # was in ENGLISH_CONTENT until it fired on correct Indonesian prose.
    # "not" is Indonesian for a MUSICAL note (from Dutch "noot"; "not balok" is
    # staff notation). It fired ~35 times on the correct grade-7 fractions
    # chapter, whose weekend problem is about note values. Losing English "not"
    # costs nothing: a forgotten English sentence containing "not" always
    # carries "is"/"the"/"does" as well, and the `untranslated` class sees it.
    "not",
    "minimum", "supremum", "infimum", "volume", "basis", "linear",
    "interval", "parallel", "perimeter", "digit", "digits", "meter",
    "koordinat", "gradien", "polinomial", "determinan", "ortogonal",
    "konvergen", "divergen", "kontinu", "dimensi", "variabel", "skala",
    "desimal", "persen", "segmen", "poligon", "kubus", "sampel",
    # ---- physics -----------------------------------------------------------
    # "air" is Indonesian for WATER. It is on nearly every page of Book 1
    # (air panas, air mendidih, permukaan air, air raksa) and gating the
    # English word "air" would fire hundreds of times on perfect prose. This is
    # the physics twin of "not" (a musical note) in the math copy: losing
    # English "air" costs nothing, because a forgotten English sentence about
    # air always carries "the"/"is"/"of" with it and the `untranslated` class
    # sees it.
    "air",
    # "bar" is the pressure unit, written the same in both languages.
    "bar",
    # Spelled identically in Indonesian and English -- KBBI has all of them.
    # Their ENGLISH PLURALS are gated instead (see ENGLISH_CONTENT).
    "magnet", "gas", "atom", "ion", "proton", "neutron", "orbit", "planet",
    "laser", "motor", "radio", "momentum", "plasma", "meteor", "resistor",
    "spektrum", "generator", "isolator", "konduktor", "kapasitor", "dioda",
    "transformator", "dinamo", "turbin", "satelit", "komet", "kompas",
    "prisma", "fokus", "lensa", "optik", "kuantum", "relativitas", "inersia",
    "isotop", "molekul", "kristal", "vakum", "nuklir", "radioaktif",
    "elektron", "foton", "amplitudo", "frekuensi", "periode", "resonansi",
    "difraksi", "interferensi", "polarisasi", "refraksi", "radiasi",
    "konveksi", "konduksi", "efisiensi", "gravitasi", "energi", "termometer",
    "barometer", "voltmeter", "amperemeter", "galvanometer", "spektroskop",
    # SI unit names, spelled the same in both languages wherever they are
    # written out rather than symbolised. (Unit SYMBOLS never reach visible
    # text: \qty, \unit, \num and \SI drop their arguments in the shared
    # reduction.)
    "newton", "joule", "watt", "volt", "ampere", "ohm", "kelvin", "hertz",
    "pascal", "tesla", "weber", "farad", "henry", "becquerel", "sievert",
    "candela", "lumen", "coulomb",
    # ---- university physics (Book 3) ---------------------------------------
    # "as" is Indonesian for an AXLE (as roda, as putar) -- and Book 3 is half
    # mechanics. Gating English "as" would fire on correct prose exactly the
    # way "air" (water) and "not" (a musical note) would; the same argument
    # applies: a forgotten English sentence containing "as" always carries
    # "the"/"is"/"of" as well, and the `untranslated` class sees it.
    "as",
    # "per" is Indonesian too (meter per detik) -- and it is on every page of
    # a mechanics book.
    "per",
    # Loanwords KBBI spells exactly as English does. Every one of these was in
    # the block above until it fired on correct Indonesian physics prose;
    # re-adding any of them to ENGLISH_CONTENT will break a green gate.
    "radius", "uniform", "loop", "model", "input", "output", "pendulum",
    "amplifier", "horizontal", "radial", "pupil", "virtual", "sinusoidal",
    "solenoid", "solenoida", "filter", "level", "medium", "polar", "formula",
    "diagram", "spin", "sensor", "terminal", "fiber", "natural", "helium",
    "internal", "alternator", "starter", "diesel", "rigid", "rim", "net",
    "disk", "feedback", "emf", "ggl", "torsi", "kalor", "usaha",
    # "camera obscura" is a Latin phrase Indonesian keeps verbatim (it is in
    # the shipped grade-6 id chapter three times); the device itself is
    # "kamera", so gating the English spelling would cost a false alarm on
    # correct prose for no coverage.
    "camera",
    "kilogram", "sentimeter", "milimeter", "kilometer", "detik", "sekon",
    # Indonesian technical vocabulary that happens to be Latin-looking and
    # would otherwise trip the -s plural rule or a suffix.
    "impuls", "fluks", "entropi", "entalpi", "adiabatik", "isotermal",
    "isobarik", "isokorik", "kapasitas", "resistansi", "impedansi",
    "induktansi", "kapasitansi", "reaktansi", "amplitudo", "fase",
    "harmonik", "osilator", "osilasi", "resonansi", "difraksi", "refleksi",
    "dioptri", "lensa", "cermin", "medan", "gaya", "massa", "berat",
}

# Brand, markup names and unit symbols that legitimately stay Latin.
ALLOWED = {
    "one", "course", "com", "www", "http", "https", "math", "book",
    "tex", "latex", "pdf", "html", "github", "md",
    "si", "iso", "cm", "mm", "km", "kg", "mg", "ml", "hz", "rad",
    # Appended by the Book 2 id edition. Chemical element symbols are
    # international and print unchanged in every language; they reach the
    # gate whenever a figure label sets the mass number in math and leaves
    # the symbol outside it ("{$^{4}$He}" in the binding-energy curve).
    # Only the symbol that actually collides with an English word is listed:
    # "he". A genuine English sentence containing "he" still fires on its
    # other words and on the sentence-density rule.
    "he",
}

# A curated list cannot be complete, and the words it misses are exactly the
# ones nobody thought of ("thousands" in a place-value node, "metres" in a
# \text{}). Two generic rules close most of that gap without touching correct
# Indonesian:
#
#   * ENGLISH_SUFFIX -- endings Indonesian orthography does not produce. Applied
#     to LOWERCASE words only, which removes the proper-noun risk entirely: the
#     books are full of Smith-shaped surnames and Indonesian keeps them in
#     Latin. "-ing" is deliberately absent (penting, kucing, masing-masing are
#     ordinary Indonesian) and so is "-ed" (it would fire on names).
#   * the plural rule -- a listed noun with an English -s/-es on it.
ENGLISH_SUFFIX = re.compile(
    r"(?:tion|sion|ly|ness|ous|ful|ght|th|ance|ence|ship|hood|wise)$")
# Title-Case words need a NARROWER set. Environment optional titles are Title
# Case ("[Characterization]", "[Linearization]", "[Invertibility mod $n$]"),
# and the lowercase-only rule above let every one of them through a green gate
# -- the one defect class this edition could ship with. But the books are also
# full of surnames, so -th, -ght, -ly and -ous are dropped here: Smith, Booth,
# Wright, Knight would all fire. None of the series' mathematicians (Gauss,
# Cauchy, Riemann, Lebesgue, Frobenius, Legendre, Sylvester, ...) matches this.
ENGLISH_SUFFIX_CAP = re.compile(
    r"(?:tion|sion|ness|ance|ence|ship|hood|wise|ity)$")

# An English possessive is unambiguous: Indonesian has no 's, it writes the
# possessor after the noun (hukum Newton, medan Bumi). Book 3's English bodies
# are full of them ("Newton's third law", "the Earth's field", "Gauss's law"),
# and a forgotten two-word figure label is far too short for the
# sentence-density class to see. LATIN_WORD keeps the apostrophe inside the
# token, so the whole possessive is one match.
ENGLISH_POSSESSIVE = re.compile(r"^[a-z]{2,}'s$")

DOTTED_ABBREV = re.compile(r"\b(?:i\.e\.|e\.g\.|etc\.|cf\.|viz\.)")
# "No. 3" / "no. 3" is Indonesian for "nomor"; "no" elsewhere is English.
NUMBER_ABBREV = re.compile(r"\b[Nn]o\.\s*\d")

# ---------------------------------------------------------------------------
# 2. Untranslated sentences.
# ---------------------------------------------------------------------------
# The commonest Indonesian function words. A visible sentence of any length
# worth reading contains at least one; a long one that contains none was never
# translated. Kept small on purpose -- a long list would excuse real defects.
ID_MARKERS = {
    "yang", "dan", "di", "ke", "dari", "untuk", "dengan", "adalah", "ialah",
    "itu", "ini", "pada", "atau", "tidak", "bukan", "jika", "maka", "kita",
    "setiap", "sebuah", "suatu", "akan", "sudah", "telah", "juga", "dapat",
    "bisa", "harus", "karena", "sehingga", "yaitu", "yakni", "oleh", "agar",
    "lalu", "kemudian", "hanya", "masih", "sama", "lebih", "kurang",
    "bilangan", "himpunan", "fungsi", "misalkan", "maka", "jadi", "ada",
    "semua", "banyak", "tiap", "bagi", "kali", "hasil", "nilai", "berapa",
    "hitung", "hitunglah", "tentukan", "buktikan", "gambar", "gambarlah",
    "tunjukkan", "carilah", "cari", "jawab", "solusi", "latihan", "soal",
    "bab", "halaman", "contoh", "definisi", "teorema", "bukti", "sifat",
    # Added after Book 1: a paragraph built out of noun phrases can go a long
    # way without any of the words above, and fired ~35 times on correct prose.
    # Every one of these is unambiguously Indonesian, so widening the list
    # cannot let an English sentence through.
    "tetapi", "namun", "sedangkan", "tanpa", "antara", "menjadi", "sesudah",
    "sebelum", "seperti", "sampai", "bahwa", "masing-masing", "saling",
    "sendiri", "mengapa",
    # Added after Book 4, same reason. "per" was proposed and REJECTED: English
    # writes "per" too ("per cent", "per second"), so it would excuse a real
    # English sentence. Every marker in this set must be unambiguously
    # Indonesian, or the class stops meaning anything.
    "daripada", "sebagaimana", "merupakan", "atas", "demi", "itulah",
    # ---- physics -----------------------------------------------------------
    # A physics paragraph can be built almost entirely out of quantity nouns
    # and still be perfectly Indonesian ("Gaya gesek pada benda bermassa ...").
    # Every word here is unambiguously Indonesian -- English spells each of
    # them differently -- so widening the list cannot excuse an English
    # sentence, which is the only rule this set has.
    "gaya", "benda", "massa", "berat", "arus", "medan", "energi", "daya",
    "usaha", "suhu", "kalor", "tekanan", "gelombang", "cahaya", "bunyi",
    "muatan", "kecepatan", "kelajuan", "percepatan", "waktu", "jarak",
    "panjang", "tinggi", "lebar", "besaran", "satuan", "pengukuran",
    "listrik", "rangkaian", "cermin", "sinar", "warna", "panas", "dingin",
    "bergerak", "diam", "jatuh", "matahari", "bumi", "bulan", "udara",
    "zat", "kawat", "pegas", "gesek",
    # ---- appended by the Physics Book 2 (id) agent, 2026-08-20 ----------
    # Each fired on correct Indonesian prose in the grade-10..12 solutions,
    # where a sentence built out of numerals and quantity nouns carries none
    # of the markers above. Every word here is unambiguously Indonesian --
    # English spells each of them differently -- so the class keeps its only
    # rule: it can still not excuse an English sentence.
    "sekitar", "kira-kira", "saat", "ketika", "seluruh", "setelah",
    "selama", "terhadap", "menurut", "sebesar", "sepanjang", "melalui",
    "satu", "dua", "tiga", "empat", "lima", "enam", "tujuh", "delapan",
    "sembilan", "sepuluh", "puluh", "ratus", "ribu", "juta", "miliar",
    "semesta", "bintang", "planet-planet", "sebagai", "supaya", "hingga",
    # ---- appended for Physics Book 3 (university), 2026-08-21 -------------
    # A university physics clause is noun-phrase-heavy and can run past eight
    # words on circuit and thermodynamics vocabulary alone ("tingkat pertamanya
    # hambatan Thevenin-nya tegangan keluarannya tak ..."). Same rule as every
    # block above: English spells each of these differently, so the class can
    # still not excuse an English sentence.
    "tegangan", "hambatan", "tingkat", "keluaran", "masukan", "penguat",
    "kumparan", "induktor", "kapasitor-nya", "rangkaiannya", "sumbu",
    "poros", "putaran", "simpangan", "amplitudonya", "getaran", "redaman",
    "tumbukan", "momentumnya", "kekekalan", "kelembaman", "acuan",
    "fluida", "zat-cair", "uap", "wujud", "peleburan", "penguapan",
    "entropinya", "siklus", "mesin", "pendingin", "kerja", "usahanya",
    "muatannya", "kapasitor", "dielektrik", "induksi", "fluksnya",
    "lintasan", "kelengkungan", "jari-jari", "sudut", "torsi-nya",
    "keseimbangan", "kesetimbangan", "tetapan", "besarnya", "arahnya",
    "terhitung", "berbanding", "sebanding", "berbalik", "terhadapnya",
    # ---- appended by the Physics Book 1 (id) agent, 2026-08-20 ----------
    # Same rule as above: every word here is unambiguously Indonesian (English
    # spells each of them differently), so the class can still not excuse an
    # English sentence. Each one fired on correct grade-1..9 prose, where a
    # list-heavy or subordinate-clause sentence runs past eight words without
    # touching any marker already listed.
    "dalam",        # "berada dalam kesetimbangan" (grade 2)
    "kalau",        # conditional, the young-book form of "jika"
    "begitu",       # "begitu jauh sehingga ..."
    "saja",         # "perabaan saja tidak dapat dipercaya"
    "sesuatu",      # "ada sesuatu yang terperangkap di dalamnya"
    "selalu",       # "bayang-bayang selalu berseberangan dengan sumbernya"
    "melainkan",    # "bukan tepi penggarisnya, melainkan angka 0"
    "walaupun",     # concessive
    "meskipun",     # concessive
    # ---- second block from the Physics Book 2 (id) agent, 2026-08-20 -----
    # Same rule again. Each fired on correct grade-10..12 prose: a sentence
    # built from a classifier plus optics/mechanics nouns can run past eight
    # words without touching any marker above. Every word is unambiguously
    # Indonesian, so the class still cannot excuse an English sentence.
    "seorang", "seekor", "sehelai", "sebutir", "sebatang", "selembar",
    "disebut", "dinamakan", "terletak", "berada", "titik", "garis",
    "sudut", "bidang", "lensa", "bayangan", "arah", "bentuk", "ukuran",
    "jumlah", "bagian", "keadaan", "getaran",
}
MIN_SENTENCE_WORDS = 8
SENTENCE_SPLIT = re.compile(r"[.!?;:\n]+")

# ---------------------------------------------------------------------------
# 3-6. Indonesian-specific spelling damage.
# ---------------------------------------------------------------------------
# "bilangan - bilangan" / "bilangan -bilangan": reduplication must be a single
# token joined by a bare hyphen.
REDUP_SPACE = re.compile(r"\b([a-z]{3,})\s+-\s*\1\b|\b([a-z]{3,})\s*-\s+\2\b",
                         re.IGNORECASE)
# The enclitic written as a word. "nya" never stands alone in Indonesian.
ENCLITIC_SPACE = re.compile(r"(?<=[a-zA-Z])\s+-?nya\b")
# A word glued to a thousands group by a thin space: "bilangan\,000".
SPLIT_NUMBER = re.compile(r"[A-Za-z]{2,}\s*\\,\s*\d{3}\b")


# ---------------------------------------------------------------------------
# 7. Titles left byte-identical to the English twin.
# ---------------------------------------------------------------------------
# Book 3 shipped seven untranslated environment titles -- [Characterization],
# [Properties], [Cofactor expansion], [Vandermonde determinant], [Square Cramer
# systems], [Linearization], [Invertibility mod $n$] -- through a FULLY GREEN
# prose gate. A title is short, Title-Cased and often a single word, so the
# word lists and the sentence-density rule all slide off it.
#
# The decisive check is not a word list at all: compare the title with the
# SAME title in the English twin file. If they are byte-identical and the
# title contains real words, it was never translated. Legitimately identical
# titles -- [Gram--Schmidt], [Bolzano--Weierstrass], [Rolle], [Ring],
# [$\arcsin$, $\arccos$] -- survive, because after math and macros are
# stripped they contain no lowercase word and no English-looking one.
TITLE_ENVS = ("definition", "theorem", "proposition", "lemma", "corollary",
              "example", "remark", "method", "notation", "exercise",
              "problem", "proof", "omfigure", "figure", "table")
TITLE_RE = re.compile(
    r"\\begin\{(?:" + "|".join(TITLE_ENVS) + r")\}"
    r"\[((?:[^\[\]]|\[[^\]]*\])*)\]"
    r"|\\(?:chapter|section|subsection)\*?\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}")


def _titles(text: str):
    return [(m.group(1) if m.group(1) is not None else m.group(2))
            for m in TITLE_RE.finditer(text)]


def _looks_english(word: str) -> bool:
    low = word.lower()
    if low in ALLOWED or low in NOT_GATED:
        return False
    if low in ENGLISH_WORDS:
        return True
    if word.islower() and len(word) > 3 and ENGLISH_SUFFIX.search(low):
        return True
    if word[:1].isupper() and len(word) > 4 and ENGLISH_SUFFIX_CAP.search(low):
        return True
    # a lowercase word of real length that is not an Indonesian function word:
    # "Plane isometries" is caught here and by nothing else.
    return word.islower() and len(word) > 2 and low not in ID_MARKERS


# An ACCENT-AWARE word pattern, unlike LATIN_WORD. The shared LATIN_WORD is
# [A-Za-z]-only, so it splits "Caratheodory"-with-an-acute into "Carath" +
# "odory" -- and the second half is a lowercase non-Indonesian word, i.e. a
# false positive on a mathematician's name. Every accented surname in the
# series (Caratheodory, Poincare, Levy, Godel, Muller, ...) breaks the same way.
TITLE_WORD = re.compile(r"[^\W\d_]+", re.UNICODE)


def _title_has_words(title: str) -> bool:
    t = re.sub(r"\$[^$]*\$", " ", title)
    t = re.sub(r"\\[A-Za-z@]+", " ", t)
    return any(_looks_english(w) for w in TITLE_WORD.findall(t))


def check_titles(path: pathlib.Path, body: str, findings: list) -> None:
    twin = pathlib.Path(str(path).replace("/id/", "/"))
    if not twin.is_file():
        return
    en = _titles(strip_comments(twin.read_text(encoding="utf-8")))
    idt = _titles(body)
    if len(en) != len(idt):
        return          # a structural divergence; check_translation.sh owns it
    for e, i in zip(en, idt):
        if e.strip() == i.strip() and _title_has_words(i):
            findings.append(
                (str(path), body.count("\n", 0, body.find(i)) + 1, "title",
                 f"title identical to English (untranslated?): {i.strip()[:60]!r}"))


def check_file(path: pathlib.Path, findings: list) -> None:
    raw = path.read_text(encoding="utf-8")
    rel = str(path)
    body = strip_comments(raw)
    # visible_text also reports the shared `math-space` class into findings.
    seen = visible_text(body, findings, rel)
    _occ: dict = {}

    # --- 1. residual English -------------------------------------------
    for m in NUMBER_ABBREV.finditer(seen):
        seen = seen[:m.start()] + " " * (m.end() - m.start()) + seen[m.end():]
    for m in LATIN_WORD.finditer(seen):
        word = m.group(0)
        low = word.lower()
        if low in ALLOWED or low in NOT_GATED:
            continue
        stem = low[:-2] if low.endswith("es") else low[:-1] if low.endswith("s") else None
        if (low in ENGLISH_WORDS
                or ENGLISH_POSSESSIVE.match(low)
                or (stem and stem in ENGLISH_WORDS and stem not in NOT_GATED)
                or (word.islower() and len(word) > 3
                    and ENGLISH_SUFFIX.search(low))
                or (word[:1].isupper() and len(word) > 4
                    and ENGLISH_SUFFIX_CAP.search(low))):
            findings.append((rel, _locate(body, word, _occ), "english",
                             f"English in visible text: {word!r}"))
    for m in DOTTED_ABBREV.finditer(seen):
        findings.append((rel, _locate(body, m.group(0), _occ), "english",
                         f"English abbreviation: {m.group(0)!r}"))

    # --- 2. sentences that were never translated ------------------------
    for chunk in SENTENCE_SPLIT.split(seen):
        words = [w.lower() for w in LATIN_WORD.findall(chunk)]
        if len(words) < MIN_SENTENCE_WORDS:
            continue
        if any(w in ID_MARKERS for w in words):
            continue
        snippet = " ".join(words[:10])
        findings.append((rel, _locate(body, words[0], _occ), "untranslated",
                         f"no Indonesian function word in {len(words)} words: "
                         f"{snippet}..."))

    # --- 7. titles left identical to the English twin -------------------
    check_titles(path, body, findings)

    # --- 4-6. spelling damage, measured on the raw body -----------------
    for cls, rx, msg in (
            ("redup-space", REDUP_SPACE,
             "reduplication split by spaces (write bilangan-bilangan)"),
            ("enclitic", ENCLITIC_SPACE,
             "enclitic -nya written as a separate word"),
            ("split-number", SPLIT_NUMBER,
             "\\, between a word and a thousands group (split number?)"),
    ):
        for m in rx.finditer(body):
            findings.append((rel, body.count("\n", 0, m.start()) + 1, cls,
                             f"{msg}: {m.group(0)[:40]!r}"))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("dirs", nargs="+", help="directories of .tex files")
    ap.add_argument("--quiet", action="store_true",
                    help="print only the per-class summary")
    ap.add_argument("--max-detail", type=int, default=8,
                    help="detail lines to show per class (default 8)")
    args = ap.parse_args()

    findings: list = []
    files = 0
    for d in args.dirs:
        p = pathlib.Path(d)
        if not p.is_dir():
            continue
        for f in sorted(p.glob("*.tex")):
            files += 1
            check_file(f, findings)

    if not findings:
        print(f"  indonesian prose gate: OK ({files} files)")
        return 0

    by_class: dict = {}
    for rel, line, cls, msg in findings:
        by_class.setdefault(cls, []).append((rel, line, msg))

    print(f"  indonesian prose gate: {len(findings)} issue(s) in {files} files")
    for cls in sorted(by_class):
        hits = by_class[cls]
        bad_files = len({h[0] for h in hits})
        print(f"    {cls:<14} {len(hits):>5} hit(s) in {bad_files} file(s)")
        if not args.quiet:
            for rel, line, msg in hits[:args.max_detail]:
                print(f"        {rel}:{line}: {msg}")
            if len(hits) > args.max_detail:
                print(f"        ... {len(hits) - args.max_detail} more")
    return 1


if __name__ == "__main__":
    sys.exit(main())
