# Translation score: One Physics Book 4, Simplified Chinese (`zh`)

| Field | Value |
|-------|--------|
| **Book** | One Physics Book 4 (University Year 2), `one_physics_book_4_university_year_2_zh.tex` |
| **Language** | Simplified Chinese (`zh`), mainland textbook usage |
| **Overall score** | **88 / 100**, sampled: 20 passages, seed 1 (14 course, 6 solutions), not read in full |
| **Ship status** | **Pilot tier**: gates green; not read sentence by sentence; figures checked by script (all), contact sheets read by eye |
| **Date** | 2026-11-18 |
| **Model** | `claude-haiku-5-5` (Haiku 5.5, effort medium), pilot method: one headless call per section, 574 calls (translation, retries and repairs); three rejected sections finished by hand (`fixsec.py`); glossary, infrastructure and coordinator `claude-opus-5-5` (Opus 5.5), one coordinator for the whole physics + chemistry run, no subagents |
| **Canon** | English as committed; no English edit. Noted, not fixed: 11 unit words inside `\qty` (`{days}`, `{kWh/year}`, `{fringe}`, `{turns/s}`, `{lines/mm}`), translated in the Chinese edition |
| **Tokens** | Haiku: 574 calls, about $5.7 list price (`draft/pilot-bachelor-2-zh/post.log`, line `all:`). Coordinator: shared with the run; weekly plan (all models) 13 % before and after this book (chemistry Book 1 translating meanwhile; `sources/TRANSLATION_BOOKS_1-5_ZH.md`) |
| **Scope** | 31 chapters + 31 solution files under `parts/bachelor-2/zh/` and `parts/bachelor-2/solutions/zh/`; credits `frontmatter/image-credits-book4.zh.tex`; glossary `sources/GLOSSARY_BOOK_4_ZH.md`; term config `tools/term_config/book4_zh.py` |

## Verdict

Correct second-year university register (求…, 由…给出, 量级估计, 在本阶段不加证明地承认). Standard terms (失速速度, 指示
速度, 弛豫时间, 散斑, 啁啾, 基横模, 强迫, 气候敏感度, 佩尔顿水轮). Clauses reordered across lines as Chinese needs;
weekend-problem titles read as titles. Weak points: a few literal turns (“也是旧街道的常客”), and some exercises mix
ASCII “(a)” with full-width “（b）”. No sentence in the sample was wrong in sense.

## Build and gates

- `build/one_physics_book_4_university_year_2_zh.pdf`: 313 pp (English 345, French 359). XeLaTeX + xeCJK, Fandol.
  Errors 0, undefined 0, overfull 0, nullfont 0, missing character 0, invalid-in-math 0, zero-height 0; `.fls` 62/62.
  TeX Live 2026.
- `tools/check_translation.sh bachelor-2 zh`: PASSED, gate 9 (`check_chinese_prose.py`) included.
- `link_defined_terms.py --book 4 --lang zh --check`: every file matches. 1,629 links to 150 targets (English 1,231 to
  143). Seven English targets are not reached. Six are linked once or twice in English; the seventh is *enthalpy*
  (9 English links on the open-system first law), which is 焓, one character, so the Chinese linker cannot link it.
- `pdfsweep.py` against the French PDF: 8 English-only word types before the unit fix below; left after it: the COP
  subscripts (`coph`, `copc`) and the credits' licence line.
- `figcheck.py lint`: 0 label collisions; the 62 drawn figures read on contact sheets (one collision found by eye,
  fixed below).

## What was read

- Text: 20 passages (seed 1), the sweep, number and PDF-sweep reports, every gate hit.
- Numbers: every `numtrace.py` difference traced (`draft/zh/numtrace-bachelor-2.log`). The differences are:
  - "the Year 1/2/3 volume" → 本科N年级分册;
  - number words written as digits (twenty-five → 25, a hundred → 100, four percent → 4\%);
  - order 1/2 → 一级/二级, (1D)/(3D) → 一维/三维;
  - numbers moved to the next line by clause reordering.

  None was lost.

## Defects found and fixed, by class

| Class | Count | Example | Fix |
|---|---:|---|---|
| Sections still rejected after the passes | 3 | ch. 7, 8, 9 section 2: an English twin line, a `$` inside a display, a missing `$`, `\text`/math alternation | `fixsec.py`, hand-aligned |
| English `\text{}` subscripts | 36 kinds, ~190 | `V_{\text{sat}}`, `q_{\text{cond}}`, `g_{\text{th}}`, `t_{\text{sp}}` (spreading) | 饱和, 冷凝, 阈, 展宽 … (tot → 总, rad → 辐射, as Book 3); rms, mol, ppm kept |
| `\foreach` label lists in English | 2 | `{0/threshold of hearing, 1/rustling leaves,…}`, `{0/absorption,…}` | 听阈, 树叶沙沙声 …; 吸收, 自发辐射, 受激辐射 |
| Index keys in English | 8 | `\index{viscosity}`, `\index{Navier--Stokes equation}` | 黏度 … 纳维--斯托克斯方程 |
| Index key split over a line break | 9 | `\index{定态\n定态}` (key printed 定态 定态) | new `indexjoin` sweep rule; two by hand |
| Unit word inside `\qty` | 12 | `{days}`, `{fringe}`, `{lines/mm}` | `\text{天}`, `\text{条纹}`, `\text{线}/mm` |
| A line left in English | 2 | `infrared spectrometers.`, `stored beam.` | `%` (the line before carries it) |
| Names in Latin | 3 | Jurin, Drude | 朱林定律, 德鲁德模型 |
| Caption words in English | 2 | `（LIGO Laboratory）`, `$y = $ const` | LIGO 实验室, 常数 |
| Figure label collision | 1 | ch. 11 boundary conditions: `$\vect j_s$（垂直纸面向里）` over the ⊗ marks | （向里） |
| pgfplots legend merged by `、` | 1 | ch. 14 `\legend{铜、海水}` printed one entry (found at chemistry Book 1's close; PDF rebuilt 313 pp, 0/0/0) | `, `; `legend` sweep rule now takes `、` |
| Overfull inline formulas (zh only) | 2 | ch. 1 moments of inertia, ch. 21 geometric series | `\allowbreak` |
| Over-linking against English's choices | ~800 links | 起偏器 54 (English 2), 采样 34, 天线 40, 谐振腔 36, 衰减 87 against 23 | `STOP`/`DROP` in `book4_zh.py`; 马吕斯定律 in `EXTRA` |

## Tooling this book added (run back over every later year)

- `zh_sweeps.py` `indexjoin` (fix): an `\index` key split over a line break is joined on the first line, the line count
  kept. Run back over Books 1–3 (5 keys in Book 2, fixed); the math `zh` books carry 74 such keys (listed in the run
  file, not fixed).
- `common.visible()` and `langs/zh.py` drop `\pgfmathparse{…}` (a node `{\pgfmathparse{int(20*\l)}…}` was rejected
  as English "int").
- Gate (physics and chemistry): rpm, ppm, sinc, erfc and element pairs (He--Ne) are not flagged; the plain-credit
  blanking after 照片： stops at a macro (a caption beginning 照片： hid the `\omterm` after it, exposing its label).
