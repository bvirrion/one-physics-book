"""Book 1 -- Simplified Chinese. Curation only; the rules live in tools/termlink/.

Written 2026-11-18 for the pilot run (sources/TRANSLATION_BOOKS_1-5_ZH.md) before the translation existed, from the
English and French configs' choices; refined at the book's close against the link census (pilot_translation/census.py).
Chinese is matched in CJK mode (lang_zh.py): no word boundary inside Han text, so a word that is also part of a common
compound or an everyday verb must be stopped or dropped here. One-character terms are never linked.
"""

# result names are never terms (the French NOT_A_TERM, in Chinese)
NOT_A_TERM = ("定理", "引理", "不等式", "公式", "判据", "准则", "原理", "恒等式", "法则", "定律", "悖论", "问题")

# Mirrors book1_en.py at the book's close (census, 2026-11-18). English links only the phrases "electric current" and
# "electric circuit"; in Chinese 电流 and 电路 are the whole term, and linking every one gave 402 and 126 links where
# English has 4 each (and 电路 was linked inside the definiendum \emph{串联电路}). They stay linked in their own chapter.
STOP = {
    "电流", "电路",
    # English STOPs "balanced"; Chinese 平衡 is also the scale's balance and 配平 (82 links against 5)
    "平衡", "平衡的",
    # English STOPs "symbol", "observation", "observe"
    "符号", "观察", "观察结果",
    # "at that moment": English DROPs "moment"; 时刻 is constant in prose (62 links against 13)
    "时刻",
}
# English DROPs: the senses (hearing kept, as in English), night/daytime, bare adjectives of shape
DROP = {"感官", "视觉", "触觉", "嗅觉", "味觉", "夜晚", "白天", "直线的", "圆周的"}
EXTRA = {}          # manual {term: label}, added at the book's close (index-only keys have no space in Chinese)
NO_CAPITAL = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 20
EXTRA_PROTECT = []
