"""Book 2 -- hi. Curation only; the rules live in tools/termlink/.

Hindi bodies (parts/grade-10..12/hi) use UTF-8 Devanagari.
High-school physics: AMBIG_POLICY nearest-preceding for the school spiral.

Hindi brings three problems English does not have.

* **Compounds are written apart.**  मात्रक, बल, क्षेत्र, ऊर्जा, तरंग are the
  *heads* of dozens of defined terms (गुरुत्वाकर्षण बल, विद्युत क्षेत्र,
  गतिज ऊर्जा …) and each head is also an ordinary noun used on nearly every
  page.  Harvested bare they would link the whole book to one definition, so
  the bare heads sit in ``STOP``/``DROP`` while the full phrases keep linking.
* **Postpositions glue to the noun.**  क्षेत्र/क्षेत्र‍ों, मात्रक/मात्रकों:
  ``lang_hi.py`` grows the oblique tails, so no plural table is needed here.
* **Unit names and physicists' names collide.**  न्यूटन is the unit *and* the
  man (न्यूटन का दूसरा नियम), जूल the unit *and* the effect (जूल प्रभाव),
  ओम the unit *and* the law.  ``NO_CAPITAL`` keeps the surnames out of the
  unit definitions.
"""

# Environment names that are never terms in themselves.
NOT_A_TERM = ("प्रमेय", "उपप्रमेय", "असमिका", "सूत्र", "मानदंड",
              "सिद्धांत", "सर्वसमिका", "नियम", "नियम की", "नियम के",
              "विरोधाभास", "समस्या", "नियम का", "नियम में",
              "परिभाषा", "प्रतिज्ञप्ति", "टिप्पणी", "उदाहरण", "विधि")

# A word still links inside the chapter that defines it, but nowhere else:
# these are ordinary Hindi nouns that also head a defined compound.
STOP = {
    # heads of compound terms, and ordinary words everywhere else
    "बल", "ऊर्जा", "कार्य", "क्षेत्र", "तरंग", "वेग", "चाल", "गति",
    "दाब", "ताप", "ऊष्मा", "आवेश", "धारा", "प्रतिरोध", "शक्ति",
    "मात्रक", "मान", "संकेत", "प्रकाश", "लेंस", "नाभिक", "कक्षा",
    "भार", "द्रव्यमान", "दूरी", "समय", "आयाम", "आवृत्ति", "क्षमता",
    "स्रोत", "रेखा", "बिंदु", "तंत्र", "माध्यम", "सतह", "अवस्था",
    # words the MT harvest would otherwise pick up bare
    "योग", "युग्म", "संयोजन", "सभी", "एक साथ", "क्रमित",
    "पहला", "पहली", "सामान्य", "धारणा", "कठोरता से",
}

# Unit names that are also the physicists' surnames: only the lower-case
# unit sense is a defined term, the surname must not link.
NO_CAPITAL = {
    "न्यूटन", "जूल", "वाट", "पास्कल", "केल्विन", "टेस्ला",
    "हर्ट्ज़", "कूलॉम", "कूलंब", "वोल्ट", "ऐम्पियर", "एम्पियर",
    "ओम", "फैराड", "हेनरी", "बेक्रेल", "सीवर्ट", "ग्रे", "क्यूरी",
    "वेबर", "सीमेंस", "डायॉप्टर",
}

# Phrases the harvester cannot see (they never appear as \emph{...} in a
# definition) but that a reader should still be able to click.
EXTRA = {
    "प्रकाश तरंग": "def:g12:light-as-wave:lightwave",
    "निर्वात में तरंगदैर्घ्य": "def:g12:light-as-wave:lightwave",
    "प्रति न्यूक्लियॉन बंधन ऊर्जा": "def:g12:nuclear-energy:pernucleon",
    "निरोधी विभव": "def:g12:quantum-world:stopping",
    "बॉयल के नियम": "prop:g10:pressure:boyle",
    "बॉयल का नियम": "prop:g10:pressure:boyle",
    "स्नेल का नियम": "thm:g10:refraction:snell",
    "स्नेल के नियम": "thm:g10:refraction:snell",
    "स्नेल का अपवर्तन नियम": "thm:g10:refraction:snell",
    "न्यूटन का पहला नियम": "thm:g12:newtons-laws:first",
    "न्यूटन के पहले नियम": "thm:g12:newtons-laws:first",
    "न्यूटन का दूसरा नियम": "thm:g12:newtons-laws:second",
    "न्यूटन के दूसरे नियम": "thm:g12:newtons-laws:second",
    "न्यूटन का तीसरा नियम": "thm:g12:newtons-laws:third",
    "न्यूटन के तीसरे नियम": "thm:g12:newtons-laws:third",
    "आइंस्टाइन का प्रकाश-विद्युत संबंध": "thm:g12:quantum-world:einstein",
    "प्रकाश-विद्युत संबंध": "thm:g12:quantum-world:einstein",
    "कार्य फलन": "thm:g12:quantum-world:einstein",
    "परिमाण की कोटि": "def:g10:orders-of-magnitude:oom",
    "सार्थक अंक": "def:g10:orders-of-magnitude:sigfig",
    "वैज्ञानिक संकेतन": "def:g10:orders-of-magnitude:scinot",
    "जड़त्व का सिद्धांत": "thm:g10:inertia:principle",
    "ऊर्जा संरक्षण": "thm:g10:energy-conservation:conservation",
    # Named laws and statements whose Hindi form the harvester cannot see,
    # because the English carries them in an environment title rather than
    # in an \emph{...}\index{...} pair.
    "ओम का नियम": "prop:g11:circuits-and-power:ohm",
    "ओम के नियम": "prop:g11:circuits-and-power:ohm",
    "काल-विस्तारण": "thm:g12:special-relativity:dilation",
    "लंबाई-संकुचन": "prop:g12:special-relativity:contraction",
    # Compounds whose Hindi plural the oblique-tail rules do not reach.
    "क्षेत्र रेखाएँ": "def:g11:electric-gravitational-fields:lines",
    "शंकु कोशिकाएँ": "def:g11:color-light-sources:cones",
    "शंकु कोशिका": "def:g11:color-light-sources:cones",
}

# Spans masked before linking: a phrase whose words belong to a different
# sense than the definition they would otherwise reach.
#   * "वायु का प्रतिरोध" is aerodynamic drag, not the electrical quantity;
#   * "दस की घातें" is a mathematical power, not the physical one;
#   * "सूर्य का नाभिक" / "लोहे का क्रोड" are cores, not atomic nuclei;
#   * "चिह्न" is the algebraic sign, not the signal of g10 ch08.
# Never consume a `$` (use a lookahead) and never write a literal space
# (prose wraps): see the header of tools/termlink/protect.py.
EXTRA_PROTECT = [
    r"वायु\s+का\s+प्रतिरोध",
    r"वायु\s+के\s+प्रतिरोध",
    r"दस\s+की\s+घात",
    r"दो\s+की\s+घात",
    r"सूर्य\s+का\s+नाभिक",
    r"लोहे\s+का\s+क्रोड",
    r"पृथ्वी\s+का\s+क्रोड",
    r"एक\s+ही\s+चिह्न",
    r"चिह्न\s+बदल",
    r"तंतु\s+का\s+क्रोड",
    # Hindi has no capitals, so the man Newton and the unit newton are the
    # same string: mask the surname senses, keeping the named laws (EXTRA).
    r"न्यूटन\s+ने",
    r"न्यूटन\s+को",
    r"न्यूटन\s+की",
    r"न्यूटन\s+के\s+नियम",
    r"न्यूटन\s+के\s+तोप",
    r"स्वयं\s+न्यूटन",
    r"तो\s+न्यूटन",
]

DROP = set(STOP)
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40
