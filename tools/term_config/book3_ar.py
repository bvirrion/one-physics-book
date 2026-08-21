"""Physics Book 3 (University Year 1) -- Arabic term configuration.

Curated, NOT a translation of book3_en.py: the English config's STOP/DROP
lists key on English words that do not exist here, and Arabic raises traps of
its own (see arabic_style_card.md §4 and the note in book2_ar.py).

Two Arabic facts drive everything below.

  * Proclitics. ال and the one-letter particles و ف ب ك ل attach to the front
    of every word of a noun phrase (lang_ar.py, HEAD_ON_EVERY_WORD). A one-word
    term therefore fires far more often than its English twin, and much of the
    extra is wrong-sense -- hence a STOP list roughly twice the English one.
  * Broken plurals. lang_ar.py sets DERIVE = False, so any plural this book
    actually uses is declared in DERIVED, term by term.

Regenerate after editing:
    python3 tools/link_defined_terms.py --book 3 --lang ar --unwrap --apply
    python3 tools/link_defined_terms.py --book 3 --lang ar --apply
"""

# Result-names: words that head a STATEMENT, never a defined term.
NOT_A_TERM = ("مبرهنة", "قضية", "نتيجة", "متراجحة", "صيغة", "معيار",
              "مبدأ", "متطابقة", "قانون", "قاعدة", "مفارقة", "مسألة",
              "خاصية", "علاقة", "تعريف", "ملاحظة")

# Ordinary language in this register, or a word whose sense elsewhere in the
# book is not the sense its definition gives it. A STOPped word still links
# inside the chapter that defines it.
STOP = {
    # --- the bare nouns of mechanics and thermodynamics: after ch. 12 a link
    # on every occurrence is pure noise (the English config stops the same
    # eleven words) -------------------------------------------------------
    "قوة", "كتلة", "سرعة", "تسارع", "ضغط", "الضغط", "حرارة", "الحرارة",
    "شغل", "شغلها", "عزم", "عزمه", "توتر", "التوتر",
    # --- overloaded exactly as in English --------------------------------
    "بار",            # the unit vs the numbers of ch. 21-25
    "صورة",           # the optical image vs "صورة المرآة" in the symmetry proofs
    "بؤرة",           # focus (optics) vs the ordinary noun
    "تدفق",           # electric flux (ch. 26) vs magnetic flux (ch. 29) vs
                      # the mass flow rate of ch. 24
    "وحدة", "الوحدة", # the SI unit vs "واحدة الكتلة", "متجهة واحدية"
    "بُعد",            # physical dimension vs "على بعد", "بُعد الصورة"
    "تحول", "التحول", # thermodynamic transformation vs ordinary usage
    "كسب",            # op-amp gain vs the verb
    "قلب",            # fibre core vs the Earth's core (ch. 26) and the coaxial
                      # core (ch. 28) and the iron core of a transformer (29)
    "غلاف",           # fibre cladding vs the cable sheath of ch. 28
    # --- Arabic-only collisions ------------------------------------------
    "إشارة", "الإشارة",  # signal (ch. 5) AND the *sign* of a charge, of a
                          # number: the second sense is on every page of 26-27
    "الطور",             # phase of matter (ch. 25) AND phase of a sinusoid
                          # (ch. 8, 29): one word, two chapters
    "مرجع",              # frame of reference vs "المرجع الأرضي" the circuit
                          # ground and "درجة الحرارة المرجعية"
    "مسار",              # trajectory vs "المسار" of a thermodynamic path and
                          # of an integration path
    "تقارب",             # convergence of a lens vs "تقارب الكثافتين" (ch. 25)
    "مطابقة",            # accommodation of the eye vs "مطابقة" = aligned,
                          # which is how ch. 27-28 describe a dipole in a field
    "حالة",              # state (thermodynamics) vs "في هذه الحالة"
    "نظام",              # regime (transients) vs "نظام إحداثيات", "جملة"
    "مجال",              # field vs "مجال من درجات الحرارة" (ch. 24)
    "طاقة",              # energy, everywhere from ch. 13 on
    "مقدار",             # quantity (ch. 1) vs "بمقدار" the ordinary preposition
    "قياس",              # measurement (ch. 1) vs "بالقياس إلى"
    "خطأ",               # error (ch. 1) vs the ordinary word
    "دور",               # period vs cycle vs "دور كارنو"
    "مركز",              # centre, ubiquitous
    "سطح",               # surface, ubiquitous
    "عين",               # the eye vs "عين" = the very same
    "وسط",               # medium vs "الوسط الخارجي", "في وسط"
    "جسم",               # body, ubiquitous
    "جملة",              # system, ubiquitous
    "مادة",              # matter/substance, ubiquitous
}

# Never a link anywhere: harvested from a definition that merely uses the word.
DROP = {
    # bare adjectives and adverbs, as the English config drops
    # ideal / ideally / linear / central
    "المثالي", "مثالي", "خطيًّا", "خطي", "مركزية", "مركزي",
    "محافظة", "محافظ",
    # "متوسط" is the arithmetic mean everywhere; harvested from the
    # mean-free-path / mean-power statements
    "متوسط", "المتوسط",
}

# Named laws and phrases the harvest cannot reach: NOT_A_TERM rejects every
# display headed by قانون / مبرهنة / مبدأ / قاعدة / علاقة / صيغة, and those are
# exactly the heads Arabic gives the results of this book. Mapping them by hand
# recovers the English link targets.
EXTRA = {
    "قانون كولوم":               "thm:b1:electrostatics-gauss:coulomb",
    "قانون غاوس":                "thm:b1:electrostatics-gauss:gauss",
    "قانون بيو-سافار":           "thm:b1:magnetostatics:biotsavart",
    "قانون لابلاس":              "prop:b1:first-law:transformations",
    "قانون فاراداي":             "thm:b1:induction:faraday",
    "قانون لنز":                 "thm:b1:induction:faraday",
    "قانونا جول":                "prop:b1:first-law:gas",
    "مبرهنة أرخميدس":            "thm:b1:fluid-statics:archimedes",
    "مبرهنة كارنو":              "thm:b1:heat-engines:carnot",
    "مبرهنة أمبير":              "thm:b1:magnetostatics:ampere",
    "مبرهنة كولوم":              "thm:b1:potential-capacitors:conductor",
    "متراجحة كلاوزيوس":          "thm:b1:heat-engines:clausius",
    "مبدأ الارتياب":             "thm:b1:quantum-introduction:heisenberg",
    "المبدأ الأول للترموديناميك": "thm:b1:first-law:firstlaw",
    "المبدأ الثاني للترموديناميك": "thm:b1:second-law-entropy:secondlaw",
    "علاقة كلاوزيوس-كلابيرون":   "thm:b1:phase-changes:clapeyron",
    "علاقة ماير":                "prop:b1:first-law:gas",
    "قاعدة الرافعة":             "thm:b1:phase-changes:lever",
    "قاعدة اليد اليمنى":         "prop:b1:magnetostatics:maps",
    "صيغة بولتزمان":             "prop:b1:second-law-entropy:boltzmann",
    "نصّ كلاوزيوس":              "prop:b1:second-law-entropy:clausiuskelvin",
    "نصّ كلفن":                  "prop:b1:second-law-entropy:clausiuskelvin",
    "العلاقة الأساسية لسكون الموائع": "thm:b1:fluid-statics:fundamental",
}

# Phrases where a defined word means something else. In a caseless script this
# is also the only way to keep a unit apart from the physicist it is named
# after (English does that with NO_CAPITAL, which is inert here).
EXTRA_PROTECT = (
    # --- Ampère the man, not the ampere the unit -------------------------
    r'مبرهنة\s+أمبير', r'حلقة\s+أمبير', r'مستطيل\s+أمبير',
    r'أمبير-لفات', r'الأمبير\s+\(تعريف\)', r'تعريف\s+الأمبير',
    r'لدى\s+أمبير', r'بتطبيق\s+أمبير', r'كلفن\s+من\s+جديد',
    # --- Pascal the man, not the pascal the unit -------------------------
    r'مبدأ\s+باسكال',
    # --- Kelvin the man, not the kelvin the unit -------------------------
    r'نصّ\s+كلفن', r'\(كلفن\)', r'كلفن\)',
    # --- Tesla / Henry / Weber never appear as people here, nothing needed
    # --- سعة: capacitance (ch. 27) vs amplitude (ch. 5, 8, 14, 29) --------
    r'سعة\s+التيار', r'سعة\s+السرعة', r'سعة\s+القوة', r'سعة\s+الاهتزاز',
    r'بالسعة\s+نفسها', r'سعته\s+\\qty', r'وسعته',
    # --- الثانية: the ordinal, not the SI second -------------------------
    r'السنة\s+الثانية', r'الجهة\s+الثانية', r'الثانية\s+عشرة',
    r'المرحلة\s+الثانية', r'الحالة\s+الثانية',
    # --- مول: the mole vs the verb-like uses -- none needed --------------
)

# Broken plurals and the few sound plurals this book actually uses; lang_ar.py
# derives nothing, so each has to be named.
DERIVED = {
    "عدسة رقيقة": ["عدسات رقيقة"],
    "موجة مستقرة": ["موجات مستقرة"],
    "خط المجال": ["خطوط المجال"],
    "حالة مجهرية": ["حالات مجهرية"],
    "نقطة كمومية": ["نقاط كمومية"],
    "تيارات دوامية": ["تيار دوامي"],
    "ثنائي قطب كهربائي": ["ثنائيات قطب كهربائية"],
    "ثنائي قطب مغناطيسي": ["ثنائيات قطب مغناطيسية"],
}

PRIMARY_OK = set()
NO_CAPITAL = set()    # inert in a caseless script; use EXTRA_PROTECT instead

AMBIG_POLICY = "drop"
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40
