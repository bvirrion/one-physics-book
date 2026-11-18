# Translation score: One Physics Book 3, Simplified Chinese (`zh`)

| Field | Value |
|-------|--------|
| **Book** | One Physics Book 3 (University Year 1), `one_physics_book_3_university_year_1_zh.tex` |
| **Language** | Simplified Chinese (`zh`), mainland textbook usage |
| **Overall score** | **88 / 100**, sampled: 20 passages, seed 1 (17 course, 3 solutions), not read in full |
| **Ship status** | **Pilot tier**: gates green; not read sentence by sentence; figures checked by script (all), contact sheets read by eye |
| **Date** | 2026-11-18 |
| **Model** | `claude-haiku-5-5` (Haiku 5.5, effort medium), pilot method: one headless call per section, 516 calls (translation, retries and repairs); five rejected sections finished by hand (`fixsec.py`); glossary, infrastructure and coordinator `claude-opus-5-5` (Opus 5.5), one coordinator for the whole physics + chemistry run, no subagents |
| **Canon** | English as committed; no English edit. |
| **Tokens** | Haiku: 516 calls, about $4.6 list price (`draft/pilot-bachelor-1-zh/post.log`, line `all:`). Coordinator: shared with the run; weekly plan (all models) 11 % before this book, 13 % after it, with chemistry grades 1–6 translating meanwhile (`sources/TRANSLATION_BOOKS_1-5_ZH.md`) |
| **Scope** | 30 chapters + 30 solution files under `parts/bachelor-1/zh/` and `parts/bachelor-1/solutions/zh/`; credits `frontmatter/image-credits-book3.zh.tex`; glossary `sources/GLOSSARY_BOOK_3_ZH.md`; term config `tools/term_config/book3_zh.py` |

## Verdict

Correct first-year university register (求…, 证明…, 由此得出结论, 在本阶段不加证明地承认 for "admitted"). Standard
terms (光焦度, 负载效应, 终端速度, 尖端效应, 上止点, 中性浮力, 复摆, 扭摆). Clauses are reordered across lines as Chinese
needs, and the numbers moved with them. Weak points: some long caption sentences in English clause order, and a few
literal turns (“火焰的大部分品质都浪费在加热水上” for the flame's *quality* in the exergy sense). No sentence in the
sample was wrong in sense.

## Build and gates

- `build/one_physics_book_3_university_year_1_zh.pdf`: 308 pp (English 332, French 349). XeLaTeX + xeCJK, Fandol.
  Errors 0, undefined 0, overfull 0, nullfont 0, missing character 0, invalid-in-math 0, zero-height 0; `.fls` 60/60.
  TeX Live 2026.
- `tools/check_translation.sh bachelor-1 zh`: PASSED, gate 9 (`check_chinese_prose.py`) included.
- `link_defined_terms.py --book 3 --lang zh --check`: every file matches. 3,041 links to 217 targets (English 2,342 to
  196). The surplus (+30 %) is real occurrences: Chinese repeats 电压, 振幅, 透镜 where English uses a pronoun or a symbol.
- `pdfsweep.py` against the French PDF: 8 English-only word types left, all intended: `rms` subscripts (irms, urms, …,
  kept as in every edition), `copmax` (COP), and the credits' institution name (US Department of Energy) and licence line.
- `figcheck.py lint`: 1 hit, a false alarm (a vector arrow in running text, p. 200); the 69 drawn figures read on
  contact sheets.

## What was read

- Text: 20 passages (seed 1), the sweep, number and PDF-sweep reports, every gate hit.
- Numbers: every `numtrace.py` difference traced (`draft/zh/numtrace-bachelor-1.log`): "the Year 2/3 volume" →
  本科二/三年级分册, number words written as digits (eleven → 11 伏, sixty → 60, forty percent → 40\%), stage 1/2 → 第一/二级,
  and numbers moved to the next line by clause reordering (\qty{3}{m}, \qty{16}{mm^2}); none lost.

## Defects found and fixed, by class

| Class | Count | Example | Fix |
|---|---:|---|---|
| Sections still rejected after the passes | 5 | ch. 6 sections 1, 3, 6; ch. 22 section 1; ch. 29 solutions section 1 (math order, `\emph` position, `l=dipole`) | `fixsec.py dump/save`, hand-aligned; ch. 22 §1 translated by hand |
| English `\text{}` / `\mathrm{}` subscripts | 15 kinds | `\text{orb}`, `\text{nc}`, `S_{\mathrm{created}}`, `S_{\mathrm{exch}}`, `\text{tot}` (solutions) | 轨道, 非保守, 产生, 交换, 总 (`tot` in the course too) |
| Unit word inside `\qty` | 3 kinds | `{dB/decade}`, `{years}`, `{turns/m}` | `dB/\text{十倍频程}`, `\text{年}`, `\text{匝}/m` |
| A line left in English | 4 | ch. 30:100, 30:439, 21:98, 06:83 | `%` (the line before carries it) |
| Index keys left in English | 5 | ch. 6 `\index{Thévenin's theorem}` | 戴维南定理, 诺顿定理, 叠加定理, 米尔曼定理, 线性二端元件 |
| A dropped number | 1 | ch. 16:332 `\qty{42200}{km}` | restored |
| Doubled word at a line break | 4 | ch. 8:293 取 / 取 | by hand (`dupbreak`) |
| Credit name half transliterated | 1 | 照片：斯特藩 Andrej Shambora | Stefan Andrej Shambora |
| Overfull inline formula (zh only) | 1 | solutions ch. 14, ex. 9 | two `\allowbreak` |
| Under-linking: index-only notions unharvested | 109 English targets missed | 动能 (the kinetic-energy theorem, 47 English links) | `harvest.py` opt-in `INDEX_CJK`; `高斯定理`, `安培环路定理`, `斯涅耳定律` in `EXTRA` (as `book3_fr.py`) |
| Over-linking against English's choices | ~1,600 links | 电流 283 (English 4), 电荷 142, 光线 129, 功率 74 → *work* | `STOP`/`DROP` in `book3_zh.py` |

## Tooling this book added (run back over every later year)

- `tools/termlink/harvest.py` (physics): a config may set `INDEX_CJK = True`, so an index-only key of two or more
  characters is a term (Chinese has no spaces, so the English "two words" rule dropped every key). Default off; English
  and the other editions unchanged. Books 4–5 and chemistry should set it and calibrate the same way.
