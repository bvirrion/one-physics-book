# Translation score: One Physics Book 5, Simplified Chinese (`zh`)

| Field | Value |
|-------|--------|
| **Book** | One Physics Book 5 (University Year 3), `one_physics_book_5_university_year_3_zh.tex` |
| **Language** | Simplified Chinese (`zh`), mainland textbook usage |
| **Overall score** | **88 / 100**, sampled: 20 passages, seed 1 (14 course, 6 solutions), not read in full |
| **Ship status** | **Pilot tier**: gates green; not read sentence by sentence; figures checked by script (all), contact sheets read by eye |
| **Date** | 2026-11-18 |
| **Model** | `claude-haiku-5-5` (Haiku 5.5, effort medium), pilot method: one headless call per section, 582 calls (translation, retries, a 10-chapter rerun and repairs); two rejected sections finished by hand (`fixsec.py`); glossary, infrastructure and coordinator `claude-opus-5-5` (Opus 5.5), one coordinator for the whole physics + chemistry run, no subagents |
| **Canon** | English as committed; no English edit. Noted, not fixed: `\qty{…}{atoms/m^3}` (3 sites, a unit word inside `\qty`), translated in the Chinese edition |
| **Tokens** | Haiku: 582 calls, about $5.9 list price (`draft/pilot-bachelor-3-zh/post.log`, line `all:`). Coordinator: shared with the run; weekly plan (all models) 14 % at this book's close (`sources/TRANSLATION_BOOKS_1-5_ZH.md`) |
| **Scope** | 27 chapters + 27 solution files under `parts/bachelor-3/zh/` and `parts/bachelor-3/solutions/zh/`; credits `frontmatter/image-credits-book5.zh.tex`; glossary `sources/GLOSSARY_BOOK_5_ZH.md`; term config `tools/term_config/book5_zh.py` |

## Verdict

Correct third-year register (由…可得, 在本阶段不加证明地承认, 求…并说明…). Standard terms (本征子空间, 可寻址的光镊,
交换空穴, 维里定理, 自引力, 布拉格反射, 时空间隔, 固有时). Clauses reordered across lines as Chinese needs. Weak points:
some literal turns ("我们的眼睛恰好进化到对准它的峰值", "完美热光谱"), a repeated verb across a line (补充…补充).
No sentence in the sample was wrong in sense.

## Build and gates

- `build/one_physics_book_5_university_year_3_zh.pdf`: 273 pp (English 302, French 323). XeLaTeX + xeCJK, Fandol.
  Errors 0, undefined 0, overfull 0, nullfont 0, missing character 0 (English's baseline is 10, a nullfont class Chinese
  does not have), invalid-in-math 0, zero-height 0; `.fls` 54/54. TeX Live 2026.
- `tools/check_translation.sh bachelor-3 zh`: PASSED, gate 9 (`check_chinese_prose.py`) included.
- `link_defined_terms.py --book 5 --lang zh --check`: every file matches. 1,153 links to 104 targets (English 916 to
  100). Not reached: *hyperfine* (5 English links; 超精细结构 is used only inside its own example), *binding energy*
  (3; 结合能 names both the crystal's cohesive energy and the nucleus's binding energy, so it is stopped), two targets
  linked once in English.
- `pdfsweep.py` against the French PDF: 1 English-only word type left, intended: CSCO (the standard abbreviation).
- `figcheck.py lint`: 0 label collisions; the 47 captioned figures read on contact sheets.

## What was read

- Text: 20 passages (seed 1), the sweep, number and PDF-sweep reports, every gate hit.
- Numbers: every `numtrace.py` difference traced (`draft/zh/numtrace-bachelor-3.log`): 1D/2D/3D → 一维/二维/三维, the
  Year N volume → 本科N年级分册, number words written as digits, 57 billion → 570 亿, 4.5 billion → 45 亿, 1st/2nd/3rd
  → 第一/二/三代, and math moved to the neighbouring line by clause reordering ($n = 1$, $2 \to 1$, $\Delta s^2$,
  $2, 8, 8, 18$, $k \approx 1$; each found on the line before or after). None lost.

## Defects found and fixed, by class

| Class | Count | Example | Fix |
|---|---:|---|---|
| Sections still rejected after the passes | 10 chapters, then 2 sections | first run: whole weekend problems left in English (logged "done" by a queue bug); after a rerun of 10 chapters, ch. 8 §1 (English twin lines, a doubled `\[`, two merged lines, a lost `\emph{two}`) and ch. 15 §1 (an English twin line) | rerun; `fixsec.py`, hand-aligned |
| English `\text{}` subscripts | 38 kinds, ~150 | `S_{\text{res}}` (the reservoir), `E_{\text{conf}}`, `H_{\text{iron}}`, `m_{\text{eff}}`, `\text{deg}` | 库, 约束, 铁, 有效, 简并 … (tot → 总, rad → 辐射, as Books 3–4); rms kept |
| Unit word inside `\qty` | 3 | `\qty{8.5e28}{atoms/m^3}` | `\text{原子}/m^3` |
| The lost Ω (`\Omega` as a `\qty` unit) | 1 missing char | `\qty{1.7e-8}{\Omega.m}` printed U+000A | `\ohm.m` |
| Lines left in English | 3 | `unit volume is …`, `describes.`, `mathematics volume gives …` | by hand / `%` |
| English left in prose | 5 | `boost` ×5 (Lorentz boost) | 洛伦兹推促 |
| Photo credit frames | 5 | `（Orren Jack Turner 摄，…）`, `（NASA, ESA, … public domain）`, `copyrighted free use`, `Bell Laboratories display` | 照片：… frame; 公有领域, 版权所有者允许自由使用, 贝尔实验室展品 |
| ASCII brackets in `\text{}` | 3 | `\text{(接近时：}` | full-width, or `\text{ (` paired with a math `)` |
| Doubled word at a line break | 2 | 这 / 这正是; 空间态反对称，/ 态， | by hand |
| Over-linking against English's choices | ~550 links | 简并 95 (English 0), 费米子/玻色子 83, 对称性 68, 带隙 46, 氢原子 41; 约束 in its "confinement" sense | `STOP`/`DROP` in `book5_zh.py` |

## Tooling this book added (run back over every later year)

- `tools/id_apply.py` (physics): a node's coordinate may hold one level of parentheses, `at ($(35:3.4)+(0.25,0)$)` (ported
  from chemistry, where it was fixed 2026-10-04); before, the node's label compared as drawing code and no translation
  of it could pass.
- Gate (physics and chemistry): lattice and quark-content symbols (fcc, bcc, uud), units (Mpc, Gyr, ppb), proper names
  (KamLAND, Bevatron, PKJKP), sub-question ranges `(b--c)`, and a `\legend{…}` with one brace level are not flagged.
- `zh_sweeps.py`: `legend` takes `、` and one brace level; `fix_names` leaves photo credits alone.
