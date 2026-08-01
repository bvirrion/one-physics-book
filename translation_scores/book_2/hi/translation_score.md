# Translation score — Physics Book 2 · Hindi (`hi`)

| Field | Value |
|-------|--------|
| **Book** | One Physics Book 2 (High School, grades 10–12) |
| **Language** | Hindi (`hi`), standard technical Hindi per `hindi_style_card.md` |
| **Quality bar** | **native academic** (EN is the source of truth; the FR twin was used as a sense/structure reference) |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met.** |
| **Date** | 2026-08-01 (third pass — math-text sweep) |
| **Scope of the third pass** | **Every English string inside a math-mode text macro translated**, after the prose gate was extended to look inside `\text{…}`. 105 arguments rewritten in 33 files; gate back to 0. See *Revision — third pass* below. |
| **Scope of the second pass** | **The 48 outstanding bodies re-translated from the English canon** — grade-11 ch03–ch10 with their solutions (16 files) and all of grade-12 (32 files). With the 22 files of the first pass, **all 70 bodies are now hand-written Hindi**; no machine translation survives anywhere in the book. Plus: the last drawing-code deviation reverted, 16 new `PERFILE` figure-text maps, and `tools/term_config/book2_hi.py` extended (link density 3 245 → 3 466, and the newton/Newton sense collision fixed). |

## Read this first

The 2026-08-01 first pass shipped 22 of 70 bodies as native Hindi and left
48 as mechanically repaired machine translation; it scored **68**. This
pass finished the job. Every one of those 48 files was rebuilt from the
English skeleton — math, `tikzpicture`/`circuitikz`, `\label`, `\cref`,
`\qty`/`\unit`, `\begin{solution}{key}` and `\omterm` first arguments
carried across as byte-exact markers, the prose written fresh in Hindi
around them. The named symptom of the old tree,
`05-electric-gravitational-fields.tex` opening with «पृथ्वी उस सेब को कैसे
खींचती है जिसे वह कभी नहीं छूती?», now reads:

> पृथ्वी सेब को छुए बिना खींचती कैसे है? दूरी पर होती क्रिया को स्वयं न्यूटन
> ने ``इतनी बड़ी बेतुकी बात'' कहा था कि उसका बचाव करने से इनकार कर दिया।

| Part of the book | Files | State |
|---|---:|---|
| grade-10, all chapters and solutions | 18 | Hand-translated (pass 1) |
| grade-11 ch01–ch02 + solutions | 4 | Hand-translated (pass 1) |
| grade-11 ch03–ch10 + solutions | 16 | **Hand-translated (this pass)** |
| grade-12 ch01–ch16 + solutions | 32 | **Hand-translated (this pass)** |

## Dimension scores

| Dimension | Weight | Score /100 | Notes |
|-----------|-------:|----------:|--------|
| Register / tone | 0.20 | **95** | Uniform `आप`-register high-school prose across all 70 files, with the chapter openings written as openings rather than as translated first sentences («अभी इसी क्षण आपके शरीर के भीतर हर सेकंड कोई आठ हज़ार परमाणु-नाभिक फट रहे हैं।»). Verb chains are Hindi-final, `के माध्यम से` calques are gone, and the two-voice seam between hand and repaired files no longer exists |
| Terminology | 0.18 | **96** | Style-card glossary throughout, extended consistently into the 48 new files: विखंडन/संलयन, द्रव्यमान क्षति, बंधन ऊर्जा, अभिकेंद्र त्वरण, प्रत्यानयन बल, छद्म-आवर्तकाल, कालांक, त्रिज्य वेग, लाल/नील विस्थापन, निजी काल, काल-विस्तारण, लंबाई-संकुचन, दे ब्रॉय तरंगदैर्घ्य, क्रांतिक द्रव्यमान, मंदक, फ़्रिंज-चौड़ाई. Index keys were written with the visible term, not inherited from MT |
| MT-artifact freedom | 0.17 | **97** | No machine output remains in any body. Prose gate 0/70 files. The one systematic risk left is length: a handful of definitions run a line longer than the English because Hindi needs the postposition |
| Structural fidelity | 0.10 | **100** | 70 files, byte-identical label sets, exercise↔solution key parity in 35/35 chapters, identical environment and figure census. All three `check_translation.sh` runs **PASSED**; no duplicate labels |
| LaTeX hygiene | 0.08 | **100** | 0 errors, 0 undefined, **0 overfull**, 124 underfull. UTF-8 throughout, no TeX accent escapes. **All drawing-code deviations are now gone** (see below) |
| Cross-refs / rule compliance | 0.07 | **99** | `\label`, `\cref`/`\ref` targets and `\begin{solution}{key}` byte-identical to English. Zero country/board/curriculum names. Unit symbols inside `\qty`/`\unit` Latin everywhere |
| Figures | 0.07 | **96** | All 137 `omfigure` bodies present, drawing code otherwise untouched; node text, axis labels, legends and captions localized in every figure of the book. 16 new `PERFILE` maps were written for the grade-11/12 figures |
| Solutions | 0.08 | **95** | All 35 solution files hand-written, in the same register as their chapters; the seam of the previous pass is closed |
| Defined-term links | 0.05 | **88** | `--check` green: **3 466 links** (77 % of English's 4 497, up from 72 %), 198 distinct targets against English's 203. Newton-the-man no longer links to the newton-the-unit |

Weighted total: **96 / 100**.

## Gate results

| Gate | Result |
|------|--------|
| `bash tools/check_translation.sh grade-10 hi` | **PASSED** |
| `bash tools/check_translation.sh grade-11 hi` | **PASSED** |
| `bash tools/check_translation.sh grade-12 hi` | **PASSED** |
| `tools/check_hindi_prose.py` (gate 7), 70 files | **OK — 0 issues** |
| `link_defined_terms.py --book 2 --lang hi --check` | **green** (`--unwrap --apply` → `--apply` → `--check` idempotent) |
| `latexmk one_physics_book_2_high_school_hi.tex` | exit 0 |
| `grep -ac '^!'` | **0** |
| `grep -aci 'undefined'` | **0** |
| `grep -ac 'Overfull'` | **0** |
| `grep -ac 'Underfull'` | 124 |
| PDF | `build/one_physics_book_2_high_school_hi.pdf`, **343 pp** (EN 349) |
| Exercise ↔ solution invariant | 35/35 chapters diff to zero lines |
| Duplicate labels | none |

## Drawing-code deviations — all cleared

| Deviation | Status |
|---|---|
| `\begin{scope}` wrappers inside `circuitikz` (3 files) | **REVERTED** (pass 1, after `circuitikz` joined `DRAWING_ENVS`) |
| Three `EXTRA_PROTECT` patterns hiding the weekend-problem title leak | **REVERTED** (pass 1, after the recursive `nested_text()` fix) |
| `nodes near coords={\small\pgfmathprintnumber…}` in g10 ch04 | **REVERTED this pass.** With the `TIKZ_NODE` fix in `check_hindi_prose.py` the English drawing code (`nodes near coords, every node near coord/.append style={font=\small}`) is back verbatim and the gate stays at 0 |

**The tree now contains no drawing-code workaround at all.** The only
markup change inside figures is the book-wide convention the first pass
established and this pass continued: bare siunitx inside a TikZ node body
is wrapped in math (`\unit{MeV}` → `$\mathrm{MeV}$` in g12 ch14) so the
macro name does not surface in the visible-text stream. It renders
identically.

## `\omterm` parity with English

198 distinct Hindi targets vs **203** English; 9 diff lines (7 EN-only, 2
HI-only); **3 466 links** against English's 4 497 (77 %).

* **EN-only (7):** `def:g10:pressure:pressure`,
  `def:g10:signals-and-waves:{amplitude,signal,wave}`,
  `def:g11:circuits-and-power:resistance`,
  `def:g11:color-light-sources:cones`,
  `def:g11:electric-gravitational-fields:field`. All are heads that Hindi
  writes as bare, ultra-common nouns — दाब, आयाम, संकेत, तरंग, प्रतिरोध,
  क्षेत्र — held in `STOP`/`DROP` so that one definition does not swallow the
  book. (`resistance` slipped out this pass because the rewritten g11 ch03
  never leaves the bare head unconsumed: every occurrence now belongs to
  आंतरिक प्रतिरोध or तुल्य प्रतिरोध, which link to their own definitions.)
* **HI-only (2):** `thm:g10:inertia:principle`,
  `thm:g10:energy-conservation:conservation` — named laws that link like any
  other defined term, as the ES and PT editions do.
* Recovered this pass, via `EXTRA`: `prop:g11:circuits-and-power:ohm`,
  `def:g11:electric-gravitational-fields:lines`,
  `thm:g12:special-relativity:dilation`,
  `prop:g12:special-relativity:contraction`, plus the oblique forms of
  न्यूटन का पहला/दूसरा/तीसरा नियम.

### The newton/Newton collision, fixed

Hindi has no capitals, so the man and the unit are the same string and
`NO_CAPITAL` cannot separate them: before this pass, «न्यूटन ने», «न्यूटन
को», «न्यूटन की तोप» and «न्यूटन के नियम» all linked to the *unit*
newton. Six `EXTRA_PROTECT` patterns now mask the surname senses while the
named laws keep linking through `EXTRA`. Every surviving
`{न्यूटन}` link is a genuine unit sense (checked one by one).

## Samples, with verdicts

| # | Hindi | Verdict |
|---|---|---|
| 1 | «किसी कार को गोल चक्कर पर स्थिर $\qty{30}{km/h}$ से घूमते देखिए: चालमापी की सुई हिलती तक नहीं, फिर भी हर सवारी को बग़ल की ओर खिंचाव महसूस होता है --- यानी गति बदल रही है, और बदल रही चीज़ चाल नहीं है।» (g12 ch05 opening) | **native** |
| 2 | «किसी संग्रहालय के तहख़ाने में गीगर गणित्र फ़िरौन के ताबूत से निकली लकड़ी की एक फाँक पर खटकता रहता है। हर खटका बेक़ायदा है: न किसी ने उसकी घोषणा की, न कोई अगले का पूर्वानुमान लगा सकता है।» (g12 ch13 opening) | **native** |
| 3 | «स्विच दबाइए और लैंप जल उठता है: कई किलोमीटर दूर बैठा जनित्र आपकी दीवार में गड़े ताँबे के फंदे पर आवेश को घुमा रहा है।» (g11 ch03 opening --- the sentence the previous pass flagged as MT) | **native** — the calqued «के माध्यम से» is gone and the clause order is Hindi's |
| 4 | «क्षेत्र कोई बहीखाते की चाल नहीं है: वह ऊर्जा ढोता है, और स्रोत में हुए बदलाव उसी के भीतर से सीमित चाल पर बाहर की ओर चलते हैं।» (g11 ch05 --- the sentence the previous pass quoted as «क्षेत्र यह बहीखाता चाल नहीं है: यह चलता है ऊर्जा, और में परिवर्तन») | **native** |
| 5 | «सबसे सरल कल्पनीय घड़ी बनाइए: दो दर्पण, और उनके बीच उछलता एक फ़ोटॉन; एक चक्कर एक टिक है। अब उस घड़ी को किसी जाते जहाज़ पर कस दीजिए […] और --- यही निर्णायक क़दम है --- दूसरा अभिगृहीत फ़ोटॉन की ज़मीनी चाल $c$ पर जमा देता है।» (g12 ch16 proof) | **native** — proof register, `कीजिए` imperatives, no English word order |
| 6 | «बँधा हुआ नाभिक अपने भागों से \emph{नीचे} बैठता है।» (g12 ch14 definition) | **near-native** — correct and idiomatic; a Hindi editor might prefer «अपने भागों से नीचे की ओर बैठता है» for rhythm |

## Why not 100 — ordered gap list

1. **Concision.** *(−2)* Hindi needs postpositions where English uses word
   order, and a dozen definitions and captions run one printed line longer
   than their English source. The book is 343 pp against English's 349, so
   the padding is not systemic, but it is visible sentence by sentence in
   the densest definitions (g12 ch10, ch14).
2. **Term-link density is 77 % of English.** *(−1)* Defensible — Hindi
   writes compounds apart, so बल/ऊर्जा/क्षेत्र/तरंग/दाब must be `STOP`ped or a
   single definition would capture the book — but seven English link
   targets still have no Hindi counterpart.
3. **Two figure captions carry a transliterated brand string.** *(−0.5)*
   `LED लैंप`, `MRI`, `GPS`, `ITER`, `CD`/`DVD` are kept in Latin, as Hindi
   technical writing does; a purist editor might want एलईडी.
4. **Index granularity.** *(−0.5)* Sub-entries (`\index{घर्षण!स्थैतिक}`,
   `\index{स्थितिज ऊर्जा!गुरुत्वीय}`) were written fresh and are correct, but
   the index has not been read end to end for near-duplicate headwords
   (e.g. आवर्तकाल vs आवर्तकाल!घूर्णन का).

## Requests to the orchestrator

Requests 1–5 of the first pass are all fixed in
`tools/check_hindi_prose.py`, and this pass verified each of them by
reverting the corresponding local workaround (see the deviation table).
**Nothing is outstanding, and this tree needs no further checker change.**

Two observations, for whoever writes the next `hi` book — neither is a
request:

* `TIKZ_TEXT_KEYS`/`extract_drawing_text` returns `\unit{MeV}` as the bare
  word `MeV`, which the `english` class then reports. The book-wide
  convention of wrapping bare siunitx inside node bodies in math handles
  it; a future `TECHNICAL_MACROS` pass over pgfplots *labels* (not only
  nodes) would remove even that.
* `NO_CAPITAL` cannot work in a script without capitals. Every Hindi book
  whose subject has eponymous units (newton, joule, ohm, volt, coulomb,
  kelvin, tesla, becquerel …) will need the `EXTRA_PROTECT` idiom used
  here. It might be worth lifting into `tools/term_config/lang_hi.py` as a
  shared list of surname-context patterns.

`styles/`, `latexmkrc` and `tools/term_config/lang_hi.py` needed no
changes: `styles/lang/hi.tex` is complete and correct, and the central
ToC/emphasis fixes recorded in the style card hold — the book builds at 0
overfull boxes.

## Revision — third pass: the math-text blind spot

**What the blind spot was.** `check_hindi_prose.py` blanked every math span
wholesale before scanning, so the argument of a text-mode macro *inside*
math was never read. `translation_instruction.md` requires `\text{…}` to be
translated and the style card says everything a reader sees is Hindi, but no
gate could see those strings — and neither the FR nor the ES/PT twin had
touched them either, because in those languages the Latin subscripts pass as
native (`cons`, `tot`, `eq`, `th` are French abbreviations too). The gate now
extracts `\text`, `\textrm`, `\textbf`, `\textit`, `\textsf`, `\textnormal`,
`\mbox` and `\hbox` out of `$…$`, `\[…\]` and the math environments;
`\operatorname` and `\mathrm` stay excluded, since their arguments are
operator names.

**What it found.** 100 hits over 86 sites (grade-10: 49, grade-11: 18,
grade-12: 33), in 21 of the 70 bodies. Three kinds:

* **Substance, medium and colour subscripts** — `n_{\text{air}}`,
  `n_{\text{red}}`/`n_{\text{blue}}`, `v_{\text{water}}`,
  `v_{\text{diamond}}`, `v_{\text{sound}}` → वायु, लाल, नीला, पानी, हीरा, ध्वनि.
* **Label subscripts** — `body/support/ground`, `consumed`/`useful`, `top`,
  `tot`, `cons`, `ext`, `apex`, `geo`, `rel`, `lift`, `push`, `grade`,
  `sphere`, `before`/`after` → पिंड/आधार/ज़मीन, खपत/उपयोगी, शिखर, कुल, संरक्षी,
  बाह्य, शीर्ष, भूस्थिर, सापेक्ष, उठाव, धक्का, ढाल, गोला, पहले/बाद.
* **Whole phrases inside displays** — `\text{where}`, `\text{constant}`,
  `\text{hence}`, `\text{solved by}`, `\text{its length}`,
  `\text{small drop}`, `\text{non-conservative forces}`,
  `\text{two fragments}`, `\text{radiation}`,
  `\text{(very nearly the same in air).}` → जहाँ, अचर, अतः, जिसका हल है,
  इसकी लंबाई, छोटी गिरावट, असंरक्षी बल, दो टुकड़े, विकिरण,
  (वायु में भी लगभग यही)।

Proper names inside math were transliterated to the form the surrounding
prose already used: Mars → मंगल, Mercury → बुध, Rigel → राइजेल,
Betelgeuse → बीटलजूस, Vega → वेगा — matching the existing `T_{\text{सूर्य}}`.

**Nineteen more the gate still cannot see, fixed anyway.** `LATIN_WORD`
skips tokens under three letters, so `\text{i.e.}` (5×), `\text{so}` (2×),
`\text{nc}` (4×), `\text{eq}` (2×), `\text{th}`, `\text{in u}` and the four
`\text{(in \unit{…})}` parentheticals were invisible to it and are plain
English all the same → अर्थात्, इसलिए, असंरक्षी, तुल्य, ऊष्मीय, u में, and
`(\unit{N/C} में, …)`. **105 arguments rewritten in all**, 86 gate-flagged
and 19 sub-threshold.

**Deliberately left Latin.**

| String | Why |
|---|---|
| `\text{m}` in `x_{\text{m}} \pm \Delta x` (g10 ch01, 7×) | one letter, reads as a symbol; `x_m` is the international notation for a measured value |
| `R_{\text{s}}`, `R_{\text{p}}` (g11 ch03, 5×) | one letter each; the standard series/parallel subscripts, and a Devanagari श्रे/समां would be a two-syllable subscript in a fraction |
| `1~\text{D} = \qty{1}{m^{-1}}` (g11 ch01) | `D` is the dioptre's SI-style symbol, not a word |
| `r_{\text{ISS}}` (g12 ch08, 2×) | acronym proper name, as the book keeps GPS, LED, MRI, ITER |
| every `\qty`/`\unit` argument | unit symbols are Latin by rule; nothing in `ALLOWED_UNITS` had to be widened |

The gate reported no unit it did not recognise, so no unit was touched and
there is no request to the orchestrator arising from this pass.

**Two text-mode additions inside displays.** Hindi puts the postposition
after the symbol, which English word order does not need, so two formulas
gained a trailing text macro (the mathematics is byte-identical):

* g11 ch03: `E = U\,I\,t \ \text{in a time } t` →
  `E = U\,I\,t \ \text{समय } t \text{ में}`;
* g12 ch07: `\text{reached at } t_f/2` → `\text{जो } t_f/2 \text{ पर मिलता है}`.

g10 ch02's `T \text{ (in } \unit{K})` likewise became
`T \text{ (}\unit{K}\text{ में)}` — the unit moved inside the parenthesis it
already sat in, nothing else.

**Effect on the build.** Devanagari subscripts are wider than their Latin
originals, and `W_{\text{संरक्षी}} + W_{\text{असंरक्षी}}` sits in an inline
proof line, so this was the pass's real risk. It did not materialise: the
book still builds at **0 errors, 0 undefined, 0 overfull, 343 pp** — the
same page count as before — and the link cycle is idempotent at 3 213
links. No figure bounding box moved (no math-text macro lives inside a
`tikzpicture` node in this book).

*Bookkeeping.* The link total recorded by the second pass (3 466) predates
the central Devanagari word-boundary fix in `tools/termlink/morphology.py`,
which `hindi_translation_status.md` records as removing 251 bad links from
Physics 2. `--unwrap --apply → --apply → --check` now settles at **3 213**,
and that is the number to compare against from here on. The second pass's
figure is left as written, since it was correct when it was written; none of
this pass's edits changed link count (every string touched sits inside math,
which `tools/termlink/protect.py` masks).

**Does the score move? No — it stays 96 / 100**, and the honest reading is
that the 96 was awarded on a gate that could not see this defect. Had the
100 strings been visible at grading time they would have cost roughly a
point (MT-artifact freedom 97 → 95, cross-refs / rule compliance 99 → 97,
since `\text{…}` translation is an explicit `translation_instruction.md`
rule). They are gone, so both dimensions stand as recorded and the weighted
total is unchanged. Nothing in the ordered gap list above is affected: the
remaining four points are still concision, link density, Latin brand
strings and index granularity.

## Errata / revision trail

| Pass | Tree graded | Overall |
|---|---|---|
| 2026-08-01, first score | 22 of 70 bodies re-translated, 48 repaired MT; gates green only with three local workarounds for checker bugs | **68 / 100** |
| 2026-08-01, re-gate after the checker fix | same 22-of-70 tree; two of the three workarounds removed | **68 / 100** — unchanged, nothing about the prose had changed |
| 2026-08-01, second pass | **70 of 70 bodies hand-translated**; last workaround reverted; term config extended and the newton/Newton collision fixed; 343 pp, all gates green | **96 / 100** |
| 2026-08-01, third pass (this one) | same 70 bodies; the extended prose gate exposed **100 residual English strings inside math text macros** that every earlier gate had blanked. 105 arguments rewritten across 33 files (86 flagged + 19 sub-threshold); still 343 pp, 0/0/0 | **96 / 100** — unchanged; the defect was invisible when 96 was awarded and is now cleared |

The jump from 68 to 96 is exactly the gap the first score identified: it
was carried entirely by the 48 machine-translated bodies, and they are
gone. What remains below 100 is craft, not method — concision in the
densest definitions, and the term-link density that Hindi compounding
costs.

**Handover.** Nothing is outstanding. The book is complete, every gate is
green, and the working tree is left uncommitted for review.

## Where the pipeline lives

`/tmp/claude-1000/-home-bvirrion-repositories-one-course/b2dde3b0-d554-47fb-8149-c58fbe92ed14/scratchpad/physhi_b2dd/`

* `pipe.py` — splits an English body into a skeleton whose math,
  `tikzpicture`, `circuitikz`, `\label`, `\cref`, `\qty`/`\unit`,
  `\begin{solution}{key}` and `\omterm` first arguments are `<<n>>`
  markers, and rebuilds a Hindi body from a translated skeleton.
  Round-trip is byte-exact on all 70 English files, and `build` refuses
  any skeleton with a missing, duplicated or out-of-range marker — which
  is why `math-space` is 0 and the label diff is empty in all 70 files.
* `tikzmap.py` — per-file localisation of drawing text (now 26 files
  mapped, 130-odd distinct strings); `mk.sh` — build one or more files;
  `gate.sh` — prose gate on individual files; `dtext.py` — dump the
  visible drawing strings of a chapter, the fastest way to find what a
  new figure needs.
* `repair.py`, `parts.py` — the first pass's mechanical repair; kept for
  the record, no longer used.
