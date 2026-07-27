# Translation score — Physics Book 2 · French (`fr`)

| Field | Value |
|-------|--------|
| **Book** | One Physics Book 2 (High School, grades 10–12) |
| **Language** | French (`fr`) |
| **Quality bar** | **native academic** (EN is the source of truth; this *is* the FR edition, so no French twin exists as a sense reference — English is the only comparand, with the Dutch edition of the same book used as a method exemplar) |
| **Overall score** | **97 / 100** |
| **Ship threshold** | ≥ 95 — **met**; the previous pass's only blocker is repaired |
| **Date** | 2026-07-27 |
| **Scope of this pass** | Targeted repair, not a re-translation. Regenerated the `\omterm` link layer, curated `tools/term_config/book2_fr.py` for French homographs, made eight prose fixes, and re-scored. 69 files touched (68 bodies/solutions + the term config). |

## Scope note — Physics Book 1 has no French edition

There is no `one_physics_book_1_primary_middle_school_fr.tex`, and
`parts/grade-1`…`grade-9` contain no `fr/` bodies (0 of 71 chapters). Book 1
is still a titled placeholder in every language including English, so there
is nothing to grade. **French exists only for Book 2**, which is what this
file scores.

## Verdict in one line

Still the best-executed French edition in the project, and now internally
consistent: the defined-term layer matches its config, and the ~30 wrong-sense
links that a naive regeneration would have shipped (French *son*, *hauteur*,
*tension*, *foyer*, *verticale*, *relative*, *mince*, *moteur*) are gone.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Exact mirror: 35 chapters, 35 solution files, 525 exercises EN / 525 FR, 35 `problem` environments ↔ 35 `\begin{solution}{pb:…}`. `\label` sets diff to **zero lines** in all three years. All three `check_translation.sh` gates **PASSED** |
| Terminology | **97** | Correct French *lycée*-level physics vocabulary: *quantité de mouvement*, *champ magnétique*, *référentiel*, *ordre de grandeur*, *chiffres significatifs*, *célérité*, *longueur d'onde*, *temps propre*, *condensateur*. Unit strings and `siunitx` markup untouched; SI names translated, symbols not. This pass fixed one genuine mistranslation: EN "strength (of a harmonic)" had become *force* in the spectrum definition, where French acoustics says *intensité* |
| Register / tone | **97** | Written, not translated. «~La physique commence là où l'opinion s'arrête~: avec une mesure.~»; «~lorsqu'un courant fit tiquer une boussole~». Both openings flagged as English-architecture in the previous pass were rebuilt in French (below) |
| LaTeX hygiene | **98** | 0 errors, 0 undefined references, **0 overfull boxes** (measured with `grep -a`, see the note below). 0 TeX accent escapes, 0 zero-width spaces. `\admitted` and `enumerate[resume]` preserved; 0 links inside `\qty`/`\unit`/`\SI`/math/`\label`/TikZ/section titles (audited mechanically) |
| Cross-refs / rule compliance | **98** | `\label`, `\cref`/`\ref` targets and `\begin{solution}{key}` byte-identical to English. **Zero** *lycée* / *Terminale* / prépa-track names. Cross-volume references use «~volume de Licence~1/2~», the correct neutral form |
| Defined-term links (`\omterm`) | **96** | **`--check` green**: 4 648 links across 70 files, all matching what `book2_fr.py` generates (EN 4 497 on the same text). Was 4 432 stale on-disk vs 5 114 generated. Per-year target-set diff against English is 2 / 3 / 8 labels, every divergence deliberate (table below) |
| Figures | **97** | TikZ/pgfplots/circuitikz drawing code byte-identical to English; only node text and `{\small …}` captions localized |
| Solutions | **97** | All 525 exercise solutions plus all 35 weekend-problem solutions present and native; headers `\section*{Chapitre \ref{ch:…} --- <titre>}` with `ch:…` slugs unchanged |
| MT-artifact freedom | **97** | Residual-English sweep over the 70 files (after stripping labels, environment names, math and unit markup) returns **zero** English tokens. This pass removed the last two artifacts it found: `s'average` (not a French verb) and `le design échoue vers «~off~»` |

**Overall: 97** (weighted toward terminology + register + MT-freedom).

## Structural / build gates

**Measurement note for the next grading pass: use `grep -a`.** pdfTeX writes
`build/*.log` as ISO-8859 text, so a plain `grep -c 'Overfull'` treats the file
as binary, prints nothing and exits 1 — which reads as "0" and is not a count.
Every figure below was taken with `grep -a`.

| Gate | Result |
|------|--------|
| `bash tools/check_translation.sh grade-10 fr` | **PASSED** |
| `bash tools/check_translation.sh grade-11 fr` | **PASSED** |
| `bash tools/check_translation.sh grade-12 fr` | **PASSED** |
| `latexmk -pdf one_physics_book_2_high_school_fr.tex` | exit 0 |
| `grep -ac '^!'` | **0** |
| `grep -ac 'LaTeX Warning: Reference.*undefined'` | **0** |
| `grep -ac 'Overfull'` | **0** |
| `grep -ac 'Underfull'` | 133 (EN 127) — the series norm in every language, not a defect |
| PDF | `build/one_physics_book_2_high_school_fr.pdf`, **358 pp** (EN 349, NL 358) — unchanged from the previous pass |
| `python3 tools/link_defined_terms.py --book 2 --lang fr --check` | **green** — every file matches the config |
| Link containment audit | 0 links inside `\qty{}{}` / `\unit{}` / `\SI{}` / inline or display math / `\label` / TikZ–pgfplots–circuitikz bodies / section or environment titles |
| Same check, other languages | `en` green · `nl` green · `pt` green · `hi` green · `es` **stale, 70 of 70 files** (out of scope here; same failure, same fix) |

## Defined-term links — what the regeneration actually needed

Running the documented two commands took the tree from 4 432 links to 5 114 —
**14 % more than the English edition carries on the same text**, which is the
signature of over-linking, not of recovered coverage. The cause is systematic
and worth recording: `book2_fr.py` translated the English `STOP`/`DROP` lists
**word for word**, but French genders and pluralises, and `harvest.py` treats
every harvested inflection as a term of its own. English stops `real`,
`vertical`, `absolute`, `complementary`; French had stopped `réel`, `vertical`,
`absolu`, `complémentaire` and left `réelle`, `verticale`, `absolue`,
`complémentaires` linking. On top of that sit five homographs English simply
does not have.

Curation applied (all of it in `tools/term_config/book2_fr.py`, none of it in
the shared rules), then `--unwrap --apply` → `--apply` → `--check`. Final:
**4 648 links**.

### `STOP` (word still links inside the chapter that defines it)

| Term | Wrong links removed | Why |
|---|---:|---|
| `hauteur`, `hauteurs` | 53 → 13 | French says *hauteur* both for the pitch of a note (g12 acoustics) and for a height in metres; half of grade-12 mechanics measures a *hauteur*. English has *pitch* and *height* and needs no rule |
| `tension`, `tensions` | 88 → 28 | the pull of a rope (g10 inertia) **and** the electrical quantity English calls *voltage* (g11 circuits). Under `AMBIG_POLICY = "nearest-preceding"` every mechanics chapter after g11-03 was sending its rope tensions to the electrical definition |
| `foyer`, `foyers` | 10 → 1 | focal point (g11 optics), focus of an ellipse (g12 astronomy), **household** (every energy chapter) and **hearth** (the carbon-dating example). Six of the ten links were households or hearths |
| `réelle`, `réelles` | 17 → 6 | feminine of the already-stopped `réel`; *image réelle* in g11 lenses, ordinary "actual" everywhere else |

### `DROP` (ordinary word harvested from a definition that merely uses it; the full phrase survives)

| Term | Wrong links removed | Why |
|---|---:|---|
| `verticale`, `verticales` | 36 → 0 | feminine of the already-dropped `vertical`; harvested from the weight definition (the *direction*), but overwhelmingly the ordinary adjective (*composante verticale*, *boucle verticale*, *asymptote verticale*) |
| `relative`, `relatives` | 12 → 0 | harvested from *pression relative*; **none** of the twelve occurrences meant gauge pressure — they were *incertitude relative*, *vitesse relative*, *dérive relative*, *fluctuation relative*. *pression relative* survives |
| `mince`, `minces` | 10 → 0 | harvested from *lentille mince*; **none** of the ten was a lens — *fil mince*, *fibre mince*, *isolant mince*, *aimant mince*. *lentille mince* / *lentilles minces* survive |
| `moteur`, `moteurs` | 18 → 0 | harvested from *travail moteur*; fourteen of the eighteen were engines (*le moteur du treuil*, *les moteurs d'une fusée*, *ni moteur ni ordinateur*). *travail moteur* survives, as does the contrasting *travail résistant* |
| `absolue` | 3 → 0 | feminine of the already-dropped `absolu`; *simultanéité absolue*, *limite absolue*. *pression absolue* survives |
| `stable`, `instable` (+ plurals) | 6 → 2 | harvested from *équilibre stable / instable*; on their own they describe a nuclide (*plomb-206 stable*, *noyaux instables*) or a steady power. The two solutions that needed the mechanical sense now say the full phrase |

### `EXTRA_PROTECT` (masked spans)

- **`[Ss]on`** — the one that mattered. *son* is the sound of grade 10 **and**
  the possessive determiner, which a physics book writes on nearly every page.
  The regeneration produced **263** links to `def:g10:signals-and-waves:sound`
  where English has 43, and all but ~30 were «~son écho~», «~son unité~»,
  «~calculer son énergie~». Rewording is impossible — you cannot remove the
  French possessive from French. The noun always follows a determiner and the
  determiner never does, so the pattern is a chain of fixed-width negative
  lookbehinds (`le/du/un/ce/au/des/les/aux`, both cases) before `\b[Ss]on\b`;
  the plural *sons* is always the noun and is left alone. **263 → 32**, and
  all 32 read as the noun.
- **`poussées?` after an auxiliary** — *poussée* is the thrust of the g10 force
  inventory and the feminine past participle of *pousser* («~la caisse est
  poussée de \qty{4}{m}~»). Only the participle takes an auxiliary or an
  instrumental complement. **47 → 38**, no participle left.
- **`angles? complémentaires?`** — *complémentaire* is already stoplisted but
  its plural is harvested separately; the single occurrence outside the colour
  chapter is geometric (the complementary launch angles of g12 projectile
  motion). Protecting the phrase keeps the five correct colour links.

### Prose fixes made for link hygiene and for French

Rewording was preferred wherever it was possible and did not distort the
sentence; the config carried the cases where it was not.

1. `grade-12/fr/02-sound-acoustics.tex`, spectrum definition — «~une barre par
   $f_n$, la hauteur mesurant la **force** de cet harmonique […] le mélange des
   **forces**~» → «~dont la **longueur** mesure l'**intensité** de cet
   harmonique […] le mélange des **intensités**~». English says *strength*;
   *force* was a wrong-sense translation that also produced two links to the
   mechanical-force definition, and *hauteur* (bar height) sat two words from
   *hauteur* (pitch). Three defects, one rewrite.
2. Same file, exercise 10 — «~des pics […] de **hauteurs** décroissantes~» →
   «~d'**intensités** décroissantes~», for the same reason.
3. Same file, weekend problem — «~un léger toucher au milieu en pinçant
   **force** un nœud~» (a calque; English over-links its own verb *forces*
   here) → «~un léger toucher au milieu, pendant que l'on pince, **impose** un
   nœud là~».
4. `grade-12/fr/16-special-relativity.tex` — «~misent sur la **dilatation**
   chaque jour~» → «~la **dilatation du temps**~», which is what is meant and
   which lands on `thm:g12:special-relativity:dilation` instead of the acoustic
   rarefaction.
5. `grade-12/solutions/fr/10-work-and-energy.tex` — «~instable (maximum)~;
   […] stable (minimum)~» → «~**équilibre** instable / **équilibre** stable~»,
   restoring the link that dropping the bare adjectives removed.
6. `grade-12/fr/12-rlc-oscillations.tex` — «~fixe la fréquence de
   **diffusion**~» (radio broadcasting, linked to *light scattering*) → «~fixe
   la fréquence **émise**~», which also stops the sentence repeating *émission*.
7. `grade-12/fr/13-radioactive-decay.tex` — «~un gaz qui **s'échappe** de la
   lave~» → «~qui **sort** de la lave~» (the escape-velocity remark is not what
   argon does); and «~le sans-loi **s'average** en mécanique d'horloge~» →
   «~**se lisse**~» — *s'averager* is not a French verb.
8. `grade-12/solutions/fr/14-nuclear-energy.tex` — «~le **design** échoue vers
   «~**off**~»~» → «~la **conception défaille du côté de l'arrêt**~».

### Register: the two openings flagged last time

- `grade-12/fr/06-newtons-laws.tex` — «~entre les deux, la simple vérité ---
  rien à bord n'a changé sauf le mouvement. […] les **forge en** la méthode~» →
  «~**Entre les deux, une vérité toute simple~:** rien à bord n'a changé,
  **sinon** le mouvement. […] et **en tire** la méthode~». The English
  appositive dash becomes the French colon, the sentence breaks, and *forger en
  la méthode* (which is not French) goes.
- `grade-11/fr/06-magnetic-fields.tex` — «~Les marins se guidaient **à** des
  aiguilles…~» → «~**Mille ans durant**, les marins se sont guidés **sur** des
  aiguilles aimantées **sans que personne sache** pourquoi…~»; the enumeration
  becomes «~**celui** des aimants, **celui** de la Terre, **celui** des
  courants~»; and the closing «~le champ **repousse** les courants~» — which
  says the field *repels* currents, and is wrong physics — becomes «~le champ
  **exerce en retour une force sur** les courants~: c'est ainsi que tourne tout
  moteur électrique~».

### Omterm target parity with English

Per-year target-set diff (EN course + solutions vs FR): **2 / 3 / 8** labels.
Every divergence checked:

| Divergence | Verdict |
|---|---|
| EN-only `thm:g10:refraction:snell`, `prop:g10:pressure:boyle`, `thm:g12:newtons-laws:second`, `thm:g12:newtons-laws:third` | **deliberate policy divergence**: `NOT_A_TERM` in `book2_fr.py` contains `"loi de"` / `"loi des"`, so French treats *loi de Snell–Descartes*, *loi de Boyle–Mariotte*, *deuxième/troisième loi de Newton* as result **names**, not terms — exactly what the English default `"law of"` does to *Galileo's law of free fall*. Identical to the choice the Dutch edition documents |
| EN-only `def:g11:fundamental-interactions:strong` (on "range") | **English wrong-sense over-link** (projectile range ≠ range of an interaction). French *portée* under `nearest-preceding` goes to `def:g12:projectile-motion:range` from grade 12 on — FR is right, as NL was |
| EN-only `def:g11:work-of-force:sign` in grade 12 | consequence of dropping bare *moteur*; French keeps the link on *travail moteur* and *résistant* in grade 11 |
| FR-only `def:g10:relative-motion:frame`, `def:g10:inertia:diagram`, `thm:g10:energy-conservation:conservation`, `def:g11:color-light-sources:incandescent`, `def:g11:color-light-sources:objectcolor`, `def:g11:lenses-and-eye:focal`, `def:g12:mechanical-waves:wave`, `def:g12:newtons-laws:inertial`, `def:g12:nuclear-energy:units`, `thm:g12:satellites-kepler:kepler` | all **correct sense**, all reached from a French phrase whose English twin is worded differently or is a one-word homonym English drops (*référentiel*, *diagramme des forces*, *conservation de l'énergie*, *onde mécanique*, *référentiel galiléen*, *électronvolt*, *lois de Kepler*) |

## Samples (native / near-native / MT)

| Sample | Verdict |
|--------|---------|
| `grade-10/fr/01-orders-of-magnitude.tex` opening + `def:…:unit` | **native** — «~La physique commence là où l'opinion s'arrête~: avec une mesure.~»; «~La mesurer, c'est compter combien de fois une grandeur de référence --- l'unité --- y tient.~» |
| `grade-11/fr/06-magnetic-fields.tex` opening (rewritten this pass) | **native** — «~Mille ans durant, les marins se sont guidés sur des aiguilles aimantées sans que personne sache pourquoi elles pointent le nord.~»; «~le champ exerce en retour une force sur les courants~: c'est ainsi que tourne tout moteur électrique.~» |
| `grade-12/fr/06-newtons-laws.tex` opening (rewritten this pass) | **native** — «~Entre les deux, une vérité toute simple~: rien à bord n'a changé, sinon le mouvement.~»; the method reads as a French teacher's checklist («~choisir un système, dessiner ses forces, projeter $\sum \vect F = m\vect a$~») |
| `grade-12/fr/02-sound-acoustics.tex` `def:…:timbre` (rewritten this pass) | **native** — «~une barre par $f_n$, dont la longueur mesure l'intensité de cet harmonique. L'oreille entend $f_1$ comme la hauteur et le mélange des intensités comme le timbre --- la couleur du son.~» |
| `grade-12/fr/11-rc-rl-circuits.tex` weekend problem `pb:…:1` | **native** — «~un sifflement de deux secondes, une milliseconde de gloire, et le cousin mural qui redémarre les cœurs --- une seule exponentielle les fait tous tourner~»; the whole 20-part problem is rendered, `\qty`/`\unit` markup intact |
| `grade-12/solutions/fr/16-special-relativity.tex` header + sols 1–3 | **native** — «~Les \qty{10.0}{s} du vaisseau sont le temps propre~: le métronome (une horloge) est présent aux deux battements.~» |

## Why not 100 — ordered gap list

1. **Link coverage on two core words is now chapter-local.** *tension*
   (88 → 28 links) and *hauteur* (53 → 13) link only inside the chapters that
   define them. That is the right trade — a wrong-sense link is worse than a
   missing one, and it is the trade the Dutch edition made — but a French
   reader gets no hyperlink on «~la tension du fil~» in the Newton chapter
   where an English reader gets one on "tension". No configuration of the
   current engine can do better: French uses one word where English uses two,
   and the engine resolves ambiguity only by chapter order.
2. **`spectre` in the light chapters points at the sound definition.** In g12
   Doppler, nuclear-energy and quantum-world, *spectre* means a light spectrum
   but resolves to `def:g12:sound-acoustics:timbre` (13 links). **English does
   exactly the same** on the same sentences, so this is inherited, not a French
   defect, and diverging would cost parity for no gain. It should be fixed in
   the English config, for every language at once.
3. **siunitx range phrase and cleveref conjunctions are still English.** The
   PDF prints «~27.5 to 4186 Hz~» and «~Chapitres 25 and 29~». The Dutch pass
   closed this with one `\sisetup{range-phrase=…, list-pair-separator=…}` plus
   `\crefpairconjunction` / `\creflastconjunction` redefined inside
   `\AtBeginDocument`. **French, Spanish and Portuguese still carry the gap** —
   one block per `styles/lang/<lang>.tex`. Left untouched here because it is a
   style-file change shared with other editions, not an `fr/` body change.
4. **Decimal point kept in all math** (`$0.63$ s`, `9.81 m/s²`) while French
   prose elsewhere writes the comma (`$0{,}50$~euro`). The series keeps the
   point in every language so the shared `parts/` physics is identical; a
   French pupil reads a mildly foreign notation throughout.
5. **Theorem-name links are absent by policy** (`NOT_A_TERM` contains
   *loi de*): a French reader gets no hyperlink on «~deuxième loi de Newton~»
   where the English reader gets one. Defensible and consistent, but a real
   difference in reading experience.
6. **`\cref` reads as a bare noun** («~d'après le \cref{thm:…}~»); acceptable
   French, but a native author would sometimes write «~le théorème de…~».
7. Nothing else found. No missing content, no encoding defects, no curriculum
   or country names, no residual English, no link inside protected markup.

## Note on the ES edition

`python3 tools/link_defined_terms.py --book 2 --lang es --check` is stale on
**70 of 70 files** (4 045 links generated). Out of scope for this file, but it
is the same failure and the same fix — and, given what French turned up, the
Spanish repair should be treated as a curation job too, not as two commands:
Spanish has the same gender/number inflection problem (`real`/`reala`,
`vertical`/`verticales`, `absoluto`/`absoluta`) and its own homographs
(*tensión*, *altura*, *foco*, *potencia*).
