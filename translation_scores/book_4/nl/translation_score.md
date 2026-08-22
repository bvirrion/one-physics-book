# One Physics Book 4 (University, Year 2) — Dutch edition: self-score

**Date:** 2026-08-22
**Quality bar:** *native academic* (the bar of `../../../translation_instruction.md`
and `nl` practice, i.e. the university *collegedictaat* register).
**Sense/structure reference:** the English canon (`parts/bachelor-2/*.tex`,
`parts/bachelor-2/solutions/*.tex`) for content; the French twin
(`parts/bachelor-2/fr/`) as a sense reference, never as a ceiling. For settled
Dutch physics vocabulary the comparands were Book 3 nl
(`parts/bachelor-1/nl/`, 96/100) and Books 1–2 nl.

## Overall: **96 / 100**

| Dimension | Score | Note |
|---|---:|---|
| **Register** (academic Dutch, weighted) | **96** | *Collegedictaat* voice held over 31 chapters: narrative present in the openings ("Kantel een compactschijf onder een lamp en zij werpt een regenboog"), `Toon aan dat…` / `Leid af…` / `Ga na dat…` / `Bepaal…` / `Vat samen…` in exercise stems, `Beschouw…` / `Neem…` / `Zoek…` / `Vul in` in proofs. Verb-final subordinate clauses throughout; no `wij zullen aantonen` padding, no English clause order, no calqued participial openings. |
| **Terminology** (weighted) | **96** | One settled glossary across bodies and solutions (see below); every `\index{}` key equals its visible Dutch term. Sense discipline: *midden* is the physical medium, *fluïdum* the fluid, *spankracht* the string tension against electrical *spanning*, *weerstand* stoplisted because it is at once the resistor (ch. 10), the drag (ch. 04) and the thermal resistance (ch. 25); *lager* stoplisted because it is the bearing of ch. 01 and the comparative "lower" everywhere else. |
| **MT-artifact freedom** (weighted) | **96** | Residual-English sweep over visible prose (drawing environments and math stripped) returns **zero** English function words after Dutch homographs (*of*, *was*, *in*, *over*, *door*, *als*) are excluded — the one survivor, a stranded `only if` in ch. 09 left outside a range, was found and fixed. Gate 9 is down from 181 findings to **34**, all one-word true cognates plus one proper-name label; Book 3 nl shipped at 26 on 60 files. |
| Structure | **100** | `bash tools/check_translation.sh bachelor-2 nl` **PASSED**. Every one of the 62 files written as line-range replacements on the English canon through `tools/id_apply.py`, so labels, `\cref` targets, `\begin{solution}{key}`, math displays, `\qty{}{}` and drawing code are byte-identical to English. Ordered `\label{}` sequence diffs to **0 lines** against English (801 ↔ 801); 403 `solution` envs ↔ 403; 31 `problem` envs ↔ 31; 372 exercises. |
| LaTeX hygiene | **99** | 0 errors, 0 undefined references, **0 overfull boxes**, 0 "invalid in math mode"; `nullfont` **60 = the English baseline** (a canon artefact in drawing code, unchanged). 0 TeX accent escapes — including the inherited `von K\'arm\'an` in ch. 04, rewritten as UTF-8 `von Kármán`. No `\hyphenation{}` list was needed. |
| Cross-references | **100** | Identical ordered label sequence; every `\cref`, `\ref` and solution key preserved by the tool, not by hand. |
| Figures | **97** | Drawing code byte-identical to English (enforced by `id_apply`'s `draw` census); node text, axis labels, `\legend{}`, `\addlegendentry{}` and `{\small …}` captions translated. Two `!draw` opt-outs remain, both for `\foreach` label lists that carry prose (ch. 07 decibel ladder, ch. 23 emission labels); both lists were re-read by eye after the final write. |
| Solutions | **96** | All 31 solution files translated; `\textbf{n.}` numbering, every number and every unit preserved; headers read `\section*{Hoofdstuk \ref{ch:…} --- <Nederlandse titel>}` with the `ch:…` slug unchanged. |
| Defined-term links | **95** | **1 166** `\omterm` links against English's **1 231** (0.95×) across **145** distinct targets against English's 143. `tools/term_config/book4_nl.py` rewritten from scratch: the Book 3 seed's **67 dangling `EXTRA` targets** (all `…:b1:…`) are gone, replaced by 71 Book-4 targets, 0 dangling. |

**Overall 96**, weighted toward register + terminology + MT-artifact freedom.

## Structural / build gates

| Gate | Result |
|------|--------|
| `bash tools/check_translation.sh bachelor-2 nl` | **PASSED** |
| `latexmk -g one_physics_book_4_university_year_2_nl.tex` | OK, exit 0 |
| Fatal errors (`grep -c '^! '`) | **0** |
| Undefined references | **0** |
| Overfull `\hbox` | **0** |
| `nullfont` | **60** — equal to the English baseline |
| `invalid in math mode` | **0** |
| Non-ASCII / English words inside `\qty{}` / `\unit{}` / `\num{}` | **0** — every unit argument read by eye; the 17 English words the canon smuggles in are Dutch (`dag`, `dagen`, `jaar`, `kWh/jaar`, `kWh/dag`, `K.dag`, `omw/s`, `omw/min`, `lijnen/mm`, `beelden/s`, `franje`, `kg/jaar`); `cent` kept, it is the musical interval |
| TeX accent escapes (`\'e`-class) | **0** (raw UTF-8: *coëfficiënt*, *vacuüm*, *Kármán*, *Ampère*, *Fabry–Pérot*) |
| End-of-line elision apostrophe / leading punctuation / split hyphen | **0 / 0 / 0**, re-swept after the final edit and after the term-link pass |
| `python3 tools/check_latin_prose.py …` (gate 9) | 34 findings, all cognates (table below) |
| `python3 tools/link_defined_terms.py --book 4 --lang nl --check` | every file matches what the config generates (**1 166** links, 355 linkable terms) |
| `.fls` sanity | **62** distinct `parts/bachelor-2/**/nl/*.tex` — the whole edition, forced rebuild |
| PDF | `build/one_physics_book_4_university_year_2_nl.pdf`, **359 pp** (EN 345 pp, fr 345, hi 358, ar 357) |
| `--force-classes` used | **none**; `!draw` on two ranges only (ch. 07, ch. 23 `\foreach` label lists) |

## Sampled passages, judged

Five passages read cold against the English and against Book 3 nl.

1. **ch. 19, opening (native).** "Een zeepbel bestaat uit een kleurloze
   vloeistof en schittert toch van kleur; een olievlies op een natte weg toont
   dezelfde regenboogbanden…" — the semicolon chain and the fronted concessive
   *en schittert toch* are Dutch construction, not English order; *olievlies*
   and *regenboogbanden* are welded the way Dutch welds.
2. **ch. 25, Fourier's law statement (native).** "Warmte stroomt de
   temperatuurgradiënt af, van warm naar koud --- de tweede hoofdwet ingebouwd
   in een lineaire wet." *de gradiënt af* (separable, verb-final) is the Dutch
   idiom for "down the gradient"; *hoofdwet* is the Dutch name of the law.
3. **ch. 28, entropic elasticity (native).** "de band trekt terug omdat zijn
   uitgerekte ketens minder schikkingen hebben" — verb-final causal clause,
   *schikkingen* (not *configuraties*) for the microstates.
4. **ch. 23, proof of the Einstein relations (near-native).** "de limiet
   $T \to \infty$ (waar $u \to \infty$) dwingt $B_{12} = B_{21}$ af" — correct
   and idiomatic, but the split *dwingt … af* straddles a long parenthesis and
   a mathematician would probably re-order; it reads like careful written
   Dutch rather than spoken lecture Dutch.
5. **ch. 31 solutions, item 24 (near-native).** "Zij wordt door het molecuul
   alleen vastgelegd, is voor elk molecuul dezelfde en ongevoelig voor de
   buitenwereld" — accurate, but the three-member coordination keeps the
   English rhythm; *het trekken van de holte* for "cavity pulling" is a literal
   rendering of a term Dutch labs usually leave in English.

No passage read as machine translation.

## Settled glossary (excerpt)

fluïdum · vloeistof · stroomlijn / baanlijn / stroombuis · massadebiet /
volumedebiet · continuïteitsvergelijking · onsamendrukbaar · vorticiteit ·
rotatievrij · stuwpuntstroming · puntwervel · stelling van Bernoulli ·
stuwdruk · venturimeter · pitotbuis · draagkracht · drukleiding · waterslag ·
viscositeit / schuifspanning / hechtvoorwaarde · reynoldsgetal · laminair /
turbulent · stroming van Poiseuille · wet van Stokes · grenslaag ·
weerstandscoëfficiënt · oppervlaktespanning / laplacedruk · controlevolume ·
impulsbalans · stuwkracht · peltonturbine / schoep · drukhoogte / opvoerhoogte ·
spankracht · golfvergelijking van d'Alembert · eigentrillingen / harmonischen /
grondtoon · knoop / buik · impedantie · elasticiteitsmodulus · wet van Hooke ·
overdruk · geluidssnelheid · geluidsniveau · dopplereffect · machkegel ·
dispersierelatie · fasesnelheid / groepssnelheid · golfpakket · evanescent ·
afsnijfrequentie · zwevingen · draaggolf / omhullende · coaxkabel ·
telegraafvergelijkingen · karakteristieke impedantie · terugkoppeling /
lusversterking · wienbrugoscillator · hysteresecomparator / schmitttrigger ·
astabiele multivibrator · bemonstering / aliasing / antialiasingfilter ·
kwantisatie · synchrone detectie / lock-in · ladingsdichtheid /
stroomdichtheid · driftsnelheid · model van Drude · geleidbaarheid /
soortelijke weerstand / beweeglijkheid · halleffect · gradiënt / divergentie /
rotatie / laplaciaan · vergelijkingen van Maxwell · verplaatsingsstroom ·
vectorpotentiaal / ijk · overgangsrelaties · quasistationair · poyntingvector ·
stralingsdruk · polarisatie · polarisator / wet van Malus · dubbelbreking /
golfplaatje · plasmafrequentie · huideffect / indringdiepte · diëlektricum /
susceptibiliteit · hoek van Brewster · totale interne weerkaatsing ·
staandegolfverhouding · golfgeleider / trilholte · glasvezel / numerieke
apertuur · oscillerende dipool / stralingszone · formule van Larmor ·
stralingsweerstand · rayleighverstrooiing · optische weglengte / golffront ·
golftrein / coherentietijd / coherentielengte · streepafstand / wegverschil ·
gekanneleerd spectrum · michelsoninterferometer / bundelsplitser /
compensatieplaat · luchtwig / luchtplaat · tralie / tralievergelijking /
hoofdmaximum / nevenmaximum · finesse / vrij spectraal bereik · buiging /
fraunhoferbuiging / airyschijf · fouriervlak / ruimtelijke filtering ·
gestimuleerde emissie / bevolkingsinversie / verzadigingsintensiteit ·
gaussische bundel / taille / rayleighlengte · diffusie / aantalsdichtheid /
diffusiecoëfficiënt · toevalswandeling · warmtegeleiding / warmteweerstand /
biotgetal / koelrib · warmtestraling / zwart lichaam / emissievermogen /
broeikaseffect · open systeem / controlevolume / enthalpie / straalpijp /
smoorventiel / warmtewisselaar · vrije energie / vrije enthalpie / chemische
potentiaal · boltzmannfactor / toestandssom / schaalhoogte · golffunctie /
regel van Born / stationaire toestand / golfpakket · opsluitingsenergie /
tunneleffect / tunnelsplitsing.

## Gate 9 (`check_latin_prose.py`): the 34 survivors

| Class | Count | Verdict |
|---|---:|---|
| `text-1word` | 22 | `cond` (condensor), `mol`, `kin` (kinetisch), `diss` (dissipatie), `volume`, `tel` (telescoop), `sub` (sublimatie), `water`, `ppm`, `(even)` — Dutch subscripts and words that happen to be spelled as in English. The genuinely English subscripts were all translated: `sat`→`verz`, `liq`→`vl`, `vap`→`damp`, `fus`→`smelt`, `ice`→`ijs`, `slip`→`glij`, `evap`→`verd`, `out`→`uit`, `esc`→`ontsn`, `rev`→`omk`, `coll`→`bots`, `cavity`→`holte`, `fins`→`ribben`, `exch`→`uitw`, `vib`→`tril`, `strip`→`strook`, `slit`→`spleet` (128 sites). |
| `node-1word` | 11 | `laser`, `turbine`, `sensor`, `radio`, `violet`, `chip`, `contrast`, `evanescent` — all correct Dutch. |
| `text` (multi-word) | 1 | `(Maxwell--flux)`, the proper name of $\operatorname{div}\vect B = 0$ in the `align*` of ch. 11; the other three names on the same display (Gauss, Faraday, Ampère) are proper names too. Translating it alone made gate 9 report a `dup` on the next, pure-mathematics line, so it is kept as English keeps it. |

The multi-word findings that *were* defects are all gone: `in one dimension` →
`in één dimensie`, `(one dimension)` / `(three dimensions)` → `(één dimensie)` /
`(drie dimensies)`, `; the kinetic theory gives` → `; kinetische theorie:`,
`(3D, with` → `(3D, met`, `left/right` → `links/rechts`, `for light` →
`voor licht`, `(odd)` → `(oneven)`, plus the seven multi-word figure strings
(`medium 1/2` → `midden 1/2`, `plateau ≈ 0.45` → `vlak stuk ≈ 0.45`,
`$\vect v$ (drift)` → `(driftsnelheid)`, `evanescent, …` → `evanescente golf, …`,
`rubber: …` → `voor rubber: …`, `plasma, …` → `in plasma, …`,
`$\xi\tan\xi$ (even)` → `(even toestanden)`).

## The index layer

`\index{}` was the edition's largest single defect and is now closed: **433**
index entries, of which **7** are still spelled as in English and all seven are
true Dutch cognates (*decibel*, *aliasing*, *nabla*, *plasma*, *finesse*,
*laser*, *turbine*). 117 English entries — the whole of chapters 19–31 plus
strays — were translated, which also fixed the printed index and fed the term
harvest.

## `tools/term_config/book4_nl.py`

Rewritten, not patched. What the file now says, and why:

* **`EXTRA` (71 entries, 0 dangling).** The seed's 67 Book 3 targets are gone.
  Every entry restores exactly one target that the English harvest reaches and
  the Dutch one cannot, because the Dutch name is welded into one word and
  `harvest.py` skips any `\index` entry without a space: *coherentielengte*,
  *wegverschil*, *poyntingvector*, *fraunhoferbuiging*, *coaxkabel*,
  *tunneleffect*, *schaalhoogte*, *traagheidsmoment*, … The list was built by
  diffing the two target sets (`--terms | awk '{print $NF}' | sort -u`, then
  `comm`) and then by diffing the two *link* sets, never by guesswork. An
  earlier attempt that added an `EXTRA` for **every** welded compound (136 of
  them) was reverted: it produced 1 472 links against English's 1 231 and
  47 links on *polarisator* alone, because English's own harvest skips its
  one-word index entries too.
* **`STOP`.** The five English stops term for term (*laser*, *drempel*,
  *stationair*, *rendement*, *absorptie*) plus the Dutch words that are
  ordinary language in this register (*arbeid*, *druk*, *kracht*, *massa*,
  *moment*, *snelheid*, *weerstand*, *flux*, *vermogen*, *spanning*, *stroom*,
  …) and *lager*, which carried 20 wrong links as the comparative "lower".
  Confirmed after the fact, as instructed: *lager* now carries **1** link, the
  in-chapter bearing sense that `harvest.py` keeps through the per-chapter map.
* **`DROP`.** The capitalised heads of the ch. 27 itemize
  (*Straalpijp*, *Smoorventiel*, *Warmtewisselaar*, *Compressor, pomp,
  turbine*), whose lowercase nouns are restored through `EXTRA`.

Link parity: **1 166 / 1 231 = 0.95×**, **145 targets against 143**. Four
English-linked labels have no Dutch link (`met:b2:rigid-body-mechanics:incline`,
`rem:b2:plane-waves-polarization:spectrum`,
`thm:b2:plane-waves-polarization:wave`, `prop:b2:guided-waves:cavity`): in each
the Dutch term occurs only inside its own environment, or linking it produced
22 links against English's 1. One label is over English by 10
(`def:b2:dispersion-wave-packets:complex`, 60 vs 50) because *verzwakking* and
*indringdiepte* are both single Dutch words for what English splits.

## Why not 100

1. **Four English link targets are unreached and one is over-linked** (above).
   Perfect parity would need a Dutch synonym per target that the register does
   not naturally supply. −2 on *Defined-term links*.
2. **Two `!draw` opt-outs.** Chapters 07 and 23 have `\foreach` label lists
   that carry prose; opting a *range* out opts the *file* out of the drawing
   census, so those two files' drawing code is verified only by eye and by
   gate 9, not byte-for-byte. −1 on *Figures*.
3. **`(Maxwell--flux)` stays English**, because translating it trips a
   different gate on the adjacent pure-mathematics line. −1 on *MT-artifact
   freedom*.
4. **Twenty-two one-word cognates survive gate 9.** Each was read and kept
   (*cond*, *mol*, *kin*, *volume*, *water*, *ppm*, *(even)*), but a stricter
   editor would invent Dutch-only subscripts for two or three of them.
5. **Register in the densest solutions.** Chapters 23 and 31 solutions are
   telegraphic by design; a few three-member coordinations keep the English
   rhythm (sample 5). −1 on *Register* and *Solutions*.
6. **The book is 14 pp longer than English** (359 vs 345). Dutch compounds and
   the longer connectives cost roughly 4 %, in line with fr (345), ar (357) and
   hi (358); nothing overflows, but the figure/​text balance is looser than the
   canon's in a handful of chapters.

## Findings reported to the coordinator during the run

* The seven translation agents share one scratchpad directory: another agent
  overwrote a private helper mid-run. Fixed by moving every private tool into
  a per-language subdirectory.
* `\addlegendentry{}` was invisible to every prose gate exactly as `\legend{}`
  had been, and — before the fix — forced a `!draw` opt-out to translate.
* The English canon carries the TeX accent escape `von K\'arm\'an` in
  `04-viscous-flows.tex` and on its credits page; `id_apply` copies it
  byte-identically into any edition that does not name that line in a range.
