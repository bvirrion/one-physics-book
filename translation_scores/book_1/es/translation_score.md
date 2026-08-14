# Translation score — Physics Book 1 · Spanish (`es`)

| Field | Value |
|-------|--------|
| **Book** | One Physics Book 1 (Primary & Middle School, grades 1–9) |
| **Language** | Spanish (`es`) |
| **Quality bar** | **native academic** (English is the source of truth; this *is* the ES edition, so no Spanish twin existed as a sense reference. The **French twin was not consulted** — the register and terminology exemplars were the shipped `es` edition of **Physics Book 2** (grades 10–12) and the `es` edition of **One Math Book 1**, so a term defined here is the word the senior volume already uses) |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-08-14 |
| **Scope of this pass** | Full first translation, written in one pass at native register (no machine draft, no post-editing of a machine draft). 71 chapters + 71 solution twins + the image-credits front matter + a curated `tools/term_config/book1_es.py`, then the defined-term link layer, then this score. **144 files written.** |

## Verdict in one line

A Spanish Book 1 that reads as though it had been written in Spanish for
Spanish seven-year-olds and then for Spanish fifteen-year-olds: the register
climbs year by year, the physics vocabulary is the one the *bachillerato*
volume already uses, and the structural, build and link-hygiene gates are all
green.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Exact mirror: 71 chapters, 71 solution files, **797 exercises EN / 797 ES**, **35 `problem` environments / 35**, **832 `\begin{solution}` / 832**, **74 `[resume]` / 74**. `\label` sets and order diff to zero in all nine years; all nine `check_translation.sh` gates **PASSED** |
| Terminology | **96** | Peninsular school physics, chosen for continuity with the shipped ES Book 2: *tensión*, *intensidad*, *amperímetro*, *voltímetro*, *resistor* / *resistencia*, *ley de Ohm*, *lente convergente*, *distancia focal*, *imagen real*, *año luz*, *energía cinética*, *rendimiento*, *kilovatio-hora*, *alternador*, *orden de magnitud*, *nudo* (never *nodo*, which Book 2 STOPs). SI unit names in Spanish (*amperio*, *voltio*, *ohmio*, *julio*, *vatio*, *hercio*); symbols and every `siunitx` quantity byte-identical to English |
| Register / tone | **96** | Grades 1–5 speak to the child in *tú* («La acera se nota fría a través de los calcetines»), imperatives and *pruébalo* experiments; grades 6–7 keep *tú* and add the method voice; grades 8–9 use the impersonal *se* and the clipped method style of the senior volume. Written, not converted |
| LaTeX hygiene | **99** | **0 errors, 0 undefined references, 0 overfull boxes** (measured with `grep -a`; the pdfTeX log is ISO-8859 and a plain `grep -c` returns nothing and exits 1). 0 TeX accent escapes, 0 zero-width characters, 0 `\end{…>` typos, 0 drafty `...`, 0 non-Spanish Unicode. Inverted punctuation audited mechanically: every `?` and `!` has its `¿`/`¡` in the same sentence |
| Cross-refs / rule compliance | **99** | `\label`, `\cref`/`\ref` targets, `\begin{solution}{key}`, `[resume]` and all optional arguments byte-identical to English. Zero curriculum, programme or country names in visible text; one consistent variety of Spanish throughout |
| Figures | **97** | All TikZ / pgfplots / circuitikz drawing code byte-identical — coordinates, `\foreach` lists, `xtick`/`ytick`, `samples`, colours untouched; only node text, `l=` component labels, axis labels and `{\small …}` captions localized. Compass card `W`→`O`, weather map `H`/`L`→`A`/`B`, one `yticklabels=` added to keep a bar chart's symbolic coordinates untouched while labelling it in Spanish |
| Solutions | **96** | All 797 exercise solutions and all 35 weekend-problem solutions present and native; headers `\section*{Capítulo \ref{ch:…} --- <título>}` with the `ch:…` slug unchanged. The rhyming inspector's couplet of g9-03 was re-rhymed in Spanish rather than glossed («Huecos iguales, ritmo en paz… Huecos que cambian piden razón») |
| Defined-term links (`\omterm`) | **95** | 6 794 links across 141 files (EN 6 483 on the same text, **+4.8 %**, between the shipped FR +4.1 % and a first-attempt overshoot). Per-year: 174 / 230 / 441 / 653 / 712 / 871 / 1 427 / 1 197 / 1 089. Zero links inside `\qty` / `\unit` / `\num` / math / `\label` / solution keys / TikZ bodies / titles |
| MT-artifact freedom | **97** | Residual-English sweep over the 142 files (comments, math, macro arguments, TikZ bodies and image paths stripped) returns **zero** English prose tokens. Calque sweep (*hace sentido*, *eventualmente*, *asumir*, *consistente*, *actualmente*, *remover*, *aplica para*, *en orden a*, *librería*, *reporta*, *chequea*) returns three hits, all correct Spanish: «sin remover» (stirring), «en orden a partir de la luna nueva», «estimar» |

**Overall: 96** (weighted toward terminology + register + MT-freedom).

## Structural / build gates

Measurement note: pdfTeX writes `build/*.log` as ISO-8859 text, so a plain
`grep -c 'Overfull'` treats the file as binary, prints nothing and exits 1 —
which reads as "0" and is not a count. Every figure below was taken with
`grep -a`.

| Gate | Result |
|------|--------|
| `check_translation.sh grade-1 … grade-9 es` | **PASSED** ×9 (file completeness, label sets and order, exercise↔solution key parity, environment/figure census, hygiene, UTF-8) |
| `latexmk one_physics_book_1_primary_middle_school_es.tex` | rc 0, PDF 52.2 MB |
| `grep -ac '^!'` | **0** |
| `grep -aci undefined` | **0** |
| `grep -ac Overfull` | **0** |
| `\omterm` link layer | `--unwrap --apply` then `--apply`, clean re-run, rebuilt after linking |

### The babel-spanish `\%` hazard

`styles/onephysics.sty` guards it correctly: babel is loaded as
`[spanish,es-noshorthands,shorthands=off]` inside an `\IfFileExists{spanish.ldf}`
and immediately followed by `\spanishplainpercent`, which restores the plain
`\%` whose `\lastskip` probe is fatal after a math `\,`. Two honest caveats:

* this container has **no `texlive-lang-spanish`**, so the build takes the
  documented fallback branch (`Package onephysics Warning: spanish.ldf not
  found; building Spanish without babel`) — the guard is verified by reading,
  not by execution;
* the hazard cannot fire in this book in any case: `\%` occurs **0 times** in
  the Spanish sources and **0 times** in the English ones.

The corollary is favourable: the 0 overfull boxes were achieved *without*
Spanish hyphenation patterns. Installing them can only improve the line
breaking, never worsen it.

## Link-target divergence from English

133 distinct labels carry links in English, 131 in Spanish. Every difference is
traced:

| Label | Direction | Why |
|-------|-----------|-----|
| `def:g7:short-circuits-safety:battery` | EN only (24 links) | **Expected, not a defect.** English's only carrier is the possessive *battery's*, which the harvester treats as a term of its own; no other language has that surface, and French and Portuguese ended one label short on exactly this one. Spanish's *pila* resolves to the grade-3 definition by `AMBIG_POLICY = "nearest-preceding"`, so the sense is right and the reader still lands on a battery definition |
| `def:g1:five-senses:senses` | EN only (10 links) | Deliberate: *sentido/sentidos* is ordinary Spanish on every page («en ese sentido», «los dos sentidos» of a current), so it is `DROP`ped exactly as English drops its own register words. The five senses stay linked through *vista*, *oído*, *tacto*, *olfato*, *gusto* |
| `prop:g7:states-of-matter:squeeze` | EN only (1 link) | English links the participle *compressed*; Spanish morphology in `lang_es.py` derives plurals only (`DERIVE = False`), so the participle *comprimido* is not generated from *comprimir*. One link, in one grade-9 list |
| `ex:g8:sound-pitch-loudness:decibels` | ES only (3 links) | A gain: *decibelio(s)* is a single Spanish noun and links cleanly where English's phrasing does not |

## Curation of `tools/term_config/book1_es.py`

The Spanish traps are not the English ones, and the config says so in its own
comments. What earned a `STOP` (linked only inside its defining chapter):
**medio** (the sound medium against *medio metro*, *en medio de*, *por medio
de*), **fuente** (the light source against *fuente de alimentación*),
**corriente** (the electric current against the adjective «una lámpara
corriente»), **potencia** (electric power against *potencias de diez*),
**fase**, **polo/polos**, **símbolo**. What earned a `DROP`: the young
register's ordinary words — *caliente*, *frío*, *sentido(s)*, *segundo(s)*,
*momento(s)*, *instante(s)*, *abierto*, *cerrado*, *uniforme*, *variado*,
*llena*, *año(s)*, *noche*, *día(s)*, *enciende*, *calienta*. `NO_CAPITAL`
keeps the sentence-initial imperatives (*Mide*, *Observa*) and the physicists
(*Newton*, *Julio*, *Vatio*, *Voltio*, *Amperio*, *Ohmio*, *Hercio*) out.
`EXTRA_PROTECT` covers the adverbial *con fuerza* / *a la fuerza* / *por
fuerza*, *media hora* / *media vuelta*, *resistencia del aire*, *potencias de
diez*, *trayecto de metro*, and the *estación* that is a space station, a train
station or a metro stop rather than a season.

**The `lámpara` / `bombilla` / `luz` merge that inflated another edition did
not happen here.** Spanish keeps English's own three-way split: *bombilla* =
`bulb` (226 links, EN 228), *luz* = `light` (440, EN 437), and *lámpara* =
`lamp`, which is deliberately **unlinked** in 371 occurrences exactly as
English leaves *lamp* unlinked. No single label dominates a page.

## Samples, verdicted

**Native** — grade 1, opening of *Observar el mundo: los cinco sentidos*:

> Un pájaro canta en algún sitio por encima de ti. El pan huele a caliente. La
> acera se nota fría a través de los calcetines.

Three short sensory sentences with the Spanish child-book rhythm; *se nota*
where English has *feels*, which is the idiom, not the dictionary.

**Native** — grade 3, opening of *Un primer circuito eléctrico*:

> Clic --- la linterna lanza su haz por la habitación a oscuras. Dentro de ese
> tubo de plástico viven una pila, una bombilla pequeña y dos tiras de metal,
> jugando a un juego de reglas estrictas.

*Casquillo* (not a calqued *pie*) for the bulb's base; *bornes* for the
battery's terminals — the words a Spanish school lab actually uses.

**Native** — grade 8, definition of resistance:

> La resistencia $R$ de un componente mide con cuánta fuerza se opone a la
> corriente eléctrica: a una tensión dada, cuanto mayor es la resistencia, más
> débil es el desfile que deja pasar.

The *cuanto mayor… más débil…* correlative is Spanish syntax, not English word
order carried across.

**Native** — grade 9, road safety:

> El componente más peligroso del coche no lo mide ninguna fórmula de aquí: la
> atención del conductor.

Left-dislocation with the resumptive *lo* — a construction a translator
working word-by-word does not produce.

**Near-native** — the running metaphor for current. English calls the moving
charges *the march*; Spanish carries it as **el desfile** for nine years («el
desfile que deja pasar», «un desfile sin guardián»). It reads well and is
consistent, but it is a coined register rather than an existing Spanish
textbook metaphor: a Spanish author might have written *la marcha* or dropped
the figure. Deliberate, and flagged rather than hidden.

**Near-native** — *calorcito* for English *warmth* in the grade-9 energy
chapters («fugas de calorcito», «la comisión silenciosa del rozamiento»). The
diminutive does the job English's *warmth*-against-*heat* pair does, since
Spanish has only *calor*; it is a shade more colloquial than a grade-9
textbook would normally be.

**No MT-verdicted sample exists.** The text was written, not post-edited; the
residual-English and calque sweeps return nothing, and the six defects found
during the self-review were Spanish-internal (a wrong clitic in *métele/mételo*,
a *soga-tira* coinage for tug-of-war, two typos, an invalid `\omterm` label, a
missing opening `¡`) — the failure modes of a writer, not of a machine.

## Why not 100

1. **Link density runs +4.8 % over English.** Spanish collapses some English
   two-word terms into one common noun — *balanza* carries every occurrence
   where English's term is the two-word *balance scale* (82 vs 15), *en serie*
   likewise (121 vs 63). Every one of those links is semantically right, but
   the page is bluer than the English page in the grade-3 and grade-4 circuit
   chapters. Correcting it would mean stopping honest terms.
2. **One label short of English**, on `def:g7:short-circuits-safety:battery` —
   structural to English's possessive harvest, as documented above and as seen
   in the FR and PT editions. Not chased.
3. **The babel-spanish path is unexecuted here** (no `spanish.ldf` in this
   container). The guard is right by inspection and the `\%` hazard has no
   occurrence to fire on, but the Spanish hyphenation build has not been run.
4. **Two deliberate register coinages** (*desfile*, *calorcito*) that a Spanish
   author might have played differently; both are consistent across nine years,
   which is the property that matters most for a spiral course.
5. **No second native reader.** Everything above is self-assessed against the
   shipped Spanish Book 2 and the Spanish math book; a human native
   proofreader would still be worth a pass before print.
