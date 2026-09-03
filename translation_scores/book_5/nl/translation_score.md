# One Physics Book 5 (University, Year 3) — Dutch edition: self-score

**Date:** 2026-09-03
**Quality bar:** *native academic Dutch* — the university *collegedictaat*
register of `../../../translation_instruction.md`, `nl_style` practice and, as
the binding twin, **Book 4 nl** (`parts/bachelor-2/nl/`, 96/100).
**Sense/structure reference:** the English canon (`parts/bachelor-3/*.tex`,
`parts/bachelor-3/solutions/*.tex`). Settled vocabulary was taken from Book 4 nl
and Book 3 nl so that a reader moving from year 2 to year 3 meets one glossary,
not two.

## Overall: **96 / 100**

| Dimension | Score | Note |
|---|---:|---|
| **Register** (academic Dutch, weighted) | **96** | One *collegedictaat* voice over 27 chapters: narrative present in the openings ("Verwarm water één graad en er gebeurt weinig --- tot de vloeistof zich bij één scherp bepaalde temperatuur tot damp openscheurt"), and `Toon aan dat…` / `Leid af…` / `Bereken…` / `Schat…` / `Vat samen…` in exercise stems. **Reader address is the formal *u/uw*, matching `parts/bachelor-2/nl` exactly** — the first draft of the weekend problems used *je/jouw*; all 88 occurrences across 83 lines were converted by hand (including the verb agreement: *kun je* → *kunt u*, *bouw je* → *bouwt u*, *splits je* → *splitst u*). Verb-final subordinate clauses throughout; no `wij zullen aantonen` padding, no English clause order. |
| **Terminology** (weighted) | **96** | One glossary across bodies and solutions, inherited from Book 4 nl: *spankracht* vs electrical *spanning*, *werkzame doorsnede*, *ontaardingsdruk*, *toestandssom*, *stabiliteitsvallei*, *bandkloof*, *hoofdreeks*. Eponyms follow the house pattern (*wet van Bragg*, *vergelijking van van der Waals*, *relatie van Clausius--Clapeyron*, *stelling van Noether*) and welded compounds stay lowercase (*larmorprecessie*, *blochbol*, *boltzmannfactor*, *hertzsprung-russelldiagram*). Every `\index{}` key equals its visible Dutch term — see the index audit below. |
| **MT-artifact freedom** (weighted) | **95** | Gate 9 tier 1 (multi-word English left standing) is **0**. The 69 remaining findings are tier 2: 20 conventional Latin-derived subscript abbreviations (*orb*, *rot*, *osc*, *lab*, *exc*, *loc*, *vib*, *nuc*, *grav*, *conf*, *vap*, *fus*, *liq*, *esc*, *sep*, *extra*), true cognates (*separatrix*, *oven*, *quarks*, *neutron*, *proton*, *boson*, *fermion*, *singlet*, *triplet*, *band 1/2*, *per megaparsec*) and two proper-name labels (*van der Waals*, *hadr.\ cal.*). `tools/check_orphan_lines.py`: **0**. |
| Structure | **100** | `bash tools/check_translation.sh bachelor-3 nl` **PASSED**. All 54 files written as line-range replacements on the English canon through `tools/id_apply.py`, so labels, `\cref` targets, `\begin{solution}{key}`, math displays, `\qty{}{}` arguments and drawing code are byte-identical to English. Ordered per-file `\label{}` diff against English: **0 lines** (621 ↔ 621). 324 ↔ 324 `exercise`, 351 ↔ 351 `solution`, 27 ↔ 27 `problem`, 1 682 ↔ 1 682 `\text{}`. |
| LaTeX hygiene | **99** | 0 errors, 0 undefined references, **0 overfull boxes**, 0 "invalid in math mode"; `nullfont` **10 = the English baseline**. 0 TeX accent escapes: the canon's own `Segr\`e`, `Panth\'eon`, `Amp\`ere` and `\aa ngstr\"om` were inherited through the byte-identical patches and rewritten as UTF-8 *Segrè*, *Panthéon*, *Ampère*, *ångström* (see the cohort note below). |
| Cross-references | **100** | Identical ordered label sequence; every `\cref`, `\ref` and solution key preserved by the tool, not by hand. |
| Figures | **97** | Drawing code byte-identical to English (`id_apply`'s `draw` census); node text, axis labels and `{\small …}` captions translated. **All 11 prose `\addlegendentry` / `\legend` sites of Census 2 are Dutch** (ch. 01 *put bij $\theta = 0$* / *putten bij $\pm 60^\circ$*, ch. 10 *zuiver coulombs*, ch. 14 *symmetrisch (bosonen; singletelektronen)* / *antisymmetrisch (tripletelektronen)*, ch. 18 *koud oppervlak* / *heet oppervlak*, ch. 20 *(de Zon)*, ch. 21 *één dal* / *vlakke bodem* / *twee dalen*). **No `!draw` and no `!math` opt-out was used anywhere in the book.** All 49 `\foreach` lists of Census 3 left byte-identical, as the brief requires. |
| Solutions | **96** | All 27 solution files translated; `\textbf{n.}` numbering, every number and every unit preserved; headers read `\section*{Hoofdstuk \ref{ch:…} --- <Nederlandse titel>}` with the `ch:…` slug unchanged. |
| Defined-term links | **94** | **817** `\omterm` links against English's **916** (0.89×) across **131** distinct targets against English's 100 — **every one of the 100 English targets is reachable in Dutch**. See the link audit below. |

**Overall 96**, weighted toward register + terminology + MT-artifact freedom.

## Structural / build gates

| Gate | Result |
|------|--------|
| `bash tools/check_translation.sh bachelor-3 nl` | **PASSED** |
| `latexmk -g one_physics_book_5_university_year_3_nl.tex` | OK, exit 0 |
| Pages | **320** (English 302; Dutch runs ~6 % longer, the usual compounding-plus-articles tax) |
| Fatal errors (`grep -ac '^!'`) | **0** |
| Undefined references | **0** |
| Overfull `\hbox` | **0** |
| `nullfont` | **10** — equal to the English baseline |
| `invalid in math mode` | **0** |
| `.fls` honesty check | **54** distinct `parts/bachelor-3/…/nl/…` inputs = 54 files on disk |
| `python3 tools/check_orphan_lines.py` | **0** orphan English lines |
| `python3 tools/check_latin_prose.py` (gate 9) | 69 findings, **0 in tier 1** |
| TeX accent escapes | **0** |
| Non-ASCII inside `\qty{}` / `\unit{}` / `\num{}` | **0** |

## Census 1 — the six English `\qty{}` unit arguments

| Site | Argument | Treatment |
|---|---|---|
| `nl/10-quantum-angular-momentum.tex:411` | `atoms/m^3` | inside `$…$`; kept byte-identical in the patch, then post-edited to `atomen/m^3` |
| `nl/15-scattering-theory.tex:453` | `atoms/m^3` | idem → `atomen/m^3` |
| `nl/24-electrons-in-solids.tex:377` | `atoms/m^3` | idem → `atomen/m^3` |
| `nl/24-electrons-in-solids.tex:516,517` | `euros` | running text; translated inside the patch → `euro` (invariant after a numeral in Dutch) |
| `solutions/nl/24-electrons-in-solids.tex:207` | `euros` | inside `$…$`; kept byte-identical, then post-edited → `euro` |

Every one of the 429 unit arguments was re-read after the post-edits; all are
ASCII, and `nullfont` stayed at the baseline 10, which is the mechanical proof
that nothing non-ASCII reached siunitx.

## The `\index{}` audit — the census nothing else checks

Book 4 Dutch shipped 117 English `\index{}` keys behind green gates. This
edition was diffed against `en_index_keys.txt` (297 keys) **before** scoring:
the first pass left **120 English keys**, all of them in chapters 20--27, and
all 120 were translated (*Bragg's law* → *wet van Bragg*, *valley of stability*
→ *stabiliteitsvallei*, *band gap* → *bandkloof*, *main sequence* →
*hoofdreeks*, *Chandrasekhar mass* → *chandrasekharmassa*, …).

The residue is **20 keys spelled identically in Dutch**, every one a genuine
cognate: *acceptor, baryon, boson, bra, commutator, diode, donor, fermion,
hadron, interval, ket, lepton, meson, nuclide, quark, separatrix, spin, spinor,
supernova, synchrotron*. Dutch now writes **300** distinct keys against
English's 297.

## The link audit

`tools/term_config/book5_nl.py` was rewritten, not seeded:

* `EXTRA` was rebuilt from `comm(1)` on the two target sets. The first diff
  showed **29 English targets unreachable in Dutch**, every one for the same
  structural reason — `harvest.py` takes only an `\index` entry containing a
  space, and Dutch welds what English writes as two words. Entries were added
  for those 29, then for **38 more welded compounds whose English name is two
  words** (*driftsnelheid* ← drift velocity, *toestandssom* ← partition
  function, *zwartestraling* ← blackbody radiation, *röntgendiffractie* ← X-ray
  diffraction, …). Nothing was added that English leaves unlinked, so the
  Dutch book links the same notions, not more.
* `DROP` stays empty; the Dutch harvest produced no artefacts.
* `STOP`: the five Book-5 words (*spin*, *metaal*, *gebeurtenis*, *observabele*,
  *gat*) are doing real work and each is an `\index` key here. The words carried
  from `book4_nl.py` were re-tested one by one against this book's harvest: not
  one of them is a Book 5 term, so none removes a link; they are kept as a guard
  for the plain senses they name.
* `EXTRA_PROTECT`: the seed's `\bluchtweerstand\b` protected nothing here and was
  removed. It is replaced by `\bketens?\b`, which fixes a **Dutch morphology
  accident found by counting the generated surface forms**: `lang_nl.py` inflects
  the term *ket* to *keten*, the ordinary Dutch word for *chain*, and unmasked it
  produced **38 links** — decay chains, the photon--baryon chain, the Ising chain
  — all pointing at `def:b3:quantum-formalism:state`. No census sees this;
  English never links *ket* at all.

Result: **817 links, 245 linkable terms, 131 targets, all 100 English targets
covered**, `--check` clean. The 0.89× density against English is the
welded-compound tax the brief predicts for Dutch; it is up from 0.60× before the
`EXTRA` rebuild, and the 38 bogus *keten* links were removed on purpose, not lost.

## Sampled passages, verdicted

1. **`nl/03-continuum-elasticity.tex:3` (chapter hook).**
   *"Druk uw oor tegen een lange stalen rail terwijl een werkman er ver weg op
   slaat: u hoort twee klappen --- één door het staal, één door de lucht, een
   seconde of meer uit elkaar."* — **native**. Imperative opening, formal
   address matching Book 4 nl, the `één door… één door…` parallel is Dutch
   idiom rather than a calque of *one through… one through…*.
2. **`nl/21-phase-transitions.tex:3` (chapter hook).**
   *"Verwarm water één graad en er gebeurt weinig --- tot de vloeistof zich bij
   één scherp bepaalde temperatuur tot damp openscheurt."* — **native**.
   `zich … openscheurt` is the reflexive Dutch would actually pick for *tears
   itself*; the `Verwarm … en …` conditional-imperative is native construction.
3. **`nl/22-electromagnetism-in-matter.tex:241` (definition body).**
   *"Een ruwe klomp ijzer is niet gemagnetiseerd: hij valt uiteen in domeinen,
   gebieden op micronschaal die elk volledig gemagnetiseerd zijn maar
   verschillend gericht, zodat het uitwendige veld (en de energieprijs ervan)
   vrijwel wegvalt."* — **native**. Verb-final subordinate clause, `ervan` for
   the possessive, `wegvalt` where a machine would have written *bijna annuleert*.
4. **`solutions/nl/27-astrophysics.tex:206` (solution prose).**
   *"Zijn zuurstof werd in de schil van een massieve ster gefuseerd en door een
   supernova naar buiten geslingerd; het ijzer werd in het explosieve einde zelf
   gesmeed; beide dreven door de interstellaire wolken, voegden zich bij de
   zonnenevel, de aarde, de zee, de voedselketen --- en de lezer."* —
   **native**. The three-clause cadence survives; `voegden zich bij` is the
   Dutch verb, not a calque of *joined*.
5. **`nl/26-particle-physics.tex:78` (remark, four interactions).**
   *"De sterke kracht (gluonen) grijpt quarks met een potentiaal die met de
   afstand groeit --- trek twee quarks uit elkaar en het uitgerekte veld knapt
   tot een vers quark-antiquarkpaar."* — **near-native**. Correct and idiomatic,
   but `knapt tot` is a shade more colloquial than the surrounding register;
   `springt uiteen in` would sit a hair better in a *collegedictaat*.

## Why not 100

* **Subscript abbreviations.** Twenty `\text{}` bodies (*orb*, *osc*, *lab*,
  *exc*, *loc*, *rot*, *vib*, *vap*, *fus*, *liq*, *conf*, *nuc*, *sep*,
  *grav*, *esc*, *extra*) were left as the canon writes them. They are
  Latin-derived and read identically in a Dutch text, but a Dutch author writing
  from scratch might have chosen *lok*, *aang* or *verd* for a few of them. The
  word-length `\text{}` bodies were all translated (*iron* → *ijzer*, *gap* →
  *spleet*, *vapour* → *damp*, *liquid* → *vloeistof*, *peak* → *piek*, *proper*
  → *eigen*, *nucleus* → *kern*, *band* → *elastiek*, *quark level:* →
  *quarkniveau:*).
* **Link density.** 0.89× English. Dutch structurally loses links that English
  gets for free, and `EXTRA` can only restore the ones whose English twin is a
  two-word term; single-word English index keys (*fusion*, *fission*,
  *activity*, *phonon*, *superfluidity*, *half-life*) are lost on **both** sides
  and were deliberately not "fixed" in Dutch alone.
* **One near-native sample.** Passage 5 above is idiomatic but a register notch
  loose; a full second pass over the 27 remark environments would likely find a
  handful more of these.
* **Length.** 320 pages against 302. Nothing was padded, but Dutch compounding
  plus obligatory articles costs about 6 %, and a tighter pass could recover
  perhaps a page or two of that without loss.

## Cohort note (reported to the coordinator)

Two defect classes here affect **all seven editions**, not just Dutch:

1. **Inherited TeX accent escapes.** The English canon itself writes
   `Segr\`e`, `Panth\'eon`, `Amp\`ere` (3 sites) and `\aa ngstr\"om` /
   `angstr\"om` (3 sites). Because `id_apply` patches are byte-identical
   substitutions on the English twin, every Latin-script edition inherits them
   verbatim — and `check_translation.sh` gate 6 fails **only on translations**,
   never on English, so the canon never warned anyone. Fixed here as UTF-8.
2. **`\index{}` keys in late chapters.** Nothing in the toolchain checks index
   keys, and the `index` census in `id_apply` compares counts only. 120 of this
   edition's keys were still English after the bodies landed.
