# One Physics Book 3 (University, Year 1) --- Spanish edition: self-score

**Date:** 2026-08-21
**Quality bar:** *native academic* (the bar of `translation_instruction.md`).
**Sense/structure reference:** the English canon (`parts/bachelor-1/*.tex`) for
content; the Spanish Books 1--2 of this series (`parts/grade-*/es/`) and
`../one-math-book/parts/bachelor-1/es/` for the university register.  No
French twin of Book 3 exists yet, so French was used only for *sense* on the
handful of terms Spanish and English name differently (*ditherm*, *monotherm*,
*régime*, *poder de las puntas*).

## Overall: **96 / 100**

| Dimension | Score | Note |
|---|---:|---|
| Register (academic Spanish, weighted) | 96 | Impersonal *se* + subjunctive imperatives (*muéstrese*, *dedúzcase*, *compruébese*) throughout the exercises and proofs, as a Spanish lecture text does; narrative present in the chapter openings. |
| Terminology (weighted) | 96 | Settled per-chapter glossary below; index keys equal the visible terms. |
| MT-artifact freedom (weighted) | 97 | No calqued word order found on sampling; every `\text{...}`, TikZ node, axis label and environment optional title is Spanish (swept mechanically, see *Checks*). |
| Structure | 100 | `check_translation.sh` green; every body written as line-range replacements on the English canon through `tools/id_apply.py`, so labels, `\cref` targets, solution keys, `\qty{}{}`, `\foreach`, `xtick=` and every math display are byte-identical to English. |
| LaTeX hygiene | 99 | 0 errors, 0 undefined references, 0 overfull boxes; UTF-8 accents only. One class of fault was found and fixed (below). |
| Cross-references | 100 | Every `\cref`/`\ref` target byte-identical to English; 12 exercises + 1 weekend problem per chapter, one solution each. |
| Figures | 98 | Drawing code untouched; only node text, axis labels and captions translated. |
| Solutions | 96 | All 30 solution files translated; `\textbf{n.}` numbering and every number preserved. |

## What was produced

- `parts/bachelor-1/es/01`--`30` and `parts/bachelor-1/solutions/es/01`--`30`
  (chapters 01--20 were written in an earlier run of this same job; 21--30 in
  this one, and the whole book was re-gated, re-linked and re-scored here).
- `tools/term_config/book3_es.py` --- curated, not translated.
- Build: 345 pages, `0` errors, `0` undefined, `0` overfull.

## Checks

```
bash tools/check_translation.sh bachelor-1 es      -> TRANSLATION GATE: PASSED
latexmk one_physics_book_3_university_year_1_es.tex
  grep -ac '^!'      -> 0
  grep -aci undefined-> 0
  grep -ac Overfull  -> 0        (345 pages)
python3 tools/link_defined_terms.py --book 3 --lang es --apply
  -> 2400 links across 60 files  (English: 2342 -- 1.02x, not the 2x a
     Romance edition drifts to when the stop list is under-curated)
```

Omterm **target** parity with English: 194 distinct targets in English,
215 in Spanish; only three English targets are missing in Spanish
(`ex:b1:systems-of-points:rolling`, `prop:b1:filters-transfer-functions:highpass1`,
`thm:b1:fluid-statics:fundamental`), each because the Spanish name of the term
happens not to recur verbatim outside its own chapter.  Coverage is therefore
at or above English everywhere else.

No `--force-classes` and no `!class` per-range opt-out was used anywhere in
the book: all ten `id_apply` censuses (labels, envs, solution keys, emph/index
adjacency, index count, math spans, drawing code, per-range `\[ \]`, braces,
surviving `\omterm`) passed unaided on all 60 files.

## Sampled passages

1. **`parts/bachelor-1/es/01-units-dimensions.tex`, opening** ---
   *"En un laboratorio del sótano oscila un péndulo, un cronómetro hace clic y
   un estudiante escribe $g = \qty{9.77}{m/s^2}$. […] La física mide, y una
   medida sin su incertidumbre es un rumor."*
   **Verdict: native.** The inversion *"En un laboratorio del sótano oscila un
   péndulo"* is Spanish word order, not an English calque; *"es un rumor"*
   keeps the English aphorism without translating it word for word.

2. **`parts/bachelor-1/es/12-newton-dynamics.tex`, opening** ---
   *"Un camión en una carretera de montaña avanza a paso lento en una marcha
   corta, sostenido por el mismo rozamiento que le permite detenerse en llano."*
   **Verdict: native.** *marcha corta*, *en llano* are the ordinary Spanish
   expressions; the participial clause is idiomatic.

3. **`parts/bachelor-1/es/23-second-law-entropy.tex`, remark "Cómo leer el
   principio"** --- *"A diferencia de la energía, la entropía no se conserva:
   se \emph{intercambia} con el calor […] y la \emph{crea} todo proceso
   irreversible."*
   **Verdict: native.** The post-verbal subject (*la crea todo proceso
   irreversible*) is exactly the construction a Spanish lecturer writes; a
   machine would have produced *"todo proceso irreversible la crea"*.

4. **`parts/bachelor-1/es/27-potential-capacitors.tex`, theorem
   "Propiedades de un conductor en equilibrio"** --- the four numbered
   properties.
   **Verdict: near-native.** Correct and terse, but the enumerated statements
   are as clipped as the English; a Spanish textbook would sometimes expand
   *"Justo fuera, el campo es normal a la superficie"* into a full clause.
   Deliberate: the series' house style is the terse statement.

5. **`parts/bachelor-1/solutions/es/29-induction.tex`, item 16** ---
   *"rendimiento del $0.08\%$ --- los altavoces son estufas que susurran."*
   **Verdict: native.** The joke survives the crossing, which post-edited MT
   almost never manages.

6. **`parts/bachelor-1/es/30-quantum-introduction.tex`, opening** ---
   *"Envíense electrones de uno en uno a través de dos rendijas y llegarán
   como puntos […] y los puntos van formando, al cabo de miles, las franjas
   de una onda."*
   **Verdict: native.** *de uno en uno*, *al cabo de miles*, *van formando*
   are Spanish idiom, not glosses of "one at a time", "over thousands",
   "build up".

## Settled terminology (chapters 21--30, the part written in this run)

fluid statics *estática de fluidos* · buoyancy *empuje* (de Arquímedes) ·
centre of pressure *centro de presiones* · draught *calado* ·
first/second law *primer/segundo principio de la termodinámica* ·
quasi-static *cuasiestática* · monobaric *monobara* · isochoric *isócora* ·
Clapeyron diagram *diagrama de Clapeyron* · latent heat *calor latente* ·
entropy created/exchanged *entropía creada/intercambiada* ·
entropy diagram *diagrama entrópico* · microstate *microestado* ·
ditherm *ditérmica* · efficiency *rendimiento* · COP *coeficiente de eficacia* ·
cut-off ratio *relación de inyección* · regenerator *regenerador* ·
vapour-compression cycle *ciclo de compresión de vapor* ·
throttling *laminación* · lost work *trabajo perdido* ·
lever rule *regla de la palanca* · quality (vapour fraction) *título* ·
supercooling *sobrefusión* · superheating *sobrecalentamiento* ·
boiling chips *perlas de ebullición* · dew point *punto de rocío* ·
Gauss's law *teorema de Gauss* · pillbox *cilindro achatado* ·
breakdown field *campo de ruptura* · point effect *poder de las puntas* ·
capacitance/capacitor/plates *capacidad / condensador / armaduras* ·
fringing *efectos de borde* · Ampère's law *teorema de Ampère* ·
Amperian loop *contorno de Ampère* · turns *espiras* · winding *devanado* ·
moving-coil galvanometer *galvanómetro de cuadro móvil* ·
self/mutual inductance *coeficiente de autoinducción / de inducción mutua* ·
back-emf *fem contraria* · eddy currents *corrientes de Foucault* ·
voice coil *bobina móvil* · work function *trabajo de extracción* ·
stopping potential *potencial de frenado* ·
uncertainty principle *principio de indeterminación* (kept distinct from
*incertidumbre*, which chapter 1 reserves for measurement uncertainty) ·
ground state *estado fundamental* · quantum dot *punto cuántico* ·
spectral lines *rayas espectrales* · gap *banda prohibida*.

## Faults found and fixed during this pass

- **UTF-8 accents inside a `\qty{}{}` unit argument are a fatal-class bug.**
  siunitx typesets the unit in math mode, where `é` (which inputenc expands to
  `\'e`) is invalid: `\qty{-40}{dB/década}` produced *"Command \\' invalid in
  math mode"* plus a run of `nullfont` characters, i.e. silently dropped
  glyphs. Five sites in chapters 09 and 10 were rewritten as
  `\qty{-40}{dB} por década`. **A Spanish (or French, or Portuguese) edition
  must never put an accented word inside a unit argument.** The same sweep
  caught three English words smuggled into unit arguments by the canon
  (`{years}`, `{turns/m}`, `{protons/s}`); the first was moved out of the
  `\qty` entirely (it cannot be accented in math mode), the other two
  translated in place.
- Three overfull boxes (solutions 08, 09, 13) and, after the chapter 21--30
  work, two more (solutions 08, 26): all the same shape --- a long unbreakable
  inline formula preceded by Spanish prose a few characters longer than the
  English it replaces. Fixed by shortening the prose, never the mathematics.
- One residual English word in prose (`with` in chapter 05), one in a TikZ
  node (`magnet`, ch. 29), one in an axis label (`and`, ch. 30), and two
  English subscripts (`\text{out}`, `\text{or }`, ch. 09).

## Why not 100

- The series' statement style is deliberately telegraphic; in Spanish, whose
  academic prose tolerates a little more connective tissue, a few enumerated
  theorem items (ch. 27, ch. 21) read *correct and terse* rather than
  *written in Spanish first*.
- `\mathrm{}` subscripts are part of the mathematics and are byte-identical to
  English by construction, so a Spanish reader meets `S_{\mathrm{created}}`,
  `S_{\mathrm{exch}}` and `P_{\mathrm{ext}}` (chs. 22--24) in English
  abbreviations. `\text{}` subscripts, which the applier does allow to change,
  were all localised (*cte*, *sal*, *int*, *sum*, *propio*, *núcleo*, …).
- Three defined terms lose their cross-chapter link because their Spanish name
  does not recur verbatim outside the defining chapter (listed above).
- Chapters 01--20 were drafted in an earlier session of this job; they were
  re-swept mechanically here (residual English, `\text{}`, TikZ nodes, unit
  arguments, overfull boxes) and sampled by hand, but not re-read line by
  line.
