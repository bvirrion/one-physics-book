"""Book 2 -- hi. Curation only; the rules live in tools/termlink/.

Hindi bodies (parts/grade-10..12/hi) use UTF-8 Devanagari.
High-school physics: AMBIG_POLICY nearest-preceding for school spiral.
"""

NOT_A_TERM = ("प्रमेय", "उपप्रमेय", "असमानता", "सूत्र", "मानदंड",
              "सिद्धांत", "सर्वसमिका", "नियम", "नियम की", "नियम के",
              "विरोधाभास", "समस्या", "नियम का", "नियम में")

STOP = {
    "योग",
    "युग्म",
    "संयोजन",
    "सभी",
    "कठोरता से",
    "एक साथ",
    "क्रमित",
    "पहला",
    "पहली",
    "बल",
    "ऊर्जा",
    "कार्य",
    "क्षेत्र",
    "तरंग",
    "वेग",
    "सामान्य",
    "धारणा",
}

NO_CAPITAL = {
    "न्यूटन",
    "जूल",
    "वाट",
    "पास्कल",
    "केल्विन",
    "टेस्ला",
    "हर्ट्ज़",
    "कूलॉम",
    "वोल्ट",
    "एम्पियर",
    "ओम",
}

EXTRA = {
    "प्रकाश तरंग": "def:g12:light-as-wave:lightwave",
    "निर्वात में तरंग दैर्ध्य": "def:g12:light-as-wave:lightwave",
    "प्रति न्यूक्लियॉन बंधन ऊर्जा": "def:g12:nuclear-energy:pernucleon",
    "निरोधी विभव": "def:g12:quantum-world:stopping",
    "बॉयल के नियम": "prop:g10:pressure:boyle",
    "बॉयल का नियम": "prop:g10:pressure:boyle",
    "स्नेल का नियम": "thm:g10:refraction:snell",
    "स्नेल का अपवर्तन नियम": "thm:g10:refraction:snell",
    "न्यूटन का दूसरा नियम": "thm:g12:newtons-laws:second",
    "न्यूटन का तीसरा नियम": "thm:g12:newtons-laws:third",
    "आइंस्टीन का फोटोइलेक्ट्रिक संबंध": "thm:g12:quantum-world:einstein",
    "फोटोइलेक्ट्रिक संबंध": "thm:g12:quantum-world:einstein",
    "कार्य फलन": "thm:g12:quantum-world:einstein",
}

DROP = set(STOP)
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40

EXTRA_PROTECT = []
