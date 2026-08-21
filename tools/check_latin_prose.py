#!/usr/bin/env python3
"""Gate 9 -- the twin-comparison prose gate, for editions written in the Latin
alphabet (fr, nl, es, pt, id).

WHY THIS EXISTS. Gates 5 and 6 are Latin-oriented but score nothing about
whether a fragment was translated; gate 7 (Devanagari, Arabic) works because
residual English is *visibly foreign* in a non-Latin script; gate 8
(Indonesian) works because a curated list of English words that are not
Indonesian words can be built. Neither trick is available for French, Dutch,
Spanish or Portuguese: an English word is spelled with the same letters as a
French one, and no word list can separate them cheaply.

So this gate does not ask "is this English?". It asks a question that needs no
per-language knowledge at all:

    IS THIS FRAGMENT BYTE-IDENTICAL TO ITS ENGLISH TWIN, AND DOES IT CONTAIN
    A LOWERCASE WORD?

A translated fragment that still equals the English one either was never
touched or is a proper noun. Proper nouns (Gauss, Thevenin, Bolzano--
Weierstrass, RLC) carry no lowercase word once math and macros are stripped,
so requiring one removes nearly every false positive without knowing a word of
the target language. The comparison is positional: the Nth fragment of the
translated file against the Nth fragment of its English twin, and it is
skipped entirely when the counts differ, because then check_translation.sh
owns the divergence.

WHAT IT COVERS -- exactly the classes that shipped green in real editions:

  title     environment optional titles (\\begin{definition}[Physical quantity])
            and \\chapter/\\section headings
  text      \\text{...} inside math, including the subscripts that no reader of
            the source ever looks at (S_{\\text{created}})
  node      TikZ/pgfplots node text, node[...] {...}, and axis labels
  dup       a line repeated verbatim from the English twin sitting immediately
            above or below its own translation (an applier misuse: the
            English line was kept AND translated)

Each class was a real defect in a shipped or nearly-shipped edition. The
Portuguese Book 3 edition carried three untranslated environment titles, one
duplicated English line, fourteen English \\text{} subscripts and one English
TikZ node -- all of them through a green check_translation.sh and a clean PDF.

DELIBERATE BLIND SPOTS. \\mathrm{} is mathematics and stays English across
every edition by series convention (S_{\\mathrm{created}}), so it is never
compared. Unit arguments (\\qty, \\unit, \\num) are mathematics too. A fragment
whose lowercase words are all in ALLOWED_IDENTICAL is skipped: those are
strings a Latin-script edition legitimately leaves alone.

Usage:
    python3 tools/check_latin_prose.py parts/bachelor-1/fr parts/bachelor-1/solutions/fr
    python3 tools/check_latin_prose.py --quiet <dirs...>

The English twin is found by dropping the /<lang>/ path component, the same way
check_indonesian_prose.py does it.
"""
import argparse
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from check_hindi_prose import strip_comments          # noqa: E402

# --------------------------------------------------------------------------
# Fragment extractors. Each returns a LIST in document order, so the Nth
# fragment of a translation can be compared with the Nth of its twin.
# --------------------------------------------------------------------------
TITLE_ENVS = ("definition", "theorem", "proposition", "lemma", "corollary",
              "example", "remark", "method", "notation", "exercise",
              "problem", "proof", "omfigure", "figure", "table")
TITLE_RE = re.compile(
    r"\\begin\{(?:" + "|".join(TITLE_ENVS) + r")\}"
    r"\[((?:[^\[\]]|\[[^\]]*\])*)\]"
    r"|\\(?:chapter|section|subsection)\*?\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}")

# \text{...} but NOT \mathrm{...}: the first is prose, the second mathematics.
TEXT_RE = re.compile(r"\\text\{([^{}]*)\}")

# TikZ node text: "node {...}", "node[opt] {...}", "node[opt] (name) {...}",
# plus pgfplots xlabel=/ylabel=/title= values in braces.
#
# The option bracket must be consumed as a UNIT, not with a lazy [^{;]*?: a
# lazy run stops at the first "{" it can, which inside "node[lab/.style={font=
# \small}]" is the *style* group, so the gate reported "font=\small" as node
# text. Match an optional [...] (allowing one nested brace group inside it),
# then an optional (name), then the real body.
NODE_RE = re.compile(
    r"\\?node\b\s*"
    r"(?:\[(?:[^\[\]{}]|\{[^{}]*\})*\]\s*)?"
    r"(?:\([^()]*\)\s*)?"
    r"(?:at\s*\([^()]*\)\s*)?"
    r"\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}"
    r"|(?:xlabel|ylabel|zlabel|title)\s*=\s*\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}")

# Environments whose bodies are drawing code, copied byte-identically by
# design. A "duplicated English line" inside one of these is not a defect --
# it is the applier doing exactly what it promises.
DRAW_ENV_OPEN = re.compile(
    r"\\begin\{(?:tikzpicture|axis|semilogxaxis|semilogyaxis|loglogaxis|"
    r"scope|circuitikz|groupplot|pgfonlayer)\}")
DRAW_ENV_CLOSE = re.compile(
    r"\\end\{(?:tikzpicture|axis|semilogxaxis|semilogyaxis|loglogaxis|"
    r"scope|circuitikz|groupplot|pgfonlayer)\}")
# A continuation line of drawing code carries no leading macro to key on:
# "xmin=0, xmax=4.3, ymin=0, ymax=21, xtick={0,1,2,3,4},". Key on the shape.
DRAW_OPTION_LINE = re.compile(
    r"^[^a-zA-Z]*(?:[a-z][a-z ]*\s*=\s*[^=]*,?\s*)+$|^[-\d.,()\s{}\[\]+*/]+;?$")

LOWER_WORD = re.compile(r"(?<![A-Za-z])[a-z]{3,}(?![A-Za-z])")

# Strings a Latin-script edition legitimately leaves byte-identical.
ALLOWED_IDENTICAL = {
    # brand, markup and file names
    "one", "course", "com", "www", "http", "https", "tex", "latex", "pdf",
    "github", "book", "md",
    # internationalisms and symbols that are the same word in the targets
    "min", "max", "log", "exp", "sin", "cos", "tan", "arg", "det", "lim",
    "sup", "inf", "abs", "mod", "rad", "deg", "cte", "const",
    "in", "out", "on", "off", "up", "down",          # circuit port labels
    "gaz", "gas", "air", "ion", "bar", "net", "cm", "mm", "km", "kg",
    "obscura", "camera",                              # camera obscura
    "et", "al",                                       # et al.
    # Spectroscopy series labels. "Lyman (ultraviolet)" and "Balmer
    # (visible)" are byte-identical in French, Spanish, Portuguese and Dutch
    # because BOTH words are the same in all of them -- the parenthesis is
    # not untranslated English. Verified in the fr and es Book 3 editions.
    "ultraviolet", "visible", "infrarood", "infrarouge",
    # Same word in Dutch as in English, verified in the nl Book 3 edition:
    # a guitar "fret" and a "pseudo-integrator" op-amp stage.
    "fret", "pseudo", "integrator",
    # Conventional subscript abbreviations. These are the SAME abbreviation in
    # French, Spanish, Portuguese, Dutch and Indonesian (ext = extérieur /
    # exterior / externo / extern; tot = total; cons = conservatives /
    # conservativas), so an identical \text{ext} is correct, not untranslated.
    # Verified against the shipped Book 2 editions before being listed.
    "ext", "int", "tot", "cons", "max", "min", "eff", "abs", "rel", "gen",
    "th", "eq", "crit", "ref", "res", "init", "fin", "moy", "med", "num",
    "den", "obs", "src", "det", "acc", "rms", "emf", "dc", "ac", "pp",
}

# A fragment of a single word is reported in a SEPARATE, lower-confidence
# class. In the Latin-script targets a one-word fragment is very often a true
# cognate -- French "distance", "signal", "amplitude", "absorption", "visible"
# and Spanish "amplitud"-class words are correct prose, and firing on them
# would make the gate useless. A multi-word fragment left byte-identical is
# the high-confidence defect: no two languages agree on a whole phrase by
# accident. Both tiers are reported; only the multi-word tier is worth
# blocking on.
def _word_count(s):
    s = re.sub(r"\$[^$]*\$", " ", s)
    s = re.sub(r"\\(?:qty|unit|num|SI|si)\s*(?:\{[^{}]*\})?\{[^{}]*\}", " ", s)
    # A label argument is not prose: "def:b1:kinetic-theory:temperature" would
    # otherwise count as four words and make a bare \omterm line look like a
    # duplicated English sentence. It fired on three shipped editions at once.
    s = re.sub(r"\{[^{}]*:[^{}]*\}", " ", s)
    s = re.sub(r"\\[A-Za-z@]+", " ", s)
    return len(re.findall(r"[A-Za-z]{2,}", s))


def _fragments(text):
    """[(class, string, char-offset)] for every comparable fragment."""
    out = []
    for m in TITLE_RE.finditer(text):
        out.append(("title",
                    m.group(1) if m.group(1) is not None else m.group(2),
                    m.start()))
    for m in TEXT_RE.finditer(text):
        out.append(("text", m.group(1), m.start()))
    for m in NODE_RE.finditer(text):
        out.append(("node",
                    m.group(1) if m.group(1) is not None else m.group(2),
                    m.start()))
    return out


def _has_lowercase_word(s):
    """A lowercase word that is not an allowed internationalism."""
    # Strip math and macros first: [$\arcsin$] and [Gram--Schmidt] must not fire.
    s = re.sub(r"\$[^$]*\$", " ", s)
    s = re.sub(r"\\[A-Za-z@]+", " ", s)
    return any(w not in ALLOWED_IDENTICAL for w in LOWER_WORD.findall(s))


def _line_of(text, offset):
    return text.count("\n", 0, offset) + 1


def check_duplicated_lines(path, body, en_body, findings):
    """An English line kept AND translated: the twin's line sits verbatim in
    the translation, adjacent to a line that is not in the twin at all."""
    en_lines = {ln.strip() for ln in en_body.split("\n") if len(ln.strip()) > 40}
    lines = body.split("\n")
    depth = 0
    for i, ln in enumerate(lines):
        s = ln.strip()
        # Track drawing environments: everything inside one is copied
        # byte-identically on purpose, so a "duplicate" there means nothing.
        opens, closes = len(DRAW_ENV_OPEN.findall(ln)), len(DRAW_ENV_CLOSE.findall(ln))
        was_inside = depth > 0
        depth = max(0, depth + opens - closes)
        if was_inside or opens:
            continue
        if len(s) <= 40 or s not in en_lines:
            continue
        if not _has_lowercase_word(s) or _word_count(s) < 4:
            continue
        # Prose only: drawing code and math are copied verbatim by design.
        if re.search(r"\\(?:draw|fill|path|node|addplot|foreach|coordinate|"
                     r"begin|end|label|cref|ref|index|input|item|omterm)\b", s) or "$" in s:
            continue
        if DRAW_OPTION_LINE.match(s):
            continue
        neighbours = [lines[j].strip() for j in (i - 1, i + 1)
                      if 0 <= j < len(lines)]
        if any(n and len(n) > 40 and n not in en_lines for n in neighbours):
            findings.append((str(path), i + 1, "dup",
                             "English line kept beside its translation: "
                             f"{s[:70]!r}"))


def check_file(path, findings):
    twin = pathlib.Path(re.sub(r"/[a-z]{2}/(?=[^/]*$)", "/", str(path)))
    if not twin.is_file() or twin == path:
        return
    body = strip_comments(path.read_text(encoding="utf-8"))
    en_body = strip_comments(twin.read_text(encoding="utf-8"))

    mine, theirs = _fragments(body), _fragments(en_body)
    by_class = {}
    for cls, s, off in mine:
        by_class.setdefault(cls, []).append((s, off))
    en_by_class = {}
    for cls, s, off in theirs:
        en_by_class.setdefault(cls, []).append((s, off))

    for cls, items in by_class.items():
        en_items = en_by_class.get(cls, [])
        if len(items) != len(en_items):
            # A structural divergence; check_translation.sh owns it.
            continue
        for (s, off), (e, _) in zip(items, en_items):
            if s.strip() == e.strip() and _has_lowercase_word(s):
                tier = cls if _word_count(s) >= 2 else cls + "-1word"
                findings.append((str(path), _line_of(body, off), tier,
                                 f"identical to English ({cls}): {s.strip()[:70]!r}"))

    check_duplicated_lines(path, body, en_body, findings)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("dirs", nargs="+")
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--max-detail", type=int, default=8)
    args = ap.parse_args()

    findings, files = [], 0
    for d in args.dirs:
        p = pathlib.Path(d)
        if not p.is_dir():
            continue
        for f in sorted(p.glob("*.tex")):
            files += 1
            check_file(f, findings)

    if not findings:
        print(f"  latin prose gate: OK ({files} files)")
        return 0

    by_class = {}
    for rel, line, cls, msg in findings:
        by_class.setdefault(cls, []).append((rel, line, msg))
    print(f"  latin prose gate: {len(findings)} issue(s) in {files} files")
    for cls in sorted(by_class):
        hits = by_class[cls]
        print(f"    {cls:<8} {len(hits):>5} hit(s) in "
              f"{len({h[0] for h in hits})} file(s)")
        if not args.quiet:
            for rel, line, msg in hits[:args.max_detail]:
                print(f"        {rel}:{line}: {msg}")
            if len(hits) > args.max_detail:
                print(f"        ... {len(hits) - args.max_detail} more")
    return 1


if __name__ == "__main__":
    sys.exit(main())
