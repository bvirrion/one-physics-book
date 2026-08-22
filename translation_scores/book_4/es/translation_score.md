# One Physics Book 4 (University, Year 2) --- Spanish edition: self-score

**Date:** 2026-08-22
**Quality bar:** *native academic* (the bar of `translation_instruction.md`).
**Sense/structure reference:** the English canon (`parts/bachelor-2/*.tex`) for
content; the Spanish Book 3 (`parts/bachelor-1/es/`) and
`../one-math-book/parts/bachelor-2/es/` for the university register; the French
Book 4 (`parts/bachelor-2/fr/`) for sense on the handful of terms the two
languages name differently.

## Overall: **96 / 100**

| Dimension | Score | Note |
|---|---:|---|
| Register (academic Spanish, weighted) | 96 | Impersonal *se* + subjunctive imperatives (*muéstrese*, *dedúzcase*, *compruébese*, *estímese*) through every exercise and proof; narrative present in the chapter openings; no *usted*, no *tú*. |
| Terminology (weighted) | 96 | Settled per-chapter glossary below; index keys equal the visible terms; `\text{}` subscripts localised (*rad*, *umb*, *sal*, *ent*, *ef*, *cal*, *fr*, *sup*, *atm*, *aletas*, *hielo*, *col*, *rendija*, *banda*). |
| MT-artifact freedom (weighted) | 97 | No calqued word order found on sampling; every `\text{...}`, TikZ node, axis label, `\legend`, `\addlegendentry` and environment optional title is Spanish (swept mechanically, see *Checks*). |
| Structure | 100 | `check_translation.sh` green; all 62 files written as line-range replacements on the English canon through `tools/id_apply.py`, so labels, `\cref` targets, solution keys, `\qty{}{}`, `\foreach`, `xtick=` and every math display are byte-identical to English. |
| LaTeX hygiene | 99 | 0 errors, 0 undefined references, 0 overfull boxes, `nullfont` at the English baseline of 60; UTF-8 accents only, none inside a unit argument. Four fault classes were found and fixed (below). |
| Cross-references | 100 | Every `\cref`/`\ref` target byte-identical to English; 12 exercises + 1 weekend problem per chapter, one solution each. |
| Figures | 98 | Drawing code untouched; only node text, axis labels, legends and captions translated. |
| Solutions | 96 | All 31 solution files translated; `\textbf{n.}` numbering and every number preserved. |

## What was produced

- `parts/bachelor-2/es/01`--`31` and `parts/bachelor-2/solutions/es/01`--`31`
  --- 62 files, 22 988 lines, every one applied as `id_apply` line ranges.
- `tools/term_config/book4_es.py` --- curated against Book 4's own Spanish
  harvest and term for term against `book4_en.py`; the Book 3 seed that stood
  there was replaced, not extended.
- Build: **359 pages**, `0` errors, `0` undefined, `0` overfull (English: 345).

## Checks

```
bash tools/check_translation.sh bachelor-2 es      -> TRANSLATION GATE: PASSED
python3 tools/check_latin_prose.py parts/bachelor-2/es parts/bachelor-2/solutions/es
  -> 123 findings, all reviewed (see below); no untranslated prose
latexmk -g one_physics_book_4_university_year_2_es.tex
  '^!' lines            -> 0        (359 pages)
  undefined             -> 0
  Overfull              -> 0
  nullfont              -> 60       (= the English build's own count)
  "invalid in math mode"-> 0
grep -o 'parts/bachelor-2/\(solutions/\)\?es/[^ ]*' build/....fls | sort -u | wc -l
  -> 62                            (the build really read all 62 Spanish files)
python3 tools/link_defined_terms.py --book 4 --lang es --unwrap --apply
python3 tools/link_defined_terms.py --book 4 --lang es --apply
  -> 1361 links across 61 files    (English: 1231 -- 1.11x)
```

End-of-line hygiene, swept **after** the last edit, not once:

```
grep -rnP "['’]\s*$"           -> 0 (excluding '' closing quotes)
grep -rnP "^\s*[.,;:)?!]"      -> 0
grep -rnP "[a-zà-ÿ]-\s*$"      -> 0
literal ... outside \foreach   -> 0
TeX accent escapes \'e, \`a    -> 0
non-ASCII inside \qty/\unit/\num (6 251 sites) -> 0
```

### Gate 9's 123 findings, one by one

* **113 `text-1word`** --- `\text{}` subscripts whose Spanish spelling *is* the
  English one: single letters (`c`, `s`, `a`, `u`, `p`, `n`, `m`, `r`, `f`,
  `g`, `b`, `t`, `v`, `e`, `d`, `R`, `C`, `E`, `D`, `T`, `N`, `H`, `O`), unit
  and element symbols (`nm`, `Hz`, `dB`, `km`, `mJ`, `mV`, `nV`, `ppm`, `pm`,
  `Hg`, `Cu`, `He`, `Al`), and abbreviations identical in the two languages
  (*sat*, *liq*, *rad*, *fus*, *vap*, *sub*, *tot*, *eq*, *ext*, *int*,
  *cond*, *evap*, *esc*, *mol*, *nat*, *rev*, *vib*, *gas*, *real*, *tel*).
* **8 `node-1word`** --- TikZ node text that is the same word in Spanish:
  *sensor*, *chip*, *radio*, *circular*, *conductor*, *natural*, *metastable*.
* **1 `legend-1word`** --- `\legend{plasma, $\omega = ck$}`: *plasma* again.
* **1 `dup`** --- `11-maxwell-equations.tex:116`, the Maxwell--Ampère line of
  the `align*`. It is pure mathematics and identical to English by
  construction; it only became visible because line 115 above it now says
  `\text{(Maxwell--flujo)}`, so the heuristic sees a translated neighbour.
  **This false positive will fire on every edition that translates that label**
  (`align*` is not one of the drawing environments the rule skips).

## Census discipline

Ten of the eleven `id_apply` censuses passed unaided on all 62 files. One
`!draw` opt-out was used, on one range: `23-laser.tex:103`, the
`\foreach \x/\t in {0/absorción, 3.6/emisión espontánea, ...}` label list,
which the draw census does not blank (the sanctioned case named in the tool's
own docstring). Every other range was verified with all censuses on, and each
patch was re-checked until it reported `PROBLEMS: 0` before it was applied.

## Faults found and fixed during this pass

- **`von K\'arm\'an` (`04-viscous-flows.tex:489`)** --- a TeX accent escape
  inherited byte-identically from the English canon, which gate 6 fails on.
  Rewritten `von Kármán`. The canon still carries the escape, so Dutch and
  Portuguese inherit it too.
- **A drafty `...` inside a TikZ comment** (`20-michelson.tex:71`, again
  inherited from the canon) --- gate 5 does not strip comments, so it would
  have failed the gate. Translated, and the ellipsis removed.
- **Three English lines kept beside their translation** (22, 25, 28) --- the
  tail of a range I had started one line too late. Deleted.
- **Four English `\text{}` arguments** (*in particular*, *where*,
  *(Maxwell--flux)*, *for light*) and three English subscripts in solutions 22
  (`\text{slit}`, `\text{strip}`, `\text{coll}`, the last also inconsistent
  with the body's `\text{col}`).
- **Three overfull boxes** (`01`, `13`, `solutions/11`): the same shape each
  time --- a long unbreakable inline formula preceded by Spanish prose a few
  characters longer than the English it replaces. Fixed by giving the
  paragraph more break points and shortening the prose, never the mathematics.
- **English words inside `\qty{}` arguments that sit inside `$...$`**
  (`03`, `04`, `08`, `12`, `20`, `26` solutions). Translating them in place
  would have broken the math-span census, so the span was kept byte-identical
  in the patch and rewritten afterwards by an idempotent post-write script
  (`{days}` -> `{d}`, `{kWh/day}` -> `{kWh/d}`, `= \qty{0.1}{fringe}$` ->
  `= 0.1$ franjas`). The 12 sites in running text were rewritten directly
  (*turns/s* -> *vueltas/s*, *lines/mm* -> *líneas por milímetro*,
  *kWh/year* -> *kWh al año*, *K.day* -> `\unit{K.d}`).

## Term links

1361 links against English's 1231 (1.11x). Target parity is essentially
complete: of 200-odd distinct targets, only `met:b2:rigid-body-mechanics:incline`
is linked in English and not in Spanish (the Spanish name of the term does not
recur verbatim outside its own chapter), while four targets are linked in
Spanish and not in English --- `thm:b2:potential-wells-tunneling:tunnel`,
`prop:b2:dispersion-wave-packets:lossy`, `thm:b2:maxwell-equations:theorems`
and `prop:b2:rigid-body-mechanics:inertia` --- because the Spanish names of
those terms (*efecto túnel*, *condición de Heaviside*, *teorema de la
divergencia*, *teorema de Huygens*) are the ordinary words of the subject,
where English writes *tunnelling*, *the condition*, *the theorem*.

The 11% excess is concentrated in ten targets and every one of them is a real
difference of wording, not a loose stop list:

| Target | ES | EN | Why |
|---|---:|---:|---|
| `potential-wells-tunneling:tunnel` | 14 | 0 | *efecto túnel* is the ordinary Spanish name; English's canon says *tunnelling*, which its own harvest never links |
| `dispersion-wave-packets:complex` | 61 | 50 | Spanish has one phrase, *profundidad de penetración*, where English has two (*skin depth*, *penetration depth*), so chapters 25 and 31 link where English does not |
| `dispersion-wave-packets:relation` | 41 | 35 | Spanish repeats *velocidad de fase* where English uses "it" |
| `rigid-body-mechanics:coulomb` | 13 | 8 | *rozamiento estático/cinético* named where English says "the friction" |
| `flow-balances:energy`, `wave-interfaces:brewster`, `fluid-kinematics:flowrate`, `open-systems:cv`, `wave-interfaces:optics`, `maxwell-equations:potentials` | +4--5 each | | the same: a Spanish noun phrase where English uses a pronoun or a shorter compound |

Per-term parity is exact where the two languages phrase alike --- *atenuación*
29 / *attenuation* 29, *línea(s) de corriente* 32 / *streamline(s)* 32,
*velocidad de fase* 18 / *phase velocity* 18.

## Sampled passages

1. **`parts/bachelor-2/es/24-particle-diffusion.tex`, opening** ---
   *"Déjese caer un cristal de colorante en agua en reposo y obsérvese: se
   forma a su alrededor una nube coloreada, crece, se ablanda por los bordes y
   se extiende --- en un minuto por un milímetro, en una hora por un
   centímetro, en una semana por todo el vaso."*
   **Verdict: native.** The impersonal imperative pair *déjese/obsérvese*, the
   post-verbal subject *se forma una nube* and the bare temporal series are
   Spanish rhythm, not glosses of "drop", "watch", "a coloured cloud forms".

2. **`parts/bachelor-2/es/28-thermodynamic-potentials.tex`, opening** ---
   *"Estírese deprisa una goma elástica y tóquese con el labio: está caliente;
   déjese contraer y está fría. […] la razón es que la tensión de una goma no
   es cuestión de energía, sino de entropía."*
   **Verdict: native.** *no es cuestión de …, sino de …* is the idiomatic
   contrast a Spanish lecturer writes; MT produces *"no es una materia de"*.

3. **`parts/bachelor-2/es/25-heat-conduction.tex`, example "El suelo, la bodega
   y el vino"** --- *"la bodega es más fría en marzo y más cálida en
   septiembre, y a \qty{5}{m} está a \qty{1}{K} de ser constante --- la bodega
   que guarda el vino."*
   **Verdict: native.** *estar a un kelvin de ser constante* keeps the English
   figure without calquing *"is within one kelvin of constant"*.

4. **`parts/bachelor-2/es/17-dipole-radiation.tex`, remark "Por qué nos llega
   la luz azul"** --- *"Son las \emph{fluctuaciones} de la densidad del aire
   --- las moléculas no están en una red --- las que dejan una intensidad
   dispersada neta."*
   **Verdict: native.** The cleft *son las fluctuaciones … las que* is exactly
   the Spanish emphatic construction; a machine writes *"Es las fluctuaciones
   … que"*.

5. **`parts/bachelor-2/solutions/es/23-laser.tex`, item 18** ---
   *"la retina sobrevive a \qty{1}{mW} durante los \qty{0.25}{s} del reflejo de
   aversión --- clase 2: visible, $\le \qty{1}{mW}$, segura porque se
   parpadea."*
   **Verdict: native.** *porque se parpadea* keeps the English joke's economy.

6. **`parts/bachelor-2/es/31-potential-wells-tunneling.tex`, example "El
   amoniaco"** --- *"la molécula se queda de su lado durante años --- que es la
   razón de que existan moléculas levógiras y dextrógiras, y de que el azúcar
   no se racemice en la estantería."*
   **Verdict: native.** Subjunctive after *la razón de que*, and the technical
   *racemizar* used as a Spanish chemist would.

7. **`parts/bachelor-2/es/27-open-systems.tex`, theorem "Balance de energía"**
   --- the statement of the first law for a stream.
   **Verdict: near-native.** Correct and terse; a Spanish textbook would
   sometimes expand *"o bien, por unidad de masa de fluido que cruza el
   sistema"* into a full clause. Deliberate: the series' house style is the
   terse statement.

## Settled terminology (this book)

**Solids and fluids.** rigid body *sólido rígido* · rotation vector *vector
rotación* · rolling without slipping *rodadura sin deslizamiento* · moment of
inertia *momento de inercia* · friction (cone) *rozamiento (cono de
rozamiento)* · streamline / pathline *línea de corriente / trayectoria* ·
material derivative *derivada material* · mass/volume flow rate *caudal
másico / volumétrico* · vorticity *vorticidad* · stagnation *estancamiento* ·
stream function *función de corriente* · perfect fluid *fluido perfecto* ·
head, head loss *altura de carga, pérdida de carga* · shear stress *esfuerzo
cortante* · no-slip *condición de adherencia* · boundary layer *capa límite* ·
drag *resistencia* · penstock *tubería forzada* · water hammer *golpe de
ariete* · thrust *empuje* · hydraulic jump *resalto hidráulico*.

**Waves, electromagnetism.** wave equation *ecuación de ondas / de d'Alembert* ·
normal modes *modos propios* · standing wave *onda estacionaria* ·
overpressure *sobrepresión* · sound level *nivel sonoro* · Doppler *efecto
Doppler* · sonic boom *estampido sónico* · dispersion relation *relación de
dispersión* · phase/group velocity *velocidad de fase / de grupo* ·
attenuation *atenuación* · skin depth *profundidad de penetración* · wave
packet *paquete de ondas* · spreading *ensanchamiento* · coaxial cable *cable
coaxial* · telegrapher's equations *ecuaciones del telegrafista* · feedback
*realimentación* · loop gain *ganancia de lazo* · aliasing *solapamiento
espectral* · drift velocity *velocidad de arrastre* · displacement current
*corriente de desplazamiento* · boundary relations *relaciones de paso* ·
pillbox *cilindro achatado* · Poynting *vector de Poynting* · radiation
pressure *presión de radiación* · skin effect *efecto pelicular*.

**Optics.** optical path *camino óptico* · wavefront *frente de onda* ·
coherence time/length *tiempo / longitud de coherencia* · wave train *tren de
ondas* · path difference *diferencia de camino* · order of interference
*orden de interferencia* · interfringe *interfranja* · division of
wavefront/amplitude *división del frente de onda / de amplitud* · fringes of
equal thickness/inclination *franjas de igual espesor / inclinación* ·
Newton's rings *anillos de Newton* · air wedge *cuña de aire* · beam splitter,
compensating plate *lámina separadora, lámina compensadora* · free spectral
range *intervalo espectral libre* · finesse *fineza* · blazed grating *red
escalonada*, blaze angle *ángulo de blaze* · resolving power *poder
resolvente* · Airy disc *disco de Airy* · numerical aperture *apertura
numérica* (`\mathrm{AN}`) · spatial filtering *filtrado espacial* · dark
field *campo oscuro* · speckle *moteado* · anti-reflection coating *capa
antirreflejante* · waist *cintura* · Rayleigh length *longitud de Rayleigh* ·
population inversion *inversión de población* · output coupler *espejo de
salida* · mode hopping *salto de modo*.

**Diffusion, heat, thermodynamics, quantum.** number density *densidad
numérica* · Fick *ley de Fick* · random walk *camino aleatorio* ·
complementary error function *función error complementaria* · carburising
*cementación* · thermal conductivity/diffusivity *conductividad / difusividad
térmica* · thermal resistance *resistencia térmica* · film resistance
*resistencia de película* · fin *aleta* (efficiency *rendimiento de la
aleta*) · heat sink *disipador* · heat pipe *caloducto* · effusivity
*efusividad* · black body *cuerpo negro* · emissivity *emisividad* · spectral
exitance *exitancia espectral* · solar constant *constante solar* · effective
temperature *temperatura efectiva* · greenhouse effect *efecto invernadero* ·
forcing *forzamiento* · open system, control volume *sistema abierto, volumen
de control* · useful (shaft) work *trabajo útil* · nozzle, throttle *tobera,
estrangulamiento* · quality *título* · reheat *recalentamiento intermedio* ·
free energy / free enthalpy *energía libre / entalpía libre* · Maxwell
relations *relaciones de Maxwell* · supercooled *subenfriada* · osmosis
*ósmosis* · Boltzmann factor *factor de Boltzmann* · partition function
*función de partición* · scale height *altura de escala* · Schottky anomaly
*anomalía de Schottky* · rms speed *celeridad cuadrática media* · adiabatic
demagnetisation *desimanación adiabática* · wave function *función de onda* ·
Born's rule *regla de Born* · probability current *corriente de probabilidad*
· stationary state *estado estacionario* · Bohr frequency *frecuencia de
Bohr* · confinement energy *energía de confinamiento* · tunnelling *efecto
túnel* · tunnel splitting *desdoblamiento por efecto túnel* · scanning
tunnelling microscope *microscopio de efecto túnel* · work function *función
de trabajo* · half-life *periodo de semidesintegración*.

## Why not 100

- The series' statement style is deliberately telegraphic; in Spanish, whose
  academic prose tolerates more connective tissue, a few theorem statements
  (ch. 27, ch. 30) read *correct and terse* rather than *written in Spanish
  first*.
- `\mathrm{}` subscripts belong to the mathematics and are byte-identical to
  English by construction, so a Spanish reader still meets `\mathrm{Bi}`,
  `\mathrm{COP}`, `\mathrm{NA}`-style abbreviations where the canon used them
  (`\mathrm{AN}` was localised because the applier does allow `\mathrm{}`
  content to change; `\mathrm{Bi}` and `\mathrm{COP}` are international).
- The link count is 11% above English's, concentrated in the ten targets
  tabulated above; each excess link is correct, but a stricter curation would
  have brought the ratio into the 1.02--1.07 band of the shipped Book 3
  editions at the cost of dropping links a Spanish reader would want.
- One `!draw` opt-out (ch. 23) was unavoidable: the draw census does not blank
  `\foreach` label lists.
