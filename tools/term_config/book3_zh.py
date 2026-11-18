"""Book 3 -- Simplified Chinese. Curation only; the rules live in tools/termlink/.

Written 2026-11-18 for the pilot run (sources/TRANSLATION_BOOKS_1-5_ZH.md) before the translation existed, from the
English and French configs' choices; refined at the book's close against the link census (pilot_translation/census.py).
Chinese is matched in CJK mode (lang_zh.py): no word boundary inside Han text, so a word that is also part of a common
compound or an everyday verb must be stopped or dropped here. One-character terms are never linked.
"""

# result names are never terms (the French NOT_A_TERM, in Chinese)
NOT_A_TERM = ("定理", "引理", "不等式", "公式", "判据", "准则", "原理", "恒等式", "法则", "定律", "悖论", "问题")

STOP = {
    # mirrors book3_en.py STOP (seeded 2026-11-18; refined with the census at the book's close)
    "热量", "热", "加速度", "纤芯", "铁芯", "量纲", "通量", "焦点", "增益", "接地", "质量", "力矩", "动量", "物镜",
    "压强", "压力", "温度", "变换", "单位", "速度",
    # the census at the close (links against English): words English links a handful of times or not at all
    "电场",      # 72 against 0
    "质点",      # 62 against 3 ("point particle")
    "电势",      # to the voltage definition; English links "voltage" only
    "过程",      # thermodynamic "transformation": 47 against 5
    "波长",      # 50 against 0
    "光子",      # 39 against 0
    "电动势",    # 36 against 0
    "望远镜", "棱镜", "偏向角",
    "能级", "谱线", "稳态", "势阱",
}
DROP = {
    # mirrors book3_en.py DROP: "central", "ideal", "linear" as bare adjectives
    "中心", "有心", "理想", "理想的", "线性", "线性的",
    # index-only keys (INDEX_CJK) that English never links, or links in another sense
    "功率",      # power, harvested onto the WORK definition: 74 links of the wrong word
    "重力",      # weight, onto the gravitational-field proposition: 85 against 3
    "张力", "弹簧",   # onto Hooke's law: 72 against 2
    "阻力",      # onto Stokes's law: 40 against 3
    "碰撞",      # collision, onto a centre-of-mass EXAMPLE: 26 against 0
    "共振", "带宽",   # onto the resonance theorem: 91 against 0
    "谐波", "二极管", "扬声器", "麦克风", "低通滤波器", "积分器", "浮力",
    # bare words English never links, even in the chapter that defines them (a STOP still links there)
    "电流", "电荷", "光线", "磁场", "折射率", "磁通量", "干涉", "地震仪", "隔振", "回旋加速器", "等势面",
}
INDEX_CJK = True    # index-only keys are terms too (harvest.py): theorem and proposition notions
EXTRA = {
    # result names, which NOT_A_TERM drops (定理, 定律) but English links: the French config restores the same two
    "高斯定理": "thm:b1:electrostatics-gauss:gauss",
    "安培环路定理": "thm:b1:magnetostatics:ampere",
    "斯涅耳定律": "thm:b1:rays-reflection-refraction:snell",
}          # manual {term: label}, added at the book's close (index-only keys have no space in Chinese)
NO_CAPITAL = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 20
EXTRA_PROTECT = []
