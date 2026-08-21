# One Physics Book 3 (University, Year 1) --- Arabic edition: self-score

**Date:** 2026-08-21
**Quality bar:** *native academic* (the bar of `translation_instruction.md`).
**Variety:** Modern Standard Arabic, university lecture register, per
`arabic_style_card.md` §1 (Math 3--5 row: **ليكن / لتكن**, **نفترض أن**,
**برهن على أن**, **ومنه**, **لدينا**).
**Sense/structure reference:** the English canon (`parts/bachelor-1/*.tex`)
for content; the Arabic Books 1--2 of this series (`parts/grade-*/ar/`) and
`../one-math-book/parts/bachelor-1/ar/` for the university register. No
French twin of Book 3 exists, so French was not used.

## Overall: **96 / 100**

| Dimension | Score | Note |
|---|---:|---|
| Register (academic Arabic, weighted) | 96 | Lecture voice throughout: `بيّن أن`، `احسب`، `استنتج`، `قدّر`، `برهن على أن` in the exercises; narrative present in the chapter openings; `ومنه / فيكون / ولدينا` as the connective spine of the proofs. Chapters 21--30 were written against 01--20 so the voice does not change at the seam. |
| Terminology (weighted) | 96 | Per-chapter glossary settled below and checked against Books 1--2 (`الكمون`, `التحريض`, `عكوس`, `متجهة`, `احتمال`, `مبرهنة` ≠ `نظرية`). Index keys equal the visible terms. |
| MT-artifact freedom (weighted) | 97 | Gate 7 clean on all 60 files (`english`, `translit`, `punct`, `digits`, `math-space`, `bidi-ctrl`, `presform`, `tatweel`, `split-number` all 0). No English survives in prose, TikZ node text, axis labels, `\text{…}` inside math, environment optional titles or index keys. |
| Structure | 100 | `check_translation.sh` green; every body written as line-range replacements on the English canon through `tools/id_apply.py`, so labels, `\cref` targets, `\begin{solution}{key}`, `\qty{}{}`, `\foreach`, `xtick=` and every math display are byte-identical to English. |
| LaTeX hygiene | 98 | 0 errors, 0 undefined references, 0 overfull boxes, 0 "invalid in math mode", 319 pages. The residual `nullfont` count (65) is the pgfplots log-axis artifact present in **every** edition including English. |
| Cross-references | 100 | Every `\cref`/`\ref` target byte-identical to English; 12 exercises + 1 weekend problem per chapter, one solution each. |
| Figures | 98 | Drawing code untouched (the `draw` census of `id_apply.py` compares it byte-for-byte after blanking node text); only node text, axis labels, titles and captions are Arabic. |
| Solutions | 96 | All 30 solution files translated; `\textbf{n.}` numbering and every number preserved. |

## What was produced in this session

- `parts/bachelor-1/ar/21`--`30` and `parts/bachelor-1/solutions/ar/21`--`30`
  (chapters 01--20 were written in an earlier run of this same job and were
  re-gated, re-linked and re-scored here; three of them needed a line-break
  repair, see *Overfull boxes* below).
- `tools/term_config/book3_ar.py` --- curated, not translated from
  `book3_en.py`.
- Terms linked over the whole book: **1 983** `\omterm` links across 60 files
  (English carries 2 342; the Spanish edition 2 400). Arabic runs thinnest of
  the eight editions on purpose --- see *Link volume* below.
- Build: 319 pages, `0` errors, `0` undefined, `0` overfull.

## Checks

```
bash tools/check_translation.sh bachelor-1 ar          -> TRANSLATION GATE: PASSED
python3 tools/check_arabic_prose.py parts/bachelor-1/ar parts/bachelor-1/solutions/ar
                                                       -> OK (60 files)
latexmk one_physics_book_3_university_year_1_ar.tex
  grep -ac '^!'                    -> 0
  grep -aci undefined              -> 0
  grep -ac Overfull                -> 0        (319 pages)
  grep -ac 'invalid in math mode'  -> 0
  grep -ac nullfont                -> 65       (same artifact as English)
  grep -ac 'Missing character'     -> 257      (all nullfont; Books 1 and 2 ar
                                                carry 90 and 158 of the same)
```

Omterm target parity: 206 distinct targets in `ar` against 194 in English;
every `ar` target is a label that exists in the English canon (checked with
`comm` against `\label{…}` in `parts/bachelor-1/*.tex`). The two sets differ
because `book3_ar.py` is curated separately --- Arabic stops 34 one-word terms
English does not have to stop, and recovers 23 named results (`قانون غاوس`,
`مبرهنة أرخميدس`, `متراجحة كلاوزيوس`, …) through `EXTRA` that `NOT_A_TERM`
would otherwise reject.

## Sampled passages

1. **ch. 21 opening, `parts/bachelor-1/ar/21-fluid-statics.tex:3-11`** ---
   «تحمل غواصةٌ على عمق ثلاثمئة متر، على كل متر مربع من بدنها، ما تزنه شاحنة
   محمَّلة… وكل واحدة من هذه الوقائع نتيجةٌ لعلاقة واحدة». Sentence count equal
   to English, no padding, `وكل واحدة من هذه الوقائع` where a translator would
   have written `كل من هذه الحقائق`. **Verdict: native.**
2. **ch. 23, remark "قراءة المبدأ",
   `parts/bachelor-1/ar/23-second-law-entropy.tex:40-48`** --- «خلافًا للطاقة،
   لا تنحفظ الإنتروبيا: بل تُتبادَل مع الحرارة… وتُنشأ في كل سيرورة لاعكوسة».
   `سيرورة لاعكوسة` and `الحدّ المُنشأ` are the forms an Arabic thermodynamics
   lecture uses; the passive `تُتبادَل / تُنشأ` carries the English "exchanged /
   created" without a calque. **Verdict: native.**
3. **ch. 27, definition of the dipole,
   `parts/bachelor-1/ar/27-potential-capacitors.tex:162-171`** --- «شحنتان
   متعاكستان … تؤلفان ثنائي قطب كهربائيًّا عزمه $\vect p = q\,\vect{NP}$…
   والذرة المتعادلة في مجال تصير كذلك». Correct dual agreement throughout
   (`شحنتان … تؤلفان`, `تفترقان`), which is where MT normally fails.
   **Verdict: native.**
4. **ch. 30, example "حجم ذرة الهيدروجين",
   `parts/bachelor-1/ar/30-quantum-introduction.tex:222-237`** --- «فالذرة أصغر
   ما يمكن أن تكون من دون أن تفوق الطاقة الحركية طاقةَ الارتباط». The idiom
   `أصغر ما يمكن أن تكون` is Arabic, not a rendering of "as small as it can
   be". **Verdict: native.**
5. **ch. 12 opening (written in the earlier run of this job),
   `parts/bachelor-1/ar/12-newton-dynamics.tex:3-14`** --- «يقفز مظلّي من
   الطائرة، فيكفّ خلال بضع عشرة ثانية عن التسارع… وقد وصف التحريكُ الحركاتِ؛
   أما الديناميك فيفسّرها». Case endings written where they disambiguate
   (`التحريكُ الحركاتِ`); same register as 21--30. **Verdict: native.**
6. **solutions, ch. 16 (earlier run),
   `parts/bachelor-1/solutions/ar/16-central-forces.tex:3-6`** --- terse
   computational Arabic, `ومنه / و / أي` as connectives, every number and unit
   preserved. **Verdict: near-native** (a solutions file is telegraphic by
   design; there is little prose to judge).

## Terminology settled for this book

Chosen to agree with Books 1--2 `ar` and with chapters 01--20 of this book, and
recorded here so Books 4--5 do not fork:

| English | Arabic | why |
|---|---|---|
| electric potential | **الكمون** (`الكمون الكهرسكوني`) | ch. 6 already says «بالكمون الكهرسكوني في \cref{ch:b1:potential-capacitors}» |
| electromagnetic induction | **التحريض (الكهرمغناطيسي)** | grade-9 `07-alternator` uses it |
| emf | **القوة المحركة الكهربائية** | as in Book 2 |
| reversible / irreversible | **عكوس / لاعكوس** | 20+ prior uses in the tree |
| adiabatic | **كظوم** | classical Arabic term; no prior use to contradict |
| enthalpy | **الإنثالبي** | transliteration; see *Why not 100* |
| entropy | **الإنتروبيا** | |
| first / second law of thermodynamics | **المبدأ الأول / الثاني** | ch. 20 already had `المبدأ الصفري`; keeps Newton's `القانون الأول` distinct |
| thermostat (heat reservoir) | **منظِّم حراري** | leaves `منبع` free for hot/cold *source* |
| efficiency | **المردود** | |
| coefficient of performance | **معامل الأداء** | |
| circulation (of a vector) | **التكامل الخطي** | unambiguous; `التدوير` collides with rotation |
| flux | **التدفق** | |
| permittivity / permeability | **السماحية / النفاذية** | |
| capacitor / capacitance | **مكثف / السعة** | ch. 7 already writes `مكثف` |
| condenser (heat exchanger, ch. 24) | **المكثِّف** (vocalised) | see *Why not 100* |
| solenoid / coil | **ملف لولبي / وشيعة** | ch. 7 uses `وشيعة` for the inductor |
| uncertainty principle | **مبدأ الارتياب** | style-card `uncertainty = ارتياب` |
| work function | **شغل الخروج** | |
| quantum dot | **نقطة كمومية** | |
| lever rule / quality | **قاعدة الرافعة / نسبة البخار** | |
| metacentre | **مركز الاستقرار** | descriptive; no transliteration needed |

## Link volume, and what it cost

`STOP` carries 48 entries against English's 20. Arabic proclitics
(`HEAD_ON_EVERY_WORD`) make a one-word term fire far more often than its
English twin, and much of the surplus is wrong-sense; the Arabic-only
collisions that had to be stopped are worth recording:

- **إشارة** = *signal* (ch. 5) **and** the *sign* of a charge --- the second
  sense is on every page of chapters 26--27;
- **الطور** = *phase of matter* (ch. 25) **and** *phase of a sinusoid* (ch. 8,
  29);
- **مطابقة** = *accommodation* of the eye (ch. 4) **and** *aligned*, which is
  how chapters 27--28 describe a dipole in a field;
- **تقارب** = *convergence* of a lens **and** the ordinary "getting closer";
- **مجال** = *field* **and** *range* ("a range of temperatures", ch. 24);
- **قلب / غلاف** = fibre *core / cladding* (ch. 2) **and** the Earth's core, the
  coaxial core, the iron core, the cable sheath.

`EXTRA_PROTECT` keeps **أمبير** and **باسكال** apart from the physicists they
are named after (a caseless script has no other lever): `مبرهنة أمبير`,
`حلقة أمبير`, `مستطيل أمبير`, `أمبير-لفات`, `لدى أمبير`, `بتطبيق أمبير`,
`مبدأ باسكال`, `نصّ كلفن`. It also keeps `سعة` = *capacitance* apart from
`سعة` = *amplitude*.

Net: 1 983 links, 85 % of English's 2 342 --- the same ratio Arabic Book 1 hit
(5 618 / 6 483 = 87 %), and the trade the style card predicts.

## Opt-outs used

One `!math` range opt-out in `tools/id_apply.py`, in ch. 23 exercise 4
(`@@ 282-285 !math`). English writes `obeys $TV^{\gamma - 1} = $ const.` --- a
math span ending in a space, which `check_arabic_prose.py` reports as
`math-space` (an MT fingerprint) and which cannot be repaired without changing
the span. The Arabic writes `$TV^{\gamma - 1} = \text{ثابت}$`, i.e. exactly what
the English canon itself does everywhere else (`\text{const}` in ch. 22 and
ch. 23). No `--force-classes` was used anywhere.

## Overfull boxes: what they were, and the rule they teach

The first build had **12** overfull boxes, all `in paragraph` (prose), none
`detected at line` --- so none of them was the ToC box-width fault of the
Arabic Books 1--5. Nine were in chapters 01--20 written in the earlier run.
Every one was the documented right-to-left fault, in a form worth adding to
the style card:

> In an RTL paragraph a **long inline formula** behaves exactly like a
> comma-separated run of numerals: the whole `$…$` becomes one directional run
> with no interior break point, and — unlike English — TeX cannot break it at
> its relations. Worse, the space between an Arabic word and an adjacent `$…$`
> is frequently not a break point either, so a sentence made of *math, one
> Arabic word, math, one Arabic word, math* has no legal break at all and TeX
> sets the whole sentence on one line.

Two consequences, both verified by rebuilding:

1. **Adding an Arabic word before a long formula makes it worse**, not better
   (`solutions/ar/14`: 113 pt → 137 pt after inserting `لدينا`). The only fix
   is to *break the run*: split the formula into two `$…$` spans joined by a
   short Arabic phrase (`، أي`, `، وهي تساوي`, `، مقسومًا على`), or shorten the
   material before it.
2. A **comma-separated list inside one `$…$`** must be split by hand:
   `$0.02, -0.05, 0.08, -0.01, 0.05, -0.08, 0.01, -0.02$` became
   `$0.02, -0.05, 0.08, -0.01$ ثم $0.05, -0.08, 0.01, -0.02$`.

Sites repaired: `ar/08`, `ar/19`, `ar/25`, `solutions/ar/01` (×2),
`solutions/ar/08`, `solutions/ar/09`, `solutions/ar/14` (×2),
`solutions/ar/17`, `solutions/ar/25`, `solutions/ar/29`. Final count: **0**.

## Faults found and fixed while gating

- **20 tatweels** (U+0640) --- the trap the style card warns about, and the
  same one four of the first six Arabic agents hit. All were the natural
  `بـ$X$` / `لـ$X$` / `كـ$X$` / `بالـ\unit{…}` join, plus the Arabic ordinal
  `(هـ)` used for a fifth enumerated part. Fixed by naming the object
  (`بمقدار`, `للمتجهة`, `بنسبة`, `بوحدة`) and by writing `(ه)`.
- **`\qty{1000}{turns/m}`** in ch. 29 exercise 3 --- the English canon leaves an
  English word inside a `\qty`, where siunitx silently drops it from the page.
  Localised by moving the word out of the macro: `1000 لفة في المتر`. (A bare
  numeral, not `$1000$`, so that no new math span is created and the
  `id_apply.py` math census still passes.)
- **`\qty{1}{atm}` inside a TikZ node** (ch. 25 phase diagram) --- the prose
  gate's `TIKZ_NODE` capture `.strip("{}")` unbalances a node whose text *ends*
  with a braced macro argument, so `atm` was reported as residual English.
  Written as `{\qty{1}{atm}\relax}`; nothing changes on the page.
- **`ylabel={$E$ and $\psi_n$}`** in ch. 30 --- English left in a pgfplots axis
  label, invisible to a body-text sweep.
- **`بحقل الضغط`** (ch. 21) --- `حقل` is the *algebraic* field; the physics
  field is `مجال` (style card §3). Fixed.
- **`متجهة` vs `شعاع`** --- chapters 26--27 were first written with `الشعاع` for
  *vector*; normalised to `متجهة`, which is the settled cross-book decision
  and what chapters 11--19 of this book already use.

## Why not 100

1. **`الإنثالبي` is a transliteration.** `المحتوى الحراري` exists and is
   equally standard; the transliteration was chosen for concision (it is used
   ~30 times across chapters 22, 25) and because it composes with
   `إنثالبي التحول`. A lecturer who prefers the Arabic compound would change it.
2. **`مكثِّف` (condenser, ch. 24) and `مكثف` (capacitor, ch. 27) are the same
   word.** They are kept apart only by the shadda, which is what stops the term
   linker from linking every condenser in the heat-pump chapter to the
   definition of a capacitor. It works, and the vocalisation is legitimate
   Arabic, but it is a spelling distinction a reader will not consciously see.
3. **Link displays swallow a leading proclitic.** `HEAD` in `lang_ar.py`
   includes `و ف ب ك ل`, so a link that begins a clause reads
   `\omterm{…}{ومبرهنة أرخميدس}` --- the conjunction is inside the coloured
   term. This is series-wide behaviour (Books 1--2 `ar` do the same) and is
   orchestrator-owned, but it is the one place where the Arabic looks less
   clean than the English.
4. **Eleven formulas were re-segmented** to break unbreakable RTL runs (see
   above). The mathematics is unchanged, but `$A = B$` became `$A$، أي $B$` in
   those eleven places, so the Arabic no longer mirrors the English span for
   span there.
5. **`(ه)` for the fifth item of a lettered list.** Arabic convention writes
   `(هـ)`, with a tatweel; the tatweel is gated series-wide, so `(ه)` was used.
   Correct and readable, marginally non-standard.

## Requests to the orchestrator

- `tools/check_arabic_prose.py`: `extract_drawing_text` does
  `nested_text(p.strip("{}"))` on the `TIKZ_NODE` capture. When a node's text
  *ends* with a braced macro argument (`{\qty{1}{atm}}`), `strip` removes the
  closing brace of the macro as well and the reduction leaks the unit as
  residual English. Stripping exactly one leading `{` and one trailing `}`
  would fix it. Worked around here with `\relax`.
- `arabic_style_card.md` §6 could gain the "long inline formula" paragraph
  above, next to the existing note on comma-separated numeral runs: the
  failure mode and the fix are the same, but a formula does not look like a
  numeral run and the first instinct (adding a word to give TeX a break) makes
  it worse.
