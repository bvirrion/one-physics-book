# Translation score — Physics Book 2 · Dutch (`nl`)

| Field | Value |
|-------|--------|
| **Book** | One Physics Book 2 (High School, grades 10–12) |
| **Language** | Dutch (`nl`) |
| **Quality bar** | **native academic** (EN is the source; the French twin `parts/grade-1{0,1,2}/fr/` used as sense/structure reference, never as ceiling) |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 |
| **Date** | 2026-07-26 |
| **Scope** | Full re-translation from scratch: 35 bodies + 35 solution files (70 files, ~23 000 lines of English) deleted and rewritten from the English, including the 35 weekend problems and their 20-part solutions |

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Exact mirror (35 + 35); identical label sets and order; 35 `problem` envs ↔ 35 `\begin{solution}{pb:…}`; per-environment and figure census equal to English in all three years; `enumerate[resume]` and `\admitted` kept where English has them |
| Terminology | **96** | School Dutch throughout: impuls, traagheidsstelsel, resulterende kracht, normaalkracht, wrijvingscoëfficiënt, schijnbaar gewicht, dracht/vluchttijd/werphoek, grenssnelheid, omloopbaan/omlooptijd, halve lange as, perihelium/aphelium, mathematische slinger, veerconstante, terugdrijvende kracht, demping/pseudoperiode/eigenfrequentie/resonantie, conservatieve kracht, keerpunt, stabiel/labiel evenwicht, condensator/capaciteit/spoel/zelfinductie/tijdconstante, vervalconstante, massadefect/bindingsenergie per nucleon/kernsplijting/kernfusie/coulombbarrière, foton/uittreearbeid/remspanning/energieniveau/materiegolf, eigentijd/tijddilatatie/lengtecontractie. Quantity symbols and unit strings (m/s, N, J, W, Pa, V, A, Ω, mol, eV, u) untouched |
| Register / tone | **96** | Written, not translated: `Zij $x$ zijn uitwijking uit het evenwicht.` (never "Laat … zijn"), "Merk op dat", "Ga na dat", "Bijgevolg", imperative exercise stems (Bereken, Bepaal, Toon aan, Leid af, Schat, Schets, Ga na). Chapter openings keep the English hook without its syntax ("Smokkel een personenweegschaal een lift in") |
| Hygiene / LaTeX | **99** | 0 errors, 0 undefined refs, 0 overfull boxes; warnings identical to English apart from the by-design `dutch.ldf not found` line; UTF-8 accents only (0 `\'e`-class escapes); series decimal **point** kept in all math |
| Cross-refs | **98** | `\label`, `\cref`/`\ref` targets and `\begin{solution}{key}` byte-identical to English; cross-volume references prose-only ("het onderbouwvolume", "het volume van bachelorjaar 1", "de universitaire volumes") — no country or curriculum name anywhere |
| Figures | **97** | TikZ/pgfplots/circuitikz drawing code byte-identical; only node text and `{\small …}` captions translated (Aarde, Zon, bovenaanzicht/achteraanzicht, omloopbaan/ontsnapt/valt, kernfusie/kernsplijting, helling $= h$, zichtbaar, geïoniseerd); the one drafty `{1,2,...,7}` tick list expanded to an explicit list |
| Solutions | **97** | Every solution rewritten from the English solution; Dutch headers `\section*{Hoofdstuk \ref{ch:…} --- <Nederlandse titel>}`; all 20-item weekend-problem solutions fully rendered |
| MT-artifact freedom | **95** | No calques of English word order; verb-final subordinate clauses throughout; residual-English sweep over the 70 files returns only label names inside `\omterm{…}` and `\begin{proof}`. Two wrong-sense links produced by literal wording were caught and reworded (see below) |

**Overall: 96** (weighted toward terminology + register + MT-freedom).

## Structural / build gates

| Gate | Result |
|------|--------|
| `bash tools/check_translation.sh grade-10 nl` | **PASSED** |
| `bash tools/check_translation.sh grade-11 nl` | **PASSED** |
| `bash tools/check_translation.sh grade-12 nl` | **PASSED** |
| `latexmk one_physics_book_2_high_school_nl.tex` | OK |
| Fatal errors (`^!`) | 0 |
| Undefined references | 0 |
| Overfull `\hbox` | 0 |
| PDF | `build/one_physics_book_2_high_school_nl.pdf`, **358 pp** (EN 349 pp) |
| `python3 tools/link_defined_terms.py --book 2 --lang nl --check` | every file matches what the config generates (**4 111** links, 420 linkable terms) |
| LaTeX warnings | 8 vs EN 7; the 6 `hyperref Token not allowed` are the same math-in-title warnings English has, the extra one is `dutch.ldf not found; building Dutch without babel` (emitted by `styles/onephysics.sty` by design) |

## Samples (native / near-native / MT)

| Sample | Verdict |
|--------|---------|
| G12 `06-newtons-laws` opening + `met:…:method` | **native** — "Smokkel een personenweegschaal een lift in… er is aan boord niets veranderd behalve de beweging"; the method reads as a Dutch teacher's checklist (Systeem / Stelsel / Inventaris / Projecteren / Oplossen en controleren) |
| G12 `08-satellites-kepler` §"Vallen rond de Aarde" | **native** — "de $R$ vergeten is de klassieke blunder van dit hoofdstuk"; Kepler's three laws in idiomatic Dutch ("het lijnstuk Zon--planeet bestrijkt gelijke oppervlakken in gelijke tijden") |
| G12 `09-oscillators-and-time` `rem:…:dimensional` | **native** — "de massa \emph{kan} er niet in zitten, want geen enkel ander gegeven draagt een kilogram om haar weg te delen" |
| G12 `pb:g12:rc-rl-circuits:1` (the camera flash) | **native** — "twee seconden gejank, een milliseconde glorie"; "een energietank of een vermogenshefboom?" |
| G12 `13-radioactive-decay` `rem:…:crowds` | **native** — "wetteloosheid middelt uit tot uurwerk"; "Werp $100$ munten op: verwacht $50$ keer kop, maar schrik niet van $43$" |
| G12 `16-special-relativity` proof of time dilation | **near-native** — correct and readable, but the chain "en --- de cruciale stap --- het tweede postulaat legt … vast op $c$" keeps the English appositive-dash architecture |
| G12 `15-quantum-world` solutions 1–15 | **native** — "het oog werkt tot op honderd korrels van de absolute grens: bijna een fotonenteller" |
| G10–G11 (earlier years of this same pass) | **native** — e.g. "de weegschaal leest de versnelling af, niet de snelheid" (g12-06 sol. 11), "gelijke polen stoten elkaar af" (g11-06) |

## Defined-term links (`\omterm`) — target parity vs English

Regenerated with `--unwrap --apply`, then `--apply`, then `--check` (green).
Per-year target-set diff against English, every divergence investigated:

| Divergence | Verdict |
|---|---|
| g10, g12: EN links `thm:g10:refraction:snell`, `prop:g10:pressure:boyle`, `thm:g12:newtons-laws:second`, `thm:g12:newtons-laws:third` | **deliberate policy divergence**: `NOT_A_TERM` in `book2_nl.py` contains `"wet van"`, so Dutch treats *wet van Snellius / wet van Boyle / tweede wet van Newton* as theorem **names**, not terms — exactly what the English default `"law of"` does to *Galileo's law of free fall*. Consistent across the Dutch edition; not overridden |
| g12: EN links `def:g11:fundamental-interactions:strong` on "range" | **English wrong-sense over-link** (projectile range ≠ range of an interaction). Dutch has two distinct words in play and `AMBIG_POLICY = nearest-preceding` sends *dracht* to `def:g12:projectile-motion:range` from grade 12 on — NL is right |
| g12: EN links `def:g11:magnetic-fields:solenoid` ("coil") | same sense, different target: Dutch *spoel* is defined in its own right in `def:g12:rc-rl-circuits:inductor` (EN defines "inductor" there and keeps "coil" from g11) |
| g12: EN links `def:g10:energy-conservation:transfer` ("converter"), `def:g11:mechanical-energy:dissipation` ("dissipated"), `def:g11:work-of-force:sign` ("resistive"/"motor"), `def:g10:relative-motion:frames` ("ground frame") | wording, not sense: the Dutch sentences say *omvormer*, *verstookt*, *remmend/drijvend*, *stelsel van de grond*. Linking the ordinary Dutch adjectives would flood the book |
| g11: EN links `def:g10:light-spectra:continuous`, `:kelvin`, `def:g10:refraction:refraction`, `def:g10:signals-and-waves:signal`, `def:g11:color-light-sources:lamps`, `prop:g11:circuits-and-power:ohm`, `:networks`; g12: `def:g11:color-light-sources:cones`, `:perception` | Dutch solid compounds (*kleurenspectrum*, *lichtbron*, *wet van Ohm*, *kegeltjes*) do not match a component by design of `lang_nl.py` (`DERIVE = False`, no component matching) — thinner coverage, never a wrong link |
| NL links EN does not have: `def:g10:energy-conservation:potential`, `thm:g10:energy-conservation:conservation`, `def:g10:inertia:diagram`, `def:g11:mechanical-energy:potential`, `def:g11:nucleus-radioactivity:abg`, `def:g12:light-as-wave:iridescence`, `def:g12:newtons-laws:inertial`, `def:g12:nuclear-energy:units`, `thm:g10:pressure:depth`, `thm:g12:satellites-kepler:kepler` | all **correct sense**, all reached from a Dutch phrase whose English twin is either a one-word homonym (dropped in EN) or worded differently (*potentiële energie*, *behoud van energie*, *krachtenschema*, *elektronvolt*, *wetten van Kepler*) |

### Config deltas (`tools/term_config/book2_nl.py`)

- **`EXTRA` (new, 8 entries, commented in the file)** — Dutch writes as one solid
  word what English writes as two, and `harvest.py` only keeps an `\index` entry
  attached to a statement when it contains a space. Restored by hand, one entry
  per English link target: `RC-kring`, `RL-kring`, `LC-kring`, `tijddilatatie`,
  `lengtecontractie`, `ijzerpiek`, `veeroscillator`, `tijdschakelingen`.
  This recovered `thm:g12:rc-rl-circuits:charging`, `prop:g12:rc-rl-circuits:rl`,
  `prop:g12:rlc-oscillations:equation`, `thm:g12:special-relativity:dilation`,
  `prop:g12:special-relativity:contraction`, `prop:g12:nuclear-energy:ironpeak`,
  `prop:g12:oscillators-and-time:spring-period`, `rem:g12:rc-rl-circuits:applications`.
- Nothing else touched: `STOP`, `NO_CAPITAL`, `DROP`, `EXTRA_PROTECT`,
  `AMBIG_POLICY`, `MAX_TERM_*` are as they were.

### Prose fixes made for link hygiene (not style)

- *evenwicht* in "de vergelijking in evenwicht brengen" (g12-13, g12-14) linked
  the **balanced-equation** sense to the force-equilibrium definition → reworded
  to "kloppend maken" / "Laat de vergelijking kloppen".
- bare *weerstand* meaning **air drag** (g12-07 body + solutions, g12-10
  solutions) linked to the electrical-resistance definition → reworded to
  *luchtweerstand* (already in `EXTRA_PROTECT`) and once to "remmende kracht".
- g12-10 solution 12: "labiel (maximum)" → "een labiel evenwicht (maximum)", so
  the Dutch text carries the term English links (`prop:g12:work-and-energy:equilibria`).
- Two overfull boxes (both in earlier years of this pass) fixed by rewording:
  "Gebruik, tenzij…" → "Neem, tenzij…" (g10-04 data card) and
  "een koffer van $23$ kilogram" → "een koffer van \qty{23}{kg}" (g11-04).

## Why not 100

- ~~`\omadmittedtext` reads "Toegegeven op dit niveau."~~ **Fixed after this
  score was written** (`styles/lang/nl.tex` → "Op dit niveau zonder bewijs
  aangenomen.", matching the Dutch math series); it now renders under all 49
  `\admitted` results.
- ~~siunitx range phrase never localized~~ and ~~cleveref's English conjunction~~
  **fixed in the same pass**: `styles/lang/nl.tex` now sets
  `\sisetup{range-phrase={ tot }, list-pair-separator={ en },
  list-final-separator={ en }}` and redefines `\crefpairconjunction` /
  `\creflastconjunction` to " en " inside `\AtBeginDocument` (cleveref installs
  its own at begin-document). Verified in the PDF: "27.5 tot 4186 Hz",
  "Hoofdstukken 25 en 29"; zero remaining `N to M` / `N and M` in the Dutch text.
  **French, Spanish and Portuguese still carry this gap** — one `\sisetup` +
  conjunction block per language file would close it.
- **Decimal point kept in all math** (`$0.63$ s`, `9.81 m/s²`). Dutch writes a
  decimal comma; the series keeps the point in every language so the shared
  `parts/` physics is identical. A Dutch pupil reads unfamiliar notation
  throughout.
- **Theorem-name links are absent by policy** (see the table above): a Dutch
  reader gets no hyperlink on "tweede wet van Newton" where the English reader
  gets one on "Newton's second law". Defensible, but it is a real difference in
  reading experience.
- **Compound-word link coverage is structurally thinner** than English:
  `lang_nl.py` deliberately refuses component matching, so *SI-basiseenheid*,
  *kleurenspectrum*, *lichtbron*, *kegeltjes* never link. 4 111 links vs the
  English edition's ~4 500 on the same text.
- **A few long weekend problems keep English sentence architecture** — the
  triple-dash appositive ("… — en het ene getal dat het bordje mag beloven"),
  which Dutch tolerates but uses less freely. A pass by a Dutch physics teacher
  would break some of these in two.
- **`\cref` reads as a bare noun** ("volgens \cref{thm:…}"); acceptable Dutch,
  but a native author would sometimes write "de stelling in …".

## Pipeline actually used

1. Glossary + register sheet fixed up front (terms, `Zij …`, `Weekendopgave`,
   `Deel I --- …`, `\section*{Hoofdstuk \ref{ch:…} --- <titel>}`), reused
   verbatim across all 70 files.
2. Year by year, chapter by chapter: delete the stale NL file, read the English
   body, write the Dutch body; then the English solutions file → Dutch solutions
   file. No post-editing of the previous translation anywhere.
3. `bash tools/check_translation.sh grade-N nl` at each year boundary; the one
   reported class (drafty `...` in a pgfplots tick list) fixed on the spot.
4. `link_defined_terms.py --unwrap --apply`, then `--apply`; per-year target-set
   diff against English; the config/prose curation above; `--check` green.
5. `latexmk` build gate to 0/0/0, then `pdftotext` spot-reads of three chapters
   and two weekend problems.
6. Sweeps: curriculum/country names (none), TeX accent escapes (none), decimal
   commas in prose and math (none), residual English (none outside label names).
