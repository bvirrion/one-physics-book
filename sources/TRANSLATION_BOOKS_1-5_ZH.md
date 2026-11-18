# Run file — One Physics Book 1–5 in Simplified Chinese (`zh`), pilot method

Scope: Books 1–5 (15 years: grade-1 … grade-12, bachelor-1 … bachelor-3) into Simplified Chinese (mainland), by the pilot method (`../pilot_translation_instruction.md`).
Started 2026-11-18, one run with physics Books 1–5 and chemistry Books 1–4 (run 1 of 2 (physics first, then chemistry)).

| **Model** | `claude-haiku-5-5` (Haiku 5.5, effort medium), pilot method: one headless call per section; glossary and coordinator `claude-opus-5-5` (Opus 5.5) |
|---|---|

Shape (user, 2026-11-18): one coordinator (the main session), no subagents, one session for both series; at most three
years (`run.py` jobs) at once and at most 9 Haiku calls in flight (`--workers 3` each; spare workers go to the last
jobs). **Pause rule for this run: pause and report at +25 points of the weekly plan** from the run's start (9 %, so at
34 %; points before and after a weekly reset are added). Order: physics Books 1–5, then chemistry Books 1–4.

## Usage readings (`claude -p /usage`, all models, current week)

| When | Week used |
|---|---:|
| Run start, 2026-11-18 00:25 | 9 % |
| Physics Book 1 closed, 2026-11-18 02:35 | 10 % |
| Physics Book 2 closed, 2026-11-18 03:35 | 11 % |
| Physics Book 3 closed, 2026-11-18 05:55 | 13 % |
| Physics Book 4 closed, 2026-11-18 06:55 | 13 % |
| Physics Book 5 closed, 2026-11-18 07:40 | 14 % (chemistry Book 1 closed the same hour; chemistry bachelor-1/2/3 translating) |
| Chemistry Book 2 closed, 2026-11-18 10:15 | 16 % |
| Chemistry Books 3–4 closed, run closed, 2026-11-18 10:40 | 16 % (+7 points for nine books and two ports; pause rule +25) |

## Infrastructure (step 0)

Ported from `one-math-book` on 2026-11-18 (the 7 items of "Porting zh to another series"):
- `latexmkrc`: `_zh` to XeLaTeX, index through `upmendex -s styles/zh-pinyin.ist`, empty-`.idx` guard; five `_zh` entries.
- `styles/onephysics.sty`: the math `zh` blocks (xeCJK + Fandol, Kai italic, 第 N 章 / 第一部分, solution header and
  pointer, `\cref` names in `\text{}`, conjunctions, statement heads without full stop, `\om@chapmarkprefix`);
  `styles/lang/zh.tex` (+ siunitx range/list words 至/和/、, which math has no need of).
- Entry files `one_physics_book_{1..5}_*_zh.tex`; `frontmatter/preface.zh.tex` (coordinator) and the four
  `image-credits*.zh.tex` (one Haiku call each, then corrected: Book 1's ten photo titles came back in English).
  `release.yml` is updated at the close, so that no tag ships a half edition.
- Term linker: CJK mode (`termlink/morphology.py`, `harvest.py` copied from math, identical otherwise), `zh` in
  `books.py`/`link_defined_terms.py`, `term_config/lang_zh.py`, `book{1..5}_zh.py` stubs. English and French
  `--check` unchanged.
- Gates: `tools/check_chinese_prose.py` as gate 9 (fires on English: 12,657 hits on grade-7, exit 1 on an empty
  directory, silent on the Chinese preface); `id_apply.py` with the `zh` dispatch; physics units and `\text{}`
  subscripts allowed (MeV, enc, ext, eff, tot…).
- Pack: shared `langs/zh.{md,py}`; series card `pilot_translation/langs/series/one-physics-book.zh.md`.
- `pilot_translation/glossary.py terms` now also lists the `\emph` terms of `definition` boxes whose `\index` keys come
  first: University Years define nearly every term that way, and bachelor-1 listed 3 terms instead of 265.
- Glossaries `sources/GLOSSARY_BOOK_{1..5}_ZH.md` (225/316/204/165/152 lines, new lines only, a later line overriding);
  `draft/zh/merge_glossary.py N` merges Books 1..N before `glossary.py split`.
- Book 3 zh entry with English fallbacks: 332 pp, 0/0/0, missing characters 0.

Trial (2026-11-18), effort medium:
- grade-8 ch. 07 (lenses, figures): 7 calls, $0.04; one section rejected three times (the reply stopped at line 93, before
  the burning-glass safety remark, each time), accepted on a plain re-run. Probe 7 pp, 0/0/0, missing characters 0.
- bachelor-2 ch. 11 (Maxwell, formula-dense): 8 sections in 14 calls (1.75 a section), none rejected three times, $0.16.
  Probe 11 pp, 0/0/0. Prose gate: 5 hits, all allowed tokens (MeV, `\text{enc}`, a leaked `\iint`). NUMDIFF: "Year 1"
  → 本科一年级 ×8, plus line 596 to check at the close (question 3).
- Figures read on contact sheets: translated; one collision ((垂直纸面向里) on $j_s$, ch. 11 boundary-conditions figure).

## Open defects (kept on disk, cleared as fixed)

- Math `zh` books (closed 2026-11-17, not this run): 74 `\index` keys split over a line break, each printed with a
  space in the key (`zh_sweeps.py` `indexjoin` would fix them; not run there unasked).

## Per-book log

### Queue v2 (2026-11-18 01:55)

- `draft/zh-queue.sh` slept 10 min after every pass that still had a rejected section (it read the last log line,
  "Not finished…", for " 0 stopped"), and grades 5–7 then sat four passes on one section each. Replaced by
  `draft/zh-queue2.sh` (list `draft/zh-queue2.list`, log `draft/zh-queue2.log`): reads the last `written` line, sleeps only
  after a failed call, 3 passes, a line may name chapters (the chemistry trial runs as two queue lines).
- The surviving rejections were all circuitikz lines `to[lamp] (5.8,4.0) to[short] (5.8,3.2);` counted as English ("to",
  "to"): `common.visible()` now drops `to[...]` path operators. Check that `l=bulb 1`-style labels are translated.
- Queue v3 (`zh-queue3.sh`) added `cmd` lines (step 5, the chemistry credits) that take a job slot, so `repair.py`'s
  single Haiku call never makes a tenth. It read its next line *before* waiting for a slot, so an edit to that line came
  too late (grade-7 ran twice, harmlessly; one cmd line was skipped). Queue v4 (`zh-queue4.sh`, list
  `zh-queue4.list`, log `zh-queue4.log`) reads the line only once a slot is free; every line not yet started can be edited.

### Physics Book 1 (grades 1–9) — closed 2026-11-18 02:35

- 415 Haiku calls, about $2.6 list; plan 10 % (all models). 398 pp, 0/0/0, missing characters 0, `.fls` 12/12, 7,755 links
  to 129 targets (English 6,483 / 133), gates green for all nine years. Score 88, pilot tier
  (`translation_scores/book_1/zh/translation_score.md`, with the defect classes).
- New rules, to run on every later year: `zh_sweeps.py` `credit`, `parens`, `textparen` (fixes), `cirlabel`, `engline`,
  `entitle` (reports); gate exemptions (image path, credit names, formulas, `\foreach` lists, kept Latin words);
  series-card lines for circuitikz labels and photo credits; `book1_zh.py` STOP/DROP mirroring English.
- The grade-8 `，—` open defect was gone after the dash sweep.

### Physics Book 2 (grades 10–12) — closed 2026-11-18 03:35

Score 88, pilot tier (`translation_scores/book_2/zh/translation_score.md`). Model: `claude-haiku-5-5`, effort medium,
402 calls, about $3.5 list; coordinator `claude-opus-5-5`. 319 pp (en 350, fr 358), 0/0/0, missing characters 0,
`.fls` 18/18; gates green for grades 10–12; 5,334 links to 190 targets (en 4,497 / 203); pdfsweep 0; figlint 0.
New defect classes and their fixes:
- **Lost Ω in zh** (58 × U+000A, circuit chapters): `\ohm` moved to the legacy maths slot in `onephysics.sty` and
  `onechemistry.sty` (the Earth fix). It also mends the physics/chemistry `hi`/`ar` sources; shipped PDFs not rebuilt.
- **Unicode Greek** (α 射线, μ子; 55 missing chars): `\xeCJKDeclareCharClass{CJK}` for Greek in both styles (Fandol has
  it). A sweep that wrapped it in math was tried and dropped: it changes the math-span census.
- **`\legend{无阻尼，有阻尼}`**: the zh punctuation pass (`langs/zh.py`) treated a legend list as prose and merged six
  legends into one entry each. `zh.py` now masks legend lists; `zh_sweeps.py` rule `legend` restores installed files.
  Closed books checked: no hit in physics Book 1, math, quant.
- Over-linking calibrated in `book2_zh.py` (速率, 静止, 谱线, 电荷, 电流, 推力 stopped; 竖直方向, 竖直, 绝对 dropped).

### Physics Book 3 (University Year 1) — closed 2026-11-18 05:55

Model: `claude-haiku-5-5` effort medium, 516 calls, about $4.6; coordinator Opus 5.5. Score 88 (pilot tier), 308 pp
(en 332, fr 349), 0/0/0, missing characters 0, gate green, 3,041 links / 217 targets (en 2,342 / 196). Score file
`translation_scores/book_3/zh/translation_score.md`.

- Five sections still rejected after the passes, finished with `fixsec.py` (ch. 6 §§1, 3, 6; ch. 22 §1 by hand; ch. 29
  solutions §1).
- **The linker harvested no index-only term in Chinese**: `harvest.py` required a space in an `\index`-only key, so
  动能 (the kinetic-energy theorem, 47 English links) and 108 other targets were never linked. New opt-in
  `INDEX_CJK = True` in the book config (default off). It first doubled the links (4,674), then STOP/DROP calibrated
  against the English config and the census brought them to 3,041; the three result names English links (高斯定理,
  安培环路定理, 斯涅耳定律) go in `EXTRA`, as the French config does. **Set it in Books 4–5 and every chemistry book.**
- Fixed: English `\text`/`\mathrm` subscripts (15 kinds), unit words in `\qty` (dB/decade, years, turns/m), 4 English
  lines, 5 English index keys, one lost number (42,200 km), 4 doubled words, one half-transliterated credit name, one
  zh-only overfull formula.
- Every numtrace difference explained (`draft/zh/numtrace-bachelor-1.log`).

### Physics Book 4 (University Year 2) — closed 2026-11-18 06:55

Model: `claude-haiku-5-5` effort medium, 574 calls, about $5.7; coordinator Opus 5.5. Score 88 (pilot tier), 313 pp
(en 345, fr 359), 0/0/0, missing characters 0, gate green, 1,629 links / 150 targets (en 1,231 / 143). Score file
`translation_scores/book_4/zh/translation_score.md`.

- Three sections rejected after 3 passes, finished with `fixsec.py` (see the run notes).
- About 190 English `\text{}` subscripts (36 kinds: sat, cond, th, in/out, liq/vap…) mapped to Chinese as in Book 3;
  `sp` is *spreading* there (展宽), not *spontaneous*: read each kind in context before mapping.
- New `indexjoin` sweep rule (9 split `\index` keys here, 5 in Book 2, fixed; 74 in math, listed above).
- Gate fixes: the plain 照片： credit blanking hid an `\omterm` (a caption that *begins* 照片：); rpm/ppm/sinc/erfc and
  He--Ne allowed. Both repos.
- Link calibration as Book 3 (INDEX_CJK on): 2,402 → 1,629 links; 马吕斯定律 in `EXTRA`; 全反射 must stay linkable.
- Open ch. 11 items closed: the j_s label is now （向里）; line 596 reads 第 3 题.

### Physics Book 5 (University Year 3) — closed 2026-11-18 07:40

Model: `claude-haiku-5-5` effort medium, 582 calls, about $5.9; coordinator Opus 5.5. Score 88 (pilot tier), 273 pp
(en 302, fr 323), 0/0/0, missing characters 0, gate green, 1,153 links / 104 targets (en 916 / 100). Score file
`translation_scores/book_5/zh/translation_score.md`. **All five physics books are now closed in `zh`.**

- The queue bug sent the year to step 5 with 10 sections in English; a 10-chapter rerun (3 passes, 06:59–07:26) left
  2 sections, finished with `fixsec.py` (ch. 8 §1, ch. 15 §1). The step-5 rerun was not needed: `post.py` showed both
  chapters clean but for one English line, fixed by hand.
- ch. 15 §1 needed a tool fix, not a reply fix: physics `id_apply.py`'s node-text pattern did not accept a calc
  coordinate `at ($(35:3.4)+(0.25,0)$)` (chemistry's copy had the fix since 2026-10-04); ported.
- ~150 `	ext{}` subscripts (38 kinds) mapped; `res` is the heat *reservoir* in ch. 17 (库), `conf` the confinement
  energy (约束). `eff`, `deg`, `max` were caught only by `census.py` (TEXT-EN), not by the gate.
- The lost Ω again, in a new form: `\qty{…}{\Omega.m}` (a unit written as the Greek letter, not `\ohm`). Only one site in
  the physics and chemistry `zh` trees.
- Link calibration: 1,708 → 1,153; 结合能 (crystal cohesive energy and nuclear binding energy) and 约束 (constraint and
  confinement) stopped; 对称性 and 二极管 dropped.
- The `fix_names` sweep turned the photographer *Stefan* Andrej Shambora back into 斯特藩 in Book 3 on a re-run; the
  rule now leaves 照片：… alone and the credit is restored (Book 3's PDF was built before, unaffected).
- Physics Book 4 reopened once: a `\legend{铜、海水}` printed one entry (Haiku used 、 as the separator); fixed, PDF
  rebuilt (313 pp, 0/0/0), score file updated. Book 2 PDF rebuilt after its `indexjoin` fixes (319 pp, 0/0/0).

Run notes:

- Queue list edits: insert at least two lines after the last "started" line; an insert at the very next line can race
  the reader (grade-11's re-run was skipped once, then put back).
- A run directory holds the English twins too (`draft/pilot-<year>-zh/course/*.tex`): a hand fix by sed must name
  `course/zh/` and `solutions/zh/` only (a red/blue subscript fix touched the English copy once; restored from `parts/`).
- grade-10: a TikZ `mark=at position … with` option was rejected as English ("at", "with"): `common.visible()` drops it.
  Gate allows the Latin kept as such: Homo sapiens, E. coli, helios, Wi-Fi, ping, "One Math Book".
- bachelor-2 (2026-11-18 06:30): 3 sections rejected after 3 passes (ch. 7, 8, 9 section 2), finished with `fixsec.py`:
  an English twin line left after the translated one, a `$` added inside a display, a missing closing `$`, and
  `\text{…}` / math alternation reordered in a comparator display. A node `{\pgfmathparse{int(20*\l)}…}` was read as
  English ("int"): `common.visible()` and `langs/zh.py` `_english()` now drop `\pgfmathparse{…}`.
- chemistry grade-11 (2026-11-18 07:00): one section rejected 3 times for an English line that was TikZ code split over
  two lines (`amplitude=1pt, segment length=4pt}] (\a:0.55) -- …`). `common.visible()` now drops `key=number` options
  and every macro name (`\a` was read as the article "a"). Finished with `fixsec.py save`, no edit to the reply.
- **Queue bug (2026-11-18 07:05)**: `zh-queue4.sh` declared a year clean with `grep -q "0 with a rejected section; 0
  stopped"`, which "10 with a rejected section; 0 stopped" also contains. Physics bachelor-3 was logged "done (pass 2)"
  with 10 sections still in English (whole weekend problems) and went on to step 5. Fixed in the file (`"s; 0 with …"`;
  the running queue keeps the old function in memory, so every year's last `written` line is now read by hand).
  Chemistry bachelor-3 (started 06:58) was stopped and re-queued behind a third physics bachelor-3 pass.
- **Queue bug, second hit (2026-11-18 08:14)**: chemistry bachelor-1 was logged "done (pass 1)" with "10 with a rejected
  section" (the running queue still holds the old check) and sat idle for 30 minutes. Its retry passes were started by
  hand at 08:42 (a loop that stops on a real "; 0 with a rejected section"). The queue list has no line after chemistry
  bachelor-3, so bachelor-2 and bachelor-3 are checked by hand when they end.
- **Three defect classes found at chemistry Book 2's close (2026-11-18 09:00–10:00), run back over every closed book**:
  - `\foreach` lists split by `，`: TikZ splits on ASCII commas only, so `{0.5/烛光，2.0/白炽灯，…}` printed every label at
    the first position. Physics Book 2 had 4 lists (17 separators: grade 11 ch. 2 and 4, grade 12 ch. 2 and 4); the
    figure contact sheets missed them. New sweep rule `foreachsep`. Math: 0.
  - `[xy]ticklabels={…}` merged by `，`: physics grade 11 ch. 7, chemistry grade 12 ch. 11 and bachelor-1 ch. 2 and 26.
    The `legend` rule now covers tick labels. Math: 0.
  - A stray `=` before a line English starts plainly (`=\section{…}`, `  =  \item`, `=\label`): printed an equals sign
    before a title or item, and in chemistry bachelor-1 ch. 7 broke the build (`\item` outside a list). Physics grade 8
    (13), grade 10 (16), grade 12 (1); chemistry grade 11 (1), bachelor-1 (56). New sweep rule `strayeq` (compares with
    the English line). **Math hits, listed not fixed**: grade 11 ch. 9 (2, from line 149 `=\section{方差与标准差}`) and
    grade 12 ch. 2 (2, from line 376 `=\section{问题：…}`).
  - A bare `%` after a number (`1.31%、0.84%`) commented out the rest of the line: chemistry bachelor-1 (2). New rule
    `percent`. Math: 0.
  Physics Books 1 and 2 and chemistry Book 1 rebuilt after these fixes.

## Run closed (2026-11-18 10:40)

Physics Books 1–5 and chemistry Books 1–4 ship in `zh`, pilot tier 88 each, uncommitted; chemistry's per-book log is in
`../one-chemistry-book/sources/TRANSLATION_BOOKS_1-4_ZH.md`. 4,194 Haiku calls, about $36 of list price; weekly plan
9 % → 16 %. Rules found at the chemistry closes and run back over the physics books: `strayeq` (physics Book 1, 14
sites; Book 2, 17; rebuilt), `foreachsep`/`ticklabels`, `percent`, `omp`, `onium` (no physics hit). Lessons in
`../pilot_translation_instruction.md`. Not done: the HTML reader.
