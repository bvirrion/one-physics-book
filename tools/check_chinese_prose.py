#!/usr/bin/env python3
"""Simplified Chinese hygiene gate for a translated tree (gate 9 of check_translation.sh).

Like Hindi and Arabic, Chinese is written in a script that is not Latin, so
residual English is visibly foreign and a gate can flag any Latin word in the
visible text. The LaTeX reduction is imported from check_hindi_prose.py, not
copied (translation_instruction.md: "import it, do not copy it").

Classes:

  english       a Latin word in visible text: prose, \\text{...} in math, TikZ
                node text, axis labels, environment optional titles. People's
                names are written in Chinese in this edition (欧拉, 柯西), so a
                Latin name is flagged too. Acronyms of up to four capitals and
                unit symbols are allowed, as in the Hindi gate.
  legend        a Latin word in \\legend{...} or \\addlegendentry{...}, which the
                imported reduction does not read (the macro form of a legend:
                see "\\legend{...} is the other blind spot" in
                translation_instruction.md).
  ascii-punct   an ASCII , . ; : ? ! after a Chinese character, or an ASCII
                parenthesis opening or closing on Chinese text: Chinese prose
                takes the full-width forms ，。；：？！（）.

Usage:
    python3 tools/check_chinese_prose.py parts/grade-3/zh parts/grade-3/solutions/zh

Exit status is 1 if anything was flagged.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from check_hindi_prose import (  # noqa: E402
    ALLOWED_UNITS, ALLOWED_WORDS, DOTTED_ABBREV, LATIN_WORD, SHORT_ENGLISH,
    _locate, strip_comments, visible_text)

HAN = r"\u3400-\u4dbf\u4e00-\u9fff"
ASCII_PUNCT = re.compile(rf"[{HAN}][ \t]*[,;:?!]|[{HAN}]\.(?=\s|$|[{HAN}])|\((?=[{HAN}])|(?<=[{HAN}])\)")
LEGEND = re.compile(r"\\(?:legend|addlegendentry)\s*(\{(?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*\})")
MATHLESS = re.compile(r"\$[^$]*\$|\\[A-Za-z]+")

# Latin that may stay in a Chinese line: the series and product names.
ALLOWED_HERE = {"physics", "book", "one", "course", "git", "contributing", "md", "url",
                # unit and function symbols kept in Latin in Chinese texts (physics zh Book 4): 转速 in rpm, ppm, sinc, erfc
                "rpm", "ppm", "sinc", "erfc",
                # kept in Latin in Chinese texts (physics zh Book 5): lattice and quark-content symbols, the spectral
                # sequence, units, proper names of machines, experiments and seismic phases
                "fcc", "bcc", "hcp", "uud", "udd", "uuu", "ddd", "uds", "obafgkm", "mpc", "kpc", "gpc", "gyr", "myr", "ppb",
                "kamland", "bevatron", "pkjkp", "p--n", "n--p",
                # function names a display line can leave outside the blanked math (\cos\theta = \frac{\text{邻边}}{…})
                "sin", "cos", "tan", "cot", "log", "exp", "lim", "max", "min", "sup", "inf", "det", "gcd", "lcm",
                "arg", "ker", "dim", "deg", "diag", "sinh", "cosh", "tanh", "arcsin", "arccos", "arctan",
                # math names the blanking leaks from a formula split over lines (Book 5); not theta/zeta, which
                # Haiku also writes in prose ("theta 函数", "zeta 值")
                "delta", "limsup", "liminf",
                # roman numerals of item labels
                "ii", "iii", "iv", "vi", "vii", "viii", "ix", "xi", "xii",
                # physics: unit symbols the Hindi list lacks, integral names a split display leaks, and the Latin
                # subscripts physics writes in \text{} (I_enc, E_int, F_ext, P_eff, E_tot)
                "ev", "kev", "mev", "gev", "tev", "int", "iint", "iiint", "oint", "oiint",
                "enc", "ext", "eff", "tot", "rms", "th", "max", "min",
                # Latin kept on purpose in the Chinese text of this series: added per book at its close,
                # each after a grep of the whole file (the gate's line numbers can be wrong)
                "rho", "omega",  # 希腊字母 rho, omega: the letter names beside $\rho$, $\Omega$ (grades 7, 8)
                "ambulance",    # the mirror-written word on an ambulance, discussed as a word (grade 5)
                "camera", "obscura", "nist", "punctum", "proximum", "remotum",  # the device's Latin name, glossed 暗室 (grade 6)
                "math",          # the sister series One Math Book (grade 10)
                "homo", "sapiens", "coli", "helios",  # binomials and an etymology, kept in Latin (grade 10)
                "wi-fi", "wi", "fi", "ping",           # technical names used as such in Chinese (grade 10)
}


# A word made only of element symbols and counts is a formula the English writes as plain text (HCl 1.09, HBr 0.83):
# it stays as written (chemistry zh trial, 2026-11-18).
ELEMENTS = set("""H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y
Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg
Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm""".split())
FORMULA_PART = re.compile(r"[A-Z][a-z]?\d*")


def _is_formula(word):
    parts = FORMULA_PART.findall(word)
    return "".join(parts) == word and all(re.sub(r"\d", "", q) in ELEMENTS for q in parts) and len(parts) >= 2


def _flag_latin(text, body, rel, cls, findings, occ):
    for m in LATIN_WORD.finditer(text):
        word = m.group(0)
        low = word.lower().rstrip("-")   # `NIST-4`: the instrument name runs on into its number
        if (_is_formula(word) or word.rstrip("-") in ELEMENTS   # HCl; Am-241, an isotope
                or all(w in ELEMENTS for w in word.split("--"))   # He--Ne, a laser
                or re.fullmatch(r"[a-z]--[a-z]", word)):   # a sub-question range, (b--c) (physics zh Book 5)
            continue
        if low in ALLOWED_WORDS or low in ALLOWED_UNITS or low in ALLOWED_HERE:
            continue
        if word.islower() and low in SHORT_ENGLISH:
            findings.append((rel, _locate(body, word, occ), cls, f"English in visible text: {word!r}"))
            continue
        if word.isupper() and len(word) <= 4:
            continue
        if len(word) < 3:
            continue
        findings.append((rel, _locate(body, word, occ), cls, f"English in visible text: {word!r}"))


def check_file(path: pathlib.Path, findings: list) -> None:
    raw = path.read_text(encoding="utf-8")
    rel = str(path)
    body = strip_comments(raw)
    # an \includegraphics path on the line after its options is a file name, not prose (physics, 2026-11-18)
    body = re.sub(r"(\\includegraphics(?:\[[^\]]*\])?\s*)\{[^{}]*\}", r"\1{}", body)
    # a photographer's name in a caption credit stays in Latin script, as the licence attributes it: blank the
    # Latin inside \emph{照片：…} (the frame words 照片 and 裁剪 are Chinese; zh_sweeps fixes Photo:/cropped)
    body = re.sub(r"(\\emph\{照片：)((?:[^{}]|\{[^{}]*\})*)\}",
                  lambda m: m.group(1) + re.sub(r"[^\n]", " ", m.group(2)) + "}", body)
    # the same credit written plainly at a caption's end, `照片：Olga Khomitsevich，CC~BY~2.0。}` (physics Book 3)
    body = re.sub(r"(照片：)([^{}\n\\]*)", lambda m: m.group(1) + re.sub(r"[^\n]", " ", m.group(2)), body)
    seen = visible_text(body, findings, rel)
    occ: dict = {}

    _flag_latin(seen, body, rel, "english", findings, occ)
    for m in DOTTED_ABBREV.finditer(seen):
        findings.append((rel, _locate(body, m.group(0), occ), "english",
                         f"English abbreviation in visible text: {m.group(0)!r}"))

    for m in LEGEND.finditer(body):
        _flag_latin(MATHLESS.sub(" ", m.group(1)), body, rel, "legend", findings, occ)

    for k, line in enumerate(body.split("\n"), 1):
        line = re.sub(r"\$[^$]*\$", "\x00", line)
        # pgfplots lists are code: the comma separates keys (xticklabels={1月,2月}, symbolic x coords={…})
        line = re.sub(r"(?:[xyz]ticklabels|symbolic [xyz] coords)\s*=\s*\{[^{}]*\}", "\x00", line)
        # \foreach lists are code too: `{0/视觉, 2.4/听觉,` (physics zh, 2026-11-18)
        line = re.sub(r"(?:[\d.]+/)+(?:[^,{}]|\{[^{}]*\})*,", "\x00", line)
        line = re.sub(r"\\legend\{(?:[^{}]|\{[^{}]*\})*\}?", "\x00", line)   # one brace level: \legend{\qty{100}{mL} 纯水, …}
        line = re.sub(r"\bl[_^]?=[^,\]]*,", "\x00", line)   # circuitikz `to[generic, l=偶极子, v=…]`: the comma is code   # \legend{无摩擦, 有摩擦}: the comma separates entries
        # an index key never prints its `!` (sub-entry); `\text{ (或 } \C)` in display math pairs with a math `)`
        line = re.sub(r"\\index\{[^{}]*(?:\}|$)|\\text\{ \(", "\x00", line)  # a key may run on to the next line
        for m in ASCII_PUNCT.finditer(line):
            findings.append((rel, k, "ascii-punct",
                             f"ASCII punctuation in Chinese text: {line[max(0, m.start() - 6):m.end() + 4]!r}"))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("dirs", nargs="+", help="directories (or single .tex files)")
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--max-detail", type=int, default=8)
    args = ap.parse_args()

    findings: list = []
    files = []
    for d in args.dirs:
        p = pathlib.Path(d)
        files += sorted(p.glob("*.tex")) if p.is_dir() else ([p] if p.suffix == ".tex" and p.exists() else [])
    if not files:
        print("  chinese prose gate: no .tex file found in the arguments")
        return 1
    for f in files:
        check_file(f, findings)

    if not findings:
        print(f"  chinese prose gate: OK ({len(files)} files)")
        return 0
    by_class: dict = {}
    for rel, line, cls, msg in findings:
        by_class.setdefault(cls, []).append((rel, line, msg))
    print(f"  chinese prose gate: {len(findings)} issue(s) in {len(files)} files")
    for cls in sorted(by_class):
        hits = by_class[cls]
        print(f"    {cls:<14} {len(hits):>5} hit(s) in {len({h[0] for h in hits})} file(s)")
        if not args.quiet:
            for rel, line, msg in hits[:args.max_detail]:
                print(f"        {rel}:{line}: {msg}")
            if len(hits) > args.max_detail:
                print(f"        ... {len(hits) - args.max_detail} more")
    return 1


if __name__ == "__main__":
    sys.exit(main())
