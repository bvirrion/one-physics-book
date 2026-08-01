# Translation score — Physics Book 2 · Brazilian Portuguese (`pt`)

| Field | Value |
|-------|--------|
| **Book** | One Physics Book 2 (High School, grades 10–12) |
| **Language** | Brazilian Portuguese (`pt`) |
| **Quality bar** | **native academic** (EN is the source of truth; the ES edition of the same book was used as the method exemplar for term curation, the FR one as a structural reference) |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-07-31 (errata + re-audit 2026-08-01) |
| **Scope of this pass** | **Full re-translation from English**, not a repair. All 70 bodies (35 chapters + 35 solution files) were re-derived from the English canon; the pre-existing `pt/` tree was moved aside and discarded, never edited. Plus a curated `tools/term_config/book2_pt.py` (was a 24-line stub with every set empty), a corrected `tools/term_config/lang_pt.py` (see "Shared-file change — APPLIED") and a regenerated `\omterm` layer. |

## Why a re-translation and not a repair

The inherited `pt/` tree was machine output that had never been read by a
physicist. A sample of what it shipped:

* **`medidor` for the SI metre, ×46.** The unit of length was translated as
  if *meter* meant *gauge*. The defining sentence of the whole series
  (`def:g10:orders-of-magnitude:unit`) named the wrong object.
* **`impulso` for *momentum*, ×35** — impulse is a different physical
  quantity — while the same chapter's definition title said `Momento` and
  its section heading was still the English `Momentum`. Three names, three
  registers, one concept.
* **140 `\textbf{Part I --- …}` headers still in English**, 31 enumerate
  labels reading `(um)` instead of `(a)`, ~170 residual English function
  words, untranslated TikZ nodes (`{rear view (center to the left)}`) and
  table cells (`out of $+$, into $-$ & always into the mass`), and
  `UM \emph{quantidade física}` ×25.
* European-Portuguese leakage (`uma travagem trem`) inside otherwise
  Brazilian prose.

Repairing that would have meant re-writing every sentence anyway, with the
risk of inheriting the calqued sentence rhythm underneath. The rebuild was
cheaper and is auditable: every gate below is green from a clean start.

## Verdict in one line

Brazilian high-school physics prose written in Portuguese, not carried over
from English: *quantidade de movimento*, *força restauradora*, *constante
elástica*, *pseudoperíodo*, *meia-vida*, *defeito de massa*, *energia de
ligação por núcleon*, *tempo próprio*, *potencial de corte*, *função
trabalho* — with a term-link layer that now knows *tensão* is two different
quantities and that *nós* is sometimes a pronoun.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Exact mirror: 35 chapters, 35 solution files, **525 `exo:` labels EN / 525 PT**, **35 `pb:` EN / 35 PT**, **560 `solution` environments EN / 560 PT**, **149 `tikzpicture` EN / 149 PT**, 6 `circuitikz`, 34 `axis`, **137 `omfigure` EN / 137 PT**. Per-chapter `exo:`/`pb:` ↔ solution-key diff is **zero lines** in all 35 chapters. All three `check_translation.sh` gates **PASSED** |
| Terminology | **97** | Brazilian *ensino médio* register throughout: *quantidade de movimento* (not *impulso*), *referencial inercial*, *atrito estático/cinético*, *força normal*, *peso aparente*, *velocidade limite*, *constante elástica*, *frequência própria*, *pseudoperíodo*, *constante de decaimento*, *nuclídeo*, *físsil*, *barras de controle*, *dilatação do tempo*, *contração dos comprimentos*. SI unit **names** in prose are Portuguese and lower-case (joule, watt, volt, ampère, ohm, coulomb, hertz, becquerel, henry, farad, newton, pascal, tesla, cavalo-vapor); unit **symbols** inside `\qty`/`\unit` are byte-identical to English, and free-text `\qty` arguments are localized (`{anos}`, `{horas}`, `{ano}`) |
| Register / tone | **96** | Written, not translated. «Contrabandeie uma balança de banheiro para dentro de um elevador.» «Gire o botão pesado de um rádio de sótão e as estações desfilam diante do ponteiro.» English appositive dashes kept where Portuguese also uses them, turned into colons where it prefers them; no calqued word order survived the residual sweep |
| LaTeX hygiene | **97** | 0 errors, 0 undefined references, **0 overfull boxes**, 138 underfull (EN-class: 127). 0 TeX accent escapes, UTF-8 throughout, 0 `\end{…>` typos, no duplicate labels, no drafty `...`. Percent signs follow English exactly: 116 plain `\%` and the single `\,\%` that English itself uses |
| Cross-refs / rule compliance | **99** | `\label`, `\cref`/`\ref` targets and `\begin{solution}{key}` byte-identical to English. **Zero** curriculum, track or country names. Cross-volume pointers read «o volume do primeiro ano de graduação» / «do ensino fundamental», the neutral form. Decimal **point** kept everywhere, per the series convention, not the Brazilian comma |
| Defined-term links (`\omterm`) | **94** | `--check` **green**: **4 575** links across 70 files, all matching what `book2_pt.py` generates — **101.7 % of English's 4 497** on the same text, the excess audited and explained below. **441 linkable terms PT / 458 EN.** Target-set diff: 210 PT vs 203 EN — 1 EN-only, 8 PT-only. Scored **down** from the 96 claimed on 2026-07-31: that number came from a link set corrupted by a bug in my own `EXTRA_PROTECT` (errata below), the audit that "verified" it was run against the corrupted output, and the two re-audits since have removed nine wrong-sense links that the corruption and the linked-tree measurement had hidden |
| Figures | **98** | All 149 drawing bodies byte-identical to English — coordinates, `\foreach`, `xtick`/`ytick`, `samples`, `\addplot` expressions, `circuitikz` component names. Only text nodes, legends, axis labels and `{\small …}` captions localized. One deliberate exception, documented below |
| Solutions | **97** | All 525 exercise solutions plus all 35 weekend-problem solutions present and native; headers `\section*{Capítulo \ref{ch:…} --- <título>}` with `ch:…` slugs unchanged |
| MT-artifact freedom | **97** | Residual-English sweep over the 70 files (labels, environment names, math, TikZ and unit markup stripped first) returns **zero** English tokens in prose. The only hit the sweep flagged, «Um **show** é transmitido ao vivo», is ordinary Brazilian Portuguese for a concert |

**Re-scores.** The defined-term-links dimension has moved twice: **95 →
96** after the `lang_pt.py` morphology correction, then **96 → 94** after
the `EXTRA_PROTECT` bug below was found — the 96 was measured on a
corrupted link set, which is a process failure whatever the end state. The
layer is now larger and cleaner than it has ever been (4 575 links, nine
wrong-sense links removed), but it took an outside catch to get there, and
that belongs in the score.

Nothing else moved: the prose, the figures and the structure were never
touched by any link regeneration, so the three heaviest dimensions
(register, terminology, MT-artifact freedom) are unchanged. The weighted
total still rounds to **96 / 100** — one dimension of nine moving two
points cannot carry it — so **the overall score stands at 96**, now with
the errata attached.

## Structural / build gates

| Gate | Result |
|------|--------|
| `bash tools/check_translation.sh grade-10 pt` | **PASSED** |
| `bash tools/check_translation.sh grade-11 pt` | **PASSED** |
| `bash tools/check_translation.sh grade-12 pt` | **PASSED** |
| `latexmk one_physics_book_2_high_school_pt.tex` | exit 0 |
| `grep -ac '^!'` | **0** |
| `grep -aci 'undefined'` | **0** |
| `grep -ac 'Overfull'` | **0** |
| `grep -ac 'Underfull'` | 138 (EN 127; the series norm in every language, not a defect) |
| PDF | `build/one_physics_book_2_high_school_pt.pdf`, **358 pp** (EN 349, FR 358, NL 358, ES 359) |
| `python3 tools/link_defined_terms.py --book 2 --lang pt --check` | **green** — every file matches the config (4 575 links; `--unwrap --apply` → `--apply` → `--apply` is idempotent at the second pass) |
| Exercise ↔ solution invariant | 35/35 chapters diff to zero lines |
| Duplicate labels in the `pt/` tree | none |

### Build-environment caveat, for whoever grades this next

This machine has **no Portuguese hyphenation pattern file installed**. The
log says it plainly:

```
Package onephysics Warning: brazilian/portuguese.ldf not found; building
Portuguese without babel. Install texlive-lang-portuguese for hyphenation
on input line 134.
```

So the book was typeset with **English hyphenation**. Everything that
depends on line breaking — the 0 overfull boxes, the 138 underfull ones,
the 358-page total — is therefore **provisional**: install
`texlive-lang-portuguese`, rebuild, and re-check the overfull count before
printing. Nothing in the *content* scores depends on it. Deleting
`build/one_physics_book_2_high_school_pt.*` before a rebuild is required if
the format file changes (otherwise `latexmk` dies on
`! Undefined control sequence … \babel@toc`).

## Defined-term links — what Portuguese needed

`tools/term_config/book2_pt.py` was a stub: `EXTRA`, `DERIVED`,
`PRIMARY_OK`, `EXTRA_PROTECT` all empty, `DROP = set(STOP)` with five
generic words, and a `NOT_A_TERM` list that suppressed every law and
theorem. It is now a curated config. Portuguese brings four problems
English does not have.

### `STOP` (word still links inside the chapter that defines it)

| Term | Why |
|---|---|
| `tensão` | **the** Portuguese homograph, exactly as French and Spanish *tension/tensión*: the pull of a rope (g10 inertia) and the electrical quantity English calls *voltage* (g11 circuits). Under `AMBIG_POLICY = "nearest-preceding"` every mechanics chapter of grade 12 — Newton's laws, the cable-car problem, the pendulum — was sending its rope tensions to the electrical definition |
| `altura` | the *pitch* of a sound (g12 sound) and the ordinary *height* of a drop, a tower, a satellite — hundreds of mechanical uses, from the ski jump to the geostationary orbit. The phrase *altura (do som)* survives |
| `foco`, `nó` | the focus of a lens (g11) and the focus of an ellipse (g12) are one word, and the plural tail makes the two indistinguishable; each now links inside its own chapter, and *foco imagem* and *focos* survive |
| `nós` | the nodes of a standing wave (g12 sound) — **and the pronoun *we/us***, which the book uses a dozen times («a luz que chega até **nós**»). The one PT term that collides with a function word |
| `gama` | the radiation sense (g11 nucleus) is right in the nuclear chapters and wrong in the relativity chapter, whose prose *gama* names the dilation factor. *radiação gama* survives |
| `fundamental` | the fundamental of a note (g12 sound); everywhere else the ordinary adjective — and *interação fundamental*, *estado fundamental* are terms of their own |
| `motor` | harvested from *trabalho motor* (g11); bare *motor* is the engine, from the winch's to the rocket's to the clock's driving weight (*peso motor*). The phrase survives |
| `ganho` | oscilloscope gain (g10 signals); also the ordinary gain of anything — the last page of the book asks for the resolution *ganho* of an electron microscope |
| `real`, `normal`, `uniforme`, `velocidade` | guards; not harvested bare by the current text, kept so a later edit cannot open the hole silently |

### `DROP` (ordinary word harvested from a definition that merely uses it; the full phrase survives)

`absoluta` (from *pressão absoluta*; also opens *temperatura absoluta*,
*incerteza absoluta*), `delgada` (from *lente delgada*), `estável` /
`instável` (from *equilíbrio estável/instável*, but everywhere else a
nuclide or an orbit), `vertical`, `segundo` (SI second vs the ordinal *o
segundo postulado*), `em repouso` / `repouso`, `escapa` (the ordinary verb:
argon escapes the lava), and the display form `fator $\gamma$ (gama)`,
which contains math and can never match prose.

### `NO_CAPITAL` — the Portuguese-specific trap

Spanish escapes this with *julio / voltio / culombio / ohmio*; Portuguese
does not. **The unit names and the physicists' surnames are spelled
identically**, so without curation `leis de **Newton**` (45×), `efeito
**Joule**` (9×), `barreira de **Coulomb**` (13×) and `lei de **Ohm**` (5×)
would all have linked to unit definitions. `NO_CAPITAL` now holds newton,
joule, coulomb, ohm, watt, henry, becquerel, pascal, kelvin, tesla, volt,
ampère, hertz, farad, sievert, curie.

### `EXTRA_PROTECT` — spans masked before linking

16 patterns. `resistência do ar` (mechanics' drag, not the electrical
quantity); `potências? de (dez|dois)` (*potência* is both power and a
mathematical power); `compressão máxima` (a spring, not a sound wave); four
`núcleo` patterns — *núcleo de ferro (fundido)*, *sem/com o núcleo*,
*núcleo do Sol/da Terra*, *núcleos atômicos* — because Portuguese uses one
word for the core of an optical fibre (g10), the nucleus of an atom (g11),
the iron core of an electromagnet and the burning core of a star; eight
`sinal` patterns, because *sinal* is both *signal* (g10) and the algebraic
**sign** of a charge, a cosine, a work or a coordinate (*com sinal*,
*mesmo sinal*, *troca de sinal*, and the `sinal &` cell that heads the
sign row of the gravity/electricity table); and
`(ângulos?|par) complementares?`, because complementary **angles** are not
complementary **colours**.

Three rules learned the hard way. They hold for **every** pattern in the
list, not only for the ones that have already been caught failing — a
pattern that matches today is one prose reflow away from missing, and the
next `--apply` would introduce the wrong link silently:

* **Never consume a `$`.** Match it with a lookahead (`de\s+(?=\$)`), never
  with a literal `de \$`. The reason is in the header of
  `tools/termlink/protect.py`; the cost of ignoring it is in the errata
  below — 270 links.
* **Never write a literal space.** Always `\s+`. The list is compiled with
  `re.S` and real prose wraps: «cargas de mesmo\nsinal», «potências de\ndez»,
  «sem resistência\ndo ar», «núcleo de\nferro». All 16 patterns here are now
  `\s+`-only; the seven that still had literal spaces after the first fix
  were hiding four wrong links between them.
* **Audit on unwrapped source, never on the linked tree.** Counting a
  pattern against files that already contain `\omterm{…}{…}` compares two
  variants that are both broken by the wrapper's braces, so a real miss
  reads as "identical, latent". Unwrap first
  (`tools/termlink/wrap.unwrap`) — that is what the linker sees.

### `DERIVED` — trimmed to the irregular plurals only

Portuguese agrees **every** word of a noun phrase (*linha de campo* →
*linhas de campo*). `tools/term_config/lang_pt.py` used to set
`TAIL_ON_EVERY_WORD = False`, so the singular pattern never matched the
plural phrase, and the first version of this config carried a hand-measured
table of **35** plural forms as a workaround.

With the flag corrected (below), the regular plural is now produced by the
rule itself, and the table is down to **7 entries — 28 removed, 7 kept**.
What survives is exactly what an optional `(?:e?s)?` per word *cannot*
generate, the stem-changing plurals:

| Kept entry | Irregularity |
|---|---|
| `ordem de grandeza` → *ordens de grandeza* | **-m → -ns** (the rule would ask for *ordemes*); 7 uses, the most frequent irregular in the book |
| `interação fundamental` → *interações fundamentais* | **-ão → -ões** *and* **-al → -ais**, both words |
| `reflexão total` → *reflexões totais* | **-ão → -ões** and **-al → -ais** |
| `pressão absoluta` → *pressões absolutas* | **-ão → -ões** |
| `força gravitacional` → *forças gravitacionais* | **-al → -ais** |
| `energia potencial` → *energias potenciais* | **-al → -ais** |
| `distância focal` → *distâncias focais* | **-al → -ais** |

The 28 removed entries were all regular (*comprimentos de onda*, *linhas de
campo*, *cargas elementares*, *frentes de onda*, *forças conservativas*,
*campos magnéticos*, *lentes divergentes*, *números atômicos*, …) and are
verified still linked in the regenerated tree.

One entry was removed as **inert, not redundant**: `referencial inercial` →
*referenciais inerciais*. Its base is an ambiguous term resolved by
`AMBIG_POLICY = "nearest-preceding"`, and `DERIVED` only extends the
unambiguous map, so the declaration never did anything. The single plural
use (g12 ch06) is unlinked and would need an `EXTRA` entry to reach; at one
occurrence it is not worth pinning a label by hand.

### Target-set diff against English

210 distinct targets PT vs 203 EN.

* **EN-only (1):** `prop:g12:work-and-energy:equilibria` — English links the
  bare adjectives *stable* / *unstable*; Portuguese cannot, because
  *estável* / *instável* describe nuclides and orbits on every other page.
  The full phrases *equilíbrio estável/instável* still link.
* **PT-only (8):** `thm:g10:inertia:principle`,
  `thm:g10:energy-conservation:conservation`,
  `thm:g11:mechanical-energy:ketheorem`,
  `thm:g12:work-and-energy:emtheorem`, `thm:g12:satellites-kepler:kepler`,
  `def:g12:newtons-laws:inertial`, `def:g12:mechanical-waves:wave`,
  `def:g12:nuclear-energy:units`. These are gains, not drift: emptying the
  stub's `NOT_A_TERM` list (which blacklisted *teorema*, *princípio*, *lei
  de*) lets *princípio da inércia*, *teorema da energia cinética*, *leis de
  Kepler*, *referencial inercial* link like any other defined term, exactly
  as the Spanish edition does.

## Figures

All 149 drawing bodies are byte-identical to English. Localized: text
nodes, legends, axis labels, `xticklabels`, `\legend{}` entries and the
`{\small …}` captions. Examples: `{vista traseira (centro à esquerda)}`,
`{múons nascidos a \qty{15}{km}}`, `\legend{parábola (sem ar), com
resistência do ar}`, `xlabel={semieixo maior $a$ (unidades astronômicas)}`.

One deliberate exception: in `16-special-relativity.tex` the English
`ytick={1,2,...,7}` is spelled `ytick={1,2,3,4,5,6,7}` in Portuguese. The
`...` is pgfplots syntax, but `check_translation.sh` flags every literal
`...` outside `\dots`, `\foreach` and `samples at` as drafty prose; the FR
and ES editions made the same substitution.

## Samples, with verdicts

| # | Portuguese | Verdict |
|---|---|---|
| 1 | «Contrabandeie uma balança de banheiro para dentro de um elevador. Quando a cabine arranca para cima, o ponteiro marca três quilogramas a mais; perto do último andar, marca a menos; entre as duas coisas, a pura verdade --- a bordo nada mudou além do movimento.» | **native** |
| 2 | «Um foguete é uma máquina de arremessar massa. A cada segundo os motores dele lançam uma leva de gás para trás; o gás leva embora quantidade de movimento para trás, de modo que o foguete ganha a mesma quantidade para a frente.» | **native** |
| 3 | «Um núcleo que já esperou dez mil anos tem exatamente a mesma chance de decair neste segundo que um feito hoje de manhã: sem desgaste, sem aviso --- qual vai a seguir é genuinamente imprevisível.» | **native** |
| 4 | «Anuncie uma torre de \qty{37}{m} para \qty{24}{m/s} de saída --- e confesse que um quarto dela, uns \qty{7}{m} de concreto, é a sobretaxa que o atrito cobra do sonho sem atrito.» | **native** |
| 5 | «A relatividade não demoliu Newton; ela traçou a fronteira do império dele. É assim que a física cresce: refinando teorias, cada uma nova devolvendo a antiga como caso-limite.» | **near-native** — the closing cadence is a shade more compressed than the English original; a Brazilian editor might expand «cada uma nova devolvendo a antiga» to «cada teoria nova devolvendo a antiga». Meaning and register are right |

## Why not 100 — ordered gap list

1. **Line breaking is unverified.** No Portuguese hyphenation patterns on
   this machine, so the 0 overfull boxes were measured with English
   hyphenation. Until `texlive-lang-portuguese` is installed and the book
   rebuilt, treat the typography as provisional. *(−1.5)*
2. **Coverage is now 101.8 % of English, and the excess needs watching.**
   4 575 links vs 4 497. The earlier "≈4 % below English, all curation"
   account was wrong: most of that gap was the `EXTRA_PROTECT` bug, not
   curation. The true picture, per target: PT gains where Portuguese uses
   one noun for an English two-word term (*referencial* 86 vs *reference
   frame* 21) or repeats a noun where English uses an adjective (the atom
   ladder, 225 vs 161: *do núcleo* where English writes *nuclear*); PT
   loses exactly where the homograph curation bites (*tensão* 24 vs 55,
   *altura* 13 vs 26, *foco*/*lente* 66 vs 89). Both directions are
   deliberate and were sampled during the re-audit, but a layer that is
   denser than the canon deserves a re-read at the next content edit.
   *(−1)*
3. **Seven irregular plurals are still declared, not derived.** The
   `-ão → -ões`, `-al → -ais` and `-m → -ns` forms cannot come out of
   `(?:e?s)?` and are listed by hand in `DERIVED`. If a future edit writes
   *reflexões totais* somewhere new the link still appears (the form is a
   term), but a *new* irregular phrase — say *coleções de dados* — would go
   unlinked until someone adds it. A stem-aware pluraliser in
   `tools/termlink/morphology.py` would close this for pt/es/fr at once;
   out of scope here. *(−0.5)*
4. **A handful of long compounds read slightly formal.** *quantidade de
   movimento* is the correct Brazilian term and is used consistently, but
   it is four syllables longer than *momentum*, and in dense solution
   paragraphs («a quantidade de movimento total») the sentence rhythm is
   heavier than the English. Unavoidable in Portuguese; noted so nobody
   "fixes" it back to *impulso*. *(−0.5)*

## Errata — the `$`-consuming protect pattern (found 2026-08-01)

**What shipped.** One of my `EXTRA_PROTECT` patterns in `book2_pt.py` was

```python
r'sinal (?:de \$|de \\cos|compara)',      # WRONG: eats the opening $
r'sinal\s+(?:de\s+(?=\$)|de\s+\\cos|compara)',   # fixed: lookahead
```

The `de \$` branch **consumed the opening `$`** of «o sinal de $q$». The
whole protect list is one alternation scanned left to right, so from that
point the inline-math rule paired the *closing* `$` of that formula with
the *opening* `$` of the next one, and the mask ran inside out to the end
of the file: prose was treated as math and skipped, math as prose. It
raises no error. The failure mode is documented at the top of
`tools/termlink/protect.py` — the file my own patterns extend — and it had
already cost Book 3 a thousand links. I read that header when I wrote the
`núcleo` patterns and still shipped a literal `\$` two lines later.

**What it cost.** Exactly two files contained the trigger phrase:

| File | links, buggy | links, fixed |
|---|---:|---:|
| `parts/grade-11/pt/01-lenses-and-eye.tex` | 30 | 146 |
| `parts/grade-11/pt/08-work-of-force.tex` | 19 | 173 |

**270 links** — 5.9 % of the layer — were silently missing, essentially the
whole of two chapters: the lens/eye/vergence vocabulary of one and the
work/force/weight/power vocabulary of the other. The book still built with
0 errors and `--check` still reported green, because the generator and the
checker agreed on the same wrong answer. That is the part worth
remembering: **`--check` green proves reproducibility, not correctness.**

**What the re-audit then found.** The recovered 270 links had never been
sense-checked, and neither had the curation "verified" against them. Going
through them, and through every `sinal` / `tensão` / `núcleo` / `nós` link
in the book:

* the three flagged homographs are **clean**: `tensão` splits 8 rope-tension
  links (all inside `06-inertia`) and 17 voltage links (all inside
  `03-circuits-and-power`); `núcleo` splits 10 fibre-core links (all inside
  `03-refraction`) and 136 atomic-nucleus links; the 3 `nó`/`nós` links are
  all standing-wave nodes in `02-sound-acoustics`, none is the pronoun;
* **five wrong-sense links were found and killed** — four `sinal` (the
  signed numbers of g12 ch05, the sign flip of g12 ch07, the «mesmo\nsinal»
  that my literal-space pattern had missed in g11 ch04, and the `sinal &`
  table cell that heads the sign row) and one `complementares` (the
  complementary *angles* of the projectile range, pointing at the
  complementary *colours* proposition);
* **two over-eager links were kept for parity with English**: the
  accommodation *amplitude* of g11 ch01 links to the signal-amplitude
  definition, and *resistência* de rolamento in g11 ch08 links to
  electrical resistance. English links both the same way, in the same two
  sentences. Diverging silently from the canon would be a worse defect than
  reproducing it; flagged here instead.

**The same defect class, one round later.** Fixing the `sinal` patterns with
`\s+` did not fix the other seven, which still carried literal spaces. A
programmatic sweep found one live miss — «potências de\ndez» wrapping across
a line in `grade-10/solutions/pt/04-universal-gravitation.tex` — and six
patterns that looked latent. All seven were converted to `\s+` anyway, on the
principle that a pattern which matches today is one reflow away from silently
missing. That removed **four** links, not one, and all four were wrong-sense:

| Site | was linked to | is |
|---|---|---|
| g11 ch06 «\emph{sem} **núcleo** de\nferro» | atomic nucleus | a solenoid's iron core |
| g11 ch06 sol. «com o\n**núcleo**» | atomic nucleus | the same iron core |
| g11 ch06 sol. «doze **potências**\nde dez» | power (W) | powers of ten |
| g11 ch09 «sem **resistência**\ndo ar» | electrical resistance | aerodynamic drag |

**Why the "latent" six were not latent** — the measurement lesson worth more
than the fix. Both my sweep and the coordinator's counted each pattern
against the tree **as it sat on disk, already linked**. In a linked tree the
site reads «sem \omterm{...}{resistência}\ndo ar»: the wrapper's braces break
the phrase for the literal *and* the `\s+` version alike, the two counts come
out equal, and the miss is invisible. The linker itself always runs on
**unwrapped** source, where the phrase is plain text and the difference is
real. Re-run against `termlink.wrap.unwrap`-ed source, four of the seven show
the miss immediately. **Audit protect patterns on unwrapped source: the
wrongly-inserted link you are hunting is itself what hides the evidence.**

**Net:** 4 314 → 4 584 (`$` bug fixed) → 4 579 (five wrong links removed) →
**4 575** (four more, from the literal-space sweep).

## Shared-file change — APPLIED

**`tools/term_config/lang_pt.py`**, on coordinator approval (2026-07-31):

```python
TAIL_ON_EVERY_WORD = False   # was
TAIL_ON_EVERY_WORD = True    # now — correct for Portuguese
```

Portuguese, like Spanish and French, agrees **every** word of a noun
phrase: *onda estacionária → ondas estacionárias*, *força conservativa →
forças conservativas*, *lente delgada → lentes delgadas*. With the flag
`False` the generated pattern only ever pluralized the last word — it asked
for *onda estacionárias* — so every compound term was invisible in the
plural. `lang_es.py` and `lang_fr.py` were already `True`; `lang_pt.py` had
been left at the English default. (`lang_nl.py` is `False` deliberately:
Dutch writes compounds solid.) The one-line docstring was replaced with a
real note in the sibling style, recording that the tail is optional per
word — so head-only plurals like *linhas de campo* still match — and that
this flag replaced a hand-built `DERIVED` table.

Effect, measured: links **4 288 → 4 314** (+26), linkable terms **467 →
441** (the 28 hand-declared plural forms stopped being separate entries),
`DERIVED` **35 → 7** entries. Regenerated with `--unwrap --apply` →
`--apply` → `--check`; the second `--apply` inserts 0, `--check` is green,
all three translation gates still PASS and the build is still 0 errors /
0 undefined / 0 overfull at 358 pp. (Both figures were still depressed by
the protect bug in the errata above; the final count is 4 575.)

I audited the new links rather than assuming more is better: every
rule-generated plural display in the tree is a well-formed Portuguese
phrase in the right sense (*cargas elementares*, *comprimentos de onda*,
*forças não conservativas*, *índices de refração*, …), no agreement
nonsense (`forças conservativa`, `ondas mecânica`) appears anywhere, and
the sense-sensitive decisions still hold: *nós* links only inside
`02-sound-acoustics`, *altura* only inside the two sound files, and no
`tensão` outside the circuits chapters points at the voltage definition.

**Not** changed, deliberately: `one-math-book/tools/term_config/lang_pt.py`.
That repo has sibling agents mid-flight and the file is shared across all
five math books; the coordinator will flip it there once they finish.
This repo has no other `pt` edition, so the change here can only affect
Book 2.

No other shared file needed changing: `styles/lang/pt.tex` is complete and
correct (Definição/Teorema/Proposição/Lema/Corolário/Método/Exemplo/
Notação/Observação/Exercício/Problema/Demonstração, «Soluções dos
exercícios», `range-phrase={ a }`, `list-pair-separator={ e }`, Brazilian
`\today`, `Capítulo`), and `styles/onephysics.sty` already loads babel with
the Brazilian-first fallback and `shorthands=off`.
