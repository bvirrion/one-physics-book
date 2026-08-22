"""Book 4 -- en. Curation only; the rules live in tools/termlink/.

Every key is optional: anything left out falls back to the defaults in
tools/link_defined_terms.py (empty sets, AMBIG_POLICY "drop").

Curated 2026-08-22 from the harvested list (`--terms`) of the written
31-chapter book.  Regenerate with:
    python3 tools/link_defined_terms.py --book 4 --unwrap --apply
    python3 tools/link_defined_terms.py --book 4 --apply
"""

# Ordinary language in this register, or a word whose sense elsewhere in
# the book is not the sense its definition gives it. (A STOPped word is
# still linked inside the chapter that defines it.)
STOP = {
    # "laser" is named in every optics chapter long before ch. 23 defines
    # it; a link on each occurrence would be noise
    "laser",
    # the laser threshold (ch. 23) vs the hearing threshold, a threshold
    # of detection, "above threshold"
    "threshold",
    # the steady flow of ch. 27 vs the adjective everywhere
    "steady",
    # cycle/turbine efficiency vs fin efficiency, luminous efficiency, ...
    "efficiency",
    # absorption of light (ch. 23) vs absorption of sound, of heat
    "absorption",
}

NO_CAPITAL = {
    # capitalized, these are the physicists, not the units
    "newton", "joule", "watt", "pascal", "kelvin", "tesla", "hertz",
    "coulomb", "volt", "ampere", "ohm", "henry", "farad", "weber",
}

EXTRA = {
    # the devices of ch. 27 are introduced capitalised in an itemize; link
    # the lowercase nouns too
    "throttle": "prop:b2:open-systems:devices",
    "nozzle": "prop:b2:open-systems:devices",
}

DROP = {
    # bare adjectives and harvest artefacts (titles cut at a line break)
    "quantised", "four-level", "three-level", "Eulerian",
    "rotation about a fixed", "power of forces on",
}

EXTRA_PROTECT = []

AMBIG_POLICY = "drop"
