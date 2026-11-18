# Translation score: One Physics Book 2, Simplified Chinese (`zh`)

| Field | Value |
|-------|--------|
| **Book** | One Physics Book 2 (High School, grades 10–12), `one_physics_book_2_high_school_zh.tex` |
| **Language** | Simplified Chinese (`zh`), mainland textbook usage |
| **Overall score** | **88 / 100**, sampled: 20 passages, seed 1 (6 from grade 10, 6 from grade 11, 8 from grade 12), not read in full |
| **Ship status** | **Pilot tier**: gates green; not read sentence by sentence; figures checked by script (all), contact sheets read by eye |
| **Date** | 2026-11-18 |
| **Model** | `claude-haiku-5-5` (Haiku 5.5, effort medium), pilot method: one headless call per section, 402 calls (translation, retries and repairs); glossary, infrastructure and coordinator `claude-opus-5-5` (Opus 5.5), one coordinator for the whole physics + chemistry run, no subagents |
| **Canon** | English as committed; no English edit. Noted, not fixed: `\qty{4.2}{days}` (grade-12 solutions ch. 4, ex. 12), a unit word inside `\qty` |
| **Tokens** | Haiku: 402 calls, about $3.5 list price (per year in `draft/pilot-grade-1{0,1,2}-zh/post.log`, line `all:`). Coordinator: shared with the run; weekly plan (all models) 10 % before this book, 11 % after it (`sources/TRANSLATION_BOOKS_1-5_ZH.md`) |
| **Scope** | 35 chapters + 35 solution files under `parts/grade-{10,11,12}/zh/` and `parts/grade-{10,11,12}/solutions/zh/`; glossary `sources/GLOSSARY_BOOK_2_ZH.md`; term config `tools/term_config/book2_zh.py` |

## Verdict

Plain, correct mainland high-school register (称为…, 由此推出, 求…, 并判断…). Standard terms throughout (参考系, 折射率,
全反射, 相互抵消, 波节, 准周期, 托卡马克, 遏止电压). Clauses are reordered across lines as Chinese needs, weekend-problem
titles read as titles. Weak points: some long sentences that keep the English clause order, and a few literal turns
(“正如力偶会改变符号一样”). No sentence in the sample was wrong in sense.

## Build and gates

- `build/one_physics_book_2_high_school_zh.pdf`: 319 pp (English 350, French 358). XeLaTeX + xeCJK, Fandol.
  Errors 0, undefined 0, overfull 0, nullfont 0, missing character 0, invalid-in-math 0, zero-height 0; `.fls` 18/18.
  TeX Live 2026.
- `tools/check_translation.sh grade-N zh`: PASSED for N = 10, 11, 12, gate 9 (`check_chinese_prose.py`) included.
- `link_defined_terms.py --book 2 --lang zh --check`: every file matches. 5,334 links to 190 targets (English 4,497 to
  203). The surplus (+19 %, as in Book 1) is real occurrences (Chinese repeats 磁场, 折射率, 半衰期 where English uses a
  pronoun or a symbol), offset by the one-character terms Chinese cannot link (波 wave −103, 场 field −107, 力 force).
- `pdfsweep.py` against the French PDF: 0 English-only word types after the fix below.
- `figcheck.py lint`: 0 label collisions; the 56 drawn figures read on contact sheets.

## What was read

- Text: 20 passages (seed 1), the sweep, number and PDF-sweep reports, every gate hit.
- Numbers: every NUMDIFF line traced. All are "the Year 1 volume" → 本科一年级分册 or number words written as digits,
  except one real loss (grade-11 ch. 8: the crate's "and 5.0 m back" lost its distance), restored by hand.

## Defects found and fixed, by class

| Class | Count | Example | Fix |
|---|---:|---|---|
| Unicode Greek in Chinese text, absent from Latin Modern | 55 missing chars | α 射线, μ子, π 介子 | style: `\xeCJKDeclareCharClass{CJK}` for U+0391–03C9 (Fandol has Greek); β⁻ → 负 β |
| The lost Ω (`\ohm` printed U+000A) | 58 missing chars | `\qty{100}{\ohm}` in the circuit chapters | style: `\ohm` from the legacy maths font, as `oneearth.sty` |
| pgfplots legend entries merged by a full-width comma | 6 legends | `\legend{无阻尼，有阻尼}` printed one entry | `langs/zh.py` masks legend lists; `legend` sweep rule |
| `\foreach` / symbolic-axis names left in English | 9 lists | `{0/quark, 3/nucleus,…}`, `{dry road, wet road,…}` | by hand (`sites.py`); `xticklabels=` |
| circuitikz labels in English | 2 | `l=plant`, `l=village` | 发电站, 村庄 (`cirlabel` report) |
| English `\text{}` in formulas | 12 | `n_{\text{red}}`, `v_{\text{top}}`, `\text{(approach)}` | 红/蓝/顶, （靠近）/（远离） |
| A word or line left in English | 5 | `requires.`, `$… \approx 10^{36}$ is`, a title's last word `itself` | by hand; `engline` report |
| Unit word inside `\qty` | 1 | `\qty{4.2}{days}` | `\qty{4.2}{\text{天}}` |
| Over-linking against English's choices | ~520 links | 速率 183 (English "speed" stopped), 静止 121, 谱线 101, 电荷 139, 电流 144; 竖直方向 → weight | `STOP`/`DROP` in `book2_zh.py` |
| Doubled word at a line break | 3 | 电路仍在 / 在逐渐 | by hand (`dupbreak`) |
| A dropped number | 1 | 再滑回 (\qty{5.0}{m} lost) | restored |
| `\foreach` lists and tick labels split by a full-width comma | 4 lists (17 separators) + 1 | grade 11 ch. 2 `{0.5/烛光，2.0/白炽灯，…}` and ch. 4, grade 12 ch. 2 and 4: TikZ splits on ASCII commas only, so each figure printed all its labels at the first position; grade 11 ch. 7 `xticklabels` (found at chemistry Book 2's close; PDF rebuilt) | new `foreachsep` sweep rule; `legend` rule covers `[xy]ticklabels` |
| Stray `=` before a content line | 17 | grade 10 (16), grade 12 (1): Haiku's `=` mark left before a content line, printed as “=” (found at chemistry Book 2's close; PDF rebuilt 319 pp, 0/0/0) | `strayeq` sweep rule |

## Tooling this book added (run back over every later year)

- `common.visible()` drops TikZ `mark=at position … with` (a section rejected three times for "at", "with").
- Gate: element symbols with a trailing hyphen (Am-241), `\legend{a, b}` lists, `\foreach` lists with a text field in
  the middle (`2.4/1.8/black/实验室,`), and the Latin kept on purpose (Homo sapiens, E. coli, helios, Wi-Fi, ping,
  One Math Book) are not flagged.
- `zh_sweeps.py`: `legend` (fix); `textparen` takes `\unit{}` inside; `engline` reports only lines ending a sentence.
- Styles (physics and chemistry): Greek as a CJK class; the lost-Ω fix, which also mends the physics and chemistry
  Hindi and Arabic sources (their shipped PDFs are not rebuilt).
