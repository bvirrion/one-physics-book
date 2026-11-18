"""Book 4 -- Simplified Chinese. Curation only; the rules live in tools/termlink/.

Written 2026-11-18 for the pilot run (sources/TRANSLATION_BOOKS_1-5_ZH.md) before the translation existed, from the
English and French configs' choices; refined at the book's close against the link census (pilot_translation/census.py).
Chinese is matched in CJK mode (lang_zh.py): no word boundary inside Han text, so a word that is also part of a common
compound or an everyday verb must be stopped or dropped here. One-character terms are never linked.
"""

# result names are never terms (the French NOT_A_TERM, in Chinese)
NOT_A_TERM = ("定理", "引理", "不等式", "公式", "判据", "准则", "原理", "恒等式", "法则", "定律", "悖论", "问题")

STOP = {
    # mirrors book4_en.py STOP (seeded 2026-11-18)
    "吸收", "效率", "激光", "稳态", "定常", "阈值",
    # the census at the close (zh links against English): kept in the defining chapter only
    "衰减",      # 87 against 23 ("attenuation")
    "线偏振", "圆偏振",   # 57 against 4
    "波包",      # 37 against 4
    "摩擦力",    # 41 against 8
    "光程", "波前", "主极大", "次极大", "光纤", "波导", "驻波",
}
DROP = {
    # mirrors book4_en.py DROP
    "欧拉", "欧拉的", "四能级", "三能级", "量子化的",
    # bare words English never links (2 links or fewer against 10 or more): the index-only harvest (INDEX_CJK)
    # put them on a theorem or proposition that only names them
    "起偏器", "采样", "混叠", "天线", "谐振腔", "导波", "刚体", "电导率", "电阻率", "迁移率", "热阻", "推力", "声强",
    "纵模", "沉降", "干涉", "湍流", "层流", "涡轮机", "节流", "条纹间距", "谐音", "水头", "截面", "辐照度", "分束器",
    "泊松方程", "规范",
}
INDEX_CJK = True    # index-only keys are terms too (harvest.py, physics zh Book 3)
EXTRA = {
    # a result name NOT_A_TERM drops (定律) but English links ("Malus's law")
    "马吕斯定律": "prop:b2:plane-waves-polarization:malus",
}
NO_CAPITAL = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 20
EXTRA_PROTECT = []
