# One Physics Book 4 (University, Year 2) --- Arabic edition: self-score

**Date:** 2026-08-22
**Quality bar:** *native academic* (the bar of `translation_instruction.md`).
**Variety:** Modern Standard Arabic, university lecture register, per
`arabic_style_card.md` §1 --- the same voice as Book 3 `ar`
(**ليكن / لتكن**, **نفترض أن**, **برهن على أن**, **ومنه**, **لدينا**).
**Sense/structure reference:** the English canon (`parts/bachelor-2/*.tex`)
for content; `parts/bachelor-1/ar/` (Book 3) and `parts/grade-*/ar/` for the
settled register and terminology. No French twin of Book 4 exists.

## Overall: **96 / 100**

| Dimension | Score | Note |
|---|---:|---|
| Register (academic Arabic, weighted) | 96 | Lecture voice throughout the 31 chapters: `بيّن أن`، `احسب`، `استنتج`، `قدّر`، `أوجد` in the exercises; narrative present in the openings; `ومنه / فيكون / ولدينا / أي` as the connective spine of the proofs. Chapters 16--31 were written against 01--15 so the voice does not change at the seam. |
| Terminology (weighted) | 95 | Per-chapter glossary settled below, checked against Book 3 `ar`. Six cross-chapter drifts were found by the term-link audit at the end and fixed (see *Terminology drifts*) --- they existed, which is why this is not 97. Index keys equal the visible terms. |
| MT-artifact freedom (weighted) | 98 | Gate 7 clean on all 62 files (`english`, `translit`, `punct`, `digits`, `math-space`, `bidi-ctrl`, `presform`, `tatweel`, `split-number` all 0). No English survives in prose, TikZ node text, `\foreach` lists, axis labels, `\legend`/`\addlegendentry`, `\text{…}` inside math, environment optional titles, section titles or index keys (each swept separately, script by script, after the last file landed). |
| Structure | 100 | `check_translation.sh bachelor-2 ar` green; every one of the 62 files written as line-range replacements on the English canon through `tools/id_apply.py`, so labels, `\cref` targets, `\begin{solution}{key}`, `\qty{}{}`, `\foreach`, `xtick=` and every math display are byte-identical to English. |
| LaTeX hygiene | 98 | 0 errors, 0 undefined references, 0 overfull boxes, 0 "invalid in math mode", 326 pages, 62/62 translated files actually consumed by the build. No local overrides: the four paragraphs that needed extra stretch are carried by the book preamble's `\emergencystretch` (see *Overfull boxes*). |
| Cross-references | 100 | Every `\cref`/`\ref` target byte-identical to English; 12 exercises + 1 weekend problem per chapter, one solution each, all 31 solution files present. |
| Figures | 97 | Drawing code untouched (the `draw` census of `id_apply.py` compares it byte-for-byte after blanking node text); only node text, `\foreach` label lists, axis labels, legends and captions are Arabic. Two captions had to swap left/right (see *The RTL caption rule*). |
| Solutions | 96 | All 31 solution files translated; `\textbf{n.}` numbering and every number, unit and label preserved. |

## What was produced

- `parts/bachelor-2/ar/01`--`31` (31 chapter bodies) and
  `parts/bachelor-2/solutions/ar/01`--`31` (31 solution files) --- 62 files,
  the complete volume.
- `tools/term_config/book4_ar.py` --- curated from Book 4's own harvest, not
  translated from `book4_en.py` and no longer the Book 3 seed it started from.
- **1 183** `\omterm` links across 60 files, on **148** distinct targets.
  English carries 1 231 links on 143 targets. **Every English target is
  covered**; the five Arabic-only targets are listed below.
- Build: 326 pages, `0` errors, `0` undefined, `0` overfull.

## Checks

```
bash tools/check_translation.sh bachelor-2 ar          -> TRANSLATION GATE: PASSED
  (arabic prose gate: OK, 62 files)

latexmk -g one_physics_book_4_university_year_2_ar.tex -> exit 0
  grep -ac '^!'                    -> 0
  grep -aci undefined              -> 0
  grep -ac Overfull                -> 0        (326 pages)
  grep -ac 'invalid in math mode'  -> 0
  grep -ac nullfont                -> 60       (identical to the English build)
  grep -ac Underfull               -> 36       (English: 34)
  grep -ac 'Missing character'     -> 141      (60 nullfont, as English; plus 81
                                                U+000A -- see *Cross-edition findings*)
  ar files in the .fls             -> 62 / 62
```

`-g` is not optional. `\ominput`'s `\IfFileExists{parts/#1/\booklang/#2.tex}`
records only the **English** file as a dependency when the translated file did
not exist at the last build, so a plain `latexmk` answers *"Nothing to do"*
after a dozen new chapters have landed and reports page counts and overfull
figures measured on a nearly-all-English body. Verify with

```
grep -o 'parts/bachelor-2/\(solutions/\)\?ar/[^ ]*' \
     build/one_physics_book_4_university_year_2_ar.fls | sort -u | wc -l
```

## Term links: parity with English

| | English | Arabic |
|---|---:|---:|
| links | 1 231 | 1 183 (96 %) |
| distinct targets | 143 | 148 |
| targets in English but not Arabic | --- | **0** |

The five Arabic-only targets are all cases where English drops a term as
*defined twice* and Arabic does not, because the two Arabic wordings differ:

| target | Arabic term | why English has none |
|---|---|---|
| `prop:b2:schrodinger-wave-functions:free` | `رزمة موجة` | English says *wave packet* in both ch. 08 and ch. 30 and drops it as ambiguous |
| `def:b2:flow-balances:cv` | `جملة مفتوحة` | English's *open system* collides with ch. 27 |
| `def:b2:laser:cavity` | `الليزر` | English stops the bare word `laser` |
| `prop:b2:open-systems:mass` | `التدفق الكتلي` | English's *mass flow rate* collides with ch. 02 |
| `rem:b2:charges-currents-conduction:materials` | `محلول شاردي`, `نصف ناقل` | not emphasised in English |

The residual 48-link gap is Arabic's pronominal economy, not a miss: where
English repeats the noun (*"the coherence time and the coherence length"*,
*"its thermal resistance"*), Arabic writes the pronoun (`زمن الترابط وطوله`,
`مقاوماتها`), and a pronoun is not a linkable term. The gap is concentrated in
exactly the four targets whose English terms are noun pairs
(`…:coherence` −17, `…:complex` −8, `…:path` −7, `…:coax` −7).

### The config, and what Book 3's seed cost

`book4_ar.py` arrived as a byte copy of `book3_ar.py`. Not one entry survived
audit:

- **23 dangling `EXTRA` targets.** Every one pointed at a `thm:b1:` /
  `prop:b1:` label --- Coulomb, Gauss, Biot--Savart, Faraday, Lenz,
  Archimedes, Carnot, Clausius, Kelvin, Mayer, the lever rule, the
  right-hand rule, Boltzmann's formula, hydrostatics. Those are **Book 3**
  results; they do not exist in this volume, so each would have produced an
  undefined link target. Deleted. Book 4 needs exactly **one** `EXTRA`:
  `قانون مالوس` → `prop:b2:plane-waves-polarization:malus`, the only named
  result English links by a `قانون`-headed name (twice) and which
  `NOT_A_TERM` therefore rejects. `قانون جول الموضعي` is deliberately **not**
  added: English harvests it and never links it, and ch. 28's
  «وهو قانون جول من جديد» is Book 3's gas law under the same Arabic name.
- **48 `STOP` words and 10 `DROP` words**, none of which Book 4 harvests at
  all --- checked term by term against the raw harvest with `STOP`/`DROP`
  blanked. Dead weight, deleted.
- **9 groups of `EXTRA_PROTECT`** (the `سعة` = capacitance/amplitude split, the
  `الثانية` ordinal, and the Ampère / Pascal / Kelvin unit-vs-person
  collisions). Book 4 harvests none of those words; the tuple is now empty.
- **8 `DERIVED` plurals**, none of them a Book 4 term.

Book 4's own curation is small, because Book 4's harvest is clean:
`STOP` = 7, `DROP` = 4, `EXTRA` = 1, `PRIMARY_OK` = 1, `DERIVED` = 24.
The seven `STOP` words are the five English stops in the forms the Arabic
harvest produced (`الامتصاص`, `ليزر`/`الليزر`, `مستقر`, `العتبة`, `مردودها`)
plus one Arabic-only collision worth recording:

> **`جسم صلب`** = the *rigid body* of ch. 01 **and** the ordinary *solid*.
> Chapters 06, 15, 24, 25, 28 and 29 all say it in the second sense. Before
> stopping it the Arabic carried 14 links against English's 1 --- 13 of them
> pointing a reader who wanted "solids conduct heat" at the definition of a
> rigid body.

`PRIMARY_OK = {"جريان مستقر"}` because *steady flow* is defined twice, in
ch. 02 (the Eulerian description) and ch. 27 (the open-system balance). One
spelling, one concept: every use goes to the first definition rather than
being dropped.

## Terminology settled for this book

Chosen to agree with Book 3 `ar` and recorded so Book 5 does not fork:

| English | Arabic | why |
|---|---|---|
| rigid body | **جسم صلب** | Book 3 ch. 15 already uses it |
| control volume | **حجم التحكم** | descriptive; `جملة مفتوحة` kept for *open system* |
| streamline / pathline | **خط تيار / خط مسار** | keeps `مسار` = trajectory free |
| vorticity | **دوامية** | from `دوامة`; `دوران` is reserved for the curl |
| divergence / gradient / curl / Laplacian | **تباعد / تدرج / دوّار / لابلاسي** | the four operators of ch. 11, one word each |
| dynamic / kinematic viscosity | **لزوجة ديناميكية / حركية** | |
| boundary layer | **طبقة حدّية** | |
| wave packet | **رزمة موجية** | `رزمة` not `حزمة`, which is the optical *beam* |
| group / phase velocity | **سرعة المجموعة / سرعة الطور** | not `السرعة الزمرية`; see the drift list |
| dispersion relation / dispersive medium | **علاقة التبدد / وسط متبدّد** | |
| evanescent wave / skin depth / attenuation | **موجة متلاشية / عمق القشرة / وهن** | `وهن` not `توهين` |
| continuity equation | **معادلة الاستمرار** | the body text of chs. 27, 30, 31 already said it |
| displacement current | **تيار الإزاحة** | |
| Poynting vector | **متجهة بوينتنغ** | `متجهة`, the settled word for *vector* |
| polarization (light) | **استقطاب** | `ضوء طبيعي` for *natural light* |
| waveguide / optical fibre | **دليل موجة / ليف بصري** | |
| optical path | **مسير ضوئي** | leaves `مسار` for a mechanical path |
| coherence time / length / wave train | **زمن الترابط / طول الترابط / قطار موجة** | |
| fringe / fringe spacing / contrast | **هدبة / البعد الهدبي / التباين** | |
| diffraction / grating | **حيود / شبكة حيود** | |
| free spectral range / finesse | **المجال الطيفي الحر / الدقة** | |
| population inversion / stimulated emission | **انقلاب الجمهرة / إصدار مستحثّ** | `جمهرة` for *population*, free of `سكان` |
| gain / saturation intensity | **كسب / شدة الإشباع** | |
| thermal conductivity / resistance / fin | **ناقلية حرارية / مقاومة حرارية / زعنفة** | |
| blackbody / spectral exitance | **جسم أسود / خروجية طيفية** | |
| open system / throttle / nozzle | **نظام مفتوح / خانق / منفث** | |
| free energy / free enthalpy | **الطاقة الحرة / الإنتالبي الحرّ** | matches Book 3's `الإنتالبي` |
| chemical potential / partition function | **الكمون الكيميائي / تابع التقسيم** | `الكمون` as in Book 3 |
| wave function / stationary state | **تابع موجي / حالة مستقرة** | `تابع` for *function*, as in the math books |
| tunnelling / potential well | **أثر النفق / بئر كمون** | |
| coaxial cable | **كابل محوري** | not `كبل`; see the drift list |

## Terminology drifts found by the link audit, and fixed

The `\omterm` count per target is a terminology gate in disguise: a target with
far fewer Arabic links than English links is usually a chapter that has quietly
invented a second word. Six did, and all six were repaired across the whole
tree before the final build:

| drifted | normalised to | sites |
|---|---|---|
| `تدرّج` (shadda) vs `تدرج` | **`تدرج`** | 21 |
| `مستقرّ` (shadda) vs `مستقر` | **`مستقر`** | 214 |
| `توهين` / `التوهين` | **`وهن` / `الوهن`** | 11 |
| `كبل` | **`كابل`** | 3 |
| `معادلة الاتصال` | **`معادلة الاستمرار`** | 2 index keys |
| `السرعة الزمرية` / `السرعة الطورية` (ch. 30) | **`سرعة المجموعة` / `سرعة الطور`** | 5 |

None of these is visible to `check_arabic_prose.py` --- both spellings are
perfectly good Arabic --- and none is visible to `id_apply.py`, which does not
compare prose. The link census is the only gate that sees them. **This is the
cheapest terminology check in the toolchain and it should be run before the
score file is written, not after.**

## The RTL caption rule (this contradicts Book 3 `ar`)

Verified empirically on this book, figure by figure:

> Inside **one** `tikzpicture`, `\begin{scope}[xshift=…]` does **not** get
> reordered: left stays left, and a caption that says «على اليسار» must keep
> saying «على اليسار». Only **two separate `tikzpicture` boxes inside one
> `omfigure`**, separated by `\hfill`, are swapped by bidi, and only those
> captions need left/right exchanged.

**Thirteen** captions in this book are of the second kind and have their sides
swapped (chs. 04, 05 ×2, 06, 07, 08, 09 ×2, 10, 14 ×2, 15, 16); every other
caption keeps the English sides. The rule was verified mechanically over every
`omfigure` in the volume: a caption's leading side-word is swapped **iff** the
figure holds two or more boxes (`tikzpicture`s or `\includegraphics`), with
zero exceptions in 31 chapters. Book 3 `ar` swapped more broadly; a reader
comparing the two volumes will see the difference, and the rule above is the
one that matches what LuaTeX actually does.

## Overfull boxes: 19 → 0, and the mechanism

The first honest (`-g`) build had **19** overfull boxes, every one `in
paragraph`. Four rebuild rounds brought them to 0. What they teach, beyond
what Book 3 `ar` already recorded:

1. **Babel's `bidi=basic` wraps every inline `$…$` in an `\hbox`.** TeX
   therefore cannot break an Arabic line at a relation the way it breaks an
   English one, and a long formula is one indivisible box.
2. **Splitting `$A = B$` into `$A$ $= B$` does nothing.** The space between two
   adjacent LTR runs is a *neutral* character under UAX #9 and is absorbed into
   the run, so the two spans are re-merged into a single box; measured gain,
   1.4 pt (the difference between a math space and an interword space). An
   **Arabic word must sit between them**: `$A$، أي $B$` or `$A$ يساوي $B$`.
   Eight formulas were re-segmented this way.
3. **The same rule fixes comma-separated quantity lists.**
   `\qty{0.71}{GHz}، \qty{0.90}{GHz}، \qty{1.35}{GHz}، \qty{1.95}{GHz}` is one
   46 pt-wide unbreakable box because the Arabic comma between two numbers is
   also neutral; writing `، و \qty{0.90}{GHz}` breaks it into four.
   Likewise `TE$_{10}$ \qty{6.55}{GHz}` merges the Latin mode name with the
   number: inserting `عند` between them splits the box in two.
4. **Arabic interword glue barely stretches.** A line that would need ~20 pt of
   stretch is already past `\tolerance`, so for a paragraph made of long
   formulas there is often *no* legal break at any position and TeX sets the
   whole sentence on one line (one case here was 98 pt over, i.e. 1.3 lines of
   material with no legal breakpoint at all). Four such paragraphs could not be
   reworded into legality --- `ar/21-gratings.tex` (the N-wave proof),
   `solutions/ar/03-euler-bernoulli` (answer 23),
   `solutions/ar/12-poynting-vector` (exercise 12), `solutions/ar/21-gratings`
   (exercise 9). They are carried by
   `\setlength{\emergencystretch}{3em}` in
   `one_physics_book_4_university_year_2_ar.tex`, added by the orchestrator
   after this agent reported it (Book 2's `ar/hi/es/pt/id` files already had
   it; Book 4's did not). Three of the four settled at the global 3 em.
5. **The fourth needed rule 3 as well.** `solutions/ar/12-poynting-vector`
   exercise 12 had been held by a local 5 em; at the global 3 em it reopened
   55.6 pt over. The fix is not more stretch --- it is to make the line that
   *ends at the break point* long enough to be feasible. Breaking before the
   long trailing Poynting span left only ~250 pt of a 345 pt line (95 pt of
   stretch wanted, ~49 pt available: badness ≈ 730, past `\tolerance`), so
   thirteen characters of Arabic were added **before** the break
   (`(أ) وجريان الطاقة $\vect\Pi = …$`), which lifts that line to ~310 pt and
   makes the break legal. Note the direction: adding words *after* the break
   point makes an overfull line worse (Book 3 `ar` records that trap); adding
   them *before* it is what buys the break.

Everything else was reworded or reflowed: 50 prose edits across 19 files, plus
`scale=0.94` on the two `tikzpicture`s of the ch. 05 momentum figure, whose
Arabic node labels are wider than `\text{ext}` and `\text{wall}`.

## Faults found and fixed while writing and gating

- **Tatweel (U+0640), dozens per chapter** --- the natural `بـ$X$` / `لـ$X$` /
  `فـ$X$` / `كـ$X$` join before a formula or a `\qty`, plus `(هـ)` for a fifth
  enumerated part. Fixed by naming the object (`بالمقدار $X$`,
  `بمقدار \qty{…}`, `فيكون`, `مثل $\vect E$`, `للتابع $F$`) and by writing
  `(ه)`. Final count: 0.
- **`\foreach` label lists are invisible to both gates.** `id_apply.py` blanks
  node text in the `draw` census but not a `\foreach` list, and
  `check_arabic_prose.py` does not reach inside one either. ch. 23's
  `\foreach \x/\t in {0/absorption, 3.6/spontaneous emission, …}` therefore
  shipped English text past both gates in a first pass; found by a manual
  sweep and written as `{0/{الامتصاص}, 3.6/{الإصدار التلقائي}, …}` (each entry
  braced, because the Arabic contains no comma but the entries must survive
  `\foreach`'s own parsing).
- **`\qty{1}{fringe}` (ch. 20) and `\qty{1}{day}` (chs. 24, 26)** --- the
  English canon leaves an English word inside a `\qty`, where siunitx drops it
  from the page. Written as `= 0.1$ هدبة` and `\qty{1}{d}`.
- **Chemical formulae inside math** --- `MgF$_2$`, `AsH$_3$`, `ND$_3$` read as
  residual English to a human reviewer even though the gate passes them as
  formulae; the ones that are prose (`MgF$_2$` in ch. 15, `AsH$_3$` in ch. 31)
  became `فلوريد المغنيزيوم` and `أرسين`, the ones that are chemistry
  (`^{12}$C`, `N$_2$`, `NH$_3$`) stayed.
- **`$X = $ const` / `$= $`** --- a math span ending in a space, which the
  `math-space` class reports as an MT fingerprint. Kept verbatim through
  `id_apply --force-classes prose`, then post-edited to
  `$X = \text{ثابت}$` and `$=$`.
- **Photo credits** transliterate the photographer's name, matching
  `parts/bachelor-1/ar/*` («الصورة: أولغا خوميتسيفيتش، CC~BY~2.0.»).

## Why not 100

1. **The six terminology drifts existed at all.** Every one was caught, but
   only by the link census at the very end; a reader of an earlier draft would
   have met `توهين` and `وهن` in the same chapter.
2. **Four paragraphs depend on the book-level `\emergencystretch`.** It is
   invisible on the page except as slightly looser word spacing in those four
   places, but they are the only paragraphs in the volume that cannot be set
   at `\tolerance` on their own.
3. **Eight formulas were re-segmented** from `$A = B$` to `$A$، أي $B$` to give
   TeX a break point. The mathematics is unchanged, but the Arabic no longer
   mirrors the English span for span in those eight places.
4. **`الإنتالبي` and `اللابلاسي` are transliterations**, kept for concision and
   for continuity with Book 3 `ar`; `المحتوى الحراري` and `مؤثر لابلاس` exist.
5. **Link displays swallow a leading proclitic.** `HEAD` in `lang_ar.py`
   includes `و ف ب ك ل`, so a link that opens a clause reads
   `\omterm{…}{ومعادلة أويلر}` --- the conjunction sits inside the coloured
   term. Series-wide behaviour, orchestrator-owned, but it is the one place
   where the Arabic looks less clean than the English.
6. **`(ه)` for the fifth item of a lettered list.** Arabic convention writes
   `(هـ)`, with a tatweel; the tatweel is gated series-wide.

## Cross-edition findings (reported to the orchestrator during the run)

1. **`latexmk` without `-g` lies.** See *Checks* above. This affects every
   translated edition of every book, not only Arabic, and it invalidated the
   page counts and overfull figures reported in the middle of this run.
2. **Book 4's top-level `.tex` files lacked `\setlength{\emergencystretch}{3em}`.**
   `one_physics_book_2_high_school_{ar,hi,es,pt,id}.tex` all set it; Book 3's
   and Book 4's language files did not. For Arabic --- where inline math is
   unbreakable and interword glue barely stretches --- that setting is the
   difference between "reword the sentence" and "no legal break exists".
   Reported rather than patched, because the book file is shared; the
   orchestrator added it, this edition's four local overrides were then
   deleted, and the book rebuilt at **0 overfull** with **one** paragraph
   needing rule 3 on top of the global 3 em. No raise of the global value was
   needed.
3. **81 `Missing character: U+000A` in the Arabic build.** A literal newline
   reaches `NotoNaskhArabic-Regular`. It is silent on the page and it is
   **not** this edition's doing: Book 2 `ar` carries 58 and Book 3 `ar` 192,
   Book 1 `ar` and every English build carry 0. They cluster immediately after
   babel's `\bbl@ensure@arabic {باب} N.` chapter-mark line and on the figure
   pages that follow, i.e. in the running-header machinery
   (`\ombrandheader` + babel's chapter mark), not in chapter text. Book 3
   `ar`'s score file records its 257 missing characters as "all nullfont",
   which is not right --- 192 of them are this.
4. **The link census is a terminology gate.** Comparing per-target `\omterm`
   counts against English found six spelling/synonym drifts in this edition
   that no other gate can see. Every language agent should run it before
   scoring, not after.
