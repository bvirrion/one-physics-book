"""Physics Book 1 (Grades 1-9) — Arabic term configuration.

Curated, NOT a translation of book1_en.py: the English config's STOP/DROP
lists key on English words that do not exist here, and Arabic raises traps
of its own (see arabic_style_card.md and tools/term_config/lang_ar.py).

Young-book register: most defined vocabulary is also ordinary Arabic, so a
word earns a link only if it means the defined thing in nearly all of its
uses. Everyday furniture words are DROPped (their compound phrases survive
as terms of their own); words that are honest terms inside their own
chapter but ordinary language elsewhere are STOPped.

Two Arabic traps shape the lists below:

  * Proclitics. lang_ar.py lets ال and the particles و ف ب ك ل attach to
    every word of a term, so a one-word term matches far more surface forms
    than its English twin -- and over-links accordingly.
  * No letter case. NO_CAPITAL is structurally inert; where the English
    config used it to keep a unit apart from the physicist it honours, use
    EXTRA_PROTECT.

Regenerate after editing:
    python3 tools/link_defined_terms.py --book 1 --lang ar --unwrap --apply
    python3 tools/link_defined_terms.py --book 1 --lang ar --apply
"""

# Result-names: words that head a STATEMENT, never a defined term.
NOT_A_TERM = ("مبرهنة", "قضية", "نتيجة", "صيغة", "مبدأ", "قانون", "قاعدة",
              "مسألة", "خاصية", "خاصّية", "علاقة", "طريقة")

# Honest terms inside their own chapter, ordinary language elsewhere.
STOP = {
    # observation (g1); "ملاحظة" also heads every ordinary remark
    "ملاحظة", "الملاحظة",
    # equilibrium (g2); "متوازن/توازن" also balances books, budgets and
    # forces long before and after that chapter
    "توازن", "التوازن", "متوازن",
    # battery terminal (g3); also the magnetic pole (g4), the Earth's
    # poles and the polar star. Mirrors the English config's "pole".
    "قطب", "القطب",
    # circuit-diagram symbol (g6); "رمز" is also the symbol of a unit and
    # of every mathematical quantity
    "رمز", "الرمز",
    # lunar phase (g7); "طور" is also any stage of any process (the
    # parachutist's two phases). "الأطوار" stays linked -- always lunar.
    "طور",
    # the SI second (g2); "الثانية" is the ordinal in most of its uses
    # ("العيّنة الثانية", "المرحلة الثانية", "الثانية عشرة")
    "الثانية",
}

# Never a link anywhere: ordinary vocabulary of the register, or a harvest
# artefact. Compound phrases built on these words survive as terms.
DROP = {
    # the five senses (g1): bare sense-words are ordinary everywhere, and
    # "نافذة السمع" (g8) would point at the wrong chapter entirely.
    # "حاسّة" itself stays: it is never ordinary.
    "بصر", "البصر", "سمع", "السمع", "لمس", "اللمس",
    "شمّ", "الشمّ", "ذوق", "الذوق",
    # hot/cold (g1): ordinary adjectives, thousands of uses
    "ساخن", "بارد",
    # "جذب" is the magnet's attraction in g1 -- and gravitation's pull in
    # g9 ("قانون الجذب العام", "جذب الأرض"): wrong sense far too often
    "جذب",
    # ordinal/adverbial "ثانية" = "again, a second time", ubiquitous
    "ثانية",
    # "لحظة" = "a moment", ordinary time word (the duration definition
    # keeps its link through "مدة")
    "لحظة", "اللحظة",
    # "سنة" = this year, last year, four light-years: ordinary. The
    # phrases "فصل السنة" / "فصول السنة" keep their links.
    "سنة", "السنة",
    # bare adjectives harvested from motion/circuit definitions; the
    # phrases "مسار مستقيم", "مسار دائري", "حركة منتظمة", "حركة متغيّرة",
    # "دارة مغلقة", "دارة مفتوحة" survive
    "مستقيم", "دائري", "منتظمة", "متغيّرة", "مغلقة", "مفتوحة",
    # "الليل" and "النهار" are ordinary time-of-day words on every page;
    # "الشروق" and "الغروب" keep their links (mirrors the English config)
    "ليل", "الليل", "نهار", "النهار",
    # harvest artefacts: inflected surfaces that mean nothing on their own
    "تُلاحِظ", "صورةً", "وحدته", "مقصورًا",
}

EXTRA = {}            # manual {term: label}; overrides every rule

# Phrases where a defined word means something else. In a caseless script
# this is also the only way to keep a unit apart from its eponym.
EXTRA_PROTECT = (
    # --- الوسط: "in the middle", not the sound-carrying medium (g7) ----
    r'في\s+الوسط', r'قرب\s+الوسط', r'من\s+الوسط', r'فوق\s+الوسط',
    r'الوسط\s+ودونه', r'الوسط\s+إلى', r'دون\s+الوسط',
    r'وسط\s+ناتئ', r'ووسط\s+مجوّف',
    # --- ظلّ: the verb "kept on, remained", not the shadow (g1) --------
    r'ظلّ\s+يعمل', r'ظلّ\s+يتبع', r'ظلّ\s+منطلقًا',
    # --- بقوة: the adverb "strongly", not the force (g2) ---------------
    r'بقوة\s+العشرة', r'بقوة\s+عشرة', r'بقوة\s+أكبر', r'بقوة\s+زائدة',
    r'تكسر\s+بقوة', r'تبئّر\s+بقوة', r'الفكرة\s+بقوة',
    r'التيار\s+بقوة', r'عنه\s+بقوة',
    # --- قوة/قوى العشرة: the mathematical power of ten (g8-g9), never
    #     the physical force. Mirrors the English config's "powers of ten".
    r'قوة\s+العشرة', r'قوى\s+العشرة', r'قوة\s+عشرة',
    r'قوة\s+من\s+قوى', r'بعد\s+قوة', r'قوّتها',
    # --- حجم: "the size of", not the space a body occupies (g6) -------
    r'حجم\s+التأرجح', r'حجم\s+شهيّة', r'بحسب\s+الحجم',
    # --- بشدّة: the adverb "tightly", not the current's intensity ------
    r'ممسوكة\s+بشدّة',
    # --- the two-pole alternator, not the g5 simple machine ------------
    r'للآلة\s+البسيطة\s+ذات',
    # --- دور: "plays the part of", not the AC period (g9) --------------
    r'يؤدّي\s+دور', r'ومن\s+دور', r'دور\s+الموشور',
    # --- محور: the instrument's own axis, not the Earth's spin axis ----
    r'محور\s+الآلة',
    # --- سعة: "as wide as the sky", not the vibration's amplitude ------
    r'بسعة\s+السماء',
    # --- شدّة: "how strongly", not the current's intensity -------------
    r'مدى\s+شدّة',
    # --- قدرة: "the ability to", not electric power --------------------
    r'قدرة\s+على', r'القدرة\s+على', r'وقدرة\s+التدقيق',
    # --- وحدة: the currency unit of the energy bill, not the SI unit ---
    r'وحدة\s+نقدية', r'وحدات\s+نقدية',
    # --- ضوء: "light" the adjective of a paper cup has no Arabic twin;
    #     but "الضوء الأخضر" of a traffic light is still the phenomenon.
    # --- الجهاز/المصباح phrases need no protection: no ordinary twins.
)

DERIVED = {}          # declared plurals and variants (Arabic breaks them)
PRIMARY_OK = set()
NO_CAPITAL = set()    # inert in a caseless script; use EXTRA_PROTECT instead

AMBIG_POLICY = "nearest-preceding"   # a spiral curriculum re-defines terms
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40
