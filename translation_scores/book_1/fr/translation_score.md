# Translation score — Physics Book 1 · French (`fr`)

| Field | Value |
|-------|--------|
| **Book** | One Physics Book 1 (Primary & Middle School, grades 1–9) |
| **Language** | French (`fr`) |
| **Quality bar** | **native academic** (English is the source of truth; this *is* the FR edition, so no French twin exists as a sense reference. The shipped `fr` edition of Book 2 — grades 10–12 — was used as the terminology and register exemplar, so a term defined here is the word Book 2 already uses) |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-08-14 |
| **Scope of this pass** | Full first translation, written in one pass at native register (no machine draft). 71 chapters + 71 solution twins + the image-credits front matter + a curated `tools/term_config/book1_fr.py`, then the defined-term link layer, then this score. **144 files written.** |

## Verdict in one line

A French Book 1 that reads as though it had been written in French for
French nine-year-olds and then for French fifteen-year-olds: the register
climbs with the grade, the physics vocabulary is the one a *collège* pupil
will meet again in the *lycée* volume, and the structural, build and
link-hygiene gates are all green.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Exact mirror: 71 chapters, 71 solution files, **797 exercises EN / 797 FR**, **35 `problem` environments / 35** `\begin{solution}{pb:…}`, **832 solutions / 832**. `\label` sets and order diff to zero in all nine years; all nine `check_translation.sh` gates **PASSED** |
| Terminology | **96** | *Collège*-level French physics, chosen for continuity with the shipped FR Book 2: *tension*, *intensité*, *ampèremètre*, *voltmètre*, *résistor* / *résistance*, *loi d'Ohm*, *lentille convergente*, *distance focale*, *image réelle*, *année-lumière*, *énergie cinétique*, *rendement*, *kilowattheure*, *alternateur*, *ordre de grandeur*. SI unit names translated, symbols and all `siunitx` markup byte-identical to English |
| Register / tone | **96** | Grades 1–5 address the child directly («~Le trottoir est froid sous tes chaussettes~»), imperatives in *tu*; grades 6–7 keep *tu* in the exercises and move the course text to the impersonal *on*; grades 8–9 use the infinitive-imperative method style of the *lycée* volume. Written, not converted |
| LaTeX hygiene | **99** | **0 errors, 0 undefined references, 0 overfull boxes** (measured with `grep -a`). 0 TeX accent escapes, 0 zero-width characters, 0 `\end{…>` typos, 0 drafty `...`. French typography applied throughout: `~:` `~;` `~?` `~!`, `«~…~»` (447 / 447 balanced), `\dots`, raw UTF-8 accents and `œ` |
| Cross-refs / rule compliance | **99** | `\label`, `\cref`/`\ref` targets, `\begin{solution}{key}` and `[resume]` options byte-identical to English (74 `[resume]` lists, EN 74). Zero curriculum, programme or country names in visible text |
| Figures | **97** | All TikZ / pgfplots / circuitikz drawing code byte-identical — coordinates, `\foreach` lists, `xtick`/`ytick`, `samples`, colours untouched; only node text and `{\small …}` captions localized. Three node strings deliberately shortened relative to English so the longer French keeps the picture inside the text block |
| Solutions | **96** | All 797 exercise solutions and all 35 weekend-problem solutions present and native; headers `\section*{Chapitre \ref{ch:…} --- <titre>}` with the `ch:…` slug unchanged. The rhyming inspector's couplet of g9-03 was re-rhymed in French rather than glossed |
| Defined-term links (`\omterm`) | **95** | `--check` **green**. 6 746 links across 140 files (EN 6 483 on the same text, +4.1 %). Per-year target-set divergence 0/1/2/2/6/6/7/12/10 labels, every one traced (table below). Zero links inside `\qty` / `\unit` / `\num` / math / `\label` / solution keys / TikZ bodies / titles (audited mechanically) |
| MT-artifact freedom | **97** | Residual-English sweep over the 142 files (after stripping comments, math, macro arguments and image paths) returns **zero** English prose tokens — the only hits are TikZ `controls … and …` and `images/book1/…` paths. Calque sweep (*délivrer*, *réaliser*, *éventuellement*, *actuellement*, *supporter*, *adresser*, *faire sens*, *basé sur*) returns nothing wrong: the five *délivrer* are the standard French physics usage («~une centrale délivre \qty{1e8}{W}~») |

**Overall: 96** (weighted toward terminology + register + MT-freedom).

## Structural / build gates

Measurement note: pdfTeX writes `build/*.log` as ISO-8859 text, so a plain
`grep -c 'Overfull'` treats the file as binary, prints nothing and exits 1 —
which reads as "0" and is not a count. Every figure below was taken with
`grep -a`.

| Gate | Result |
|------|--------|
| `bash tools/check_translation.sh grade-1 fr` … `grade-9 fr` | **PASSED × 9** |
| `latexmk one_physics_book_1_primary_middle_school_fr.tex` | exit 0 |
| `grep -ac '^!'` | **0** |
| `grep -aci 'undefined'` | **0** |
| `grep -ac 'Overfull'` | **0** |
| `grep -ac 'Underfull'` | 137 (EN 121) — the series norm, not a defect |
| PDF | `build/one_physics_book_1_primary_middle_school_fr.pdf`, **454 pp** (EN 435 — French runs ~4 % longer) |
| `python3 tools/link_defined_terms.py --book 1 --lang fr --check` | **green** — every file matches the config |
| Link containment audit | 0 links inside `\qty{}{}` / `\unit{}` / `\num{}` / inline or display math / `\label` / `\begin{solution}{…}` / TikZ–pgfplots–circuitikz bodies / chapter and section titles |

## Defined-term links — what the curation actually needed

The uncurated run produced **9 148** links, **41 % more than English carries on
the same text** — the signature of over-linking. The causes are French, not
English, and are recorded in `tools/term_config/book1_fr.py`:

### `EXTRA_PROTECT` — the one that mattered

**`[Ss]on`.** French spells the noun *son* (sound, grade 3) exactly like the
possessive determiner, which a physics book writes on nearly every page
(«~son unité~», «~son écho~», «~calculer son énergie~»). Uncurated: **559**
links to `def:g3:sound-around-us:sound` where English has 99. Rewording is
impossible — you cannot remove the French possessive from French — so the
book-2 pattern was reused: a chain of fixed-width negative lookbehinds
(`le/du/un/ce/au/des/les/aux`, both cases) before `\b[Ss]on\b`; the plural
*sons* is always the noun and is left alone. **559 → 80**, and every one of
the 80 sampled reads as the noun.

Twelve smaller protected spans: *puissances de dix*, *résistance de l'air*,
*intensité sonore*, *plein volume* / *volume de lycée* / *ce volume*,
*charbon ou gaz*, *sa branche* (the apple's), *valeur moderne pile* (the
adverb), *taux de fusion de l'œil*, *moteur de voiture* / *moteurs froids*,
and six patterns for *image* meaning a **film frame** (*images par seconde*,
*image par image*, *images de la caméra*, *par image*, `(?<=\$)\s+images`, …)
rather than the picture a mirror or lens makes.

> Note for the next language: `tools/termlink/protect.py` warns that a pattern
> must **never consume a `$`**. A first draft of the frame-image rule wrote
> `\$\s*\d+\s*\$\s+images`, which eats both delimiters and silently mis-pairs
> every later inline-math span. Replaced with the lookbehind above.

### `STOP` (still links inside the chapter that defines it)

| Term | Uncurated links | Why |
|---|---:|---|
| `lampe` | 648 | one French word for the English pair **bulb / lamp**: the component in its own chapter, the ordinary household lamp in six hundred other places. English links *bulb* 228 times and leaves *lamp* alone (406 times); French cannot make that split |
| `milieu` | 65 | the substance a sound crosses (g7) **and** the middle of anything — the last chapter stands the reader «~au milieu~» of the ladder of scales on nearly every line |
| `équilibre`, `en équilibre` | 62 | the see-saw's balance (g2) and «~équilibrer les comptes~», «~les forces se compensent~», «~en équilibre sur un pied~» |
| `croissant`, `croissante`, `décroissante` | 59 | the waxing and waning Moon (g2, g7) and «~des écarts croissants~», «~des vitesses décroissantes~» in the motion chapters |
| `phase`; `pôle`, `pôles`; `symbole`; `observation`, `observer` | — | word-for-word translations of the English stoplist, which stops the same five for the same reasons |

### `DROP` (ordinary word harvested from a definition that merely uses it)

`chaud` / `froid` (191), `sens` / `vue` / `toucher` (261 — *ouïe*, *odorat*,
*goût* keep their links), `seconde` (237), `année` (158), `jour` / `nuit`
(337 — *lever du Soleil* and *coucher du Soleil* keep theirs), `instant`
(84), `fond` (96 — the bottom of a glass, not the third person of *fondre*,
which keeps its link), `ouvert` / `fermé` / `rectiligne` / `circulaire` /
`uniforme` / `varié` (the full phrases *circuit ouvert*, *trajectoire
rectiligne*, *mouvement uniforme* … all survive), and the sentence-initial
imperative `Mesurer`.

**Final: 6 746 links, +4.1 % against English.**

### Two genuine wrong-sense links found by reading the applied output

1. `parts/grade-8/fr/01-electric-current-effects.tex` — «~prise plus
   **solide**~» had linked to `def:g3:solids-liquids-gases:solid` (the state
   of matter). English protects *solid handshake* for exactly this. Reworded
   to «~prise plus **ferme**~».
2. `parts/grade-9/solutions/fr/07-alternator.tex` — «~la **machine simple** à
   deux pôles~» had linked to `def:g5:simple-machines:machine` (lever, pulley,
   ramp). Reworded to «~la machine à deux pôles, la plus simple~».

### Per-year target parity with English

Divergence, EN course + solutions vs FR: **0 / 1 / 2 / 2 / 6 / 6 / 7 / 12 /
10** labels. Every one checked:

| Divergence | Verdict |
|---|---|
| EN-only `def:g3:first-electric-circuit:bulb` (all years) | the *lampe* stop above — deliberate |
| EN-only `def:g7:sound-production:medium`, `def:g2:balance-equilibrium:equilibrium`, `def:g1:five-senses:senses`, `def:g6:water-states:changes` | the *milieu* / *équilibre* / senses stops and the *taux de fusion de l'œil* protection — deliberate |
| EN-only `def:g7:short-circuits-safety:battery` | English harvests the possessive *battery's* as a term of its own; French writes «~de la pile~» and lands on `def:g3:first-electric-circuit:battery`, the same definition |
| EN-only `def:g4:weight-and-mass:springscale` in g9 | French *dynamomètre* resolves under `nearest-preceding` to the g9 definition that names it — **more** correct than English's |
| FR-only `def:g3:levers-and-scales:scale` (89 links) | French says *balance* where English alternates *scale* / *balance* and links only the former. Same instrument, same definition |
| FR-only `def:g6:describing-motion:trajectory`, `def:g2:measuring-time:duration`, `def:g8:ohms-law:resistance`, `def:g4:conductors-insulators:conductor` / `insulator`, `def:g7:light-sources-propagation:diffusion` | French uses one word (*trajectoire*, *durée*, *résistance*, *isolant*, *diffusion*) where English alternates (*path*/*trajectory*, *time*/*duration*, *coil*/*resistance*, *insulation*/*insulator*, *scattering*/*diffusion*). All correct sense, checked line by line |
| FR-only `prop:g5:mirrors-reflection:image` in g9 | the metaphorical «~image de la chute d'eau~» — English links its own *image* in the same sentences |

## Samples (native / near-native / MT)

| Sample | Verdict |
|--------|---------|
| `grade-1/fr/01-five-senses.tex`, opening | **native** — «~Un oiseau chante quelque part au-dessus de toi. Le pain sent bon, tout chaud. Le trottoir est froid sous tes chaussettes.~» Three short sentences, a child's world, no trace of the English period |
| `grade-5/fr/07-speed-distance-time.tex`, opening | **native** — «~«~Je suis plus rapide~!~» --- «~Non, c'est moi~!~» Toutes les cours de récréation tranchent cela honnêtement~: on s'aligne, à vos marques, prêts, partez.~» The starter's call is the French one, not a gloss of "ready, steady, go" |
| `grade-8/fr/03-voltage-voltmeter.tex`, `def:…:voltage` | **native** — «~Une tension est toujours un \emph{entre}~: entre les deux bornes d'une pile, entre les deux côtés d'une lampe --- jamais en un seul point.~» The *pile plate* / *pile ronde* / *pile 9 volts* family of the example is the French drawer, not a translated one |
| `grade-9/fr/03-uniform-varied-motion.tex`, `prop:…:inertia` | **native** — «~au repos, il reste au repos~; en mouvement, il poursuit en ligne droite à vitesse constante… ne se produit que tant qu'agit une force \emph{non compensée}.~» *forces compensées / non compensées* is the French mechanics idiom, not a calque of *balanced* |
| `grade-9/solutions/fr/03-uniform-varied-motion.tex`, `pb:…:1` item 12 | **native** — the inspector's rhyme is re-rhymed, not glossed: «~Écarts égaux, allure tranquille --- nulle force en trop ne trouble la file. Écarts qui changent, il faut une cause~: une poussée non compensée, dit la clause.~» |
| `grade-8/fr/06-colors-spectra.tex`, `prop:…:objectcolor` | **near-native** — «~La couleur n'est pas \emph{dans} la peau~: elle est la réponse de la peau à la lumière qu'on lui a offerte.~» Correct and idiomatic; the *offrir / renvoyer* bookkeeping metaphor is carried from English rather than replaced by a French one, which a French author might have done differently |

## Why not 100 — ordered gap list

1. **`lampe` is chapter-local.** French has one word for *bulb* and *lamp*, so
   a French reader gets no hyperlink on «~la lampe s'allume~» where an English
   reader gets one on "bulb" 228 times. Linking all 648 would paint the book
   blue, and a wrong-sense link is worse than a missing one. No configuration
   of the current engine does better: the engine resolves ambiguity only by
   chapter order.
2. **Two terms change name between Book 1 and Book 2.** Grade 9 says
   *intensité de la pesanteur* for $g$ (the *collège* name) where the FR
   *lycée* volume says *champ de gravitation*; grade 5 defines the parallel
   circuit as *circuit en dérivation* (with «~on dit aussi en parallèle~») where
   Book 2 mostly says *en parallèle*. Both are deliberate level-appropriate
   choices and both are signposted in the text, but a reader crossing from
   Book 1 to Book 2 meets a second name.
3. **Decimal point kept in all math** (`$0.63$`, `\qty{9.8}{N/kg}`) while
   French prose writes the comma. Series policy, so the shared `parts/`
   physics is identical in every language; a French pupil reads a mildly
   foreign notation throughout.
4. **Three TikZ node strings were shortened**, not merely translated, to keep
   the wider French inside the text block (g9 gravitation's mountain gun and
   orbit labels, g8 lenses' real-image label). The information they dropped is
   carried by the caption immediately below, but the figure and its English
   twin no longer say exactly the same words.
5. **137 underfull boxes** against English's 121 — French's longer words in a
   72-column measure. The series norm in every language, and not worth
   hyphenation exceptions at this size.
6. **Four labels link more often in French than in English** (*balance*,
   *durée*, *trajectoire*, *résistance*) because French uses one word where
   English alternates two. Correct sense every time, but the reading
   experience is a little more hyperlinked than the English original's.
7. Nothing else found. No missing content, no encoding defects, no curriculum
   or country names, no residual English, no link inside protected markup.

### Not a gap: siunitx and cleveref conjunctions

An earlier draft of this list claimed that `\qtyrange` still printed
«~27.5 to 4186 Hz~» and `\cref{a,b}` «~Chapitres 25 and 29~». **That was
wrong** — asserted from the FR Book 2 score file's gap list without opening
the style file. `styles/lang/fr.tex` already carries the fix (lines 78–91):
`\sisetup{range-phrase={ à }, list-pair-separator={ et },
list-final-separator={ et }}` plus, inside `\AtBeginDocument`,
`\crefpairconjunction`, `\creflastconjunction`, `\crefrangeconjunction` and
both group conjunctions. The built PDF confirms it: no `N to N` range and no
`Chapitres N and N` anywhere in the 454 pages. Nothing to do, in this edition
or any other.
