"""Book 3 -- en. Curation only; the rules live in tools/termlink/.

Every key is optional: anything left out falls back to the defaults in
tools/link_defined_terms.py (empty sets, AMBIG_POLICY "drop").

Curated 2026-08-21 from the harvested list (`--terms`) of the written
30-chapter book.  Regenerate with:
    python3 tools/link_defined_terms.py --book 3 --unwrap --apply
    python3 tools/link_defined_terms.py --book 3 --apply
"""

# Ordinary language in this register, or a word whose sense elsewhere in
# the book is not the sense its definition gives it. (A STOPped word is
# still linked inside the chapter that defines it.)
STOP = {
    # ubiquitous bare nouns of mechanics/thermodynamics: a link on every
    # occurrence from chapter 12 on is noise, and "heat"/"work" are also
    # verbs ("heat the gas", "the method works")
    "force", "mass", "velocity", "acceleration", "momentum",
    "pressure", "temperature", "heat", "Heat", "work",
    # the bar (unit, kinetic theory) vs the sliding bar of the Laplace rails
    "bar",
    # moment of a force (ch. 15) vs "the moment the emf vanishes"
    "moment",
    # the optical image vs "mirror image" in the symmetry chapters
    "image",
    # focus (optics noun) vs the verb
    "focus",
    # electrical ground (circuits) vs the ground under a thundercloud
    "ground",
    # op-amp gain vs the verb "gains"
    "gain",
    # fibre core (ch. 2) vs the Earth's core, the coaxial core
    "core",
    # flux of the electric field (ch. 26) vs the magnetic flux (ch. 29)
    "flux",
    # SI unit (ch. 1) vs "unit vector", "per unit length", "unit mass"
    "unit",
    # physical dimension (ch. 1) vs "dimensions of the room", "one dimension"
    "dimension",
    # thermodynamic transformation (ch. 22) vs ordinary usage elsewhere
    "transformation",
    # optics "objective" vs the adjective
    "objective",
}

NO_CAPITAL = {
    # capitalized, these are the physicists, not the units
    "newton", "joule", "watt", "pascal", "kelvin", "tesla", "hertz",
    "coulomb", "volt", "ampere", "ohm", "henry", "farad", "weber",
}

EXTRA = {}            # manual {term: label}; overrides every rule

DROP = {
    # bare adjectives harvested from definitions that merely use them
    "ideal", "ideally", "linear", "central",
}

EXTRA_PROTECT = [
    # "signal" the ordinary noun in "turn signal"-like prose; the physics
    # sense is kept everywhere else
    r'\bsignal to noise\b',
]

AMBIG_POLICY = "drop"
