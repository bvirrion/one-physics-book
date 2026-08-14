# Translation score — Physics Book 1 · Dutch (`nl`)

| Field | Value |
|-------|--------|
| **Book** | One Physics Book 1 (Primary & Middle School, grades 1–9) |
| **Language** | Dutch (`nl`) |
| **Quality bar** | **native academic** (English is the source of truth; this *is* the NL edition, so no Dutch twin exists as a sense reference, and no French twin was consulted — the English source was translated directly. The shipped **Dutch Book 2** (grades 10–12, `parts/grade-1{0,1,2}/nl/`) and the Dutch math Book 1 were the terminology and register exemplars, so a term defined here is the word Book 2 already uses — *baan*, *eenparige beweging*, *spanning*, *stroomsterkte*, *weerstand*, *vermogen*) |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-08-14 |
| **Scope of this pass** | Full first translation, written in one pass at native register (no machine draft). 71 chapters + 71 solution twins + the image-credits front matter + a curated `tools/term_config/book1_nl.py`, then the defined-term link layer, then this score. **142 body files written** (+ image credits + term config). |

## Verdict in one line

A Dutch Book 1 that reads as though it had been written in Dutch — for
seven-year-olds in *jaar 1* and for fifteen-year-olds in *jaar 9* — with the
register climbing grade by grade, the physics vocabulary continuous with the
shipped Dutch Book 2, and every structural, build and link-hygiene gate green.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Exact mirror: 71 chapters, 71 solution files, **797 exercises EN / 797 NL**, **35 `problem` environments / 35**, **832 solutions / 832**. `\label` sets and order diff to zero in all nine years; all nine `check_translation.sh` gates **PASSED** |
| Terminology | **96** | Dutch school physics chosen for continuity with Book 2: *spanning*, *stroomsterkte*, *ampèremeter*, *voltmeter*, *weerstand*, *wet van Ohm*, *convergerende lens*, *brandpuntsafstand*, *reëel beeld*, *lichtjaar*, *kinetische energie*, *rendement*, *kilowattuur*, *wisselstroomgenerator*, *orde van grootte*, *schijngestalte*, *kernschaduw*/*halfschaduw*. SI unit names translated, symbols and every `siunitx` argument byte-identical to English |
| Register / tone | **96** | Grades 1–5 speak to the child directly ("Ergens boven je zingt een vogel"), imperatives in *je*; grades 6–7 keep *je* in the exercises and let the course text go impersonal; grades 8–9 use the sober textbook voice of the Dutch Book 2. Written, not converted |
| LaTeX hygiene | **99** | **0 errors, 0 undefined references, 0 overfull boxes** (`grep -a` on the log). 0 TeX accent escapes, 0 zero-width characters, 0 `\end{…>` typos, 0 drafty `...`; raw UTF-8 throughout (*ë*, *ï*, *é*, *ü*, *ampère*, *vacuüm*) |
| Cross-refs / rule compliance | **99** | `\label`, `\cref`/`\ref` targets, `\begin{solution}{key}` and `[resume]` options byte-identical to English (74 `[resume]` lists, EN 74). No curriculum, programme or country names in visible text; the part titles come from `styles/lang/nl.tex` |
| Figures | **97** | All TikZ / pgfplots / circuitikz drawing code byte-identical — coordinates, `\foreach` lists, `xtick`/`ytick`, `samples`, colours untouched; only node text and `{\small …}` captions localized. Two strings deliberately shortened/reworded so the longer Dutch keeps the picture and the paragraph inside the text block |
| Solutions | **96** | All 797 exercise solutions and all 35 weekend-problem solutions present and native; headers `\section*{Hoofdstuk \ref{ch:…} --- <titel>}` with the `ch:…` slug unchanged. The inspector's rhyming couplet of g9-03 was re-rhymed in Dutch, not glossed |
| Defined-term links (`\omterm`) | **94** | `--check` **green**. 6 009 links across 140 files (EN 6 483 on the same text, −7.3 %). Per-year target-set divergence 0/3/3/5/7/6/7/8/14 labels, every one traced (table below). Zero links inside `\qty` / `\unit` / `\num` / math / `\label` / solution keys / TikZ bodies / titles (audited mechanically: 0 hits) |
| MT-artifact freedom | **97** | Residual-English sweep over the 142 files (comments, math, macro arguments and image paths stripped) returns **zero** English prose tokens — the only hits are TikZ syntax (`ellipse (0.55 and 0.3)`, `controls … and …`) and the Dutch word *water*. Calque sweep (*realiseren*, *eventueel*, *actueel*, *gebaseerd op*, *maakt zin*, *adresseren*, *significant*, *controleren*) returns one word only — the 10 *controleren* all mean *to check*, the correct Dutch sense, never the English *to control* |

**Overall: 96** (weighted toward terminology + register + MT-freedom).

## Structural / build gates

| Gate | Result |
|------|--------|
| `bash tools/check_translation.sh grade-1 nl` … `grade-9 nl` | **PASSED × 9** |
| `latexmk one_physics_book_1_primary_middle_school_nl.tex` | exit 0 |
| `grep -ac '^!'` | **0** |
| `grep -aci 'undefined'` | **0** |
| `grep -ac 'Overfull'` | **0** |
| `grep -ac 'Underfull'` | 144 (EN 121) — the series norm, not a defect |
| PDF | `build/one_physics_book_1_primary_middle_school_nl.pdf`, **449 pp** (EN 435 — Dutch runs ~3 % longer) |
| `python3 tools/link_defined_terms.py --book 1 --lang nl --check` | **green** — every file matches the config |
| Label-set diff EN ↔ NL, per chapter and per solutions file | **0 lines** |
| Exercise / problem / solution census | 797 / 35 / 832, identical to English |

Three overfull boxes appeared in the first build and were all fixed by
rewording, not by hyphenation hacks: the image-credits line *Trommel en
trommelstokken*, the unbreakable compound *speelgoed-en-zaklampspelletjes*
in g6-06, and a TikZ node label in g8-01 that the longer Dutch pushed past
the text block.

## Defined-term links — what the curation actually needed

The uncurated run produced **6 915** links; curation brought it to **6 009**,
7.3 % below English. The causes are Dutch, not English, and are recorded in
`tools/term_config/book1_nl.py`.

### `DROP` (ordinary Dutch harvested from a definition that merely uses it)

| Dropped | Uncurated noise | Why |
|---|---|---|
| `warm`, `koud` | grade-1 vocabulary | ordinary adjectives on nearly every page |
| `zien`, `horen`, `voelen`, `ruiken`, `proeven` | the five senses as verbs | "je ziet", "we horen", "voel de warmte"; the noun *zintuig* keeps its link |
| `open` | 54 links | the verb and the adjective ("open de lus", "de open ruimte", "een open vraag"); *gesloten stroomkring* survives as a phrase |
| `gesloten` | — | same, mirrored |
| `nacht` | 74 links | ordinary time-of-day word; *zonsopgang* / *zonsondergang* keep theirs |
| `dag`, `jaar` | — | "op een dag", "dit jaar", "negen jaar" |
| `eenparig`, `veranderlijk`, `rechtlijnig`, `cirkelvormig` | — | bare adjectives; the phrases *eenparige beweging*, *veranderlijke beweging*, *rechtlijnige baan*, *cirkelvormige baan* all survive |

### `STOP` (still links inside the chapter that defines it)

`waarnemen` / `waarneming` (ordinary "we nemen waar dat"), `pool` / `polen`
(the battery's terminals, the Earth's geographic poles, the flagpole),
`symbool` — the same five the English config stops, for the same reasons.

### `EXTRA` — one term the harvester had to be given back

`weerstand` is defined **twice inside one chapter** (the quantity and the
component, g8-05), so the harvester dropped it as ambiguous and the most
useful term of the electricity years would have carried no link at all. Both
senses are the same physics here, so `EXTRA` points *weerstand* at the
quantity's definition and *weerstanden* at the component's.

### `EXTRA_PROTECT` — the spans where a good term means something else

* `drij(ft|ven) … aan` — the separable verb *aandrijven* ("de batterij drijft
  de mars aan", "stoomstralen drijven de turbine aan"), not the floating of
  grade 1. The pattern catches the particle up to six words away.
* `zijn tak los` — the apple's branch in g9-01, not the branch of a circuit.
* `licht overbelast|gekromde|hellend|…` — the adjective *licht* (slight), not
  the phenomenon.
* `kolen of gas` — the fuel, not the state of matter.
* `vol volume` — headphone loudness, not the space a body occupies.
* `as van het instrument` — the dynamometer's axis of use, not the Earth's.
* `schakel … aan|uit` — the everyday verb, not the component.

### Wrong-sense links found by reading the applied output — and how they were fixed

Dutch has several one-word-two-senses traps that no configuration can see;
each was found by reading the generated links and fixed **in the prose**,
which is also the better Dutch:

1. **`meter`** — Dutch spells the SI unit and *any measuring instrument* the
   same way. Every instrument use in the electricity years was renamed to the
   instrument itself: *voltmeter*, *ampèremeter*, *meetinstrument*,
   *decibelmeter*, *elektriciteitsmeter* (≈ 20 sites, g5, g8, g9).
2. **`as`** — the motor's shaft (g8-01) and the gearbox shaft (g9-08) had
   linked to the Earth's spin axis; reworded to *draaias* and *aandrijfas*.
3. **`beeld`** — video frames and oscilloscope traces had linked to the
   mirror's image; the film chapters now say *beeldje voor beeldje*,
   *beeldjes per seconde*, *het kader*, and the oscilloscope says *spoor*
   (which is what g8-09 already said).
4. **`drijven`** — the drive/drift sense in six places ("warmte drijft de
   rode deuren", "de kalender door de seizoenen heen drijven", "de duw drijft
   de stroom") reworded to *opent*, *laten schuiven*, *jaagt*, *stuurt*,
   *zweven*, *schuiven*.
5. **`eenvoudige machine`** — "the simple two-pole machine" of g9-07 had
   linked to the lever-and-pulley definition; reworded to "de eenvoudigste
   machine, die met twee polen".
6. **`weerstand`** — the dynamo's mechanical drag (g9-07) had linked to the
   electrical quantity; reworded to *tegenstand* / *magnetische tegenwerking*.

### Per-year target parity with English

Divergence, EN course + solutions vs NL: **0 / 3 / 3 / 5 / 7 / 6 / 7 / 8 /
14** labels. The recurring, deliberate causes:

| Divergence | Verdict |
|---|---|
| NL-only `def:g2:measuring-time:second` (all years) | English DROPs *second* because it is also the ordinal; Dutch *seconde* is never the ordinal, so every use is the SI unit and links honestly, exactly as *meter*, *gram*, *kilogram* do |
| EN-only `def:g7:short-circuits-safety:battery` | English harvests the possessive *battery's* as a term of its own; Dutch writes *van de batterij* and lands on `def:g3:first-electric-circuit:battery`, the same definition |
| NL-only `def:g2:ice-water-steam:meltfreeze` / `evapcond` in g4–g7 | Dutch uses one verb (*smelten*, *verdampen*, *condenseren*) where English alternates noun and verb forms across years; `nearest-preceding` resolves each to the year that defined it |
| NL-only `def:g2:pushes-and-pulls:force`, `def:g2:balance-equilibrium:equilibrium` | *kracht* and *evenwicht* are single Dutch words where English alternates *force*/*push*, *balance*/*equilibrium* |
| EN-only `def:g2:air-around-us:wind`, `def:g3:sound-around-us:sound`, `ex:g2:measuring-time:clock` in g6 | Dutch writes the compounds solid (*windturbine*, *geluidssnelheid*, *uurwerk*), and the word boundary correctly refuses to link inside a compound |
| EN-only `def:g3:solids-liquids-gases:solid` / `liquid` in g8–g9 | English's *solid handshake* / *liquid* metaphors have no Dutch counterpart in the same sentences |

## Samples (native / near-native / MT)

| Sample | Verdict |
|--------|---------|
| `grade-1/nl/01-five-senses.tex`, opening | **native** — "Ergens boven je zingt een vogel. Het brood ruikt warm. De stoeptegels voelen koud door je sokken heen." Three short sentences, a child's world, no trace of the English period |
| `grade-2/nl/06-pushes-and-pulls.tex`, opening | **native** — "Een deur openen, een rits dichttrekken, tegen een bal schoppen, een slee voorttrekken: je hele dag bestaat uit duwen en trekken." The verbs are the Dutch ones a child uses, not glosses |
| `grade-8/nl/05-ohms-law.tex`, `rem:…:triangle` | **native** — "Leun dit jaar op de kruk als het moet; maar plan om te lopen." Idiomatic, and it keeps the English joke without translating it word for word |
| `grade-9/nl/03-uniform-varied-motion.tex`, `prop:…:inertia` | **native** — "in rust blijft het in rust, en in beweging vervolgt het zijn weg in een rechte lijn met constante snelheid… treedt alleen op zolang er een *niet-opgeheven* kracht werkt." *opgeheven / niet-opgeheven krachten* is the Dutch mechanics idiom, not a calque of *balanced* |
| `grade-9/solutions/nl/03-uniform-varied-motion.tex`, `pb:…:1` item 12 | **native** — the inspector's rhyme is re-rhymed, not glossed: "Gelijke gaten: het tempo heeft vrede --- geen netto kracht die het stoorde in zijn schrede. Veranderende gaten eisen een oorzaak: een niet-opgeheven duw, en dat is de hele zaak." |
| `grade-8/nl/06-colors-spectra.tex`, `prop:…:objectcolor` | **near-native** — "De kleur zit niet *in* de schil: ze is het antwoord van de schil op het licht dat haar werd aangeboden." Correct and idiomatic; the *aanbieden / teruggeven* bookkeeping metaphor is carried over from English rather than replaced by a Dutch one, which a Dutch author might have handled differently |

## Why not 100 — ordered gap list

1. **The link layer is 7.3 % thinner than English.** Two structural reasons,
   both Dutch: solid compounds (*daglicht*, *zwaartekracht*, *geluidssnelheid*)
   correctly refuse to link their heads, and six everyday words had to be
   dropped (*open*, *nacht*, *dag*, *jaar*, *warm*, *koud*) that English can
   afford to link. A Dutch reader therefore meets somewhat fewer hyperlinks
   than an English one; every remaining link was checked to point at the right
   sense, and a missing link is far cheaper than a wrong one.
2. **`weerstand` is one word for two definitions.** English separates
   *resistance* (the quantity) and *resistor* (the component); Dutch says
   *weerstand* for both. The `EXTRA` mapping sends the singular to the
   quantity and the plural to the component, which is right in almost every
   sentence but is a convention, not a distinction the language makes.
3. **Two terms are named at level, not at Book-2 level.** Grade 9 says
   *zwaartekrachtsterkte* for $g$ (the school-level name) where the Dutch
   Book 2 says *gravitatieveldsterkte* (5 uses, checked), and grade 9 coins
   *plaats-tijdregistratie* for the dot-timer tape, a compound Book 2 never
   needs. Both are deliberate and level-appropriate, but a reader crossing
   into Book 2 meets a second name for $g$.
4. **Decimal point kept in all math** (`$0.63$`, `\qty{9.8}{N/kg}`) while Dutch
   prose writes the comma. Series policy, so the shared `parts/` physics is
   identical in every language; a Dutch pupil reads a mildly foreign notation
   throughout.
5. **Two figure strings were reworded, not merely translated** (the
   paperclip label of the g8-01 electromagnet, shortened to keep the picture
   inside the text block; the axis label *draaias* in the same chapter). The
   information is unchanged, but the Dutch node no longer says exactly the
   English words.
6. **144 underfull boxes** against English's 121 — Dutch's longer compounds in
   a 72-column measure. The series norm in every language, and not worth
   hyphenation exceptions at this size.
7. Nothing else found: no missing content, no encoding defects, no curriculum
   or country names, no residual English, no link inside protected markup, no
   exercise without a solution.
