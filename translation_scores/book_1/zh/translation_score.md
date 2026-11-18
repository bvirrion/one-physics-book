# Translation score: One Physics Book 1, Simplified Chinese (`zh`)

| Field | Value |
|-------|--------|
| **Book** | One Physics Book 1 (Primary / Middle, grades 1–9), `one_physics_book_1_primary_middle_school_zh.tex` |
| **Language** | Simplified Chinese (`zh`), mainland textbook usage |
| **Overall score** | **88 / 100**, sampled: 20 passages, seed 1 (2 from each of grades 1–7 and 9, 4 from grade 8), not read in full |
| **Ship status** | **Pilot tier**: gates green; not read sentence by sentence; figures checked by script (all), contact sheets read by eye |
| **Date** | 2026-11-18 |
| **Model** | `claude-haiku-5-5` (Haiku 5.5, effort medium), pilot method: one headless call per section, 415 calls (translation, retries and repairs); glossary, infrastructure and coordinator `claude-opus-5-5` (Opus 5.5), one coordinator for the whole physics + chemistry run, no subagents |
| **Canon** | English as committed; no English edit. |
| **Tokens** | Haiku: 415 calls, about $2.6 list price (per year in `draft/pilot-grade-*-zh/post2.log`). Coordinator: shared with the run; weekly plan (all models) 9 % at the run's start, 10 % after this book (`sources/TRANSLATION_BOOKS_1-5_ZH.md`) |
| **Scope** | 71 chapters + 71 solution files under `parts/grade-{1..9}/zh/` and `parts/grade-{1..9}/solutions/zh/`; preface `frontmatter/preface.zh.tex`; credits `frontmatter/image-credits.zh.tex`; glossary `sources/GLOSSARY_BOOK_1_ZH.md`; term config `tools/term_config/book1_zh.py` |

## Verdict

Natural mainland schoolbook Chinese: short, warm sentences in the young grades (请说出…, 将下列活动按先后排序), the plain
textbook register from grade 6 (称…为…, 依据什么推理？). Clauses are reordered across lines as Chinese needs. Physics terms
are the standard ones (电流表, 并联, 支路, 焦距, 晶状体, 漫射物体). Weak points: a few literal images kept from English
(收费站 for the ammeter's "tollbooth", 骑手 on a seesaw) and some long sentences in English clause order. No sentence in
the sample was wrong in sense.

## Build and gates

- `build/one_physics_book_1_primary_middle_school_zh.pdf`: 398 pp (English 435, French 454). XeLaTeX + xeCJK, Fandol.
  Errors 0, undefined 0, overfull 0, nullfont 0, missing character 0, invalid-in-math 0, zero-height 0; `.fls` 12/12.
  TeX Live 2026. Pinyin index (upmendex): 200 entries.
- `tools/check_translation.sh grade-N zh`: PASSED for N = 1…9, gate 9 (`check_chinese_prose.py`) included.
- `link_defined_terms.py --book 1 --lang zh --check`: every file matches. 7,755 links to 129 targets (English 6,483 to
  133). The surplus is real occurrences (Chinese repeats 灯泡, 电池, 质量 where English uses a pronoun), offset by the
  one-character terms Chinese cannot link (光 light −380, 力 force −102).
- `pdfsweep.py` against the French PDF: 3 English-only word types left, all intended (*omega* in 希腊大写字母 omega, the
  probe name *MESSENGER* and the licence URL in the credits).
- `figcheck.py lint`: 0 label collisions; the 30 drawn figures read on contact sheets.

## What was read

- Text: 20 passages (seed 1), the sweep, number and PDF-sweep reports, every gate hit.
- Numbers: every NUMDIFF line traced: number words written as digits (nine seconds → 9 秒) or a number repeated for
  clarity (灯泡 2); none lost.

## Defects found and fixed, by class

| Class | Count | Example | Fix |
|---|---:|---|---|
| circuitikz labels left in English | 28 | `to[battery1, l=battery]` | by hand (map); `cirlabel` sweep report; series-card line |
| `\foreach` printed names left in English | 9 lists | `{0/sight, 2.4/hearing,…}`, planets | by hand (`sites.py`) |
| Symbolic axis names in English | 2 | `symbolic y coords={cork, oak,…}` | `yticklabels={软木,…}`, keys kept |
| Last line of a section left in English | 3 | `of different roads.` | `%` (the line before carries it); `engline` sweep report |
| Environment title left in English | 2 | `[Nothing to forward, nothing to see]`, `[Telescopes are time machines]` | by hand; `entitle` sweep report |
| Photo credit frame in English | 8 | `\emph{Photo: John Morgan, CC BY 2.0.}` | `credit` sweep rule (照片：…（裁剪）。); names stay Latin; gate skips them |
| English `\text{}` subscripts | 3 | `g_{\text{here}}`, `t_{\text{air}}` | → 此处, 地球, 空气 |
| A Han character Fandol lacks | 3 | 拃 (hand span) | 手掌跨度 |
| English grammar note kept | 1 | （复数为 \emph{media}） | removed |
| ASCII brackets in Chinese node text / `\text{}` | 2 | `{涡轮机\\(转动！)}` | `parens` and `textparen` sweep rules |
| Doubled word at a line break | 1 | 这 / 这就是 | by hand (`dupbreak`) |
| Over-linking against English's choices | ~760 links | 电流 402 (English 4), 电路, 平衡, 时刻, the senses | `STOP`/`DROP` in `book1_zh.py`, mirroring `book1_en.py` |
| Index key lost its sense | 1 | `\emph{压缩}\index{压缩}` (English `compressible`) | `\index{可压缩}` |
| English word in the credits prose | 2 | 提示词produce生成 (Books 1 and 4 credits) | removed |
| Stray `=` before a content line | 14 | grade 8: Haiku's `=` (its mark for an unchanged line) left before `\item`/Han text, printed as “=” (found at chemistry Book 2's close; PDF rebuilt 398 pp, 0/0/0) | new `strayeq` sweep rule, run back over every closed year |

## Tooling this book added (run back over every later year)

- `common.visible()` drops circuitikz `to[...]` operators (four sections were rejected four times for `to[lamp] … to[short]`).
- Gate: an `\includegraphics` path on its own line, Latin names inside `\emph{照片：…}`, plain-text formulas (HCl, NaCl),
  `\foreach` value lists, and the Latin words kept on purpose (rho, omega, ambulance, camera obscura) are not flagged.
- `zh_sweeps.py`: `credit`, `parens`, `textparen` (fixes); `cirlabel`, `engline`, `entitle` (reports).
