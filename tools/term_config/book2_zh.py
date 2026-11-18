"""Book 2 -- Simplified Chinese. Curation only; the rules live in tools/termlink/.

Written 2026-11-18 for the pilot run (sources/TRANSLATION_BOOKS_1-5_ZH.md) before the translation existed, from the
English and French configs' choices; refined at the book's close against the link census (pilot_translation/census.py).
Chinese is matched in CJK mode (lang_zh.py): no word boundary inside Han text, so a word that is also part of a common
compound or an everyday verb must be stopped or dropped here. One-character terms are never linked.
"""

# result names are never terms (the French NOT_A_TERM, in Chinese)
NOT_A_TERM = ("定理", "引理", "不等式", "公式", "判据", "准则", "原理", "恒等式", "法则", "定律", "悖论", "问题")

# Mirrors book2_en.py, then the census at the book's close (2026-11-18): a STOPped word is still linked in the chapter
# that defines it.
STOP = {
    "速率",      # "speed", stopped in English; harvested from the velocity-vector definition (183 links against 38)
    "静止",      # "rest" / "at rest", stopped and dropped in English (121 links to the reference-frame definition)
    "纤芯",      # "core", stopped in English (a reactor core, the Earth's core elsewhere)
    "谱线",      # spectral lines: 101 links against English's 5, in every spectroscopy sentence
    "电荷",      # charge: English never links the bare word in this book (139 against 3, through "coulomb")
    "电流",      # current: as in book1_zh.py (144 against 7)
    "推力",      # "push" from the force inventory; in the pressure chapter it is a pressure force
}
DROP = {
    "竖直方向", "竖直",   # "vertical", dropped in English: the weight definition reached an oscilloscope's vertical axis
    "绝对",               # "absolute", dropped in English
}
EXTRA = {}          # manual {term: label}, added at the book's close (index-only keys have no space in Chinese)
NO_CAPITAL = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 20
EXTRA_PROTECT = []
