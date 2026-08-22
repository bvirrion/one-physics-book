"""Physics Book 4 (University Year 2) -- Arabic term configuration.

Curated against Book 4's own harvest, NOT a translation of `book4_en.py` and
no longer the Book 3 seed it started from: the English config keys on English
words that do not exist here, and Book 3's lists key on a different book. Run

    python3 tools/link_defined_terms.py --book 4 --lang ar --terms

after every edit; the whole volume carries ~1 230 links.

Two Arabic facts drive the shape of this file.

  * Proclitics. ال and the one-letter particles و ف ب ك ل attach to the front
    of every word of a noun phrase (lang_ar.py, HEAD_ON_EVERY_WORD), so a
    one-word term fires far more often than its English twin. Every STOP entry
    below is a one-word term for exactly that reason.
  * Broken plurals. lang_ar.py sets DERIVE = False, so any plural this book
    actually uses has to be declared in DERIVED, term by term.

The Book 3 seed carried 48 STOP words, 10 DROP words, 23 EXTRA entries and 8
DERIVED entries. Not one of them survives: the STOP and DROP words are never
harvested in Book 4 (checked term by term against the raw harvest), and every
EXTRA entry pointed at a `thm:b1:` / `prop:b1:` label -- a Book 3 result that
does not exist in this volume, i.e. 23 dangling link targets.

Regenerate after editing:
    python3 tools/link_defined_terms.py --book 4 --lang ar --unwrap --apply
    python3 tools/link_defined_terms.py --book 4 --lang ar --apply
"""

# Result-names: words that head a STATEMENT, never a defined term. Arabic gives
# the results of this book these heads, so the harvest must reject them --
# see EXTRA for the one link this costs.
NOT_A_TERM = ("مبرهنة", "قضية", "نتيجة", "متراجحة", "صيغة", "معيار",
              "مبدأ", "متطابقة", "قانون", "قاعدة", "مفارقة", "مسألة",
              "خاصية", "علاقة", "تعريف", "ملاحظة")

# Ordinary language in this register, or a word whose sense elsewhere in the
# book is not the sense its definition gives it. A STOPped word still links
# inside the chapter that defines it. These are the five words `book4_en.py`
# stops (absorption, efficiency, laser, steady, threshold), in the forms the
# Arabic harvest actually produced.
STOP = {
    "الامتصاص",   # absorption: the Einstein process (ch. 23) vs the ordinary
                  # word, which carries chs. 16-22 and 26
    "ليزر", "الليزر",  # the whole of ch. 23 says it on every line
    "مستقر",     # steady (open systems, ch. 27) vs "جريان مستقر" (ch. 02),
                  # "موجة مستقرة" (ch. 04) and "حالة مستقرة" (ch. 30):
                  # one adjective, four chapters, four senses
    "العتبة",     # the laser threshold vs "عتبة السمع" (ch. 06) and the
                  # ordinary "عتبة" of chs. 20 and 31
    "جسم صلب",   # the rigid body of ch. 01 vs the ordinary "solid": chs. 06,
                  # 15, 24, 25, 28 and 29 all say it in the second sense, and
                  # English links this term exactly once, in ch. 01
    "مردودها",    # efficiency: harvested with the pronoun from the fin
                  # statement (ch. 25), but every engine in chs. 27-28 has one
}

# Never a link anywhere: harvested from a definition that merely uses the word.
# The four English DROPs that have an Arabic counterpart -- bare adjectives and
# a bare participle, useless as links and wrong wherever they fire.
DROP = {
    "الأويلري",          # Eulerian: the description is "وصف أويلري", which
                         # is harvested separately and is the real term
    "مكمَّمة",           # quantised: the adjective, not the quantisation
    "الثلاثي المستويات", # three-level / four-level: fragments of
    "الرباعي المستويات", # "ليزر ثلاثي المستويات", which is harvested whole
}

# Named laws the harvest cannot reach: NOT_A_TERM rejects every display headed
# by قانون, and Malus is the one result of this book that English links by that
# name (twice: the chapter opening and a figure caption). Joule's local law is
# harvested in English too but never linked there, and Arabic must not link the
# "قانون جول" of ch. 28, which is Book 3's gas law under the same name.
EXTRA = {
    "قانون مالوس": "prop:b2:plane-waves-polarization:malus",
}

# Phrases where a defined word means something else. Book 3 needed nine groups
# of these (سعة, الثانية, and the Ampère / Pascal / Kelvin unit-vs-person
# collisions); Book 4 harvests none of those words, so the list is empty and
# every entry would be dead weight.
EXTRA_PROTECT = ()

# Broken plurals and duals this book actually uses; lang_ar.py derives nothing,
# so each has to be named. Terms whose plural is itself harvested from a second
# definition (موجة مستقرة / موجات مستقرة, انقلاب جمهرة / انقلاب الجمهرة) are
# deliberately absent: the harvest already covers them.
DERIVED = {
    "خط تيار": ["خطوط التيار", "خطوط تيار"],
    "المنفث": ["منفث", "منفثًا", "منافث"],
    "الخانق": ["خانق", "خانقًا"],
    "قطار موجة": ["قطارات موجية", "قطارات الموجة"],
    "جبهة موجة": ["جبهات الموجة", "جبهات موجة", "جبهتي موجة"],
    "تغذية راجعة": ["تغذيات راجعة"],
    "موجة متلاشية": ["موجةً متلاشية", "أمواج متلاشية"],
    "كثافة التيار": ["كثافات التيار"],
    "ارتفاع السلّم": ["ارتفاع سلّم"],
    "مذبذب الاسترخاء": ["مذبذبات الاسترخاء"],
    "مهتز متعدد لامستقر": ["المهتزّ المتعدد اللامستقر"],
    "متجهة الدوران": ["متجهة دوران"],
    "مقاومة حرارية": ["مقاوماتها الحرارية"],
    "موجة كهرمغناطيسية": ["أمواج كهرمغناطيسية", "أمواجًا كهرمغناطيسية"],
    "تدحرج على مستو مائل": ["يتدحرج على مستو مائل"],
    "استقطاب خطي": ["استقطابًا خطيًّا", "استقطابين خطيين"],
    "استقطاب دائري": ["استقطابًا دائريًّا", "استقطابين دائريين"],
    "خط مسار": ["خطوط المسار"],
    "جسيم مائع": ["جسيمات مائعة"],
    "صفيحة موجية": ["صفائح موجية"],
    "شبكة حيود": ["شبكات حيود", "شبكات الحيود"],
    "ثنائي قطب متذبذب": ["ثنائيات قطب متذبذبة"],
    "دوامة نقطية": ["دوامات نقطية"],
    "معادلة ماكسويل": ["معادلات ماكسويل"],
}

# "جريان مستقر" is defined twice -- ch. 02 (the Eulerian description) and
# ch. 27 (the open-system balance). One spelling, one concept: send every use
# to the first definition rather than dropping the term.
PRIMARY_OK = {"جريان مستقر"}
NO_CAPITAL = set()    # inert in a caseless script; use EXTRA_PROTECT instead

AMBIG_POLICY = "drop"
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40
