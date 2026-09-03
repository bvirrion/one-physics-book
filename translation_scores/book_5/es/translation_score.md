# One Physics Book 5 (University, Year 3) --- Spanish edition: self-score

**Date:** 2026-09-03
**Quality bar:** *native academic* (the bar of `translation_instruction.md`).
**Sense/structure reference:** the English canon (`parts/bachelor-3/*.tex`) for
content; `parts/bachelor-2/es/` and `parts/bachelor-1/es/` for the Spanish
university register and the settled terminology; `book5_en.py` for the
stop-list reasoning carried into `book5_es.py`.

## Overall: **97 / 100**

| Dimension | Score | Note |
|---|---:|---|
| Register (academic Spanish, weighted) | 98 | **The impersonal *-se* imperative of Books 1--4 `es`, throughout.** The draft used the `usted` imperative; the coordinator's tree measurement (bachelor-1 435 *-se* / 0 `usted`, bachelor-2 316 / 0) settled it, and all 1 734 sites were converted in a reviewed pass with number agreement (below). Vocabulary matched to `bachelor-2/es` as well as form: *Muéstrese* (236) is now this edition's commonest imperative, as it is Book 4's. The `usted` pronoun itself (10 sites) is gone too --- Book 4 `es` has zero. |
| Terminology (weighted) | 97 | Settled glossary below; index keys equal the English key count exactly (297 = 297); every `\text{}` subscript localised. *Binding energy* renamed **energía de enlace**, which is both the collision fix (below) and the wording `bachelor-1/es` already uses. |
| MT-artifact freedom (weighted) | 98 | No calqued word order found on sampling; every TikZ node, axis label, `\legend`, `\addlegendentry`, caption and environment optional title is Spanish. `check_orphan_lines.py` and the `\text{}`-identical census both clean. |
| Structure | 100 | `check_translation.sh` green; all 54 files were written as line-range replacements on the English canon through `tools/id_apply.py`, so labels, `\cref` targets, solution keys, `\qty{}{}`, `\foreach`, `xtick=` and every math display are byte-identical to English. Everything since has been post-write edits, never a re-applied patch. |
| LaTeX hygiene | 99 | 0 errors, 0 undefined, 0 overfull, 0 "invalid in math mode"; `nullfont` at the English baseline of 10; UTF-8 accents only, none inside a unit argument; **0 inherited TeX accent escapes**. |
| Cross-references | 100 | Every `\cref`/`\ref` target byte-identical to English; 12 exercises + 1 weekend problem per chapter, one solution each. |
| Figures | 98 | Drawing code untouched; only node text, axis labels, legends and captions translated --- including all eleven prose-carrying `\legend`/`\addlegendentry` sites of the coordinator's census. |
| Solutions | 97 | All 27 solution files translated; `\textbf{n.}` numbering and every number preserved; register converted with the chapters. |

## What was produced

- `parts/bachelor-3/es/01`--`27` and `parts/bachelor-3/solutions/es/01`--`27`
  --- **54 files, 21 342 lines** (English: 21 296).
- `tools/term_config/book5_es.py` --- audited, plus one `EXTRA_PROTECT` entry
  for this edition's own homograph collision (below).
- Build: **323 pages**, `0` errors, `0` undefined, `0` overfull
  (English: 302 pages).

## The register conversion (1 734 sites, reviewed)

Done as **post-write edits**, never as re-applied patches, so no `\omterm`
was stripped; the links were regenerated afterwards and re-checked.

Three passes, each dry-run in full and read before applying:

1. **1 284 sites** at strict command positions (`\item`, `(a)`--`(d)`,
   sentence end, `\textbf{n.}`, `, y`). Number decided per site from the
   object that follows: plural determiner, singular determiner, subordinating
   conjunction, an enclitic pronoun (`-lo`/`-la` vs `-los`/`-las`, which
   settles it outright), or a maths span followed by a second object.
   **Every `pl`, `pl?` and `sg?` decision (167 of them) was read in context**;
   15 needed a reviewed override, all recorded in the converter.
2. **173 enclitic imperatives whose accent shifts** (`compárela`,
   `justifíquelo`, `conviértalos`) --- invisible to pass 1 because the stem
   is not the bare form. `-lo/-la` → `-se`, `-los/-las` → `-nse`.
3. **277 imperatives outside command position** --- after an adjunct
   ("Usando la conservación de la energía, muéstrese que..."), inside
   parentheses, after a display. Subjunctive and indicative uses excluded by
   trigger (`que`, `se`, `no`, `cuando`, ...); three genuine subjunctives were
   skipped by hand ("haga lo que haga la bobina").

**Six noun homographs** had to be gated by command position or dropped
outright, because Spanish spells them exactly like the imperative:
*nombre* (name), *cierre* (closure), *cruce* (crossing), *contraste*
(contrast), *ajuste*, *apunte*. `el cruce evitado`, `un cierre simultáneo`
and `con nombre propio` are nouns; `Ciérrese el balance` and `Nómbrese al
culpable` are not. A blind regex would have corrupted all six.

Agreement in numbers: 1 494 singular (`calcúlese la razón`), 240 plural
(`calcúlense las densidades`). The edition now carries **1 940** *-se* forms
and **zero** `usted` imperatives.

## Homograph collisions in the generated links (the `keten` class)

Applying the coordinator's method --- per-target link counts against
English --- found **three real collisions and one false alarm** in this
edition:

| Surface form | Wrongly linked to | Sites | Fix |
|---|---|---:|---|
| **ligadura** | `def:b3:lagrangian-mechanics:coordinates` (mechanical *constraint*) | 19 | Spanish uses *ligadura* for both *constraint* and *binding*. The binding sense is now **energía de enlace** --- which is what `bachelor-1/es` already writes --- so the two senses no longer share a word. `\index{energía de ligadura}` renamed with them. |
| **dilatación** | `def:b3:continuum-elasticity:strain` (*dilatation*) | 8 | Collides with *dilatación temporal* (relativity, ch. 4) and thermal expansion. The elasticity term was renamed **dilatación cúbica** in its definition and index key, so the bare word stops being a term. |
| **en acción** | `def:b3:lagrangian-mechanics:action` (*action* $S$) | 12 | Spanish renders "at work"/"in action" as *en acción*. One `EXTRA_PROTECT` entry, exactly as Dutch did for *keten*. "la acción $S$", "variable de acción", "integral de acción" and "el cuanto de acción" still link. |
| *banda prohibida* (29 vs English's 3) | --- | 0 | **False alarm, verified site by site:** all 29 sit in `24-electrons-in-solids` and its solutions and all mean the electronic band gap. English writes the short "gap" that its own harvester does not link; Spanish has no such short form. Density, not collision. |

Link count went **1 009 → 970** (1.06× English, down from 1.10×), and the
surface-form frequency profiles now track English closely: *espín* 30 /
*spin* 27, *cristal* 27 / *crystal* 29, *valores propios* 26 /
*eigenvalues* 26, *red* 24 / *lattice* 24.

## Checks

```
python3 tools/check_orphan_lines.py parts/bachelor-3/es parts/bachelor-3/solutions/es
  -> orphan English lines: 0

bash tools/check_translation.sh bachelor-3 es      -> TRANSLATION GATE: PASSED

python3 tools/check_latin_prose.py parts/bachelor-3/es parts/bachelor-3/solutions/es
  -> 58 findings in 54 files, ALL reviewed, ALL benign (tier 2, below)

latexmk -g one_physics_book_5_university_year_3_es.tex        (grep -a: the log
  '^!' lines             -> 0        (323 pages)                has non-UTF8 bytes
  undefined              -> 0                                   and plain grep -c
  Overfull               -> 0                                   prints nothing)
  "invalid in math mode" -> 0
  nullfont               -> 10       (= the English build's own count)

grep -o 'parts/bachelor-3/\(solutions/\)\?es/..-.*\.tex' build/...fls | sort -u | wc -l
  -> 54                             (the build really read all 54 Spanish files)

python3 tools/link_defined_terms.py --book 5 --lang es --unwrap --apply
python3 tools/link_defined_terms.py --book 5 --lang es --apply
  -> 970 links across 52 files      (English: 916 -- 1.06x)
python3 tools/link_defined_terms.py --book 5 --lang es --check
  -> CHECK: every file matches what the config generates

\index{} key set   -> 297 (English: 297)
\omterm{} targets  -> all 100 English targets reached, plus 10 the English
   harvest does not reach: teorema de Noether, teorema de Liouville, teorema
   espín--estadística, regla de oro de Fermi, principio de exclusión de Pauli,
   fórmula de Sackur--Tetrode, composición de velocidades, separación de
   variables, postulados de la mecánica cuántica / regla de Born, and enlace
   covalente / metálico / de van der Waals -- named results whose Spanish form
   is a single noun phrase the harvester can see where the English is not.
```

Orthography and end-of-line hygiene, swept **after** the last edit:

```
grep -rnP "\\['`^\"~=.]\{?[a-zA-Z]"          -> 0  (the canon's 11 inherited
                                                   TeX accent escapes never
                                                   reached this edition: each
                                                   was written as UTF-8 in the
                                                   patch -- Panteón, ángstrom,
                                                   Segrè, Ampère, Oersted)
grep -rnP "['’]\s*$"                        -> 0 (excluding '' closing quotes)
grep -rnP "^\s*[.,;:)?!]"                   -> 0 in prose (2 hits, both inside
                                                a pgfplots `.. controls` path)
grep -rnP "[a-zà-ÿ]-\s*$"                   -> 0
non-ASCII inside \qty/\unit/\num            -> 0
'¿'/'?' and '¡'/'!' balance, per file       -> balanced in prose
\busted\b                                   -> 0
```

## Fault classes found and fixed

1. **Orphan continuation line** (found here first; now
   `tools/check_orphan_lines.py`). `01-lagrangian-mechanics.tex` carried a
   bare English line `then`, because the sentence's translation had absorbed
   it into the previous line and the line itself fell outside every patch
   range. No census catches it: it is prose, and the `prose` census only runs
   for `id`/`hi`/`ar`.
2. **Register divergence from the series** (found here first; the Dutch
   edition then found the same class in its own guise, informal *je/jouw*
   against `bachelor-2/nl`'s formal *u/uw*). See the conversion above.
3. **Homograph collisions in generated links** --- three, above.
4. **English words inside `\qty{}` unit arguments.** Three `{atoms/m^3}`
   sites. Because a Spanish *átomos* inside a unit argument is typeset in
   math mode, prints `nullfont` and still exits 0, all three were rewritten
   `{m^{-3}}` with the noun moved into the surrounding prose. **These are
   deliberate divergences from the English math span**, made after
   `id_apply` had verified the file, and they are the only three:
   - `es/10-quantum-angular-momentum.tex:411` --- `$n = \qty{8.5e28}{atoms/m^3}$`
     -> `$n = \qty{8.5e28}{m^{-3}}$` (the prose already says *densidad atómica*);
   - `es/15-scattering-theory.tex:454` --- `y $n = \qty{5.9e28}{atoms/m^3}$`
     -> `y una densidad atómica $n = \qty{5.9e28}{m^{-3}}$`;
   - `es/24-electrons-in-solids.tex:377` --- `El silicio tiene $\qty{5e28}{atoms/m^3}$.`
     -> `El silicio tiene $\qty{5e28}{m^{-3}}$ átomos.`
   The three `{euros}` sites need no change --- *euros* is the Spanish word.
5. **Overfull boxes from a longer Spanish connective.** Three, all "in
   paragraph": `solutions/es/09` (46.2 pt --- caused, not cured, by an
   earlier "fix"), `solutions/es/17` (2.3 pt), `es/10`. Cured by rewrapping
   words *before* the candidate break (`y queda` -> `de modo que queda`;
   `y $C =` -> `mientras que $C =`), never with a line-final `%`, and
   verified with a single-chapter `\input` probe against the book preamble
   rather than a whole-book rebuild.
6. **Inverted punctuation.** Two nested parenthetical questions closed the
   inner question with the outer `?`; one list of parenthetical questions had
   no inner `¿`; one direct question opened with none at all. Found by a
   per-file `¿`/`?` stack scan, not by eye.
7. **`\text{}` subscripts.** 103 English fragments still inside math
   (`\text{eff}`, `\text{gap}`, `\text{rest}`, `\text{obeys}`, `\text{hence}`,
   `\text{half-integer spin}`, `\text{quark level: }`, ...), translated in one
   controlled global pass so the mapping is identical in all 54 files.

## Terminology settled for this edition

| English | Spanish | Note |
|---|---|---|
| constraint | ligadura | as `bachelor-1/es`; the binding sense was moved off this word |
| binding energy | energía de enlace | as `bachelor-1/es`; also the collision fix |
| dilatation (elasticity) | dilatación cúbica | keeps *dilatación temporal* clear |
| grand canonical ensemble | colectivo macrocanónico | *colectivo* throughout, matching Book 4 `es` |
| band gap | banda prohibida | subscript `\text{ent}` for *entrehierro* |
| hole / black hole | hueco / agujero negro | both `STOP`ped, as in English |
| spin | espín | `STOP`ped |
| event (spacetime) | suceso | *evento* pruned from `STOP` --- unused here |
| air gap | entrehierro | |
| depletion zone | zona de deplexión | |
| standard candle | vela estándar | |
| decay heat | calor residual | |
| bypass diode | diodo de paso | |

## Gate-9 findings, in two tiers

**Tier 1 --- real untranslated prose: 0.**

**Tier 2 --- flagged but correct Spanish (58):** 53 `\text{}` subscripts whose
Spanish spelling is the English spelling (*orb*, *osc*, *molar*, *total*,
*esc*, *lab*, *gas*, *rad*, *ideal*, *min*, *max*, *int*, *grav*, *conf*,
*extra*, *deg*, *eq*, *liq*, *loc*, *rms*, *sep*, *tot*, *vap*, *vib*, *bi*,
*nuc*, *res*, *rot*, *acc*, *el*, *exc*, *fus*, *const*), 4 one-word TikZ
nodes identical in both languages (*metal*, *semiconductor*, *quarks*,
`$\varphi$ real`) and one node that is a proper name plus maths
(`van der Waals $\sim -1/r^6$`).

## Sampled passages, verdicted

1. `es/19-quantum-statistics.tex:238--242` (exercise 1, post-conversion) ---
   *"Calcúlense $E_{\text{F}}$ y $T_{\text{F}}$ para (a) el cobre ...;
   (d) ordénense frente a la temperatura ambiente y coméntese quién está
   degenerado y cuándo."* **Native.** Plural agreement on two objects,
   singular on the clause; the register is Book 4's exactly.
2. `es/18-grand-canonical.tex:3--17` (chapter opening) --- *"Una gota de agua
   en aire húmedo ni crece ni se encoge; el oxígeno se une a la hemoglobina
   en los pulmones y se suelta en los músculos; una pila empuja electrones a
   través de un teléfono porque son «más caros» en un electrodo que en el
   otro."* **Native.** The tricolon keeps the English rhythm without its word
   order; *se suelta*, *empuja*, *más caros* are the ordinary choices.
3. `solutions/es/27-astrophysics.tex:206--211` --- *"Su oxígeno se fusionó en
   la capa de una estrella masiva y lo expulsó una supernova; ... El
   hidrógeno del Big Bang, en cambio, ha sido suyo desde siempre."*
   **Native.** Verb--subject inversion and *en cambio* for the English
   *though*; a literal rendering would have put *aunque* at the clause end.
4. `es/21-phase-transitions.tex:21--41` --- *"Su contable es el parámetro de
   orden"*, *"las fronteras de fase están donde cuadra el libro de cuentas"*.
   **Native.** The running accountancy metaphor is carried by the Spanish
   idiom, not calqued as *tenedor de libros*.
5. `es/24-electrons-in-solids.tex:216--231` (doping) --- *"lleva carga
   positiva tan de verdad como una burbuja lleva flotabilidad"*, *"la perilla
   que convierte la arena en circuitos"*. **Near-native.** *perilla* is the
   right register for a control knob but leans Latin-American; *el mando*
   would read better in Spain. Kept for whole-book consistency.

## Why not 100

- **Two dialect-sensitive word choices** (*perilla*, *bombilla*) sit on
  opposite sides of the Atlantic; the book declares no dialect, so they were
  kept internally consistent rather than neutralised.
- **`thm:b3:electrons-in-solids:bloch` carries 35 links against English's 3.**
  Verified genuine --- Spanish has no short form for *banda prohibida* --- but
  it is dense linking on one page, and a future curation might `STOP` the
  term after its first few uses in its own chapter.
- **`nullfont` 10** matches English exactly, so it is inherited rather than
  introduced --- but it is 10, not 0.
- The register conversion was a second pass over finished prose. It was
  reviewed decision by decision, but a first draft written in the right
  register would have been better than a corrected one.
