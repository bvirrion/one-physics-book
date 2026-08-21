# One Physics Book 3 (University, Year 1) — Dutch edition: self-score

**Date:** 2026-08-21
**Quality bar:** *native academic* (the bar of `translation_instruction.md`).
**Sense/structure reference:** the English canon (`parts/bachelor-1/*.tex`) for
content; the French twin (`parts/bachelor-1/fr/`) as a sense and curation
reference, never as a ceiling. For settled Dutch physics vocabulary the
comparands were the Dutch Books 1–2 of this series (`parts/grade-*/nl/`) —
*uittree-arbeid*, *remspanning*, *zelfinductie*, *traagheidsmoment*,
*schijnkracht* — and `../one-math-book/parts/bachelor-1/nl/` for the
university lecture register.

## Overall: **96 / 100**

| Dimension | Score | Note |
|---|---:|---|
| **Register** (academic Dutch, weighted) | **96** | Dutch *collegedictaat* voice: narrative present in the chapter openings ("Duw een kinderschommel op het verkeerde moment aan en er gebeurt weinig"), `Toon aan dat…` / `Leid af…` / `Bepaal…` / `Ga na dat…` imperatives in exercise stems, `Beschouw…` / `Noteer…` / `Oriënteer…` in proofs and definitions. Verb-final subordinate clauses throughout; no `wij zullen aantonen` padding, no English clause order. |
| **Terminology** (weighted) | **96** | Settled glossary below; every `\index{}` key equals its visible term. No sense swaps found on sampling: *spanning* is the electrical quantity everywhere (Dutch calls the rope's pull *spankracht*), *koppel* is the torque and nothing else, *weerstand* is stoplisted because it is both the resistor and the drag of a fluid, *kern* only ever appears as a compound or a parenthesised term. |
| **MT-artifact freedom** (weighted) | **96** | Residual-English sweep over all 60 files returns **zero** English tokens in visible text (the only hits are `%` comments, the label slugs inside `\omterm{}`/`\begin{solution}{}`, and the credit line "US Department of Energy" in a photo caption). Gate 9 (`tools/check_latin_prose.py`) is down from 66 hits to 29, and every survivor is a genuine Dutch cognate — see the table below. |
| Structure | **100** | `bash tools/check_translation.sh bachelor-1 nl` **PASSED**. Every body written as line-range replacements on the English canon through `tools/id_apply.py`, so labels, `\cref` targets, `\begin{solution}{key}`, `\qty{}{}`, `\foreach`, `xtick=` and every math display are byte-identical to English. 897 `\label{}` ↔ 897; 390 `solution` envs ↔ 390; 30 `problem` envs ↔ 30. |
| LaTeX hygiene | **99** | 0 errors, 0 undefined references, **0 overfull boxes**; `nullfont` count 65 = the English baseline (a canon artefact inside drawing code, byte-identical in both logs). 0 TeX accent escapes, 0 "invalid in math mode", 0 non-ASCII inside `\qty{}`/`\unit{}`/`\num{}`. |
| Cross-references | **100** | Ordered `\label{}` sequence diffs to zero lines against English across bodies and solutions. 12 exercises (4★ / 5★★ / 3★★★) + 1 weekend problem per chapter, one solution each. |
| Figures | **98** | Drawing code byte-identical to English (enforced by `id_apply`'s `draw` census); only node text, axis labels and `{\small …}` captions translated. Two node strings shortened in ch. 28 to clear an overfull picture; the chapter-10 op-amp node texts (*verzadigd*, *lineair, helling*, *volger*, *inverterend*, *niet-inverterend*) were caught untranslated by gate 9 and fixed. |
| Solutions | **96** | All 30 solution files translated; `\textbf{n.}` numbering and every number preserved; headers read `\section*{Hoofdstuk \ref{ch:…} --- <Nederlandse titel>}` with the `ch:…` slug unchanged. |
| Defined-term links | **95** | 2 173 `\omterm` links against English's 2 342 (**0.93×** — thinner than English by construction, which is the expected Dutch shape). Target-set parity: 203 distinct targets vs English's 196; only 5 English targets are unreached, each carrying a single English link. |

**Overall 96**, weighted toward register + terminology + MT-artifact freedom.

## What this session produced

Chapters 01–15 (bodies + solutions) were already on disk from the earlier leg.
This pass added:

1. **Chapters 16–30** — 15 bodies and 15 solution files, all written as
   line-range replacements through `tools/id_apply.py --no-gate`, including the
   15 weekend problems and their 25-question solutions.
2. **`tools/term_config/book3_nl.py`** — curated from `book3_en.py` with the
   French curation as a cross-check, then the whole Dutch link layer generated
   (2 173 links across 58 files).
3. **Post-fix sweep over the whole book, chapters 01–30** — the untranslated
   TikZ node texts and `\text{}` subscripts gate 9 found in the earlier leg's
   chapters, three overfull boxes (chs. 13 sol., 28 fig., 26 sol.), and the
   three English words the canon smuggles into `\qty{}` arguments.

## Structural / build gates

| Gate | Result |
|------|--------|
| `bash tools/check_translation.sh bachelor-1 nl` | **PASSED** |
| `latexmk one_physics_book_3_university_year_1_nl.tex` | OK |
| Fatal errors (`grep -ac '^!'`) | **0** |
| Undefined references | **0** |
| Overfull `\hbox` | **0** |
| `nullfont` | 65 — **equal to the English log**, byte-identical lines (canon drawing code, not a translation defect) |
| Non-ASCII inside `\qty{}`/`\unit{}`/`\num{}` | **0** |
| TeX accent escapes (`\'e`-class) | **0** — accents are raw UTF-8 (*Thévenin*, *Panthéon*, *coëfficiënt*, *vacuüm*) |
| `python3 tools/link_defined_terms.py --book 3 --lang nl --check` | every file matches what the config generates (**2 173** links, 437 linkable terms) |
| PDF | `build/one_physics_book_3_university_year_1_nl.pdf`, **344 pp** (EN 332 pp) |
| LaTeX warnings | 8 vs EN 7; the 6 `hyperref Token not allowed` are the same math-in-title warnings English has, the extra one is `dutch.ldf not found; building Dutch without babel`, emitted by `styles/onephysics.sty` by design |
| `--force-classes` / `!class` opt-outs used | **none** |

## Gate 9 (`tools/check_latin_prose.py`) — 29 surviving hits, all judged

| Survivor | Verdict |
|---|---|
| `spin` (13×, ch. 15 + solutions) | Dutch uses *spin* for the spin angular momentum; the orbital counterpart was renamed `\text{orb}` → `\text{baan}` in this pass |
| `rot`, `ind`, `iso`, `enc`→`oms` | mathematical subscript abbreviations; *rot* (rotatie), *ind* (geïnduceerd), *iso* (isotherm) are the Dutch abbreviations too. `\text{enclosed}`/`\text{enc}` **were** English and are now `\text{oms}` (omsloten) |
| `lens`, `sensor`, `water`, `anode`, `flux`, `volume`, `atm`, `isotherm`, `compressor`, `seismometer`, `integrator`, `dee` (figure nodes) | all Dutch words or international technical terms; translating them would be wrong |
| `driver` (ch. 9 sol.) | the loudspeaker driver; *driver* is the standard Dutch audio term |
| `fret 5 …, fret 7 …, fret 12 …` (ch. 5 sol., flagged as a `dup`) | a line of numbers plus *fret*, the Dutch guitar term — false positive of the duplicate-line heuristic |

Fixed in this pass (genuine untranslated English found by the gate): the eight
chapter-10 op-amp figure nodes, `\text{(no load losses, no magnetizing
current)}` (ch. 29), `\text{enclosed}`/`\text{enc}` (ch. 28), `\text{circuit}`
→ `\text{kring}` (ch. 28), `\text{own}` → `\text{eigen}` (ch. 29),
`\text{loop}` → `\text{lus}` (ch. 6), `\text{top}`/`\text{bottom}` →
`\text{boven}`/`\text{onder}` (chs. 11, 12), `\text{cable}` → `\text{kabel}`
(ch. 6 sol.), `\text{drag}` → `\text{wr}` (ch. 12 sol.), `\text{orb}` →
`\text{baan}` (ch. 15) — 37 of the 66 hits.

## Samples (native / near-native / MT)

| Sample | Verdict |
|--------|---------|
| ch. 01 opening (written in the earlier leg) | **native** — "Natuurkunde meet, en een meting zonder haar onzekerheid is een gerucht." Idiomatic, aphoristic, not a calque |
| ch. 08 opening (earlier leg) | **native** — "Draai aan de knop van een oude radio en van de honderd zenders die de antenne allemaal tegelijk bereiken komt er één door"; "Het net dat in elke muur bromt is een sinus van 50 Hz" |
| ch. 14 opening (earlier leg) | **native** — "Duw een kinderschommel op het verkeerde moment aan en er gebeurt weinig; duw één keer per periode, zacht, en binnen een tiental slagen gilt het kind boven in de boog" |
| ch. 18 §"Dynamica in een niet-inertiaalstelsel" + weekend problem (this pass) | **native** — "schijnkrachten zijn geen wisselwerkingen"; "Controle: schijnkrachten verschijnen nooit in de energiebalans als ``arbeid van iemand''" |
| ch. 23 opening (this pass) | **native** — "Een film die achteruit draait herkent men meteen; de moleculen gehoorzamen wetten zonder pijl, en de wereld heeft er een." |
| ch. 30 opening (this pass) | **native** — "Stuur elektronen één voor één door twee spleten en zij landen als stippen, elk op één plaats --- en die stippen bouwen zich over duizenden heen op tot de strepen van een golf." |
| ch. 21 solutions 1–2 (this pass) | **native** — "Een pomp kan hoogstens een vacuüm boven het water maken: de atmosfeer duwt de kolom dan omhoog" |
| ch. 26 solution 5 (this pass, reworded three times to clear an overfull box) | **near-native** — correct and compact, but the telegraphic "Ring met straal $a$, dikte $\dd a$: …; integreer:" keeps the English solution's shorthand rhythm rather than recasting it as a Dutch sentence |
| ch. 10 figure captions (earlier leg, repaired here) | **near-native** — the node texts were English until this pass; they are now Dutch, but they were written by the repair, not by the original drafting hand |

## Defined-term links (`\omterm`) — target parity vs English

Regenerated with `--unwrap --apply`, then `--apply`, then `--check` (green).
**2 173 links, 437 linkable terms, 203 distinct targets** (English: 2 342 links,
467 terms, 196 targets).

Dutch runs *thinner* than English by construction and that is the correct
shape: `lang_nl.py` sets `DERIVE = False` and refuses to match a component
inside a compound, and `harvest.py` only takes an `\index` entry that contains
a space — so *knooppuntregel*, *impulsmomentstelling*, *rechterhandregel*,
*tweelichamenprobleem* hide their own heads. Nothing was restored for those,
because their English twins are named results that English drops through
`NOT_A_TERM` anyway.

| Divergence | Verdict |
|---|---|
| EN links `thm:b1:magnetostatics:ampere` on "Ampère's law"; Dutch says *stelling van Ampère*, which `NOT_A_TERM`'s `"stelling"` deletes | **restored by hand** in `EXTRA`, exactly as the French edition restores *théorème d'Ampère*. The two editions now carry the same link |
| The 18 Dutch *wet van …* results (Archimedes, Biot–Savart, Cauchy, Coulomb, Faraday, Gauss, Hooke, Laplace, Lenz, Ohm, Snellius, Stokes, Joule, Kepler, Kirchhoff, Newton, wrijvingswetten van Coulomb, derde wet van Kepler) | **all linked**. `"wet van"` is deliberately absent from `NOT_A_TERM`: the English default `"law of"` never fires on "Gauss's law", so translating it word for word would have silently deleted every named law. Bare `"wet"` is absent too — it would swallow *wetten van Kirchhoff* and, as a substring, *wetenschap* |
| 39 English targets reached by an English two-word term that Dutch welds solid (*schijnkracht*, *corioliskracht*, *traagheidsmoment*, *laplacekracht*, *uittredepupil*, *spanningsdeler*, *stroomdeler*, *uittree-arbeid*, *remspanning*, *eindsnelheid*, *normaalkracht*, *cyclotronfrequentie*, *drukmiddelpunt*, *massaspectrometer*, *snelheidsfilter*, *wegverschil*, *waterstofatoom*, *zwaartekrachtveld*, *schaalhoogte*, *symmetrievlak*, *grondtoestand*, *werkpunt*, *belastingslijn*, *schmitttrigger*, *verschilversterker*, *sommeerversterker*, *kwantumdot*, *punteffect*, *perkenwet*, *debroglie-golflengte*, *tunneleffect*, *versnelspanning*, *wervelstroom*, *bohrstraal*, *relaxatieoscillator*, *hoogdoorlaatfilter*, *ottokringproces*/*stirlingkringproces*/*dieselkringproces*, *RC-/RL-/RLC-kring*, *Hohmann-transfer*) | **restored by hand** in `EXTRA`, one entry per English link target. This is what took the target gap from 44 down to 5 |
| 14 terms whose attributive adjective inflects (*het lineaire netwerk* beside *lineair netwerk*, *het aardse stelsel*, *het kritische punt*, *het gemiddelde vermogen*, …) | **restored by hand**: `lang_nl.py` puts its plural tail on the last word only, so the -e form has to be declared beside the base |
| 5 English targets still unreached (`prop:b1:potential-capacitors:reading`, `prop:b1:filters-transfer-functions:rlc`, `ex:b1:induction:eddy`, `def:b1:kinetic-theory:equilibrium`, `def:b1:central-forces:central`) | each carries **exactly one** English link; the Dutch word occurs only inside its own defining statement, where the linker never links. Left as is |
| NL reaches 12 targets English does not (`thm:b1:first-law:firstlaw`, `thm:b1:second-law-entropy:secondlaw`, `thm:b1:central-forces:conics`, `thm:b1:mirrors-thin-lenses:lensconj`, `prop:b1:second-law-entropy:clausiuskelvin`, …) | all **correct sense**, reached from a Dutch phrase whose English twin is a one-word homonym English stoplists (*eerste/tweede hoofdwet*, *wetten van Kepler*, *betrekking van Descartes*, *uitspraak van Clausius/Kelvin*) |

### Config deltas (`tools/term_config/book3_nl.py`)

- **`NOT_A_TERM`** — the ten single-word English keywords translated
  (*stelling, lemma, ongelijkheid, formule, criterium, principe, identiteit,
  regel, paradox, probleem*); `"law of"` deliberately **not** translated.
- **`STOP` (21 entries)** — the English stoplist term for term (*kracht, massa,
  snelheid, versnelling, impuls, druk, temperatuur, warmte, arbeid, bar,
  moment, beeld, versterking, flux, eenheid, dimensie, toestandsverandering,
  objectief*) plus the two Dutch-only homographs **weerstand** (the resistor of
  chs. 6–10 *and* the drag of chs. 12, 18) and **capaciteit** (the capacitance
  of ch. 27 *and* the capacity of a compressor or of a fibre link).
  Two French traps do **not** transfer: *spanning* is voltage everywhere in
  this book because Dutch calls the rope's pull *spankracht*, and *koppel* is
  the torque and nothing else (chs. 15, 27–29 read in full) — both stay linked.
- **`DROP`** — the bare adjectives *ideale, lineair, conservatief, centraal,
  centraal conservatief*, harvested from definitions that merely use them.
- **`EXTRA` (67 entries)** — the compound and inflection restorations above.
- **`EXTRA_PROTECT`** — `\bluchtweerstand\b`, so the compound is never broken
  into (bare *weerstand* is stopped anyway).

## Why not 100

- The Dutch link layer is 0.93× English and five English targets stay unreached.
  That is the language's own shape rather than a defect, but it is a measurable
  gap against the English reading experience.
- Three passages were reworded to clear overfull boxes rather than because the
  Dutch wanted rewording; no Dutch hyphenation patterns are installed in this
  build, so long compounds cannot break and the fix is always lexical. The
  chapter-26 solution in particular is now correct but terse.
- Chapters 01–15 were drafted in an earlier leg and shipped with eight English
  figure nodes and a dozen English `\text{}` subscripts; they are fixed, but
  the fact that the twin-comparison gate had to find them means the first leg's
  figure pass was not as careful as the second's.
- The book is 344 pp against English's 332: Dutch compounding buys density in
  words and loses it in line breaks. Nothing is wrong with the setting, but the
  edition is not as tight as the English canon.
