# Translation score — Physics Book 2 · Spanish (`es`)

| Field | Value |
|-------|--------|
| **Book** | One Physics Book 2 (High School, grades 10–12) |
| **Language** | Spanish (`es`) |
| **Quality bar** | **native academic** (EN is the source of truth; the FR edition of the same book was used as the sense/structure reference and as the method exemplar for term curation) |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-07-27 |
| **Scope of this pass** | **Full re-translation from English**, not a repair. Every one of the 70 bodies (35 chapters + 35 solutions) and `frontmatter/preface.es.tex` was re-derived from the English canon; the pre-existing `es/` tree was treated as a reference only and discarded. Plus a curated `tools/term_config/book2_es.py` and a regenerated `\omterm` layer. |

## Why a re-translation and not a repair

The `es/` tree that existed before this pass was raw machine translation with
real errors of sense, not merely of register — sampled at random it produced
«el \emph{normal}» for the optical normal, «en el mismo manera», and *vigas*
(structural beams) for the beams of a spectrometer. The French score file for
this same book had already flagged the Spanish edition as the outstanding job
and predicted its homographs (*tensión*, *altura*, *foco*, *potencia*); it was
right, and every one of them is handled below. Nothing of the old tree
survives except the labels, which are English property anyway.

## Verdict in one line

A Spanish edition that reads as written rather than translated, structurally
byte-identical to English where it must be, with a defined-term layer that is
now *in the same size class as English* (4 474 links against 4 497) instead of
either starved or over-linked — and one shared-file gap, listed below, that
this pass was not allowed to close.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Exact mirror: 35 chapters, 35 solution files, **525 exercises EN / 525 ES**, 35 `problem` environments ↔ 35 `\begin{solution}{pb:…}`, **560 `solution` environments EN / 560 ES**, 155 TikZ/pgfplots/circuitikz pictures EN / 155 ES. Per-chapter `exo:`/`pb:` label ↔ solution-key diff is **zero lines** in all 35 chapters. All three `check_translation.sh` gates **PASSED** |
| Terminology | **97** | Spanish *bachillerato*-level physics register throughout: *cantidad de movimiento*, *rapidez* vs *vector velocidad*, *reacción normal*, *rozamiento estático/cinético*, *fuerza recuperadora*, *constante elástica*, *seudoperiodo*, *periodo de semidesintegración*, *defecto de masa*, *energía de enlace por nucleón*, *tiempo propio*, *potencial de frenado*, *trabajo de extracción*. SI unit **names** are Spanish and lower-case (julio, vatio, voltio, amperio, ohmio, culombio, hercio, becquerelio, henrio, faradio, newton, pascal, tesla); unit **symbols** inside `\qty`/`\unit` are untouched |
| Register / tone | **96** | Written, not translated: «Cuela una báscula de baño en un ascensor.»; «Gira el pesado dial de una radio de desván y las emisoras desfilan ante la aguja». English appositive dashes become Spanish colons where Spanish prefers them; no calqued word order found in the residual sweep |
| LaTeX hygiene | **97** | 0 errors, 0 undefined references, **0 overfull boxes**, 135 underfull (EN-class). 0 TeX accent escapes (`\'e`), UTF-8 throughout, 0 `\end{…>` typos, no duplicate labels. The `\,\%` convention is now used at **all 117** percent signs (was mixed) — which is what `styles/onephysics.sty` documents for `es` |
| Cross-refs / rule compliance | **99** | `\label`, `\cref`/`\ref` targets and `\begin{solution}{key}` byte-identical to English. **Zero** curriculum, track or country names (no *bachillerato* named as a programme, no *lycée*/*Terminale* equivalent). Cross-volume references use «el volumen del primer año de universidad», the correct neutral form |
| Defined-term links (`\omterm`) | **95** | `--check` **green**: 4 474 links across 70 files, all matching what `book2_es.py` generates (EN 4 497 on the same text). Target-set diff against English: **205 ES vs 203 EN**, 5 EN-only / 7 ES-only, every divergence checked (table below) |
| Figures | **98** | All 155 drawing bodies byte-identical to English — coordinates, `\foreach`, `xtick`/`ytick`, `samples at`, `\addplot` expressions, `circuitikz` component labels. Only text nodes, legends, axis labels and `{\small …}` captions localized. One deliberate exception, documented below |
| Solutions | **97** | All 525 exercise solutions plus all 35 weekend-problem solutions present and native; headers `\section*{Capítulo \ref{ch:…} --- <título>}` with `ch:…` slugs unchanged |
| MT-artifact freedom | **97** | Residual-English sweep over the 70 files (after stripping labels, environment names, math, TikZ and unit markup) returns **zero** English tokens in prose. The sweep also caught and fixed the one calque that had survived from an earlier draft: «las unidades **de trabajo** son el kPa y el MPa» (English *working units*) → «de modo que **en la práctica se usan** el kPa y el MPa» |

**Overall: 96** (weighted toward terminology + register + MT-freedom).

## Structural / build gates

**Measurement note.** pdfTeX writes `build/*.log` as ISO-8859 text, so a plain
`grep -c 'Overfull'` treats the file as binary, prints nothing and exits 1 —
which reads as "0" and is not a count. Every figure below was taken with
`grep -a`.

| Gate | Result |
|------|--------|
| `bash tools/check_translation.sh grade-10 es` | **PASSED** |
| `bash tools/check_translation.sh grade-11 es` | **PASSED** |
| `bash tools/check_translation.sh grade-12 es` | **PASSED** |
| `latexmk one_physics_book_2_high_school_es.tex` | exit 0 |
| `grep -ac '^!'` | **0** |
| `grep -aci 'undefined'` | **0** |
| `grep -ac 'Overfull'` | **0** |
| `grep -ac 'Underfull'` | 135 (EN-class; the series norm in every language, not a defect) |
| PDF | `build/one_physics_book_2_high_school_es.pdf`, **359 pp** (EN 349, FR 358, NL 358) |
| `python3 tools/link_defined_terms.py --book 2 --lang es --check` | **green** — every file matches the config |
| Exercise ↔ solution invariant | 35/35 chapters diff to zero lines |
| Duplicate labels in the `es/` tree | none |

### Build-environment caveat, for whoever grades this next

`spanish.ldf` is **not installed on this machine**, so `styles/onephysics.sty`
took its documented fallback branch and built Spanish **without babel** (the
package prints the warning it is designed to print). Consequences:

- the PDF has **no Spanish hyphenation**, so the 359-page count and the
  0-overfull / 135-underfull figures are the *unhyphenated* numbers; with
  `texlive-lang-spanish` installed the line breaking will differ and, on the
  evidence of FR and NL, will get slightly better, not worse;
- a **stale `build/one_physics_book_2_high_school_es.toc`** left over from an
  earlier, babel-enabled run (dated 21 July) made the first build die with
  `! Undefined control sequence. l.1 \babel@toc` — because the fallback branch
  cannot read a babel `.toc`. Deleting `build/one_physics_book_2_high_school_es.*`
  fixed it. If the next pass runs on a babel-equipped machine, delete the
  artefacts again before trusting the log.

The `\,\%` convention is unaffected either way: `styles/onephysics.sty` calls
`\spanishplainpercent` whenever babel-spanish *is* loaded, which is exactly why
the sources must (and now do) write the thin space explicitly.

## Defined-term links — what Spanish needed

The stub `book2_es.py` shipped a `STOP` list of eleven bare nouns with
`DROP = set(STOP)`, which is the wrong instrument twice over: it dropped words
that are legitimate book-wide terms in Spanish (*fuerza*, *energía*, *trabajo*,
*campo*, *onda* — English links all five) and it stopped nothing that Spanish
actually needed stopped. Regenerating on the stub produced a layer 600 links
short of English on words that carry no ambiguity at all, while leaving every
real Spanish homograph linking to the wrong definition.

Curation applied entirely in `tools/term_config/book2_es.py` (nothing in the
shared rules under `tools/termlink/`), then `--unwrap --apply` → `--apply` →
`--check`. Final: **4 474 links**, EN 4 497.

### `STOP` (word still links inside the chapter that defines it)

| Term | Why |
|---|---|
| `tensión` | **the** Spanish homograph, exactly as French *tension*: the pull of a rope (g10 inertia) and the electrical quantity English calls *voltage* (g11 circuits). Under `AMBIG_POLICY = "nearest-preceding"` every mechanics chapter of grade 12 — Newton's laws, the cable-car problem, the pendulum — was sending its rope tensions to the electrical definition. Now chapter-local: 55 EN links become 19 ES, and all 19 are right |
| `rapidez` | harvested from the velocity-vector definition (g12 kinematics) but used from grade 10 on, almost always *before* that definition exists. *velocidad media*, *velocidad del sonido*, *velocidad de escape* survive as phrases |
| `gamma` | the radiation sense (g11 nucleus) is right in the nuclear chapters and wrong in the relativity chapter, whose prose *gamma* is the dilation factor. *radiación gamma* survives |
| `nodo`, `nodos` | standing-wave node (g12 sound) vs the circuits' Kirchhoff junction |
| `fundamental` | the fundamental of a note (g12 sound); everywhere else the ordinary adjective — and *interacción fundamental* and *estado fundamental* are terms of their own |
| `motor` | harvested from *trabajo motor* (g11); bare *motor* is the engine, from the winch's to the rocket's to the electric one. *trabajo motor* survives, as does the contrasting *trabajo resistente* |
| `ganancia` | oscilloscope gain (g10 signals); also the ordinary gain of anything — resolution, energy, speed (the electron-microscope problem asks for a *ganancia* on the last page of the book) |
| `real`, `normal`, `uniforme`, `velocidad` | guards. `normal` is genuinely harvested (the refraction normal) and is now chapter-local, as in English; the other three are not harvested by the current text and cost nothing |

### `DROP` (ordinary word harvested from a definition that merely uses it; the full phrase survives)

| Term | Why |
|---|---|
| `absoluta` | bare feminine adjective from *presión absoluta*; it also opens *temperatura absoluta*, *incertidumbre absoluta*, *valor absoluto*. All three full phrases survive |
| `delgada` | from *lente delgada*; *lámina delgada*, *capa delgada* are not optics. The lens phrases survive. (English ships the un-dropped version of this defect: its PDF links "**thin** air" to the lens definition, twice) |
| `estable`, `inestable` | from *equilibrio estable/inestable*; on their own they describe a nuclide (*plomo-206 estable*, *núcleos inestables*) or an orbit. Both full phrases survive |
| `vertical` | from the weight definition, but overwhelmingly the ordinary adjective (*componente vertical*, *asíntota vertical*, *plano vertical*) |
| `segundo` | from the SI-units definition — and Spanish *segundo* is also the ordinal: *el segundo postulado*, *el segundo término*, *la segunda ley* |
| `en reposo`, `reposo` | from the reference-frame definition; the phrase means "motionless" on nearly every mechanics page. Dropping the two-word form alone is not enough — the engine keeps the bare noun, so both must go |
| `escapa` | conjugated verb harvested from the escape-speed remark; in the dating chapter argon *escapa* from lava, which is not the same idea |
| `factor $\gamma$ (gamma)` | display form with math in it; never matches prose. The dilation theorem is reachable through *dilatación del tiempo* |

### Deliberately **not** stopped

`fuerza`, `energía`, `trabajo`, `campo`, `onda` — the stub dropped all five.
They are unambiguous in Spanish, they are exactly the words English links
book-wide, and restoring them returned **≈ 600 links** (`def:g10:inertia:force`
71 → 329-class, `def:g10:energy-conservation:energy` 49 → 237-class,
`def:g10:signals-and-waves:wave` **0 → 102**). Their contexts were audited
after regeneration: every occurrence is the physical noun.

### `NOT_A_TERM` emptied

The stub carried `("teorema", "lema", …, "ley de", "ley de la", …)`, inherited
from the maths books. In a physics book that silently suppresses the
result-name links English *does* make: *segunda ley de Newton*, *ley de Snell*,
*ley de Ohm*, *ley de Boyle*, *leyes de Kepler*, *principio de inercia*,
*teorema de la energía cinética*. Emptying it added 34 links and closed six of
the eleven EN-only target divergences. (This is the opposite of the French
choice, which keeps `"loi de"` deliberately; both are defensible, but parity
with English is worth more here than internal consistency with FR.)

### `NO_CAPITAL`

Only `newton`, `pascal`, `kelvin`, `tesla`. Spanish spells the other SI units
differently from the physicists who name them — julio/Joule, voltio/Volt,
culombio/Coulomb, hercio/Hertz, ohmio/Ohm, faradio/Farad, henrio/Henry,
becquerelio/Becquerel — so those four are the entire clash set. The stub
listed the English unit names, which match nothing in a Spanish body.

### `EXTRA_PROTECT` (masked spans)

| Pattern | Why |
|---|---|
| `resistencia del aire` | mechanics' drag, not the electrical quantity. 13 occurrences |
| `potencias? de (?:diez\|dos)` | *potencia* is both power and a mathematical power. 18 occurrences — «veinte potencias de diez», «$\num{32768} = 2^{15}$: ¿por qué una potencia de dos…?». English ships this defect too (`\omterm{def:g11:work-of-force:power}{powers} of ten`) |
| `compresión máxima` | the bumper spring's compression, not the acoustic compression of a sound wave |
| `núcleo del Sol` | the Sun's core is neither an optical-fibre core nor an atomic nucleus |
| `campo entero` | «el lanzamiento de campo entero» is a full-court basketball shot, not an electric or magnetic field. 4 occurrences |

### Omterm target parity with English

**205 ES targets vs 203 EN**; 5 EN-only, 7 ES-only. Every divergence checked:

| Divergence | Verdict |
|---|---|
| EN-only `prop:g12:work-and-energy:equilibria`, `def:g12:work-and-energy:ep` | consequence of dropping bare *estable*/*inestable* and of Spanish saying *energía potencial* (a phrase that resolves to the grade-11 definition) where English says bare *potential energy*. Correct sense in both languages |
| EN-only `def:g11:mechanical-energy:dissipation` | English links bare *dissipated*; Spanish *disipada* is a feminine participle the harvester does not produce from *disipación*. Cosmetic |
| EN-only `def:g11:electric-gravitational-fields:lines`, `rem:g12:rc-rl-circuits:applications` | reached in English from *field lines* / *timing circuits*; the Spanish sentences say *líneas de campo magnético* and *circuitos temporizadores*, which land on the neighbouring (and more precise) definitions |
| ES-only `thm:g10:inertia:principle`, `thm:g10:energy-conservation:conservation`, `thm:g11:mechanical-energy:ketheorem`, `thm:g12:work-and-energy:emtheorem`, `thm:g12:satellites-kepler:kepler` | the result-name links unlocked by emptying `NOT_A_TERM`; all correct sense, and all of them links an English reader also gets from the prose around the same theorem |
| ES-only `def:g12:mechanical-waves:wave`, `def:g12:nuclear-energy:units` | *onda mecánica* and *electronvoltio* are single Spanish terms where English words the sentence differently. Correct sense |

## Figures — the one deliberate divergence

All 155 drawing bodies are byte-identical to English apart from text nodes,
legends, axis labels and captions, with a single exception:
`parts/grade-12/es/16-special-relativity.tex`, the $\gamma$ curve, where
`ytick={1,2,...,7}` was expanded to `ytick={1,2,3,4,5,6,7}`. Identical output;
the change is forced, because `tools/check_translation.sh` fails any `…` in a
translated file that is not on a line containing `\dots`, `\foreach` or
`samples at`, and a pgfplots `ytick` list is none of those. Recorded here
because it is the one place the "never touch drawing code" rule and the gate
contradict each other.

Two pgfplots keys additionally keep unaccented symbolic coordinates with
accented `xticklabels` on top (`symbolic x coords={…, Jupiter}` +
`xticklabels={…, Júpiter}`), because a UTF-8 accent inside `symbolic x coords`
is not portable.

## Non-SI "units" that were English words

The English sources write `\qty{10.0}{years}`, `\qty{54}{hours}`,
`\qty{4.6}{yr}` — free text in a `\qty` argument, not SI symbols. Left
byte-identical they print **English words in a Spanish book**; the PDF showed
12 of them. They are now `\qty{10.0}{años}`, `\qty{54}{horas}`,
`\qty{4.6}{años}`. This is the only place a `\qty` unit argument was touched,
and it touches no unit symbol: `d`, `h`, `min`, `s`, `ly`, `au` and every SI
symbol are byte-identical to English. (`ly` is kept as the international
light-year symbol, introduced in prose as «el \emph{año luz} (\unit{ly})».)

## Samples (native / near-native / MT)

| Sample | Verdict |
|--------|---------|
| `grade-12/es/06-newtons-laws.tex` opening + `met:…:method` | **native** — «Cuela una báscula de baño en un ascensor. Cuando la cabina arranca hacia arriba, la aguja marca tres kilogramos de más; cerca del último piso marca de menos; entre ambas cosas, la pura verdad --- a bordo no ha cambiado nada salvo el movimiento.» The method reads as a Spanish teacher's checklist: «elegir un sistema, dibujar sus fuerzas, proyectar $\sum \vect F = m\vect a$» |
| `grade-12/es/12-rlc-oscillations.tex` opening | **native** — «Gira el pesado dial de una radio de desván y las emisoras desfilan ante la aguja: una voz, unos violines, ruido, otra voz. Detrás del panel no hay ningún motor ni ningún ordenador…» |
| `grade-10/es/07-pressure.tex` `def:…:pressure` + `ex:…:snowshoe` | **native** — «Un esquiador se desliza sobre la nieve en la que un caminante se hunde; un empujón de \qty{5}{N} clava una aguja en un cuero que un puño no consigue abollar.» (The one calque this sample originally carried, *unidades de trabajo*, was fixed in this pass.) |
| `grade-12/solutions/es/16-special-relativity.tex` sols 1–3 + `pb` items 15, 20 | **native** — «La situación no es simétrica: solo la astronauta da media vuelta --- acelera y cambia de sistema inercial, mientras que la gemela terrestre se queda en uno solo ---, así que solo su reloj registra el tiempo más corto.» |
| `grade-11/solutions/es/06-magnetic-fields.tex` sols 1–3 | **native** — «Cada trozo es un imán completo, con un polo norte y otro sur: en cada cara cortada aparece un polo nuevo. […] Ninguna forma de cortarlo aísla un polo: cada corte crea una pareja.» |
| `frontmatter/preface.es.tex` | **native** — written as Spanish, not rendered from English: «Los resultados que se enuncian sin demostración se señalan explícitamente como admitidos.» |

No sample in this pass reads as MT.

## Why not 100 — ordered gap list

1. ~~**`styles/lang/es.tex` is missing the siunitx / cleveref localisation
   block, and the PDF prints English because of it.**~~ **RESOLVED
   2026-07-27** by the orchestrating session, after this agent's run, once no
   other agent held the physics repo. `styles/lang/es.tex` now carries the
   `\sisetup{range-phrase={ a }, list-pair-separator={ y }, …}` block plus the
   `\crefpairconjunction` / `\creflastconjunction` / `\crefrangeconjunction`
   and group-conjunction redefinitions inside `\AtBeginDocument`, mirroring
   `nl.tex`. Verified on a full rebuild: «Capítulos 25 **y** 29», zero
   remaining `and`/`to` range leaks in the PDF text.

   The same edit also added the missing `\today` localisation (`es.tex` had
   none, so the cover printed «July 27, 2026»); it now prints
   «27 de julio de 2026». Rebuild after the fix: 0 errors, 0 undefined,
   0 overfull, 359 pp — unchanged.

   `fr.tex` and `pt.tex` had both gaps too; they were fixed in the same
   session at the user's request (`à`/`et` and `a`/`e` conjunctions,
   `1\textsuperscript{er}` handling for the French first-of-month). Both
   editions rebuild at 0/0/0 — FR 358 pp, PT 355 pp — with zero English
   conjunctions or cover dates remaining.
2. **`tensión` links only inside its two defining chapters** (55 EN links → 19
   ES). A wrong-sense link is worse than a missing one, and the French edition
   made the same trade for the same word, but a Spanish reader gets no
   hyperlink on «la tensión del hilo» in the Newton chapter where an English
   reader gets one on "tension". No configuration of the current engine can do
   better: Spanish uses one word where English uses two, and the engine
   resolves ambiguity only by chapter order.
3. **`espectro` in the light chapters resolves to the sound definition.** 12
   links in grade-12 Doppler, quantum-world and nuclear-energy mean a light
   spectrum but point at `def:g12:sound-acoustics:timbre`, because the acoustic
   definition is the nearest preceding one. **English does exactly the same on
   the same sentences**, so this is inherited, not a Spanish defect, and
   diverging would cost parity for no reader gain. It should be fixed in the
   English config, for every language at once.
4. **A handful of chapter-ordered homographs are right only *usually*.**
   *foco* (focal point / focus of an ellipse), *núcleo* (fibre core / atomic
   nucleus / the Sun's core — one occurrence protected by hand), *bobina*
   (solenoid / inductor), *alcance* (range of an interaction / range of a
   projectile). Each was audited and each resolves correctly in the great
   majority of its occurrences; none is systematically wrong the way *tensión*
   was. But "audited once" is weaker than "cannot go wrong".
5. **Decimal point kept in all math** (`$0.63$`, `9.81 m/s²`) while Spanish
   convention writes the comma. The series keeps the point in every language so
   the shared `parts/` physics is identical; a Spanish pupil reads a mildly
   foreign notation throughout. Deliberate and unchanged.
6. **`\cref` reads as a bare noun** («por el \cref{thm:…}»); acceptable
   Spanish, but a native author would sometimes write «por el teorema de…».
7. **The build carries no Spanish hyphenation** on this machine (see the
   caveat above), so the typographic figures are provisional even though they
   are clean.
8. Nothing else found. No missing content, no encoding defects, no curriculum
   or country names, no residual English in prose, no link inside `\qty`,
   `\unit`, math, `\label`, TikZ bodies or section titles.

## Shared-file change needed — APPLIED 2026-07-27

Applied by the orchestrating session after this agent finished, once no other
agent held the physics repo. Verified by a full rebuild (0/0/0, 359 pp).

`styles/lang/es.tex` — added, mirroring `styles/lang/nl.tex` lines 83–91
(plus `\crefrangeconjunction` and the `\today` block, which `nl.tex` also has
and `es.tex` lacked):

```latex
\sisetup{range-phrase={ a }, list-pair-separator={ y }, list-final-separator={ y }}
\AtBeginDocument{%
  \renewcommand{\crefpairconjunction}{ y }%
  \renewcommand{\creflastconjunction}{ y }%
  \renewcommand{\crefpairgroupconjunction}{ y }%
  \renewcommand{\creflastgroupconjunction}{ y }%
}
```

(Spanish also needs `e` before a word beginning with *i-*/*hi-*, which
cleveref cannot express; « y » is the correct default and no current
cross-reference pair triggers the exception.) The same gap exists in `fr.tex`
and `pt.tex` and is documented in the French score file, so this is one shared
edit for three editions, not an `es`-only fix.

Nothing else under `styles/`, `latexmkrc`, `.github/`, `tools/termlink/`,
`tools/link_defined_terms.py`, `tools/check_translation.sh` or
`tools/term_config/lang_es.py` required a change. `latexmkrc`
(`@default_files`) and `.github/workflows/release.yml` already register
`one_physics_book_2_high_school_es.tex`; `styles/onephysics.sty` already loads
babel-spanish with `es-noshorthands, shorthands=off` and calls
`\spanishplainpercent`; `styles/lang/es.tex` is otherwise complete and
idiomatic.

---

## Addendum — 2026-07-27, shared-tooling fixes

The same two shared fixes applied to the math repo were applied here (the
`tools/termlink/` engine is byte-identical between the two projects):

1. `tools/term_config/lang_es.py` now sets `TAIL_ON_EVERY_WORD = True` —
   Spanish agrees every word of a noun phrase (*onda estacionaria* -> *ondas
   estacionarias*).
2. `tools/termlink/harvest.py` no longer tests a translated bare `\emph{…}`
   against the English label leaf; a translation defers to the emphases its
   English twin accepted.

Termlinks regenerated: **4 474 -> 4 530 links**. Re-verified: English Book 2
regenerates byte-identically, `check_translation.sh` green for grade-10/11/12,
`latexmk` 0 errors / 0 undefined / 0 overfull, **359 pp unchanged**.

The score above is unchanged: link coverage and tooling, not prose.
