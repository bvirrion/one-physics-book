# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A series of five LaTeX physics books (Grades 1–9, Grades 10–12, University
Year 1, University Year 2, University Year 3) built from **one shared
`parts/` tree**, one entry file per book at the repo root, and a single
style file. The structure, theme and tooling mirror the sibling
`one-math-book` project exactly (same One Course brand, same environments,
same label conventions, same term-link tooling).

Contents follow the old French physics programs — collège and lycée « S »
for the school years, PCSI and PC* for university years 1–2, an L3 de
physique for year 3 — **pure physics, no chemistry**. Grades 1–6, where
the French primaire taught no physics, use age-adapted chapters.

**Current state: Book 2 written, the rest structure only.** Book 2
(High School, grades 10–12) is complete: 35 chapters of course text
(~349 pp), 137 TikZ/pgfplots/circuitikz figures, exactly 15 exercises
per chapter (star ramp 5×★ / 6×★★ / 4×★★★, in that order), one
~20-question "weekend problem" per chapter, a full solution for every
exercise and problem keyed by label, and ~4,500 generated `\omterm`
links (`tools/term_config/book2_en.py` is a curated config, no longer a
stub — regenerate links after editing Book 2 definitions or prose). The
invariant checks below are live for Book 2 and must stay green. Books 1
and 3–5 still have placeholder chapter bodies (a TODO comment and an
"unwritten" line) with header-only solutions files. English only;
`\ominput` already supports FR/NL trees later.

`CONTRIBUTING.md` holds the authoritative style/structure conventions;
`THEME.md` documents the One Course cover brand. Read both before writing
chapters.

## Git

**Never create git commits yourself.** Make the changes and leave the
working tree for the user to review and commit.

## Build

```sh
make                                     # latexmk builds all books into build/
latexmk one_physics_book_3_university_year_1.tex   # a single book
```

The build is pdflatex via `latexmkrc` (which also raises pdfTeX memory
limits — don't bypass it). PDFs land in
`build/one_physics_book_<N>_<slug>.pdf`. There are no tests; the quality
gate is the log:

```sh
L=build/one_physics_book_<N>_<slug>.log
grep -c '^!' $L                 # errors — must be 0
grep -ci 'undefined' $L         # undefined references — must be 0
grep -c 'Overfull' $L           # overfull boxes — keep at 0
```

CI builds only on tagged releases (`v*`):
`.github/workflows/release.yml` compiles all books, generates
`version.tex` (overriding `\bookversion`/`\bookdate` in the entry
files) and attaches versioned PDFs to the release. Pushes to `main`
are not built — the quality gate before pushing is the local log.

## Architecture

- `one_physics_book_<N>_<slug>.tex` — entry file per book (series number N):
  loads `styles/onephysics.sty`, calls `\ombrandheader` and
  `\omsolutionlinks`, defines `\bookline` ("Book N: ..." shown on the
  shared cover), inputs `parts/<year>/part.tex` for its years, then a
  Solutions appendix inputting `parts/<year>/solutions/solutions.tex`.
- `styles/onephysics.sty` — **the only place** packages are loaded and
  macros/environments defined. Chapter files never `\usepackage` or
  `\newcommand`. Language UI strings live in `styles/lang/<lang>.tex`.
- `parts/<year>/part.tex` — shared structure: `\part{\omstr{...}}` and
  `\ominput{<year>}{NN-slug}` lines; `solutions/solutions.tex` likewise
  with `\ominputsol`.
- Books → years: Book 1 → `grade-1`…`grade-9`; Book 2 → `grade-10`…
  `grade-12`; Books 3–5 → `bachelor-1`…`bachelor-3`.
- Year label prefixes: `g1`–`g12`, `b1`–`b3`. All labels are namespaced
  `<type>:<year>:<chapter-slug>:<name>`, e.g. `thm:b1:induction:faraday`,
  exercises `exo:g12:mechanical-waves:3`, weekend problems `pb:b2:...`.
  Reference with `\cref`, never bare `\ref`.
- **Cross-volume references are prose-only** ("the Year 2 volume") —
  `\cref` to another book's label will build locally by accident and
  break that book.

## Invariants (once content is written)

Every exercise (and every university-volume weekend `problem`, label
`pb:...`) has exactly one solution, keyed by label. Per chapter:

```sh
diff <(grep -o 'label{\(exo\|pb\):[^}]*}' parts/<year>/NN-slug.tex | sed 's/label{//;s/}//') \
     <(grep -o 'begin{solution}{[^}]*}' parts/<year>/solutions/NN-slug.tex | sed 's/begin{solution}{//;s/}//')
grep -rho 'label{[^}]*}' parts/<year>/ | sort | uniq -d   # duplicate labels
```

Defined-term links (`\omterm`) are generated, not hand-written — the
engine lives in `tools/termlink/` (shared rules) and
`tools/term_config/book<N>_en.py` (per-book vocabulary, currently empty
stubs). After chapters and definitions land:

```sh
python3 tools/link_defined_terms.py --book N          # dry run
python3 tools/link_defined_terms.py --book N --apply
```

Content rules (from CONTRIBUTING.md): 8–12 exercises per chapter, graded
`[$\star$]` to `[$\star\star\star$]`, each with a full solution;
derivations essentially complete at the level of the year (`\admitted`
otherwise, with a remark saying where the result is honestly derived);
new terms introduced as `\emph{...}\index{...}` in a `definition`;
SI units throughout.

For style-file specifics (macros, semantic colors, theorem environments)
and LaTeX gotchas (TikZ/pgfplots pitfalls, overfull-box hunting), the
notes in `one-math-book/CLAUDE.md` apply verbatim — `onephysics.sty` is a
renamed copy of `onemath.sty` and will evolve physics-specific macros as
content lands.
