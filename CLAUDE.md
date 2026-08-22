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

**Current state: Books 1, 2 and 3 written, each in eight languages;
Book 4 written in English (2026-08-22); Book 5 structure only.**

- **Book 1** (Primary & Middle School, grades 1–9): 71 chapters + 71
  solutions files (~435 pp), 142 figures, photographs and AI-generated
  illustrations credited in `frontmatter/image-credits*.tex`, ~6,480
  generated `\omterm` links. Grades 1–5 carry 9–11 exercises and no
  weekend problem; grades 6–9 carry 12 exercises plus one ~13–15-question
  problem.
- **Book 2** (High School, grades 10–12): 35 chapters of course text
  (~349 pp), 137 TikZ/pgfplots/circuitikz figures, exactly 15 exercises
  per chapter (star ramp 5×★ / 6×★★ / 4×★★★, in that order), one
  ~20-question "weekend problem" per chapter, a full solution for every
  exercise and problem keyed by label, ~4,500 generated `\omterm` links.
- **Book 3** (University Year 1): 30 chapters in `parts/bachelor-1/`
  (the 28 original PCSI-derived headlines plus *Signal Propagation* as
  ch.~05 and *Introduction to Quantum Physics* as ch.~30), ~320 pp,
  ~150 TikZ/pgfplots/circuitikz figures plus photographs
  (`images/book3/`, credited in `frontmatter/image-credits-book3.tex`)
  and AI illustrations (`images/book3/ai/`, prompts in `PROMPTS.md`),
  exactly 12 exercises per chapter (4×★ / 5×★★ / 3×★★★), one
  25-question weekend problem per chapter, a full solution for every
  exercise and problem, ~2,340 generated `\omterm` links
  (`tools/term_config/book3_en.py` is curated). Ships in all eight
  languages (2026-08-21), each self-scored 96/100; link density runs
  `ar` 1,983 < `nl` 2,173 < `hi` 2,244 < EN 2,342 < `es` 2,400 <
  `fr` 2,430 < `pt` 2,509 < `id` 2,515, and 319–352 pp against
  English's 332.
  The level guard is math Book 3 (Year 1): no surface integrals, div or
  curl — Gauss's and Ampère's laws are stated in integral form and used
  through symmetry; no wave equation in ch.~05.
- **Language editions**: all three written books ship in `fr`, `nl`, `es`,
  `pt`, `hi`, `ar` and `id` alongside English — bodies under `parts/<year>/<lang>/` and
  `parts/<year>/solutions/<lang>/`, one entry file each, all registered
  in `latexmkrc` and `.github/workflows/release.yml`. Every edition is
  gated by `tools/check_translation.sh` and self-scored under
  `translation_scores/book_<N>/<lang>/`. See the workspace-root
  `translation_instruction.md` before touching any of them.
- **`tools/id_apply.py` is how a translated body should be written.** A
  translated chapter is a set of line-range replacements on the English
  canon; every line not named is copied byte-identically, so labels,
  `\cref` targets, solution keys, `\foreach` lists, `xtick=`, `\qty{}{}`
  and every math display cannot drift. The tool refuses to write a file
  unless eleven ordered censuses survive against its English twin —
  including the math-span sequence (Indonesian absorbs numerals into
  words) and a **per-range `\[ \]` count** (a range covering `\[` but
  stopping before `\]` duplicates the delimiter, passes every whole-file
  census, and kills the build). Run `python3 tools/id_apply.py --help`.
- **Indonesian (`id`) needs a prose gate, and it is not optional.** Gates
  5–7 assume the target script differs from English, so residual English
  is visibly foreign. Indonesian is written in the *same alphabet* as the
  source, so a forgotten sentence, a forgotten TikZ node, a forgotten
  `\text{…}` or an untranslated environment **optional title** is
  indistinguishable from correct output: a tree can pass every structural
  gate, build with zero errors, and still be part English.
  `tools/check_indonesian_prose.py` (gate 8) keys on a curated list of
  English words that are *not* Indonesian, plus suffix rules, a
  sentence-density rule and a comparison of every title against its
  English twin. Its word lists carry a physics block — `air` is
  Indonesian for *water* and is deliberately ungated, while the English
  plurals `magnets`, `gases`, `atoms`, … are gated because Indonesian
  pluralises by reduplication. The edition identity, glossary and traps
  live in `../indonesian_style_card.md`.
- **A Latin-script edition needs a TWIN-COMPARISON gate too, and gate 8 is
  not it.** Gate 8 asks "is this word English?", which needs a curated word
  list and therefore exists only for Indonesian. `tools/check_latin_prose.py`
  (gate 9) asks the question that needs no per-language knowledge at all:
  *is this fragment byte-identical to its English twin, and does it contain a
  lowercase word?* It compares environment optional titles, `\text{…}`, TikZ
  node text and whole duplicated lines, positionally, against the English
  twin, and reports in two tiers — a multi-word match is a defect, a one-word
  match is usually a true cognate (*visible*, *signal*, *amplitude* are French
  words too). It found real defects in three editions that a green
  `check_translation.sh` and a clean PDF had passed: an untranslated
  `\begin{proof}[Partial proof]` in `es`, `\text{energy stored}` inside a
  displayed formula in `fr`, eight English op-amp figure nodes in `nl`, and in
  `pt` three untranslated titles plus fourteen English `\text{}` subscripts.
  It is deliberately NOT wired into `check_translation.sh`: the shipped Book 2
  editions still carry hits (French `\text{body/ground}`, node
  `amplitude (arb.)`), so wiring it in would turn the repo-wide gate red
  before those are fixed.
- **All four gates learned `\legend{...}` on 2026-08-22.** Every prose gate keyed
  figure text on the pgfplots KEY form (`legend entries={…}`); the MACRO form
  has no `=` and was invisible in every script, while `id_apply`'s `draw`
  census compared it byte-for-byte and so refused any translation of it
  without `!draw`. Fixed in `check_hindi_prose.py` (inherited by
  `check_indonesian_prose.py`), `check_arabic_prose.py`, `check_latin_prose.py`
  and `id_apply.py`. It had already shipped: Hindi and Arabic Book 2 each carry
  six untranslated English legends. The generic lesson is in
  `../translation_instruction.md` — when a gate keys on a KEY=VALUE shape, ask
  what the MACRO form of the same thing looks like.
- `tools/term_config/book{1,2}_*.py` are curated configs, not stubs —
  regenerate links after editing those books' definitions or prose.

- **Book 4** (University Year 2): 31 chapters in `parts/bachelor-2/`,
  written in English 2026-08-22 on the Book 3 recipe — the chapter list
  is the **union of the old (2004) and current (2021) PC* programmes**
  with the 2013 one folded in (checked against the official annexes,
  2026-08-21; provenance comments in `parts/bachelor-2/part.tex`): ~345 pp,
  121 TikZ/pgfplots/circuitikz figures plus 13 photographs
  (`images/book4/`, credited in `frontmatter/image-credits-book4.tex`)
  and 30 AI illustrations (`images/book4/ai/`, prompts in `PROMPTS.md`),
  exactly 12 exercises per chapter (4×★ / 5×★★ / 3×★★★), one
  25-question weekend problem per chapter, a full solution for every
  exercise and problem, ~1,230 generated `\omterm` links
  (`tools/term_config/book4_en.py` is curated). Level guard = math Book 4
  (Year 2): div/curl introduced operationally in ch.~11 with Ostrogradski
  and Stokes `\admitted` (proved in the Year 3 mathematics volume),
  Fourier integrals used as a stated tool with a Year-3 remark, Fourier
  series allowed. **Ships in all eight languages (2026-08-22)** — one agent
  per edition, every one self-scored 96/100 except `fr` at 97, all at
  0 errors / 0 undefined / 0 overfull with the `.fls` honesty check at
  62/62. Pages against English's 345: `ar` 326, `hi` 332, `pt` 357,
  `es`/`fr`/`nl` 359, `id` 366. Link density against English's 1 231:
  `nl` 1 166 < `ar` 1 183 < `hi` 1 211 < `pt` 1 335 < `es` 1 361 <
  `fr` 1 365 < `id` 1 419.

The invariant checks below are live for Books 1–4 and must stay
green. Book 5 still has placeholder chapter bodies (a TODO comment
and an "unwritten" line) with header-only solutions files, English only.

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
