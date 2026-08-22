# One Physics Book 4 (University, Year 2) — Hindi edition: self-score

**Date:** 2026-08-22
**Quality bar:** *native academic* (the bar of `translation_instruction.md`,
refined by `hindi_style_card.md`).
**Source of truth:** the English canon (`parts/bachelor-2/*.tex` and
`parts/bachelor-2/solutions/*.tex`), followed line-range by line-range through
`tools/id_apply.py`. No file was hand-written whole; every one of the 62 was
produced as a patch of line ranges on its English twin.
**Register comparands:** the shipped Hindi Book 3
(`parts/bachelor-1/hi/`) for the university lecture voice and for every term
the two volumes share (पॉयनटिंग सदिश, तरंग फलन, सुरंग प्रभाव, एंट्रॉपी,
क्वांटन), and `../one-math-book/parts/bachelor-1/hi/` for the register.

## Overall: **96 / 100**

| Dimension | Weight | Score | Note |
|---|---:|---:|---|
| **Register** (Hindi academic) | 0.20 | **95** | Uniform university lecture voice: `दिखाइए`, `निकालिए`, `व्युत्पन्न कीजिए`, `आँकिए`, `मान लीजिए`, `रखिए`, `टिप्पणी कीजिए` in exercise stems; `अतः`, `यानी`, `अर्थात्`, `चूँकि` carrying proofs; chapter openings written as openings, not as rendered English first sentences (ch. 28: «रबर का कोई फ़ीता तेज़ी से खींचिए और उसे अपने होंठ से छुआइए: वह गरम है; उसे सिकुड़ने दीजिए और वह ठंडा है।»). Danda `।` closes every sentence; ASCII digits throughout. |
| **Terminology** | 0.20 | **96** | All **433** `\index{}` keys are Hindi and equal their visible term; the ordered index-key sequence matches English one for one in every chapter. Book 3's Hindi vocabulary is carried forward unchanged; the new Book 4 fields (fluid mechanics, physical optics, diffusion, thermal radiation, thermodynamic potentials, quantum wells) are established below and are binding on later `hi` work. |
| **MT-artifact freedom** | 0.20 | **97** | Nothing machine-translated: every sentence written against its English line range. `tools/check_hindi_prose.py` is **clean on all 62 files** — 0 `english`, 0 `translit`, 0 `danda`, 0 `math-space`, 0 `split-number`. Beyond the gate's reach, a manual sweep of the material it drops found **2** Latin strings in node/legend text (`CCD`, `Nd:YAG`) and **31** distinct `\text{…}` arguments with Latin (93 occurrences), all of them element symbols, unit symbols, single-letter quantity subscripts or `FSR` — the same set the French and Dutch editions keep. |
| Structure | 0.15 | **100** | `bash tools/check_translation.sh bachelor-2 hi` → **PASSED**. 62/62 files present. Ordered `\label{}` multiset diff against English: **0**. `\begin{exercise}` 372, `\begin{problem}` 31, `\begin{solution}` 403, `\begin{omfigure}` 150, `\begin{tikzpicture}` 121, `\includegraphics` 44 — every count identical to English. `--force-classes` never used; exactly **two** per-range `!class` opt-outs in the whole book, both in ch. 07 and both documented under *Why not 100*. |
| LaTeX hygiene | 0.10 | **98** | 0 `^!`, 0 undefined references, 0 "invalid in math mode", 0 TeX accent escapes, **0 non-ASCII characters inside `\qty{}` / `\unit{}` / `\num{}`** (checked by parsing every one of those macros, not by grep), `nullfont` at the English baseline of **60**, 332 pages (EN 345). Overfull boxes: **0**, down from 16 on the first build — every one was a Devanagari line that cannot hyphenate, and each was cleared by rewording, not by `\sloppy`. |
| Cross-references | 0.05 | **100** | 0 undefined; every `\label`, `\cref`, `ch:`/`def:`/`prop:`/`thm:` slug and `\begin{solution}{key}` byte-identical to the canon by construction. Solution headers localized as `\section*{अध्याय \ref{ch:…} --- <शीर्षक>}` with the key untouched. |
| Figures | 0.05 | **97** | Every visible node, axis label, `\addlegendentry`, `\legend` and `{\small …}` caption is Hindi; all drawing code (coordinates, styles, plot expressions, `\foreach` iterator lists) is byte-identical to the canon — `id_apply`'s `draw` census would have refused the file otherwise. The two exceptions are the two `\foreach` *label* lists in the book, whose strings print: ch. 07's decibel ladder (a `!draw` opt-out) and ch. 23's absorption/emission timeline (a post-edit). |
| Solutions | 0.05 | **96** | All 31 solution files translated; `\textbf{n.}` numbering, `\begin{solution}{key}` order and every numeric result preserved. |

**Weighted overall: 96 / 100.** Ship threshold ≥ 95 — met.

## Build gates

Measured on the final build of the tree as it stands, not on any earlier one.

| Gate | Result |
|---|---|
| `bash tools/check_translation.sh bachelor-2 hi` | **PASSED** |
| `python3 tools/check_hindi_prose.py` (all 62 files) | **OK — 0 findings** |
| `.fls` honesty check (`grep -o 'parts/bachelor-2/\(solutions/\)\?hi/[^ ]*' … \| sort -u \| wc -l`) | **62 / 62** — the build really reads the Hindi tree |
| `latexmk -g one_physics_book_4_university_year_2_hi.tex` | exit 0, **332 pages** (EN 345) |
| `grep -ac '^!'` | **0** |
| `grep -aci 'undefined'` | **0** |
| `grep -ac 'invalid in math mode'` | **0** |
| `grep -ac 'Overfull'` | **0** (EN 0) |
| `grep -ac 'Underfull'` | 36 (EN 34, FR 35) — the series norm |
| `grep -ac 'nullfont'` | **60** — identical to the English build. It is pgfplots' measuring pass, not a defect; a *rise* above 60 is what a stray non-ASCII character inside `\qty{}` looks like, so this number is the second, independent proof that there is none. |
| non-ASCII inside `\qty{}`/`\unit{}`/`\num{}` | **0** of 2 000+ call sites, verified by parsing all three macros' arguments |
| `python3 tools/link_defined_terms.py --book 4 --lang hi --check` | *every file matches what the config generates* |

## Defined-term links

| | EN | HI |
|---|---:|---:|
| `\omterm` links | 1 231 | **1 211** (98.4 %) |
| distinct target labels | 143 | **141** |
| targets in EN but not HI | — | 5 |
| targets in HI but not EN | — | 3 |

`tools/term_config/book4_hi.py` was rewritten from the Book 3 seed, not
inherited. Three things had to be done, and the numbers above are what they
bought:

1. **The seed was dead weight.** Every Book 3 `STOP`/`DROP` word (बल,
   द्रव्यमान, वेग, दाब, ताप, आघूर्ण, मात्रक, विमा, संकेत, आवरण, आदर्श,
   रैखिक …) was checked against the Book 4 harvest and **not one of them is a
   Book 4 term**; the same for the seed's two `EXTRA_PROTECT` regexes. They are
   gone. The new `STOP` mirrors `book4_en`'s entry for entry — स्थायी
   (*steady*), दक्षता (*efficiency*), अवशोषण (*absorption*), देहली
   (*threshold*); `book4_en`'s fifth, *laser*, has no bare Hindi counterpart
   because लेज़र is harvested only inside compounds.
2. **Eleven Hindi compounds were unreachable.** `harvest.py` accepts a notion
   introduced *outside* a `definition` from its bare `\index{}` only when the
   key contains a space. English clears that bar with two-word phrases —
   *path difference*, *wave packet*, *wave train*, *impedance matching*,
   *stationary flow*, *wave equation* — while Hindi writes each as one
   compound (पथांतर, तरंग-पुंज, तरंग-रेल, प्रतिबाधा-मिलान, स्थायी प्रवाह,
   तरंग-समीकरण). They were found by diffing the Hindi `\index{}` keys against
   their English twins position by position, and each is now an `EXTRA`
   pointing at the label its English twin links to. Worth ~110 links, most of
   them the 22 that *path difference* alone carries.
3. **Hindi has no `-s`.** `lang_hi.py` sets `WORD_TAIL = ''` and
   `DERIVE = False`, so a term matches only in its citation form while English
   gets every plural free through `(?:e?s)?`. Its own docstring says to
   declare the variants in the book config, so `DERIVED` now lists 28 bases
   with their direct and oblique plurals (धारा-रेखाएँ, तरंगाग्रों, मैक्सवेल
   के समीकरणों, अप्रगामी तरंगें/तरंगों …). Each variant was generated
   mechanically, counted against the real corpus, and kept **only while its
   target stayed within 115 % of the same target's English count** — that cap
   is why विद्युत्चुंबकीय तरंगें (5 occurrences) is absent while
   विद्युत्चुंबकीय तरंगों (1) is present: English links that target once in
   the whole book. Worth 55 links.

The five targets English links and Hindi does not are
`def:b2:rigid-body-mechanics:pivot` (6 links), `thm:b2:flow-balances:momentum`
(7), `rem:b2:rigid-body-mechanics:motions` (2),
`met:b2:rigid-body-mechanics:incline` (1) and
`thm:b2:plane-waves-polarization:wave` (1). Each was checked by hand: the
Hindi term (धुरी-धारक, संवेग अभिवाह, स्थिर अक्ष के परितः घूर्णन, आनत तल पर
लुढ़कना, विद्युत्चुंबकीय तरंग) **occurs only at its own definition site**,
which is never self-linked. English earns those links because its phrase
recurs verbatim in running prose where Hindi naturally varies the wording or
uses a plural. This is a wording fact, not missing text. The three extra
Hindi targets are one or two links each, the ordinary consequence of
`AMBIG_POLICY = "drop"` meeting a different set of ambiguous heads.

## Structural mirror

| Count | EN | HI |
|---|---:|---:|
| Chapter bodies | 31 | 31 |
| Solution files | 31 | 31 |
| `\begin{exercise}` | 372 | 372 |
| `\begin{problem}` | 31 | 31 |
| `\begin{solution}` | 403 | 403 |
| `\begin{omfigure}` | 150 | 150 |
| `\begin{tikzpicture}` | 121 | 121 |
| `\includegraphics` | 44 | 44 |
| `\label{}` | 801 | 801 (multiset diff **0**) |
| `\index{}` | 433 | 433 |

## Sampled passages

### 1. Chapter opening — ch. 28 *ऊष्मागतिकीय विभव*

> रबर का कोई फ़ीता तेज़ी से खींचिए और उसे अपने होंठ से छुआइए: वह गरम है;
> उसे सिकुड़ने दीजिए और वह ठंडा है। उस पर कोई भार लटकाइए और उसे किसी
> बाल-सुखाने वाले से गरम कीजिए: वह \emph{छोटा हो जाता है}। इस्पात का कोई
> स्प्रिंग ऐसा नहीं बरतता, और कारण यह है कि रबर के फ़ीते का तनाव ऊर्जा की
> नहीं बल्कि एंट्रॉपी की बात है --- खिंची हुई शृंखलाओं के पास ख़ुद को
> सजाने के कम तरीक़े बचते हैं।

**Verdict: native.** The imperative chain (`खींचिए … छुआइए … लटकाइए …
कीजिए`) is how a Hindi lecturer opens a demonstration; `की बात है` and
`ख़ुद को सजाने के … तरीक़े` are idiom, not rendered English. Nasta'liq-derived
spellings (`तरीक़े`, `फ़ीता`) carry their nuqtas consistently.

### 2. Theorem statement — ch. 29, the Boltzmann factor

> जिसमें योग $Z$ (वह \emph{विभाजन फलन}) प्रायिकताओं को प्रसामान्यित करता
> है; दो अवस्थाएँ (या बराबर अपभ्रष्टता के दो स्तर) अनुपात
> $N_2/N_1 = \eu^{-(E_2 - E_1)/k_BT}$ में भरी होती हैं; और किसी संतत चर
> (कोई स्थिति, कोई वेग) के लिए प्रायिकता घनत्व उस चर में
> $\eu^{-E/k_BT}$ के अनुपात में है।

**Verdict: native.** Semicolon-chained theorem register, verb-final, with the
term introduced in `\emph{}` exactly where English introduces it and the
math spans in the English order without an audible seam.

### 3. Proof — ch. 31, the finite well

> सम हल भीतर $A\cos kx$ और बाहर $B\eu^{-\kappa|x|}$ है; $\varphi'/\varphi$
> का सांतत्य $x = a$ पर $-k\tan ka = -\kappa$ देता है। … $\xi\tan\xi$ की हर
> शाखा, जो $\xi = n\pi$ से शुरू हो, और $-\xi\cot\xi$ की, जो
> $(n + \tfrac12)\pi$ से शुरू हो, वृत्त से एक बार मिलती है यदि वह उसके भीतर
> से शुरू हो: यही गिनती है।

**Verdict: native.** The relative-clause construction (`जो … से शुरू हो`)
is the natural Hindi way to keep the math spans in the canon's order without
an appositive; `यही गिनती है` closes the proof the way a Hindi text closes it.

### 4. Chapter opening — ch. 24 *कण विसरण*

> ठहरे हुए पानी में रंजक का कोई रवा डालिए और देखते रहिए: उसके चारों ओर
> कोई रंगीन बादल बनता है, बढ़ता है, अपने किनारों पर नरम पड़ जाता है, और
> फैलता जाता है --- किसी मिनट में किसी मिलीमीटर भर, किसी घंटे में किसी
> सेंटीमीटर भर, किसी हफ़्ते में पूरे गिलास भर।

**Verdict: native.** The compound-verb cascade (`बनता है, बढ़ता है, नरम पड़
जाता है, फैलता जाता है`) and the `भर` scale ladder are Hindi rhetoric; the
English's three-clause crescendo survives without calque.

### 5. Solutions — ch. 31, problem items 13–17

> **13.** दर $\sim 10^{-21}\,\unit{s^{-1}}$, अर्ध-आयु $\sim 10^{13}$ वर्ष
> --- मापे गए मान से हज़ार गुना: किसी सौ के चरघातांक के लिए, कोई कच्चा
> मॉडल कुछ ही कोटियों के भीतर उतर जाए तो अच्छा ही है।
> … **17.** हाँ: $\alpha$ के पास सदा \qty{4.2}{MeV} होता है; उसके तरंग फलन
> का रोधिका के नीचे बस कोई क्षयी भाग होता है, जहाँ कोई भी मापन उसे
> ऋणात्मक गतिज ऊर्जा के साथ नहीं पाता।

**Verdict: native.** Worked answers read as a Hindi lecturer's, with
`तो अच्छा ही है` carrying the English's dry aside.

### 6. Ordering-constrained sentences (the honest sample)

> लंबाई $L$ के किसी फ़ीते के लिए, जो तनाव $f$ के अधीन हो, …
> $\dd G = (g_1 - g_2)\dd m_1$ नियत $T$, $P$ पर ($m_1 + m_2$ नियत रखकर) …

**Verdict: near-native.** `id_apply`'s math census compares the *ordered*
sequence of math spans, and Hindi is verb-final with postpositions, so a
natural «तनाव $f$ के अधीन लंबाई $L$ का फ़ीता» would swap $f$ and $L$. Where a
relative clause could not absorb the reordering, the Hindi keeps the English
order with a trailing postpositional phrase. Grammatical and clear, one shade
stiffer than free prose. Roughly fifty sentences book-wide carry one; they are
the main reason Register is 95 and not 98.

## Why not 100

* **The math-span order tax.** Above. It is a property of the census, not of
  the translator, and it costs the register a point.
* **Eighteen deliberate byte-level divergences from the canon, in four
  classes, and no others.** The whole tree was re-compared against English
  file by file after the last edit, with all of `id_apply`'s censuses run on
  the applied files (`math`, `envs`, `labels`, `emph`, `draw`, `index`,
  `braces`) plus the prose gate. Seventeen files carry one divergence and one
  carries two; every one is listed here.

  1. **Nine trailing-space math spans of the English canon** —
     `$xy = $`, `$vS = $`, `$y = $`, `$z = $`, `$\sin i/c = $`,
     `$n(r)\cos\theta(r) = $`, `$\varphi = $`, a second `$xy = $` and a bare
     `$= $`, in `02-fluid-kinematics`, `03-euler-bernoulli`, `04-viscous-flows`,
     `13-plane-waves-polarization`, `16-guided-waves`, `18-scalar-light-model`,
     `26-thermal-radiation` and their solutions. English closes the span and
     then sets *const* / *Cte* as upright prose outside it; Hindi has to put
     `\text{अचर}` (or, for `$= $`, nothing) inside. Reported below as a canon
     defect.
  2. **Two `\foreach` label lists translated** — `07-sound-waves.tex:179`
     (the decibel ladder) under a `@@ 179 !draw` opt-out, and
     `23-laser.tex:103` (*absorption / spontaneous / stimulated emission*) as
     a post-edit. Those labels **print**, yet no prose gate scans them and the
     `draw` census demands byte-identical drawing code, so there is no other
     way. Reported below.
  3. **Six `\qty{}`/`\unit{}` arguments carrying an SI symbol where English
     wrote an English word** — `\qty{5.7}{days}` → `{d}`, `\qty{3.3}{days}` →
     `{d}`, `\qty{3.9}{days}` → `{d}`, `\qty{1.9}{kWh/day}` → `{kWh/d}`,
     `\qty{0.1}{fringe}` → `$0.1$ फ्रिंज`, `\qty{1}{day}` → «किसी एक दिन»
     (plus, outside the census, `\unit{K.day}` → «केल्विन-दिन में» and
     `\qty{600}{lines/mm}` → `\num{600} रेखा प्रति मिलीमीटर`). Devanagari may
     never enter those arguments, and an English word left inside one is
     residual English no gate can see.
  4. **One inline formula set as a display** — `21-gratings.tex`, the
     geometric series in the $N$-wave proof. Inline it overflowed by 91 pt:
     the formula is 1.2 lines wide, its only legal break is the `=`, and
     Devanagari cannot hyphenate to absorb the remainder. Content unchanged.
     Same precedent as the shipped Book 3 hi.

  One further `!math` opt-out exists that produces no byte divergence:
  `@@ 371-378 !math` in ch. 07, exercise 7, where "343 m/s in air, 323 m/s in
  argon (M = 40 g/mol) at 20 °C" cannot be said in Hindi without moving the
  temperature ahead of the two speeds. No math was altered, only its order.
  These two are the only `!class` opt-outs in the book, and `--force-classes`
  was never used.
* **Five term-link targets English reaches and Hindi does not** (6, 7, 2, 1
  and 1 links). Diagnosed above; each is a term whose Hindi wording recurs
  only at its definition.
* **Sixteen overfull boxes had to be reworded away, and it took four builds.**
  Devanagari does not hyphenate, so a line of long compounds punctuated by
  wide inline maths has few legal breaks and TeX prefers an overfull line to a
  loose one. The cure that works is counter-intuitive and worth recording:
  *add short words around the wide math*, do not shorten the sentence. Every
  attempt to shorten made the box worse (`01-rigid-body-mechanics` went
  2 pt → 54 pt → 19 pt → 69 pt before a version with four extra short tokens
  between the two integrals cleared it).

## Glossary established by this pass

Book 4 is the first Hindi book in the series to carry rigid-body mechanics,
fluid mechanics, physical optics, transport and quantum wells. These choices
are **binding on later `hi` work**:

| English | Hindi |
|---|---|
| rigid body / rotation vector / slip velocity | दृढ़ पिंड / घूर्णन सदिश / सर्पण वेग |
| rolling without slipping / rolling friction | बिना फिसले लुढ़कना / लोटनिक घर्षण |
| pivot (perfect) / bearing / friction cone | धुरी (आदर्श) / धुरी-धारक / घर्षण शंकु |
| fluid particle / continuum hypothesis / mesoscopic scale | तरल कण / सांतत्य परिकल्पना / मध्यदर्शी पैमाना |
| Lagrangian / Eulerian description | लाग्रांजीय / ऑयलरीय वर्णन |
| streamline / pathline / stationary flow | धारा-रेखा / पथ-रेखा / स्थायी प्रवाह |
| vorticity / irrotational flow / circulation | भ्रमिलता / अघूर्णी प्रवाह / परिचालन |
| perfect fluid / Euler's equation / Bernoulli | आदर्श तरल / ऑयलर समीकरण / बर्नूली |
| stagnation pressure / Venturi / Pitot tube | स्थगन दाब / वेंचुरी / पीटो नली |
| dynamic / kinematic viscosity | गतिक / शुद्धगतिक श्यानता |
| shear stress / no-slip condition / boundary layer | अपरूपण प्रतिबल / अ-सर्पण प्रतिबंध / सीमांत परत |
| Reynolds number / laminar / turbulent flow | रेनल्ड्स संख्या / स्तरीय / विक्षुब्ध प्रवाह |
| Poiseuille flow / Stokes' law / drag crisis | प्वाज़ॉय प्रवाह / स्टोक्स का नियम / कर्षण संकट |
| wave equation / d'Alembert equation | तरंग-समीकरण / दालांबेर समीकरण |
| standing wave / normal modes / harmonic | अप्रगामी तरंग / प्रसामान्य विधाएँ / संनादी |
| overpressure / acoustic impedance / sound level | अधिदाब / ध्वानिक प्रतिबाधा / ध्वनि-स्तर |
| dispersion relation / phase, group velocity | परिक्षेपण संबंध / कला वेग, समूह वेग |
| wave packet / wave train / transmission line | तरंग-पुंज / तरंग-रेल / संचरण-रेखा |
| impedance matching / standing wave ratio | प्रतिबाधा-मिलान / अप्रगामी तरंग अनुपात |
| current density / drift velocity / Drude model | धारा घनत्व / अपवाह वेग / लोरेंत्स प्रतिरूप |
| Maxwell's equations (Gauss / Faraday / Ampère) | मैक्सवेल के समीकरण (गाउस / फ़ैराडे / ऐंपियर) |
| displacement current / gradient, divergence, curl | विस्थापन धारा / प्रवणता, अपसरण, कर्ल |
| scalar, vector potential / Coulomb gauge | अदिश, सदिश विभव / कूलॉम गेज |
| Poynting vector / Poynting's theorem | पॉयनटिंग सदिश / पॉयनटिंग की प्रमेय |
| plane electromagnetic wave / polarisation | समतल विद्युत्चुंबकीय तरंग / ध्रुवण |
| linear, circular, elliptical polarisation | रैखिक, वृत्तीय, दीर्घवृत्ती ध्रुवण |
| wave plate / fast, slow axis / Brewster angle | तरंग-पट्टिका / द्रुत, मंद अक्ष / ब्रूस्टर कोण |
| plasma frequency / skin depth, skin effect | प्लाज़्मा आवृत्ति / त्वचा गहराई, त्वचा प्रभाव |
| waveguide / cut-off frequency / cavity resonator | तरंग-निर्देशिका / कटाव आवृत्ति / कोटर अनुनादक |
| oscillating dipole / radiation resistance / Larmor | दोलन करता द्विध्रुव / विकिरण प्रतिरोध / लार्मर |
| Rayleigh scattering / scattering cross-section | रैले प्रकीर्णन / प्रकीर्णन अनुप्रस्थ काट |
| scalar model of light / optical path / wavefront | प्रकाश का अदिश प्रतिरूप / प्रकाशिक पथ / तरंगाग्र |
| coherence (temporal, spatial) / coherence length | संसक्ति (कालिक, दैशिक) / संसक्ति लंबाई |
| path difference / order of interference / contrast | पथांतर / व्यतिकरण की कोटि / विभेद (फ्रिंज) |
| division of wavefront / of amplitude | तरंगाग्र-विभाजन / आयाम-विभाजन |
| fringes of equal inclination / of equal thickness | समान नति की फ्रिंजें / समान मोटाई की फ्रिंजें |
| air wedge / air plate (Michelson) | वायु-पच्चर / वायु-पट्ट (माइकेल्सन) |
| diffraction grating / grating equation / free spectral range | विवर्तन जालक / जालक का समीकरण / मुक्त वर्णक्रमी परास |
| Fabry--Perot / finesse / resolving power | फ़ाब्री--पेरो / सूक्ष्मता / विभेदन-शक्ति |
| Fraunhofer diffraction / Airy disc / Rayleigh criterion | फ्राउनहोफ़र विवर्तन / एरी चकती / रैले कसौटी |
| spatial filtering / Fourier plane / Abbe's principle | दैशिक छनन / फ़ूरिये तल / आबे का सिद्धांत |
| stimulated emission / population inversion | उद्दीपित उत्सर्जन / जनसंख्या प्रतिलोमन |
| Einstein coefficients / saturation intensity / waist | आइंस्टाइन गुणांक / संतृप्ति तीव्रता / कटि |
| Fick's law / diffusion coefficient / diffusion equation | फ़िक का नियम / विसरण गुणांक / विसरण समीकरण |
| random walk / mean free path | यादृच्छिक चाल / माध्य मुक्त पथ |
| heat flux density / thermal conductivity / fin | ऊष्मा धारा-घनत्व / ऊष्मा चालकता / पंखी |
| blackbody / emissivity / spectral exitance | कृष्णिका / उत्सर्जकता / वर्णक्रमी निर्गम |
| Stefan--Boltzmann / Wien / Planck's law | स्टेफ़न--बोल्ट्ज़मान / वीन / प्लांक का नियम |
| solar constant / effective temperature / greenhouse effect | सौर अचर / प्रभावी ताप / हरितगृह प्रभाव |
| open system / control volume / shaft (useful) work | विवृत निकाय / नियंत्रण आयतन / उपयोगी कार्य |
| enthalpy in a flow / throttle / nozzle | एंथैल्पी (किसी प्रवाह में) / थ्रॉटल / तुंड |
| isentropic efficiency / heat exchanger | सम-एंट्रॉपी दक्षता / ऊष्मा-विनिमयक |
| free energy (Helmholtz) / free enthalpy (Gibbs) | मुक्त ऊर्जा / मुक्त एंथैल्पी |
| natural variables / Maxwell relations | स्वाभाविक चर / मैक्सवेल संबंध |
| chemical potential / coexistence / Clapeyron | रासायनिक विभव / सह-अस्तित्व / क्लापेरों |
| Boltzmann factor / partition function / scale height | बोल्ट्ज़मान गुणक / विभाजन फलन / मापक ऊँचाई |
| Schottky anomaly / equipartition / Curie's law | शॉट्की विसंगति / समविभाजन / क्यूरी का नियम |
| wave function / Born's rule / probability current | तरंग फलन / बोर्न का नियम / प्रायिकता धारा |
| superposition principle / stationary state / Bohr frequency | अध्यारोपण सिद्धांत / स्थायी अवस्था / बोर आवृत्ति |
| confinement energy / quantisation of energy | परिरोध ऊर्जा / ऊर्जा का क्वांटन |
| evanescent wave (quantum) / tunnel effect / tunnel splitting | क्षयी तरंग (क्वांटम) / सुरंग प्रभाव / सुरंग विपाटन |
| feedback / loop gain / Barkhausen condition | पुनर्भरण / पाश-लब्धि / बार्कहाउज़ेन प्रतिबंध |
| Schmitt trigger / relaxation oscillator / lock-in amplifier | श्मिट ट्रिगर / शिथिलन दोलित्र / लॉक-इन प्रवर्धक |

## Requests for the orchestrator

Four findings, none of which this agent may fix, and all of which affect the
other six editions.

1. **`\foreach \x/\t in {…}` label lists are invisible to every prose gate.**
   `check_hindi_prose.py`, `check_arabic_prose.py` and `check_latin_prose.py`
   all extract node text, `\legend{}` and `\addlegendentry{}` — none of them
   reads a `\foreach` iterator list, yet those strings print. There are two
   sites in the English canon of Book 4: `07-sound-waves.tex:179` (the decibel
   ladder: *threshold of hearing, rustling leaves, quiet room, conversation,
   busy street, lorry at 10 m, rock concert, pain*) and `23-laser.tex:103`
   (*absorption, spontaneous emission, stimulated emission*). Both are
   translated in this tree; **every other edition should be checked**, because
   a gate-clean file can still print English there. The fix in the tooling is
   one regex in `extract_drawing_text`.

2. **Mixed-case chemical formulas tripped the `english` class — fixed in the
   gate, 2026-08-22.** `LATIN_WORD` matches any run of ≥2 Latin letters and
   words of ≥3 letters are flagged; uppercase runs of ≤4 are excused as
   acronyms, but `MgF`, `NaCl`, `AsH`, `GaAs` are not uppercase, and
   `\mbox{MgF}$_2$` still fired (verified). The edition briefly carried an
   empty group (`Mg{}F$_2$`) to silence it; the orchestrator instead added
   `CHEM_FORMULA = (?:[A-Z][a-z]?){2,}` to `check_hindi_prose.py` and
   `check_arabic_prose.py`, and **all five empty groups have been removed** —
   `15-wave-interfaces.tex` (×2), `solutions/15-wave-interfaces.tex`, and
   `31-potential-wells-tunneling.tex` (`AsH$_3$`, `GaAs`). The tree now
   contains **no** `X{}Y` workaround of any kind, the gate is still clean on
   all 62 files, and the rebuild is unchanged. Kept here only as the record of
   why the gate grew that pattern.

3. **Nine English-canon math spans end in a trailing space.** `$xy = $`
   (twice), `$vS = $`, `$y = $`, `$z = $`, `$\sin i/c = $`,
   `$n(r)\cos\theta(r) = $`, `$\varphi = $` and a bare `$= $`, spread over
   `02-fluid-kinematics`, `03-euler-bernoulli`, `04-viscous-flows`,
   `13-plane-waves-polarization`, `16-guided-waves`, `18-scalar-light-model`,
   `26-thermal-radiation` and three of their solution files. The English closes
   the span and sets *const* as upright prose after it; a translation must
   either reproduce the odd span or, as here, write `\text{…}` inside it,
   which every language's math census then reads as a divergence. **This one
   hits all seven editions**, and normalising the canon — close the span after
   the operator, or take the word inside as `\text{const}` — would remove nine
   unavoidable divergences from each of them.

4. **`\pgfmathparse{int(...)}` in `07-sound-waves.tex:182`** produces the
   decibel numbers of the ladder in item 1; it is fine as it stands, but it is
   the reason the `!draw` opt-out there had to cover a printing line rather
   than a comment. Noted so the next person does not "fix" the opt-out away.

5. Finally, `hindi_style_card.md` should record what Book 3 hi already
   learned and this pass re-confirmed: **`आर-पार` is unusable**, because its
   first syllable `आर` is on the `translit` stoplist as English *are*. Use
   `के पार`, `पार` or `भर`. This tree contains none.
