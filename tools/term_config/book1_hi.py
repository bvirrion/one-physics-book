"""Book 1 -- hi. Curation only; the rules live in tools/termlink/.

Young-book register, Hindi edition. The traps are not the English ones.

* **Compounds are written apart, and their heads are ordinary words.**
  प्रकाश, ऊष्मा, बल, ऊर्जा, चाल head dozens of defined phrases (प्रकाश
  स्रोत, गतिज ऊर्जा, औसत चाल …) and are also everyday nouns; the linker's
  longest-match rule lets both live, so the heads stay linkable exactly as
  their English counterparts (light, heat, force, energy, speed) do.
* **One Hindi word often carries two English ones.**  सिरा is the
  \\omterm-worthy battery terminal *and* the end of anything; चालक is the
  conductor of grade 4 *and* the driver of the road-safety chapter; मीटर is
  the length unit *and* the electricity meter by the front door. The
  ordinary senses are masked in ``EXTRA_PROTECT``, or the word is dropped
  outright when the ordinary sense dominates.
* **No capitals.**  Hindi cannot separate the unit न्यूटन from the man
  न्यूटन by spelling, so the surname senses are masked instead of listed in
  ``NO_CAPITAL``.

Terms are spelled as the bodies spell them: raw UTF-8 Devanagari, nuqta
included (क़, ज़, फ़), no TeX escapes. ``lang_hi.py`` grows no suffixes, so
oblique plurals (सिरों, कलाओं) simply do not link -- deliberate.
"""

# Environment names that are never terms in themselves.
NOT_A_TERM = ("प्रमेय", "उपप्रमेय", "असमिका", "सूत्र", "मानदंड",
              "सिद्धांत", "सर्वसमिका", "नियम", "नियम की", "नियम के",
              "विरोधाभास", "समस्या", "नियम का", "नियम में",
              "परिभाषा", "प्रतिज्ञप्ति", "टिप्पणी", "उदाहरण", "विधि")

# Still linked inside the chapter that defines them, nowhere else: honest
# terms there, ordinary Hindi everywhere else.
STOP = {
    # the Moon's phase in its chapter; कला also means art or skill
    "कला",
    # the magnet's pole in its chapter; the Earth's geographic poles and the
    # compass chapters elsewhere (उत्तरी/दक्षिणी ध्रुव keep their links)
    "ध्रुव",
    # the circuit-diagram symbol in its chapter; "(संकेत: …)" heads every
    # hint in every exercise of every other grade
    "संकेत",
    # the sound-carrying medium in its chapter; "के माध्यम से" elsewhere
    "माध्यम",
}

# Hindi has no capitals: the unit/surname collisions are handled by
# EXTRA_PROTECT below, so this stays empty.
NO_CAPITAL = set()

EXTRA = {}            # manual {term: label}; overrides every rule

DROP = {
    # the battery's terminal, and the end of every rope, ramp, tunnel and
    # sentence in nine years of prose
    "सिरा", "सिरे",
    # "उस पल", "इसी पल" -- the ordinary time word (अवधि keeps its link)
    "पल",
    # ordinary time-of-day words on every page; सूर्योदय and सूर्यास्त keep
    # their links, exactly as in the English edition
    "दिन", "रात",
    # bare adjectives: the phrases they head (एकसमान गति, परिवर्ती गति,
    # वृत्तीय गतिपथ, सरल रेखीय गतिपथ, खुला/बंद परिपथ) survive as terms of
    # their own -- while bare बंद closes doors, jars and chapters, and
    # bare खुला opens windows, on every second page
    "एकसमान", "परिवर्ती", "वृत्तीय", "सरल रेखीय", "खुला", "बंद",
    # the grade-1 adjectives of warmth: ordinary Hindi in nine grades of
    # prose ("गरम ब्रेक", "गरम चाय"), exactly as the English edition drops
    # hot/cold
    "गरम", "ठंडा",
    # the unit is unambiguous but ubiquitous -- "हर सेकंड", "कुछ सेकंड",
    # "सेकंड के दसवें हिस्से" -- and the English edition drops it too
    "सेकंड",
    # the senses that are also ordinary words ("उसकी दृष्टि में", "स्वाद
    # अच्छा है"); श्रवण and घ्राण stay linked, being technical
    "दृष्टि", "स्पर्श", "स्वाद",
}

DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"   # a spiral curriculum re-defines its terms
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40

# Spans no link may enter. Every space is \s+ -- the sources wrap at 72
# columns and a phrase split across two lines must still be protected.
# Never consume a `$` (use a lookahead): see tools/termlink/protect.py.
EXTRA_PROTECT = [
    # mechanics' drag, not the electrical quantity R = U/I
    r"हवा\s+का\s+प्रतिरोध",
    r"हवा\s+की\s+रुकावट",
    # mathematics' powers, not electric power P = U I
    r"दस\s+की\s+घात",
    r"दस\s+की\s+घातों",
    r"दस\s+की\s+इकतालीस\s+घातें",
    # the buildings, not the quantity
    r"बिजलीघर",
    # चालक: the road-safety driver and the spacecraft crew, not the
    # conductor of grade 4
    r"चालक\s+दल",
    r"वाला\s+चालक",
    r"वाले\s+चालक",
    r"हर\s+चालक",
    r"चौकन्ना\s+चालक",
    r"चौकन्ने\s+चालक",
    r"थके\s+चालक",
    r"थका\s+चालक",
    r"चालक\s+की\s+सारणी",
    r"चालक\s+का\s+ध्यान",
    r"चालक\s+भी",
    r"चालक\s+प्रतिक्रिया",
    # मीटर: the electricity meter by the front door, not the SI length unit
    r"लगा\s+मीटर",
    r"लगे\s+मीटर",
    r"इसलिए\s+मीटर",
    r"मीटर\s+जीता",
    r"मीटर\s+बनाने",
    r"मीटर\s+और\s+बिल",
    r"मीटर\s+और\s+महीने",
    r"मीटर(?=\s+\$)",
    # the film's frames and the eye, not the mirror's or lens's image
    r"प्रतिबिंब\s+उतारने",
    # Hindi has no capitals: mask the man Newton, keep the unit न्यूटन
    r"न्यूटन\s+ने",
    r"न्यूटन\s+की",
    r"न्यूटन\s+के\s+नियम",
]
