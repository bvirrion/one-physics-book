"""Book 5 -- Simplified Chinese. Curation only; the rules live in tools/termlink/.

Written 2026-11-18 for the pilot run (sources/TRANSLATION_BOOKS_1-5_ZH.md) before the translation existed, from the
English and French configs' choices; refined at the book's close against the link census (pilot_translation/census.py).
Chinese is matched in CJK mode (lang_zh.py): no word boundary inside Han text, so a word that is also part of a common
compound or an everyday verb must be stopped or dropped here. One-character terms are never linked.
"""

# result names are never terms (the French NOT_A_TERM, in Chinese)
NOT_A_TERM = ("定理", "引理", "不等式", "公式", "判据", "准则", "原理", "恒等式", "法则", "定律", "悖论", "问题")

STOP = {
    # mirrors book5_en.py STOP (seeded 2026-11-18; refine at the close)
    "事件", "空穴", "金属", "可观测量", "自旋",
    # calibration against English's choices (book5_en.py links none of these: they are index-only keys there,
    # harvested here by INDEX_CJK): linked in their defining chapter only
    "简并", "坍缩", "玻恩定则", "费米子", "玻色子", "裂变", "链式反应", "半衰期", "放射性活度", "对撞机", "聚变",
    "有效势能", "顺磁性", "抗磁性", "铁磁性", "带隙", "氢原子", "声子", "相变", "超新星", "强相互作用", "弱相互作用",
    # 结合能 is both the crystal's cohesive energy (ch. 23) and the nucleus's binding energy (ch. 25)
    "结合能",
    # 约束 is also "confinement" (the electron's box, magnetic confinement): census chapter-set hits in ch. 7, 10, 19, 25
    "约束",
}
DROP = {
    # everyday words of the whole book that English never links (对称性 68, 二极管 21 → the p-n junction)
    "对称性", "二极管",
}
INDEX_CJK = True    # index-only keys are terms too (harvest.py, physics zh Book 3)
EXTRA = {"超精细结构": "ex:b3:spin-two-level:hyperfine"}   # English links "hyperfine" (index-only key) 5 times
NO_CAPITAL = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 20
EXTRA_PROTECT = []
