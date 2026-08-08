# Translation score — Physics Book 2 · Arabic (`ar`)

| Field | Value |
|-------|--------|
| **Book** | One Physics Book 2 (High School, grades 10–12) |
| **Language** | Arabic (`ar`), Modern Standard Arabic per `arabic_style_card.md` |
| **Quality bar** | **native academic** (EN is the source of truth; the FR twin was used as a sense/structure reference only) |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met.** |
| **Date** | 2026-08-08 (single pass, written from the English canon) |
| **Scope** | **All 70 bodies hand-written in Arabic** — 35 chapters + 35 solution files, grades 10–12. No machine-translated body was ever committed: every file was produced from a marker skeleton of its English original and the prose written fresh around the markers. Plus 190 figure-text localisations and a curated `tools/term_config/book2_ar.py` |

## Read this first

The Hindi edition of this book scored 68 on a first machine-translated
pass and needed a full re-translation. That failure mode was designed out
here rather than repaired afterwards: **nothing was ever machine
translated.** A throwaway pipeline (`pipe.py`, in the scratchpad, never in
the repo) splits an English body into a skeleton in which every span the
instructions forbid touching — math, `tikzpicture`/`circuitikz`,
`\label`, `\cref`/`\ref`, `\qty`/`\unit`, `\begin{solution}{key}`, every
other technical macro, and the *first* argument of `\omterm` — is a
numbered `<<n>>` marker, and it **refuses to emit a file unless every
marker of the skeleton reappears exactly once**. The Arabic was then
written by hand around those markers, chapter by chapter, in the register
the style card fixes.

Round-trip was verified before a word was translated: `pipe.py rt` rebuilds
all 70 English bodies byte-for-byte. That is why the `math-space` and
`split-number` prose classes are 0 everywhere and why the label diff is
empty in all 70 files — the mathematics is byte-identical to English by
construction, not by inspection.

| Part of the book | Files | State |
|---|---:|---|
| grade-10, ch01–ch09 + solutions | 18 | Hand-translated |
| grade-11, ch01–ch10 + solutions | 20 | Hand-translated |
| grade-12, ch01–ch16 + solutions | 32 | Hand-translated |

## Dimension scores

| Dimension | Weight | Score /100 | Notes |
|-----------|-------:|----------:|--------|
| Register / tone | 0.20 | **96** | One school-textbook register across all 70 files: plural-of-respect imperatives (احسُب، لاحِظ، بيّن، استنتج، قدّر)، `فـ`/`ومن ثم`/`أما … فـ` connectives instead of English clause order, and chapter openings written as openings rather than as translated first sentences («في قبو متحف، يطقطق عدّاد غايغر فوق شظية خشب من تابوت فرعون»). Proofs keep the imperative-plus-consequence rhythm of the English; solutions keep the terse numbered voice |
| Terminology | 0.18 | **96** | Style-card glossary throughout and consistent across 35 chapters: متجهة (never شعاع) for vector, الشدّ for rope tension against التوتر for voltage, المرجع العُطالي، كمية الحركة، مبرهنة الطاقة الحركية/الميكانيكية، النقص الكتلي، طاقة الربط لكل نوكليون، الكتلة الحرجة، المهدِّئ، حاجز كولوم، كمون الإيقاف، شغل الخروج، مستويات الطاقة، طول موجة دي بروي، تمدد الزمن، تقلص الأطوال، الزمن الذاتي، ثابت التفكك، شبه الدور، الرنين. Index keys were written with the visible Arabic term |
| MT-artifact freedom | 0.17 | **99** | No machine output anywhere: every body was composed, not post-edited. Arabic prose gate 0 issues over 70 files (all nine classes). No English word order survives; no transliterated calques |
| Structural fidelity | 0.10 | **100** | 70 files, byte-identical label sets in every chapter, exercise↔solution key parity in 35/35, identical environment and figure census (137 `omfigure`, 155 drawing environments). All three `check_translation.sh` runs **PASSED**; zero duplicate labels |
| LaTeX hygiene | 0.08 | **100** | 0 errors, 0 undefined, **0 overfull**, 122 underfull, 331 pp. UTF-8 throughout, no TeX accent escapes, no tatweel, no presentation forms, no bidi control characters |
| Cross-refs / rule compliance | 0.07 | **100** | `\label`, `\cref`/`\ref` targets, `\begin{solution}{key}` and every `\omterm` first argument byte-identical to English. ASCII digits in prose and mathematics. `\qty`/`\unit` arguments untouched. Zero country, board or curriculum names |
| Figures | 0.07 | **97** | All 137 figure bodies present with drawing code byte-for-byte preserved; only the *text* inside them was localized — 190 replacements over 31 files (node labels, axis labels, legends, in-figure annotations) plus every caption. Two `\text{…}` strings inside math (`i.e.`, `top`) were localized book-wide by the same mechanism |
| Solutions | 0.08 | **96** | All 35 solution files hand-written in the same register as their chapters, including the ~20-question weekend-problem answers; the numbered-answer voice is uniform from grade 10 to grade 12 |
| Defined-term links | 0.05 | **94** | `--check` green and idempotent: **4 351 links** (97 % of English's 4 497) across **203 distinct targets — exactly English's 203**. `book2_ar.py` was curated from a seed: 2 `STOP`, 8 `DROP`, 44 `EXTRA_PROTECT` patterns, 13 `EXTRA` entries |

Weighted total: **96 / 100**.

## Gate results

| Gate | Result |
|------|--------|
| `bash tools/check_translation.sh grade-10 ar` | **PASSED** |
| `bash tools/check_translation.sh grade-11 ar` | **PASSED** |
| `bash tools/check_translation.sh grade-12 ar` | **PASSED** |
| `tools/check_arabic_prose.py`, 70 files | **OK — 0 issues** (english 0, translit 0, punct 0, digits 0, math-space 0, bidi-ctrl 0, presform 0, tatweel 0, split-number 0) |
| `link_defined_terms.py --book 2 --lang ar --check` | **green** (`--unwrap --apply` → `--apply` → `--check` idempotent) |
| `latexmk one_physics_book_2_high_school_ar.tex` | exit 0 |
| `grep -ac '^!'` | **0** |
| `grep -aci 'undefined'` | **0** |
| `grep -ac 'Overfull'` | **0** |
| `grep -ac 'Underfull'` | 122 |
| PDF | `build/one_physics_book_2_high_school_ar.pdf`, **331 pp** (EN 349) |
| Exercise ↔ solution invariant | 35/35 chapters diff to zero lines |
| Duplicate labels | none |

The ~95 `Missing character … nullfont` lines are the known pre-existing
quirk of this entry file and are not caused by the translation.

## Drawing code: no deviations

Not one byte of TikZ/pgfplots/circuitikz drawing code was changed. The
whole drawing environment is a single marker in the skeleton, so it is
restored verbatim; localisation happens afterwards, in a separate pass
that replaces *whole braced groups* of visible text (`{white light}` →
`{ضوء أبيض}`) and only inside a drawing environment. 190 such replacements
across 31 files; every remaining string the prose gate can see inside a
figure is Arabic, a unit symbol or a single-letter variable.

The one book-wide convention: two `\text{…}` arguments that live inside
math rather than inside a node — `\text{i.e.}` and `\text{top}` — were
translated to `\text{أي}` and `\text{القمة}` so that no reader-visible
English survives in a formula. The mathematics around them is unchanged.

## `\omterm` parity with English

**203 distinct targets, the same count as English**, 4 351 links against
English's 4 497 (97 %). The label sets differ by six each way:

* **EN-only (6):** `def:g11:magnetic-fields:earth`,
  `def:g12:light-as-wave:lightwave`, `def:g12:radioactive-decay:lambda`,
  `def:g12:work-and-energy:ep`, `prop:g10:relative-motion:relativity`,
  `thm:g12:kinematics-2d:centripetal`. Four of these (declination, decay
  constant, centripetal acceleration, wavelength in vacuum) occur in the
  Arabic exactly once, inside their own definition, which the linker
  correctly refuses to self-link; English repeats the phrase in later
  prose and Arabic uses a pronoun or the short form. `…:ep` loses to
  `def:g11:mechanical-energy:potential` under `AMBIG_POLICY =
  "nearest-preceding"`, which is the intended spiral behaviour.
* **AR-only (6):** `def:g12:nuclear-energy:units`,
  `ex:g10:signals-and-waves:ecg`,
  `prop:g12:oscillators-and-time:pendulum-period`,
  `prop:g12:sound-acoustics:speed`,
  `thm:g10:energy-conservation:conservation`,
  `thm:g12:satellites-kepler:kepler` — named results that link like any
  other defined term, as the ES and PT editions do.

### What the curation had to fix

Arabic has no capitals, so `NO_CAPITAL` is structurally inert and the
physicist cannot be told from his unit by shape. It also glues the article
and the one-letter particles to the front of a word, so a short term
matches in more places than it should. Four families of wrong-sense links
were found by reading every context of every high-frequency short term,
and all four are now closed:

| Trap | Wrong links before | Fix |
|---|---:|---|
| **نيوتن** — the man vs the newton | 24 of 26 | 21 `EXTRA_PROTECT` patterns for the surname senses (مدفع نيوتن، رمية نيوتن، اختبار نيوتن، وذكرها نيوتن …) and three `EXTRA` entries so قانون نيوتن الأول/الثاني/الثالث link to the *theorems* instead. Every surviving `{نيوتن}` link is the unit, checked one by one. Same treatment for ضياع/مفعول جول، قانون/تنافر/حاجز كولوم، قانون أوم |
| **قلب / غلاف** — fibre core and cladding | 15 + 12 | `STOP`ped, so they still link inside the refraction chapter that defines them and never again: Arabic قلب is also the heart (the ECG problem, the cardiologist of the Doppler chapter), an electromagnet's iron core and the Sun's core; غلاف is the atmosphere and the exponential envelope of a damped oscillation |
| **السعة** — capacitance vs amplitude | 6 | Both are السعة in Arabic and they are defined in different chapters; six `EXTRA_PROTECT` phrases keep the RC/RLC capacitance sense from linking to the grade-10 amplitude definition |
| **العمودي / النسبي / السكون** — words harvested from a definition that merely uses them | ~90 | `DROP`ped, mirroring the English config's `vertical`, `absolute` and `at rest`. "released from rest" must not link to a definition of a reference frame |

Six ambiguous words were additionally disambiguated in the *prose* rather
than in the config, because the Arabic read better afterwards anyway:
مجال (physics field vs time interval) → فترة for intervals; دور (period vs
role) → وظيفة for the role sense.

## Samples, with verdicts

| # | Arabic | Verdict |
|---|---|---|
| 1 | «في قبو متحف، يطقطق عدّاد غايغر فوق شظية خشب من تابوت فرعون. وكل طقطقة بلا قانون: فلا شيء أعلن عنها، ولا شيء يتنبأ بالتالية. ومع ذلك سيطبع المختبر يوم الجمعة تاريخًا مضبوطًا إلى قرن.» (g12 ch13 opening) | **native** |
| 2 | «يحمل كل تابع GPS ساعة ذرّية مضبوطة إلى ثانية واحدة في ثلاثة ملايين سنة --- وقبل الإطلاق يزيح المهندسون ضبطها عمدًا: فلو تُركت أمينة لكسبت ثمانية وثلاثين جزءًا من مليون من الثانية في اليوم.» (g12 ch16 opening) | **native** — the `فلو … لـ` conditional is Arabic's, not a rendering of "left honest, it would" |
| 3 | «ابنِ أبسط ساعة يمكن تصورها: مرآتان متقابلتان تفصل بينهما مسافة $L$، وفوتون يرتدّ بينهما؛ فالرحلة الكاملة الواحدة دقّة واحدة […] ثم --- وهي الخطوة الحاسمة --- تثبّت المسلَّمة الثانية سرعة الفوتون على الأرض عند $c$.» (g12 ch16, light-clock proof) | **native** — proof register, imperative opening, no English clause order |
| 4 | «اضغط مصراع آلة تصوير إلى منتصفه: فيرتفع أزيز رفيع ثانيتين، ويضيء ضوء أخضر --- وعندئذٍ فقط ينطلق الوماض، فيفرغ في ميلي ثانية واحدة ما أمضى ثانيتين في جمعه.» (g12 ch11 opening) | **native** |
| 5 | «زِن نواة $^A_Z\mathrm{X}$، ثم زِن بروتوناتها $Z$ ونيوتروناتها $A-Z$ على حدة: فالأجزاء \emph{أثقل} من الكل.» (g12 ch14, mass-defect definition) | **near-native** — correct and idiomatic; an Arabic editor might prefer «كلٌّ على حدة» for rhythm |
| 6 | «فالحديد أشدّ الأنوية ارتباطًا في الطبيعة. ويحرّر التفاعل طاقةً بالضبط حين تجلس نواتجه \emph{أعلى} على المنحني؛ ومن ثم تربح استراتيجيتان متعاكستان كلتاهما، وتمشيان معًا نحو الحديد.» (g12 ch14) | **near-native** — «تجلس … على المنحني» is a deliberate calque of the English image the chapter builds on; a purist would write «تقع» |

No sampled passage reads as machine translation.

## Why not 100 — ordered gap list

1. **Concision in the densest definitions.** *(−2)* Arabic needs an
   explicit noun where English uses a bare particle before a symbol —
   writing `بـ$x$` would emit a tatweel, which the gate rejects — so a
   dozen definitions and proof lines carry a filler noun (بالمقدار،
   بالعلاقة، بعامل) that the English does not have. It is correct and
   idiomatic, but it is four syllables the English never spends. The book
   is 331 pp against English's 349, so this is not systemic padding; it is
   visible sentence by sentence in the RC/RLC and work–energy chapters.
2. **Term-link density is 97 % of English, not 100 %.** *(−1)* Six English
   targets have no Arabic counterpart (listed above). Four of them exist
   only because English repeats a phrase that Arabic pronominalises; two
   are policy decisions (`nearest-preceding`), not defects. Closing them
   would mean rewriting idiomatic Arabic to create a link.
3. **Latin brand and acronym strings kept as-is.** *(−0.5)* GPS, ITER,
   LED, FM, RC, RL, LC, RLC, D–T, AA are left in Latin, as Arabic
   technical writing does; a purist editor might want جي بي إس. They also
   force a bidi seam in Arabic paragraphs, which reads fine but is not
   invisible.
4. **Index granularity.** *(−0.5)* Sub-entries (`\index{طاقة كامنة!مرنة}`,
   `\index{شبه الدور!الكهربائي}`) were written fresh and are correct, but
   the index has not been read end to end for near-duplicate headwords
   (دور ذاتي vs الدور الذاتي, تواتر vs التواتر الذاتي).

## Requests to the orchestrator

**Nothing is outstanding.** No orchestrator-owned file needed a change:
`styles/lang/ar.tex` is complete, the central RTL work recorded in
`arabic_style_card.md` §6 holds (the book builds at 0 overfull boxes and
331 pp), `tools/check_arabic_prose.py` caught exactly the classes it
claims to and never produced a false positive that forced a workaround,
and `tools/termlink/` needed no patch. The tree contains **no workaround
of any kind** — no local checker exception, no drawing-code edit, no
`EXTRA_PROTECT` pattern that exists to hide a tool bug rather than a
genuine sense collision.

Two observations for whoever writes the next `ar` book — neither is a
request:

* **`NO_CAPITAL` cannot work in a caseless script**, exactly as the seed's
  docstring warns. Every Arabic subject with eponymous units (نيوتن، جول،
  واط، باسكال، كلفن، تسلا، هرتز، كولوم، فولط، أمبير، أوم، بيكريل، هنري،
  فاراد) will need the `EXTRA_PROTECT` idiom used here. Since the
  surname contexts are the same everywhere (قانون X، مبرهنة X، تجربة X،
  مفعول X، حاجز X، مدفع X …), a shared list of *context templates* in
  `tools/term_config/lang_ar.py` would let each book name only its
  eponyms instead of writing twenty patterns by hand.
* **`EXTRA_PROTECT` patterns must use `\s+`, never a literal space.**
  Half of my first batch silently failed because the phrase happened to
  straddle a line break in the source. A one-line note in the seed
  docstring, or a `\s+`-normalisation inside `protect.py`, would save the
  next agent the same hour.

## Where the pipeline lives

`/tmp/claude-1000/-home-bvirrion-repositories-one-course/ed28ae7f-29b3-485a-bca9-208daeaa4108/scratchpad/ar/`

* `pipe.py` — `strip` an English body to a `<<n>>`-marker skeleton,
  `build` an Arabic body from a translated skeleton, `rt` self-test.
  Round-trip is byte-exact on all 70 English files; `build` refuses any
  skeleton with a missing, duplicated or out-of-range marker.
* `mkall.py` — rebuild every translated skeleton into `parts/**/ar/`.
* `tikzmap.py` — per-file map of visible drawing strings (31 files, ~180
  distinct strings), applied only inside drawing environments, plus the
  two book-wide `\text{…}` replacements.
* `dtext.py` — dump the visible drawing strings of a chapter using the
  gate's own extractors; the fastest way to see what a figure still needs.
* `ctx.py` — print every context of a given linked display, the tool the
  term-config curation was done with.
* `sk/`, `tr/` — the English skeletons and their Arabic counterparts.

**Handover.** The book is complete, all gates are green, and the working
tree is left uncommitted for review. No git commit was created.
