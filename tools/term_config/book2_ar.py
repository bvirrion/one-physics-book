"""Physics Book 2 (Grades 10-12) — Arabic term configuration.

Curated, NOT a translation of book2_en.py: the English config's STOP/DROP
lists key on English words that do not exist here, and Arabic raises traps of
its own. Seeded by the orchestrator with the parts that are language-wide;
the book agent owns everything below and should grow it while translating.

Arabic traps to expect (see arabic_style_card.md §4):

  * Proclitics. The article ال and the one-letter particles و ف ب ك ل attach
    to the front of the word, and inside a noun phrase every word carries
    them. tools/term_config/lang_ar.py handles that in HEAD; the cost is that
    a short term can now match with a leading particle it never meant, so
    watch for wrong-sense links and hand-DROP them.
  * Broken plurals. Arabic pluralises by internal vowel change (دالة/دوال،
    حد/حدود), which no suffix rule reaches. lang_ar.py sets WORD_TAIL = ''
    and DERIVE = False on purpose, so every plural a chapter actually uses
    must be declared here, in DERIVED or EXTRA, term by term.
  * NO_CAPITAL is structurally inert: Arabic has no letter case, so nothing
    keys on it. Where the English config used it to separate a unit from the
    physicist it is named after, use EXTRA_PROTECT instead.

Regenerate after editing:
    python3 tools/link_defined_terms.py --book 2 --lang ar --unwrap --apply
    python3 tools/link_defined_terms.py --book 2 --lang ar --apply
"""

# Result-names: words that head a STATEMENT, never a defined term. The
# defaults in link_defined_terms.py are English, so without this list every
# "مبرهنة فيثاغورس" would try to become a term.
NOT_A_TERM = ("مبرهنة", "قضية", "نتيجة", "متراجحة", "صيغة", "معيار",
              "مبدأ", "متطابقة", "قانون", "قاعدة", "مفارقة", "مسألة",
              "خاصية", "علاقة")

# Ordinary language in this book; still links in its own chapter.
STOP = {
    # the optical-fibre core (g10 refraction). Arabic قلب is also the heart
    # (the ECG problem of g10 signals, the cardiologist of g12 Doppler), the
    # iron core of an electromagnet (g11 magnetic fields) and the Sun's core
    # (g12 nuclear energy). Mirrors the English config's "core".
    "قلب",
    # the fibre cladding (g10 refraction). Arabic غلاف is also the atmosphere
    # (الغلاف الجوي, everywhere from g10 pressure on), the exponential
    # envelope of a damped oscillation (g12 oscillators, RLC) and a stellar
    # atmosphere (g12 quantum world). English "cladding" has no such twins.
    "غلاف",
}

# Never a link anywhere: harvested from a definition that merely uses the
# word, so every occurrence would point at the wrong statement.
DROP = {
    # harvested from the weight definition; in prose it is "the vertical" or
    # "perpendicular" (angle with the vertical, vertical component, the
    # perpendicular bisector). Mirrors the English config's "vertical".
    "العمودي",
    # harvested from the relative-pressure theorem; in prose it is always
    # "relative" (relative error, relative fluctuation, relative drift).
    "النسبي",
    # "at rest" / "motionless", harvested from the reference-frame definition:
    # "released from rest" must not link to a definition of a frame. Every
    # surface form has to be named — Arabic derivation is not suffixal.
    "السكون", "سكون", "فالسكون", "والسكون", "بالسكون",
    "ساكنًا", "ساكن", "ساكنة",
}

# Named laws and phrases the harvest cannot reach: NOT_A_TERM rejects every
# display headed by قانون, and the Arabic head of these phrases is a word the
# book uses everywhere. Mapping them by hand recovers the English link targets.
EXTRA = {
    "قانون سنيل": "thm:g10:refraction:snell",
    "قانون بويل": "prop:g10:pressure:boyle",
    "قانون أوم": "prop:g11:circuits-and-power:ohm",
    "قانون نيوتن الأول": "thm:g12:newtons-laws:first",
    "قانون نيوتن الثاني": "thm:g12:newtons-laws:second",
    "قانون نيوتن الثالث": "thm:g12:newtons-laws:third",
    "خطوط المجال": "def:g11:electric-gravitational-fields:lines",
    "خط المجال": "def:g11:electric-gravitational-fields:lines",
    "الانحراف المغناطيسي": "def:g11:magnetic-fields:earth",
    "التسارع المركزي": "thm:g12:kinematics-2d:centripetal",
    "ثابت التفكك": "def:g12:radioactive-decay:lambda",
    "دارات التوقيت": "rem:g12:rc-rl-circuits:applications",
    "صدى": "rem:g10:signals-and-waves:honest",
}

# Phrases where a defined word means something else. In a caseless script this
# is also the only way to keep a unit apart from the physicist it is named
# after (English does that with NO_CAPITAL, which is inert here).
EXTRA_PROTECT = (
    # --- Newton the man, not the newton the unit -----------------------
r'قوانين\s+نيوتن', r'مدفع\s+نيوتن', r'رمية\s+نيوتن',
    r'اختبار\s+نيوتن', r'تجربة\s+نيوتن', r'بصيرة\s+نيوتن', r'تحقّق\s+نيوتن',
    r'أجراه\s+نيوتن', r'وذكرها\s+نيوتن', r'خمّن\s+نيوتن', r'استخلص\s+نيوتن',
    r'سمّى\s+نيوتن', r'استنتج\s+نيوتن', r'تهدم\s+نيوتن',
    r'نيوتن\s+الكبرى',
    r'نيوتن\s+بأن', r'نيوتن\s+بالأرقام', r'نيوتن\s+سنة', r'نيوتن\s+لم\s+يكن',
    r'نيوتن\s+للقمر',
    # g11 ch09 cites the second law before g12 defines it: without this the
    # fallback would link نيوتن to the unit.
    r'عن\s+قانون\s+نيوتن',
    # --- the other eponyms --------------------------------------------
    r'ضياع\s+جول', r'مفعول\s+جول',
    r'قانون\s+كولوم', r'تنافر\s+كولوم', r'أرسى\s+كولوم', r'تنفرد\s+كولوم',
    r'حاجز\s+كولوم',
    # --- السعة: capacitance (g12 circuits), not amplitude (g10 signals) --
    r'حوّل\s+السعة', r'السعة\s+التي\s+تلتقط', r'السعة\s+التي\s+توالف',
    r'مقلوب\s+السعة', r'السعة\s+اللازمة', r'السعة\s+الطفيلية',
    # --- الثانية: the ordinal, not the SI second ------------------------
    r'السنة\s+الثانية', r'المسلَّمة\s+الثانية', r'الثانية\s+عشرة',
    # --- بطاقة: "the data card", not بـ+طاقة "with the energy" ----------
    r'بطاقة\s+المعطيات', r'بطاقة\s+الورشة',
    # --- مدى: "over the span of", not the projectile's range ------------
    r'على\s+مدى',
    # --- متعادلة: electrically neutral, not "balanced forces" -----------
    r'متعادلة\s+بما\s+هو\s+أفضل', r'متعادلة\s+بدقة', r'متعادلة\s+إلى\s+نحو',
    r'مماثلة\s+لها\s+متعادلة',
    # --- شدّ الحبل: the tug of war, not the tension in a rope ------------
    r'شدّ\s+الحبل',
)

DERIVED = {}          # declared plurals and variants (see the note above)
PRIMARY_OK = set()
NO_CAPITAL = set()    # inert in a caseless script; use EXTRA_PROTECT instead

AMBIG_POLICY = "nearest-preceding"
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40
