# One Physics Book 4 (University, Year 2) --- Portuguese edition: self-score

**Date:** 2026-08-22
**Variety:** Brazilian Portuguese (`pt` = pt-BR across the whole series).
**Quality bar:** *native academic* (the bar of `translation_instruction.md`).
**Sense/structure reference:** the English canon (`parts/bachelor-2/*.tex`) for
content and labels; the Portuguese Book 3 (`parts/bachelor-1/pt/`) for the
university register, the settled glossary and the term-link conventions
(`AMBIG_POLICY = "drop"`). The six sibling editions of this same book were
being written concurrently in the same working tree and were **not** used as a
reference; the English canon was the only twin consulted.

## Overall: **96 / 100**

| Dimension | Score | Note |
|---|---:|---|
| Register (academic Brazilian Portuguese, weighted) | 96 | Narrative present in the chapter openings, impersonal/imperative in the methods and exercise stems (*escreva*, *deduza*, *mostre*, *compare*, *estime*). Subject pronouns dropped throughout: **0** occurrences of the MT tell *"Nós temos / Nós podemos / Nós vamos / Nós devemos"* across 62 files. |
| Terminology (weighted) | 96 | Glossary below, continuous with the Book 3 pt edition. All 65 adjacent `\emph{...}\index{...}` pairs checked mechanically: 0 real mismatches (3 flagged, all exact mirrors of the English canon's own singular/`!`-subentry keys). |
| MT-artifact freedom (weighted) | 95 | Gate 9 run over all 62 files: after fixing the 14 real defects listed below, every remaining hit is a true Portuguese cognate or abbreviation (*sat*, *liq*, *vap*, *fus*, *evap*, *cond*, *mol*, *esc*, *diss*, *vib*, *rev*, *sub*, *tel*, *nat*, *ppm*, *real*, *volume*, and the nodes *laser*, *sensor*, *chip*, *circular*, *plasma*, *zero*, *natural*). |
| Structure | 100 | `check_translation.sh bachelor-2 pt` green. Every one of the 62 files was written as line-range replacements on the English canon through `tools/id_apply.py`, so labels, `\cref` targets, solution keys, every math span, every `\qty{}{}` and all drawing code are byte-identical to English. 31 chapters, 372 exercises, 31 weekend problems, 403 solutions --- the English counts exactly. |
| LaTeX hygiene | 100 | 0 errors, 0 undefined references, **0 overfull boxes**, 0 *"invalid in math mode"*; nullfont 60, i.e. the English build's own baseline, not one above it. UTF-8 accents only; no non-ASCII character inside any `\qty{}`/`\unit{}`/`\num{}` argument (checked by script over all 62 files). |
| Cross-references | 100 | Every `\cref`/`\ref` target byte-identical to English; 12 exercises + 1 weekend problem per chapter, one solution each. |
| Figures | 97 | Drawing code untouched; only node text, axis strings, `\legend`/`\addlegendentry` and captions translated. Two figure strings (`(arb.)`, `(normalised)`) and one `\foreach` label list needed a post-write pass because no census or gate could see them at drafting time --- see "Cross-cutting findings". |
| Solutions | 96 | All 31 solution files translated; `\textbf{n.}` numbering and every number, unit and formula preserved. |
| Term links | 96 | 1 335 links over 145 targets against English's 1 231 over 143 (1.08x). **Every one of English's 143 targets is reached**; the two extra and the five per-target gaps are each explained below. |

## What was produced in this run

- 31 chapter bodies and 31 solution files in `parts/bachelor-2/pt/` and
  `parts/bachelor-2/solutions/pt/`, drafted chapter-by-chapter (body, then its
  solutions twin, then `id_apply` green before starting the next).
- `tools/term_config/book4_pt.py` --- curated from this edition's own harvested
  term list against `book4_en.py`, replacing the Book 3 seed that had been
  copied into place. The uncurated seed produced 1 332 links but reached only
  139 of English's 143 targets and invented one; the curation reaches all 143.
- This score file.

## Checks

```
bash tools/check_translation.sh bachelor-2 pt        -> TRANSLATION GATE: PASSED
python3 tools/check_latin_prose.py parts/bachelor-2/pt parts/bachelor-2/solutions/pt
                                                     -> no true positive left
python3 tools/link_defined_terms.py --book 4 --lang pt --check
                                                     -> CHECK: every file matches
latexmk -g one_physics_book_4_university_year_2_pt.tex
  lines starting '!'              -> 0
  undefined                       -> 0
  Overfull                        -> 0        (357 pages; English 345, fr 359,
                                               nl 355, hi 353, id 350, ar 342)
  'invalid in math mode'          -> 0
  nullfont                        -> 60       (identical in the English build:
                                               pgfplots measuring a log axis,
                                               not a defect)
  distinct pt sources in the .fls -> 62       (31 + 31: the book really is
                                               reading the Portuguese tree)
```

The `.fls` count is the honesty check: `\ominput` silently falls back to the
English file when the translated one is missing, so a green log proves nothing
on its own. 62 distinct `parts/bachelor-2/pt/**` paths in the dependency list
is the proof that no chapter is quietly English.

## Term links: parity with English

|  | English | Portuguese |
|---|---:|---:|
| links | 1 231 | 1 335 (1.08x) |
| distinct targets | 143 | 145 |
| English targets not reached | --- | **0** |

Two targets exist here that English has none for, and five per-target counts
differ by six or more. Each was inspected:

* `+15  thm:b2:gratings:nwaves` (en 5, pt 20). English writes *principal
  maxima* / *secondary maxima* and has no `DERIVED` entry for the irregular
  English plural, so its own plurals go unlinked; Portuguese lists
  `"máximo principal": ("máximos principais",)` and links all 20. Portuguese is
  the more complete of the two here.
* `+12  def:b2:dispersion-wave-packets:complex` and `+7  ...:relation`.
  *atenuação*, *onda evanescente* and *relação de dispersão* recur more often
  in Portuguese prose than their English equivalents, which the English text
  more often replaces with a pronoun or a bare symbol.
* `-7  def:b2:maxwell-equations:operators` (en 44, pt 37). Deliberate.
  Portuguese splits what English spells one way: *divergente* is the vector
  operator of ch. 11, *divergência* is the angular spread of a laser beam in
  ch. 23. The English canon, having a single word, links nine ch. 23 **beam**
  divergences to the operator definition. Adding *divergência* as a derived
  form would faithfully reproduce an English mis-link; it is deliberately
  absent, and the config says so.
* `+6  thm:b2:rigid-body-mechanics:coulomb`: *atrito estático/cinético* is
  repeated where English says "it" or "friction".
* `prop:b2:dispersion-wave-packets:lossy` (pt 4, en 0) and
  `prop:b2:schrodinger-wave-functions:free` (pt 3, en 0): *condição de
  Heaviside*, *lei dos quadrados de Kelvin* and *pacote de onda* recur in
  Portuguese where the English phrases do not; in English the last of the
  three is additionally suppressed as "defined twice".

Four English targets were **missing** in the first curated pass and were each
recovered rather than written off:

| target | why it was lost | fix |
|---|---|---|
| `rem:b2:rigid-body-mechanics:motions` | *rotação em torno de um eixo fixo* is six words; English's *rotation about a fixed axis* is five, and `MAX_TERM_WORDS = 5` | `EXTRA` (not subject to the cap) |
| `prop:b2:michelson:measure` | *espectroscopia por transformada de Fourier* is 41 characters against `MAX_TERM_CHARS = 40` | `EXTRA` |
| `met:b2:rigid-body-mechanics:incline` | the index key is *descida de um plano inclinado*; the caption said *que desce um plano inclinado* | caption reworded to the noun phrase |
| `prop:b2:scalar-light-model:intensity` | the term is *fluxo de fótons*; the exercise said *Fluxo mínimo de fótons* | word order changed to *Fluxo de fótons mínimo* |

`tensão`, which the coordinator flagged: **both senses are in this volume**
(the rope tension of ch. 1, the voltage of chs. 8--10), and neither is
linkable, because Book 4 never harvests bare *tensão* --- only *tensão
superficial* and *tensão de cisalhamento*. The twenty-pattern `EXTRA_PROTECT`
block that Book 3 pt needed is therefore inert here and was removed, leaving
`EXTRA_PROTECT = []` exactly as in `book4_en.py`. The same reasoning retired
Book 3's protections for *resistência do ar* and *potências de dez*: neither
bare noun is a Book 4 term.

One Book 3 seed entry was actively dangerous and was deleted: an `EXTRA` for
*comprimento de onda de De Broglie* pointing at
`thm:b1:quantum-introduction:debroglie` --- a **Book 3** label. Kept, it would
have wrapped a term on a target that does not exist in this volume and put an
undefined reference in the log.

## Sampled passages

**A. Chapter 28 opening (thermodynamic potentials) --- native.**

> Estique depressa um elástico e encoste-o no lábio: ele está quente;
> deixe-o contrair e ele está frio. Pendure um peso nele e aqueça-o com um
> secador de cabelo: ele *encurta*. Nenhuma mola de aço se comporta assim, e a
> razão é que a tensão de um elástico não é questão de energia, mas de
> entropia --- as cadeias esticadas têm menos maneiras de se arranjar.

Imperative openings with enclitic pronouns (*encoste-o*, *deixe-o*, *aqueça-o*)
are the Brazilian lecture register; *não é questão de X, mas de Y* is idiomatic
and not a calque of *is not a matter of*.

**B. Chapter 24 example (how long diffusion takes) --- native.**

> Açúcar através de uma xícara de chá não mexida, $L = \qty{5}{cm}$:
> $2.5 \times 10^{-3}/5 \times 10^{-10} = 5 \times 10^6\,\unit{s}$, dois meses
> --- mexa.

The one-word imperative punchline (*--- mexa.*) reproduces the English *--- stir.*
without the flatness a literal rendering would have had.

**C. Chapter 31 opening (tunnelling) --- native.**

> Uma bola numa tigela vai e vem com a energia que lhe deram; um elétron num
> átomo, um núcleon num núcleo, um elétron num cristal de tamanho nanométrico
> só podem ter certas energias, e a mais baixa delas não é zero.

*vai e vem*, *lhe deram* (impersonal third-person plural) and the contracted
*num/numa* are all unforced Brazilian usage.

**D. Solutions to chapter 27, final item --- native.**

> Desenhe o volume de controle; a massa que entra é igual à que sai; ... monte
> os componentes e compare com Carnot.

Crase (*à que sai*) correct; imperative chain matches the English summary.

**E. Chapter 25 method box --- near-native.**

> (1) Estacionário: monte o circuito térmico --- paredes $e/\lambda S$,
> películas $1/hS$, cascas $\ln(r_2/r_1)/2\pi\lambda\ell$; série e paralelo.

Correct and idiomatic but telegraphic, because the English is: the method boxes
are the one place where the source's compression leaves no room to sound like
running Portuguese. This is the main reason the register score is 96 and not
higher.

## Residual-English defects found and fixed

Gate 9 found 14 real defects that no other check could see, all inside
`\text{}` subscripts or figure strings, which `id_apply`'s math and draw
censuses blank by design:

`\text{cavity}` (ch. 23, 2x) -> `\text{cav}`; `\text{for }` (ch. 26) ->
`\text{para }`; `\text{exch}` (ch. 27) -> `\text{troc}`;
`\text{cooling}`/`\text{heating}` (ch. 27) -> `\text{frio}`/`\text{quente}`,
with the solutions' `COP_c`/`COP_h` renamed to `COP_f`/`COP_q` to match;
`\text{recovered}` (ch. 28) -> `\text{recuperado}`; `\text{ice}` (ch. 28 and
its solutions, 8x) -> `\text{gelo}`; `\text{fins}` (solutions ch. 25, 2x) ->
`\text{aletas}`; and the axis strings `(arb.)` -> `(un. arb.)`,
`(normalised)` -> `(normalizado)`.

Two gate-6 failures, both inherited rather than introduced:

* `parts/bachelor-2/pt/04-viscous-flows.tex:484` wrote `von K\'arm\'an`,
  copied byte-identically from the English canon, which writes the TeX accent
  escape itself. Rewritten as UTF-8 `von Kármán` in the Portuguese file only;
  **the English canon still carries the escape** in both
  `parts/bachelor-2/04-viscous-flows.tex` and the English credits page.
* A drafty `...` inside a `%` comment in ch. 20 (the gate is line-based and
  does not strip comments). Reworded.

Three sweeps that no gate, census or log can perform were run over all 62
files **after** the last edit, not once: line-final elision apostrophes,
line-initial punctuation, and mid-word hyphens split across a source line.
All three are clean. (The single line-final apostrophe the tree contains is
`\int nn''` in the solutions to ch. 24 --- a math prime, byte-identical to
English, and math mode ignores the newline.)

## pt-BR variety sweep

Zero occurrences of the European forms *eletrão, protão, neutrão, íman,
comboio, ecrã, autocarro, impulsão, travagem, betão, ficheiro*, of the
pre-1990 *facto/acção/óptimo* spellings, or of the European progressive
*está a + infinitive* (the 15 hits of *está a* / *estão a* are all the
locative "is at": *está a \qty{1000}{K}*, *a Lua está a \qty{3.8e5}{km}*).
Present instead, throughout: *elétron* (163), *próton* (15), *nêutron* (3),
*ímã* (9), *usina* (15), *tela* (38), *trem* (63), *ônibus* (1). The optical
screen is *anteparo* (39) everywhere. *óptica* is spelled with the *p* in all
88 occurrences, the Brazilian physics-text convention, matching Book 3 pt.

## Settled glossary (Book 4 additions to the Book 3 pt list)

| English | Portuguese | note |
|---|---|---|
| wave packet | pacote de onda | |
| path difference | diferença de caminho | not *diferença de percurso* |
| fringe / interfringe | franja / interfranja | |
| screen (optical) | anteparo | not *tela*, which is the display of ch. 9 |
| grating | rede (de difração) | |
| blazed grating | rede com blaze | *blaze* kept, as in Brazilian practice |
| beam splitter | divisor de feixe | |
| compensating plate | lâmina compensadora | |
| air wedge / air plate | cunha de ar / lâmina de ar | |
| waist (of a beam) | cintura | |
| Rayleigh length | comprimento de Rayleigh | |
| population inversion | inversão de população | |
| pumping | bombeio | not *bombeamento* |
| threshold (laser) | limiar | STOPped: also the hearing threshold of ch. 6 |
| gain clamping | ganho travado | |
| cooling fin | aleta | |
| heat sink | dissipador | |
| effusivity | efusividade | |
| scale height | altura de escala | |
| partition function | função de partição | |
| Schottky anomaly | anomalia de Schottky | |
| free energy / free enthalpy | energia livre / entalpia livre | Helmholtz / Gibbs |
| steady flow | escoamento estacionário | bare *estacionário* STOPped: it is also "stationary" in chs. 30--31 |
| control volume | volume de controle | not *controlo* |
| shaft work | trabalho útil (de eixo) | |
| throttle | estrangulamento | |
| nozzle | bocal | |
| heat exchanger | trocador de calor | |
| quality (of wet steam) | título | |
| reheat | reaquecimento | |
| degree-day | grau-dia | `\unit{K.dia}` |
| black body | corpo negro | |
| greenhouse effect | efeito estufa | |
| effective temperature | temperatura efetiva | |
| tunnelling | tunelamento / efeito túnel | |
| well (potential) | poço | |
| barrier | barreira | |
| splitting | desdobramento | |
| wave function | função de onda | |
| spreading (of a packet) | alargamento | not *espalhamento*, reserved for scattering |
| supercooled | super-resfriado | |
| case hardening | cementação | |

## Cross-cutting findings (they affect the other six editions)

1. **`\addlegendentry{}` was a blind spot of the same class as `\legend{}`.**
   It is drawing code for `id_apply`'s `draw` census and was invisible to
   gate 9, so a translated legend entry needed a `!draw` opt-out that would
   have opted the whole file out of the byte-identity guarantee. This edition
   never took that opt-out: the six entries carrying real prose
   (`long fin`; `Sun,`/`Earth,`; `air,`/`helium alone,`; `(shifted)`;
   `(even)`/`(odd)`) were kept byte-identical in the patch and translated by
   one targeted post-write edit, the same route the coordinator blessed for
   `\qty{}` arguments trapped inside a math span. The gates have since been
   extended to cover `\addlegendentry`, and gate 9 now reports these six as
   translated.
2. **`\foreach \x/\t in {0/absorption, ...}` is a third instance of the same
   class.** In `parts/bachelor-2/23-laser.tex:103` the three visible labels
   under the figure live in a `\foreach` list, which no gate reads and which
   the `draw` census compares byte-for-byte. Same post-write route was used.
   Worth adding to the gates.
3. **The English canon writes `von K\'arm\'an`** in
   `parts/bachelor-2/04-viscous-flows.tex:484` and on the English credits
   page. Every Latin-script edition that copies that line byte-identically
   fails gate 6 rule 6 (UTF-8 only).
4. **A Book 3 seed's `EXTRA` can point at a Book 3 label.** The
   `book3_pt.py` -> `book4_pt.py` seed carried
   `thm:b1:quantum-introduction:debroglie`, which does not exist in Book 4.
   Any edition that shipped the seed unedited would emit an undefined
   reference. Worth a one-line check in every sibling's config.

## Why not 100

* **Method boxes (register).** The English method boxes are telegraphic lists
  of formulas; Portuguese follows them faithfully and therefore reads as a
  list rather than as prose. Making them flow would move them away from the
  canon's own compression.
* **Link density is 1.08x English.** Every English target is reached and every
  gap is explained, but a language whose technical nouns recur more often than
  English's pronouns will always link a little more. 1.08x is inside the band
  the sibling editions of Book 3 settled at (pt 1.07x, es 1.02x).
* **One accepted gate-9 `dup`.** `parts/bachelor-2/pt/11-maxwell-equations.tex:115`
  --- the Maxwell--Ampère line inside an `align*` is byte-identical to English
  by design (it is pure mathematics), and now sits beside a translated line
  114, which the two-tier twin comparison reads as an English line kept.
* **The `\text{}` abbreviations that survive** (*sat*, *liq*, *vap*, *fus*,
  *cond*, *evap*, ...) are correct Portuguese abbreviations of *saturação*,
  *líquido*, *vapor*, *fusão*, *condensador*, *evaporador* --- but they are
  correct by coincidence of the two languages' Latin roots, not by choice, and
  a reader who expanded them would not always guess the Portuguese word.
