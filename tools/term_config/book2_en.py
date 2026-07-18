"""Book 2 -- en. Curation only; the rules live in tools/termlink/.

Every key is optional: anything left out falls back to the defaults in
tools/link_defined_terms.py (empty sets, AMBIG_POLICY "drop").
"""

# Ordinary language in this register, or a word whose sense in the book is not
# the sense the definition gives it. (A STOPped word is still linked inside
# the chapter that defines it.)
STOP = {
    # harvested from the *velocity vector* definition (g12 kinematics); the
    # word is everywhere from grade 10 on, mostly before that definition
    # exists. "average speed", "speed of sound" survive as phrases.
    "speed",
    # the optical-fiber core (g10 refraction); elsewhere "core" is a reactor
    # core (g12 nuclear energy) or the Earth's core.
    "core",
    # radiation sense (g11 nucleus) is right in nuclear chapters but wrong in
    # the relativity chapter, where prose "gamma" is the dilation factor.
    # "gamma radiation" survives as a phrase.
    "gamma",
    # standing-wave node (g12 sound); the circuits chapters use "node" for a
    # junction in Kirchhoff's sense.
    "node",
    # the normal at an interface (g10 refraction); in mechanics "normal
    # component", "normal force" mean the Frenet/contact sense.
    "normal",
    # real image (g11 lenses); bare "real" is ordinary language everywhere.
    "real",
    # harvested from the uniform-field definition; "uniform motion" and
    # "uniform circular motion" are kinematics, not electrostatics.
    "uniform",
    # complementary colors (g11); "complementary pair" of angles elsewhere.
    "complementary",
    # harvested from the reference-frame definition; its derived form catches
    # the ordinary verb ("everything rests on the law").
    "rest",
    # retina rods (g11 color chapter); pendulum rods and control rods
    # elsewhere. Both forms: the plural is harvested as its own term.
    "rod", "rods",
    # oscilloscope gain (g10 signals); the verb "gains" is everywhere in
    # clock-drift prose.
    "gain",
}

NO_CAPITAL = {
    # capitalized, these are the physicists, not the units
    "newton", "joule", "watt", "pascal", "kelvin", "tesla", "hertz",
    "coulomb", "volt", "ampere", "ohm", "becquerel", "henry", "farad",
}

EXTRA = {}            # manual {term: label}; overrides every rule

DROP = {
    # bare adjective harvested from the diving method ("absolute pressure");
    # it also opens "absolute temperature", "absolute uncertainty", where a
    # link to the pressure method would be wrong. The three full phrases all
    # survive as terms of their own.
    "absolute",
    # display form with math in it; never matches prose. The dilation theorem
    # is reachable through the surviving phrases.
    "$\\gamma$ (gamma) factor",
    # ordinary words of the register, harvested from definitions that merely
    # use them: "vertical" (from the weight definition), "second(s)" (from
    # the SI-units definition), "at rest" (whose derived form catches the
    # verb "rests").
    "vertical",
    "second", "seconds",
    "at rest",
}

DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"   # a spiral curriculum re-defines its terms
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40

EXTRA_PROTECT = [
    # mechanics' drag, not the electrical quantity
    r'\bair resistance\b',
    # the verb ("speed delays nothing"), not the wave-arrival delay
    r'\bdelays nothing\b',
    # ordinary "works" (functions), not work done by a force
    r'\bstill works at\b',
    r'\bworks within a hundred\b',
]
