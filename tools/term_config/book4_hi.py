"""Book 4 -- hi. Curation only; the rules live in tools/termlink/.

Curated 2026-08-22 from the harvested list (`--terms`) of the written
31-chapter Hindi edition, starting from `book3_hi.py` and re-checked term by
term against Book 4's own harvest.  Regenerate with:

    python3 tools/link_defined_terms.py --book 4 --lang hi --unwrap --apply
    python3 tools/link_defined_terms.py --book 4 --lang hi --apply

The English curation for this book is `book4_en.py`; this file mirrors it
entry for entry, because the two editions must carry the same link density
(~1 230 links, 143 targets).

What changed from the Book 3 seed
---------------------------------
Every Book 3 ``STOP``/``DROP`` word (बल, द्रव्यमान, वेग, दाब, ताप, आघूर्ण,
मात्रक, विमा, संकेत, आवरण, आदर्श, रैखिक, ...) was checked against the Book 4
harvest: **none of them is a harvested Book 4 term**, so they were dead
weight and are gone.  The same is true of Book 3's ``EXTRA_PROTECT`` pair
(पास्कल का सिद्धांत / ऐंपियर-फेर): Book 4 never writes those phrases, and
पास्कल appears only as a unit name in exercise wording, never as a term.

Hindi-specific notes (see also ``book2_hi.py``, ``book3_hi.py``):

* **Compounds are written apart**, so the bare head of a compound term is
  also an ordinary word on nearly every page.  In Book 4 four such heads are
  harvested and stopped below; the full phrases keep linking everywhere.
* **``NO_CAPITAL`` is inert**: Devanagari has no letter case, so the man and
  the unit are the same string.  Book 4 hi needs no unit-vs-surname split at
  all -- no unit name is a harvested term here.
"""

# Ordinary language in this register, or a word whose sense elsewhere in the
# book is not the sense its definition gives it.  (A STOPped word is still
# linked inside the chapter that defines it.)  Mirrors book4_en's STOP.
STOP = {
    # en "steady": the steady flow of ch. 27 (def:b2:open-systems:cv) vs the
    # adjective everywhere -- स्थायी अवस्था (stationary state), अर्ध-स्थायी
    # (quasi-static), स्थायी प्रावस्था (stable phase), स्थायित्व ...
    "स्थायी",
    # en "efficiency": fin efficiency (ch. 25) vs cycle, turbine, isentropic
    # and luminous efficiency
    "दक्षता",
    # en "absorption": absorption of light (ch. 23) vs absorption of sound,
    # of heat, of a wave in a medium
    "अवशोषण",
    # en "threshold": the laser threshold (ch. 23) vs the hearing threshold
    # (ch. 7) and "देहली से ऊपर" as ordinary wording
    "देहली",
    # en "laser" has no bare Hindi counterpart: लेज़र is harvested only
    # inside compounds (चार-स्तरीय लेज़र, देहली (लेज़र)), so nothing to stop.
}

# Structurally inert in Devanagari (no letter case).
NO_CAPITAL = set()

# Manual {term: label}; overrides every rule.
#
# These are the Hindi counterpart of book4_en's two EXTRA entries, and then
# some.  A notion introduced *outside* a `definition` environment is harvested
# from its bare \index{} only when the key contains a space (harvest.py: a
# one-word index key in a theorem is ordinary emphasis far more often than it
# is a term).  English clears that bar with two-word phrases -- "path
# difference", "wave packet", "wave train", "impedance matching" -- while the
# Hindi equivalents are single compounds (पथांतर, तरंग-पुंज, तरंग-रेल,
# प्रतिबाधा-मिलान), so every one of them was unreachable.  Each entry below
# was found by diffing the Hindi \index{} keys against their English twins
# position by position, and each points at the label its English twin links
# to.  Without them the edition lost ~110 links, most of the 22 that "path
# difference" alone carries.
#
# (तुंड and थ्रॉटल, book4_en's own two EXTRA entries, already harvest to
# prop:b2:open-systems:devices in Hindi and need nothing here.)
EXTRA = {
    "स्थायी प्रवाह":   "def:b2:fluid-kinematics:euler",              # stationary flow
    "तरंग-समीकरण":     "thm:b2:waves-on-strings:equation",           # wave equation
    "ध्वनि-विस्फोट":   "rem:b2:sound-waves:mach",                    # sonic boom
    "तरंग-पुंज":       "prop:b2:dispersion-wave-packets:group",      # wave packet
    "संचरण-रेखा":      "prop:b2:dispersion-wave-packets:coax",       # transmission line
    "तरंग-पट्टिका":    "prop:b2:plane-waves-polarization:plates",    # wave plate
    "प्रतिबाधा-मिलान": "thm:b2:wave-interfaces:normal",              # impedance matching
    "तरंग-रेल":        "prop:b2:scalar-light-model:coherence",       # wave train
    "पथांतर":          "thm:b2:two-wave-interference:formula",       # path difference
    "तरंगाग्र-विभाजन": "prop:b2:two-wave-interference:young",        # division of wavefront
    "आयाम-विभाजन":     "prop:b2:two-wave-interference:film",         # division of amplitude
}

DROP = {
    # bare adjectives (en: "quantised", "four-level", "three-level",
    # "Eulerian") and one harvest artefact: a definition title that is a
    # comma list of three devices
    "क्वांटित", "चार-स्तरीय", "तीन-स्तरीय", "ऑयलरीय",
    "संपीडक, पंप, टरबाइन",
}

# Inflected variants, kept by the harvester only if they really occur.
#
# ``lang_hi.py`` sets ``WORD_TAIL = ''`` and ``DERIVE = False``: Hindi has no
# Latin -s plural, so the linker matches a term only in the exact citation
# form and its own docstring says to "declare irregular variants term by term"
# here.  Book 4's prose is full of the direct and oblique plurals below --
# धारा-रेखाएँ, तरंगाग्रों, मैक्सवेल के समीकरणों -- every one of which English
# links for free through its `(?:e?s)?` tail.  Each entry was found by
# generating the regular Hindi plural/oblique of every linkable term, counting
# its real occurrences in this tree, and keeping it only while the target
# stays within 115% of the same target's English count; that cap is why
# विद्युत्चुंबकीय तरंगें (5 occurrences) is absent while विद्युत्चुंबकीय
# तरंगों (1) is present -- English links that target once in the whole book.
DERIVED = {
    "धारा-रेखा": ["धारा-रेखाएँ"],
    "तरंगाग्र": ["तरंगाग्रों"],
    "मैक्सवेल के समीकरण": ["मैक्सवेल के समीकरणों"],
    "अप्रगामी तरंग": ["अप्रगामी तरंगें", "अप्रगामी तरंगों"],
    "तरंग-रेल": ["तरंग-रेलें", "तरंग-रेलों"],
    "बिना फिसले लुढ़कना": ["बिना फिसले लुढ़कने"],
    "स्थायी अवस्था": ["स्थायी अवस्थाओं"],
    "तरंग-पट्टिका": ["तरंग-पट्टिकाएँ"],
    "रेनल्ड्स संख्या": ["रेनल्ड्स संख्याएँ"],
    "अनुदैर्घ्य तरंग": ["अनुदैर्घ्य तरंगें", "अनुदैर्घ्य तरंगों"],
    "तरंग फलन": ["तरंग फलनों"],
    "पुनर्भरण": ["पुनर्भरणों"],
    "प्रवणता": ["प्रवणताएँ", "प्रवणताओं"],
    "अभिलंब प्रतिक्रिया": ["अभिलंब प्रतिक्रियाएँ"],
    "एकवर्णी तरंग": ["एकवर्णी तरंगें", "एकवर्णी तरंगों"],
    "चतुर्थांश-तरंग परत": ["चतुर्थांश-तरंग परतें", "चतुर्थांश-तरंग परतों"],
    "मुक्त एंथैल्पी": ["मुक्त एंथैल्पियाँ"],
    "सीमांत परत": ["सीमांत परतें"],
    "घर्षण बल": ["घर्षण बलों"],
    "टेलीग्राफ समीकरण": ["टेलीग्राफ समीकरणों"],
    "तुंड": ["तुंडों"],
    "पथांतर": ["पथांतरों"],
    "मध्यदर्शी पैमाना": ["मध्यदर्शी पैमाने"],
    "रासायनिक विभव": ["रासायनिक विभवों"],
    "रैखिक ध्रुवण": ["रैखिक ध्रुवणों"],
    "विद्युत्चुंबकीय तरंग": ["विद्युत्चुंबकीय तरंगों"],
    "वृत्तीय ध्रुवण": ["वृत्तीय ध्रुवणों"],
    "संचरण-रेखा": ["संचरण-रेखाओं"],
}

# No unit name is a harvested term in Book 4 hi, so nothing needs masking.
EXTRA_PROTECT = []

AMBIG_POLICY = "drop"
