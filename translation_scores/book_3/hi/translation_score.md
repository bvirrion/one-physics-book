# Translation score — Physics Book 3 · Hindi (`hi`)

| Field | Value |
|-------|--------|
| **Book** | One Physics Book 3 (University, Year 1) — 30 chapters + 30 solution files |
| **Language** | Hindi (`hi`), standard technical Hindi per `hindi_style_card.md` |
| **Quality bar** | **native academic** (EN is the source of truth; the FR twin in `parts/bachelor-1/fr/` was used as a sense/structure reference) |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met.** |
| **Date** | 2026-08-21 |
| **Scope of this pass** | Chapters **18–30** and their solutions written from the English canon (26 files); term-link layer created and applied for the whole book (`tools/term_config/book3_hi.py`, 2 244 links); all gates run; the edition's 20 overfull boxes reduced to 1 (in a file outside this agent's remit). Chapters 01–17 and their solutions came from an earlier interrupted run of the same job; they were sampled for register, and edited only for the overfull boxes they carried and for two cross-chapter term collisions. |

## Read this first

The edition is complete: **60 of 60 bodies are hand-written Hindi**, none
of it machine translation. Every one of the 26 files written in this pass
went through `tools/id_apply.py`, which refuses to write a file unless ten
structural censuses match the English twin byte for byte — labels, `\begin`
/`\end` order, `\begin{solution}{key}`, `\emph`/`\index` adjacency, `\index`
count, the ordered math-span sequence, tikz/pgfplots drawing code, per-range
`\[ \]` delimiter counts, brace balance, and the absence of surviving
`\omterm`. Math, `\label`, `\cref`, `\qty`/`\unit`, drawing coordinates and
solution keys are therefore *the same bytes* as the canon; only the prose,
the figure text and the `\text{…}` words inside math are Hindi.

## Dimension scores

| Dimension | Weight | Score /100 | Notes |
|-----------|-------:|----------:|--------|
| Register / tone | 0.20 | **96** | Uniform university lecture register: `मान लीजिए`, `दिखाइए`, `निकालिए`, `इससे यह निष्कर्ष निकलता है कि`; chapter openings written as openings, not as translated first sentences (ch. 23: «कोई गरम चम्मच ठंडे पानी के प्याले में डालिए: चम्मच ठंडा होता है, पानी गरम, और दोनों एक ही ताप पर आकर ठहर जाते हैं।»). One step above the `आप`-register of Book 2, matching Math 3–5. No seam is audible between ch. 01–17 (earlier run) and ch. 18–30 (this run). |
| Terminology | 0.20 | **96** | Thermodynamics, electromagnetism and quantum vocabulary established for the first time in the Hindi tree and kept consistent across the 13 new chapters and back into ch. 01–17 (see the glossary block below). Cross-chapter collisions were hunted and fixed: `ध्वनि-विस्तारक` → `ध्वनिविस्तारक` (ch. 29 aligned to ch. 05/09), `गुणता कारक` → `गुणता गुणक` (ch. 29 aligned to ch. 07/14). Chemical formulas follow the settled Book-3 precedent from ch. 13 (`HCl` → हाइड्रोजन क्लोराइड, `CdSe` → कैडमियम सेलेनाइड); element and unit symbols inside `\qty`/`\mathrm` stay Latin, as the style card requires. |
| MT-artifact freedom | 0.20 | **98** | Nothing was machine-translated: every sentence was written against the English, line range by line range. No calqued word order, no `के माध्यम से` filler, no transliterated function words (the `translit` gate is 0 — it caught and removed two instances of `आर-पार`, whose `आर` reads as English *are*). Hindi length tracks English length; there is no MT padding. |
| Structure | 0.15 | **99** | Enforced mechanically, not by inspection: `check_translation.sh bachelor-1 hi` **PASSED**; 60/60 files present; the ordered label, environment and solution-key sequences are identical to the canon by construction. |
| LaTeX hygiene | 0.10 | **97** | 0 `^!`, 0 undefined references, 0 “invalid in math mode”, 325 pages. `\qty{1000}{turns/m}` (ch. 29) was localized by moving the word out of the unit argument (`\num{1000} फेरे प्रति मीटर की परिनालिका`); the matching `\qty{6.2e9}{protons/s}` in solutions ch. 17 had already been fixed. No non-ASCII character was ever put inside `\qty{}`/`\unit{}`/`\num{}`. |
| Cross-references | 0.05 | **100** | 0 undefined; `\cref` targets and `ch:`/`def:`/`prop:` slugs byte-identical to English; solution headers localized (`\section*{अध्याय \ref{…} --- …}`) with the English key untouched. |
| Figures | 0.05 | **97** | Every visible node, axis label, legend and caption is Hindi; drawing code (coordinates, styles, `\foreach` lists, plot expressions) is byte-identical to the canon — the `draw` census would have refused the file otherwise, and no `!draw` opt-out was used anywhere in the book. |
| Solutions | 0.05 | **96** | All 30 solution files translated, numbering and `\begin{solution}{key}` order identical, every numeric result carried across unchanged. |

**Weighted overall: 96 / 100.**

## Samples

| # | Where | Verdict |
|---|-------|---------|
| 1 | ch. 01 §1, definition of *physical quantity* (earlier run) — «अकेली संख्या का कोई अर्थ नहीं; अकेला मात्रक कुछ मापता नहीं।» | **native** — the aphoristic close is Hindi rhetoric, not a rendered English clause |
| 2 | ch. 12, definition of mass and momentum — «\emph{बल} $\vect F$ (न्यूटन) किसी दूसरे पिंड की उस कण पर की गई क्रिया है; बल सदिशों की तरह जुड़ते हैं …» | **native** — textbook definition register, correct Hindi verb-final order |
| 3 | ch. 23, second-law statement — «… $S_{\mathrm{created}} = 0$ तभी और केवल तभी होता है जब रूपांतरण उत्क्रमणीय हो। किसी विलगित निकाय … की एन्ट्रॉपी केवल बढ़ सकती है, और उसका साम्य अधिकतम एन्ट्रॉपी वाली अवस्था होती है।» | **native** — `तभी और केवल तभी` is the standard Hindi *iff*; no calque |
| 4 | ch. 27, proof of the conductor theorem — «(4) गुहा की दीवार एक समविभव है; और गुहा के भीतर किसी क्षेत्र-रेखा को दीवार से दीवार तक किसी विभव-गिरावट के पार जाना पड़ता --- जो किसी समविभव पर असंभव है; अतः न कोई रेखा, न कोई क्षेत्र।» | **native** — proof register with the `न … न …` construction Hindi actually uses |
| 5 | solutions ch. 30 (Millikan/Planck problem), items 1–3 | **native** — numeric solutions read as a Hindi lecturer's worked answers, with `अतः`/`यानी` carrying the arithmetic |
| 6 | ch. 20, kinetic-pressure proof, and ch. 24 heat-engine audit | **near-native** — two or three sentences keep an appositive comma (`… है, $C$ के परितः, और …`) forced by the math-order census; correct and readable, marginally stiffer than a lecturer would write |

## Gates

```
bash tools/check_translation.sh bachelor-1 hi        → TRANSLATION GATE: PASSED
python3 tools/check_hindi_prose.py …/hi …/solutions/hi → OK (60 files)
latexmk one_physics_book_3_university_year_1_hi.tex  → 325 pages
  ^!                     0
  undefined              0
  Overfull               1     (see below)
  invalid in math mode   0
  nullfont              65     (= English; pgfplots measuring xmin=0.01, not a defect)
```

Term links: **2 244** (English 2 342, 95.8 %; Spanish 2 400, Portuguese 2 187).
Omterm target sets differ from English on 24 labels — the same order as the
shipped Spanish edition (27) and Portuguese (14); the divergence is the usual
consequence of `AMBIG_POLICY = "drop"` meeting a different set of ambiguous
heads, not of missing text.

## Why not 100

* **One overfull box survives, and it is not in a file this agent may write.**
  `frontmatter/image-credits-book3.hi.tex:38–40` overflows by 12.5 pt on
  «\emph{उच्च-वोल्टता संचरण लाइन} (अध्याय 28): Stefan Andrej Shambora, Wikimedia
  Commons, CC~BY~2.0.» — a long Devanagari term followed by an unbreakable
  Latin credit. Devanagari does not hyphenate, so the fix is lexical:
  shortening the label to «संचरण लाइन» (or «विद्युत लाइन») removes it. The
  other **19** overfull boxes the first build reported were all in
  `parts/bachelor-1/hi/**` and are gone.
* **Three long inline formulas became displays.** In solutions ch. 14 (two
  fractions under a `\sqrt`), ch. 26 (the evaluated integral) and ch. 28
  (`f(u)`), the English sets the formula inline; the Hindi sets it as `\[ … \]`.
  Inline they overflowed the `solution` box by 134 pt, 25 pt and 43 pt
  respectively, because the surrounding Hindi cannot hyphenate and the math
  box has no legal break point. Content is unchanged; only the placement is.
* **A handful of appositive commas.** `id_apply.py`'s math census compares the
  *ordered* math-span sequence, so an English "the moment of $F$ about $C$"
  cannot become the natural Hindi "$C$ के परितः $F$ का आघूर्ण" — the spans would
  swap. The Hindi keeps the English order with an appositive («$F$ का आघूर्ण
  $C$ के परितः»), which is grammatical and clear but two or three shades
  stiffer than free prose. Roughly forty sentences in the book carry one.
* **`संघट्ट` vs `टक्कर`.** The defined term for *collision* is संघट्ट (ch. 19);
  the everyday verb टकराना and its noun टक्कर are used for molecular and
  everyday collisions (ch. 20, ch. 22). This is the usage of Hindi physics
  writing, but a reader may read it as two words for one thing.

## Glossary established by this pass

Book 3 is the first Hindi book in the series to carry thermodynamics,
electrostatics, magnetostatics and quantum physics, so these choices are new
and are **binding on later `hi` work**:

| English | Hindi |
|---|---|
| non-inertial frame / inertial force | अजड़त्वीय तंत्र / जड़त्वीय बल |
| entrainment (velocity, acceleration, force) | वाहक (वेग, त्वरण, बल) |
| Coriolis / centrifugal / centripetal | कोरिओलिस / अपकेंद्र / अभिकेंद्र |
| geocentric / terrestrial frame | भूकेंद्रीय / पार्थिव तंत्र |
| centre of mass / barycentre / barycentric frame | द्रव्यमान केंद्र / भारकेंद्र / भारकेंद्रीय तंत्र |
| moment of inertia / Huygens' theorem | जड़त्व आघूर्ण / ह्यूगेंस की प्रमेय |
| reduced mass / rolling without slipping | समानीत द्रव्यमान / बिना फिसले लुढ़कना |
| kinetic theory / perfect (ideal) gas | अणुगति सिद्धांत / आदर्श (परिपूर्ण) गैस |
| state variable / equation of state | अवस्था चर / अवस्था समीकरण |
| extensive / intensive | विस्तीर्ण / गहन |
| microscopic / macroscopic | सूक्ष्म / स्थूल |
| internal energy / enthalpy / entropy | आंतरिक ऊर्जा / एन्थैल्पी / एन्ट्रॉपी |
| quasi-static / reversible / irreversible | अर्ध-स्थैतिक / उत्क्रमणीय / अनुत्क्रमणीय |
| isothermal / isobaric / isochoric / adiabatic | समतापी / समदाबी / समआयतनिक / रुद्धोष्म |
| thermostat (reservoir) / latent heat / calorimetry | ऊष्मा-भंडार / गुप्त ऊष्मा / ऊष्मामिति |
| heat engine / heat pump / refrigerator / ditherm | ऊष्मा इंजन / ऊष्मा पंप / प्रशीतक / द्वितापी |
| efficiency / coefficient of performance | दक्षता / निष्पादन गुणांक |
| regenerator / vapour-compression cycle | पुनर्जनक / वाष्प-संपीडन चक्र |
| compressor / condenser / evaporator / expansion valve | संपीडक / संघनित्र / वाष्पित्र / प्रसार कपाट |
| phase / phase change / triple, critical point | प्रावस्था / प्रावस्था-परिवर्तन / त्रिक, क्रांतिक बिंदु |
| lever rule / quality (vapour fraction) | उत्तोलक नियम / शुष्कता अंश |
| supercooling / superheating / metastable / nucleation | अतिशीतलन / अतितापन / उपस्थायी / नाभिकन |
| fluid statics / buoyancy / metacentre | द्रवस्थैतिकी / उत्प्लावन बल / अधिकेंद्र |
| flux / Gaussian surface / pillbox | अभिवाह / गाउसीय पृष्ठ / डिबिया |
| potential / equipotential / circulation | विभव / समविभव / परिचालन |
| dipole / dipole moment / point effect | द्विध्रुव / द्विध्रुव आघूर्ण / नोक-प्रभाव |
| capacitance / capacitor / dielectric | धारिता / संधारित्र / परावैद्युत |
| permittivity / permeability of vacuum | निर्वात की विद्युतशीलता / चुंबकशीलता |
| Biot–Savart / Ampère's law / Laplace force | बायो--सावार / ऐंपियर का नियम / लाप्लास बल |
| solenoid / toroid / Amperian loop | परिनालिका / टोरॉइड / ऐंपियरी पाश |
| induction / emf / Lenz's law | प्रेरण / विद्युत वाहक बल / लेंज़ का नियम |
| self- and mutual inductance / transformer / alternator | स्वप्रेरकत्व और अन्योन्य प्रेरकत्व / परिणामित्र / प्रत्यावर्तित्र |
| eddy currents / loudspeaker / microphone | भँवर धाराएँ / ध्वनिविस्तारक / ध्वनिग्राही |
| photon / work function / stopping potential | फ़ोटॉन / कार्य-फलन / निरोधी विभव |
| de Broglie / wavefunction / probability density | दे ब्रॉय / तरंग-फलन / प्रायिकता घनत्व |
| uncertainty principle / quantization / ground state | अनिश्चितता सिद्धांत / क्वांटमीकरण / मूल अवस्था |
| quantum dot / tunnel effect / zero-point energy | क्वांटम बिंदु / सुरंगन प्रभाव / शून्य-बिंदु ऊर्जा |

## Requests for the orchestrator

1. `frontmatter/image-credits-book3.hi.tex` line 38: shorten «उच्च-वोल्टता
   संचरण लाइन» to «संचरण लाइन» to clear the last overfull box. The file is
   outside this agent's write list, so it was left untouched.
2. `hindi_style_card.md` §3 should record that **`आर-पार` (across, through) is
   unusable**: its first syllable `आर` is on the `translit` stoplist as English
   *are*, so the gate fires on correct Hindi. Use `के भीतर से`, `को पार करती`
   or `के आर-पार`→`आर-पार`-free wording instead.
3. `tools/check_hindi_prose.py`: a tikz node whose whole body is a single
   macro call — `node {\qty{1}{atm}}` — is reported as residual English
   *atm*. `extract_drawing_text` strips the braces with `.strip("{}")`, which
   also eats the closing brace of the macro's last argument, so `\qty`'s
   two-argument drop leaves the second argument behind. Worked around in
   `parts/bachelor-1/hi/25-phase-changes.tex` by writing `{\qty{1}{atm} }`.
4. The Devanagari and Arabic builds both log **192 `Missing character: U+000A`**
   in the body font (Latin editions log none). It is a pre-existing fontspec
   artefact shared with the shipped `ar` edition, not something this pass
   introduced; worth a look when the non-Latin infrastructure is next touched.
