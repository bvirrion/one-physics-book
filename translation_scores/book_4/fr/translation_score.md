# One Physics Book 4 (University, Year 2) — French edition: self-score

**Date:** 2026-08-22
**Quality bar:** *native academic* (the bar of `translation_instruction.md`).
**Sense/structure reference:** the English canon (`parts/bachelor-2/*.tex`),
followed line-range by line-range through `tools/id_apply.py`.
**Register comparands:** the finished French Book 3 (`parts/bachelor-1/fr/`)
for the university *cours de licence* voice and for every term the two volumes
share (*vecteur de Poynting*, *équation d'onde*, *effet tunnel*, *fonction
d'onde*, *quantification*), and `../one-math-book/parts/bachelor-1/fr/` for the
lecture register.

## Overall: **97 / 100**

| Dimension | Score | Note |
|---|---:|---|
| **Register** (academic French, weighted) | **96** | Standard *cours de licence* voice: narrative present in the chapter openings, infinitive imperatives in exercise stems (`Montrer que…`, `En déduire…`, `Établir…`, `Estimer…`), `Considérons…` / `Cherchons…` / `Posons…` in proofs. No `nous allons montrer` padding; no English clause order; French punctuation spacing (`~:`, `~;`, `~?`, `~!`) and «~guillemets~» throughout. |
| **Terminology** (weighted) | **96** | Glossary below. Every `\index{}` key is French and equals its visible term; the 92 English index keys inherited from the canon in chapters 21–31 were all translated in this pass. No sense swaps found on sampling. |
| **MT-artifact freedom** (weighted) | **96** | Residual-English sweep over all 62 files returns **zero** English tokens in visible prose (the only `and`/`with` hits are TikZ `controls … and …`). Gate 9 (twin comparison) returns **one** multi-word fragment in the whole tree, `(Maxwell--flux)`, which is the proper name of an equation. The French-only line-wrap defect of *Why not 100* is gone from the shipped artefact, verified two independent ways — a `%`-agnostic source sweep and the rendered PDF — but it took two passes to fix properly, so this is not a 100. |
| Structure | **100** | `check_translation.sh bachelor-2 fr` **PASSED**. Every one of the 62 files written as line-range replacements on the English canon through `tools/id_apply.py`; no `--force-classes`, no per-range `!class` opt-out anywhere in the book. |
| LaTeX hygiene | **100** | 0 errors, 0 undefined references, **0 overfull boxes** (EN 0), 0 "invalid in math mode", 0 TeX accent escapes, 0 non-ASCII inside `\qty{}`/`\unit{}`/`\num{}` (`nullfont` stays at the English baseline of 60, which is the proof), and 0 line-continuation `%` in the tree. |
| Cross-references | **100** | Ordered `\label{}` multiset diffs to **0 lines** against English across bodies and solutions. |
| Figures | **99** | Drawing code byte-identical to English (enforced by `id_apply`'s `draw` census); only node text, `\legend{}`, `\addlegendentry{}`, axis labels and `{\small …}` captions translated. 150 `omfigure`, 121 `tikzpicture`, 44 `includegraphics` — identical to English. |
| Solutions | **97** | All 31 solution files translated; `\textbf{n.}` numbering and every number preserved; headers read `\section*{Chapitre \ref{ch:…} --- <titre>}` with the `ch:…` slug unchanged. |
| Defined-term links | **96** | 1 365 `\omterm` links against English's 1 231 (**1.11×**). 144 target labels against 143; parity table below. |

**Overall 97**, weighted toward register + terminology + MT-artifact freedom.
Measured on the tree as it stands after the second elision pass and the
rebuild that followed it — not on any earlier build.

## Build gates

Measured with `grep -a` — pdfTeX writes the log as ISO-8859, and a plain
`grep -c` treats it as binary, prints nothing and exits 1, which reads as "0"
and is not a count.

| Gate | Result |
|---|---|
| `.fls` honesty check (`grep -o 'parts/bachelor-2/\(solutions/\)\?fr/[^ ]*' … \| sort -u \| wc -l`) | **62 / 62** — the build really reads the French tree |
| `bash tools/check_translation.sh bachelor-2 fr` | **PASSED** |
| `latexmk -g one_physics_book_4_university_year_2_fr.tex` | exit 0, **359 pages** (EN 345) |
| `grep -a '^!'` | **0 lines** (not merely a count — the lines were read; none exists) |
| `grep -aci 'undefined'` | **0** |
| `grep -ac 'Overfull'` | **0** (EN 0) |
| `grep -ac 'invalid in math mode'` | **0** |
| `grep -ac 'Underfull'` | 35 (EN 34) — the series norm |
| `grep -ac 'nullfont'` | **60** — identical to the English build; it is a pgfplots measuring pass, not a defect, and a *rise* above 60 would mean a non-ASCII character inside a `\qty{}` |
| `python3 tools/check_latin_prose.py` (gate 9) | 134 hits: **1 multi-word**, 133 one-word cognates |
| `pdftotext` prose check on the rendered book | **0** dangling elisions (`d’ `, `l’ `, `qu’ `, …), **0** `word- word`, `' . '` / `' , '` / `' )'` rates within 1.5 % of the untouched English PDF |
| `grep -c '[^ %]%$'` (line-continuation `%`) | **0** — house style, as chapters 01–17 and the shipped Book 3 fr |

### Gate 9 in detail

| Class | Hits | Verdict |
|---|---:|---|
| `text` (multi-word) | 1 | `11-maxwell-equations.tex:114` `(Maxwell--flux)` — the proper name of the equation, identical in French. |
| `text-1word` | 117 | Math subscripts French spells the same: `\text{sat}` (55), `\text{liq}`, `\text{vap}`, `\text{fus}`, `\text{evap}`, `\text{cond}`, `\text{mol}`, `\text{diss}`, `\text{surf}`, `\text{sub}`, `\text{vib}`, `\text{ppm}`. |
| `node-1word` | 15 | `plasma`, `laser`, `image`, `violet`, `radio`, `compression`, `saturation`, `populations`, `turbine`, `plateau`, `section $S$`, `$\vect u$ (propagation)`. |
| `legend-1word` | 1 | `plasma, $\omega = ck$` — one French word plus mathematics. |

Two genuine defects that gate 9 caught during the pass are **fixed**:
`16-guided-waves.tex` node `$a$ (the $y$ axis)` → `$a$ (l'axe $y$)`, and
`21-gratings.tex` axis label `(units of $\lambda/N$)` → `(en unités de
$\lambda/N$)`. Four more were found by eye in the same sweep:
`$M_\lambda$ (normalised)` → `(normalisé)`, two `(arb.)` → `(u.a.)`,
`\addlegendentry{long fin}` → `{ailette longue}`, `{$\xi\tan\xi$ (even)}` /
`{(odd)}` → `{(pair)}` / `{(impair)}`, `\addlegendentry{Sun,}` / `{Earth,}` →
`{Soleil,}` / `{Terre,}`, and `\addlegendentry{$|\psi|^2$ (shifted)}` →
`(décalé)`.

## Structural mirror

| Count | EN | FR |
|---|---:|---:|
| Chapter bodies | 31 | 31 |
| Solution files | 31 | 31 |
| `\begin{exercise}` | 372 | 372 |
| `\begin{problem}` | 31 | 31 |
| `\begin{solution}` | 403 | 403 |
| `\begin{omfigure}` | 150 | 150 |
| `\begin{tikzpicture}` | 121 | 121 |
| `\includegraphics` | 44 | 44 |
| `\label{}` multiset diff | — | **0 lines** |

## Sampled passages

Five samples across the book, easy to hard.

### 1. Chapter opening — ch. 28 *Potentiels thermodynamiques*

> Étirez vivement un élastique et portez-le à vos lèvres~: il est chaud~;
> laissez-le se contracter et il est froid. Suspendez-lui un poids et
> chauffez-le au sèche-cheveux~: il \emph{raccourcit}. Aucun ressort d'acier
> ne se comporte ainsi, et la raison est que la tension d'un élastique n'est
> pas affaire d'énergie mais d'entropie --- les chaînes étirées ont moins de
> façons de se ranger.

**Verdict: native.** The imperative chain with enclitic pronouns
(`portez-le`, `Suspendez-lui`, `chauffez-le`), `n'est pas affaire de` for "is
not a matter of", and `moins de façons de se ranger` are French moves, not
renderings of English ones. Length matches the source.

### 2. Definition — ch. 25 *Conduction thermique*

> En régime stationnaire sans sources, une lame d'épaisseur $e$, d'aire $S$,
> de conductivité $\lambda$, entre les températures $T_1$ et $T_2$, a un
> profil linéaire et porte le flux […] sa \emph{résistance thermique}. La
> température joue le rôle du potentiel, le flux celui du courant~: les
> résistances en série (couches d'un mur) s'ajoutent, celles en parallèle
> (mur et fenêtre) ajoutent leurs inverses.

**Verdict: native.** The ellipsis in `le flux celui du courant` (verb gapped,
demonstrative pronoun kept) is exactly how written French compresses a
parallel clause; English needs "the flux that of the current".

### 3. Proof — ch. 27 *Bilans thermodynamiques et systèmes ouverts*

> Suivons le système fermé formé du fluide contenu dans $\Sigma$ à l'instant
> $t$ plus la tranche $\dd m = \dot m\,\dd t$ sur le point d'entrer~; à
> $t + \dd t$ il se compose du fluide contenu dans $\Sigma$ (même état, régime
> permanent) plus la tranche $\dd m$ qui est sortie.

**Verdict: native.** `Suivons…` is the French proof imperative; `sur le point
de` for "about to"; `il se compose de` rather than the calque `il consiste en`.

### 4. Exercise stem — ch. 31 ex. 6 *Puits fini*

> (b) Montrer graphiquement qu'il y a toujours un état lié et les compter pour
> $R = 1$, $4$, $10$. (c) Électron, $V_0 = \qty{1}{eV}$, $2a = \qty{1}{nm}$~:
> $R$, nombre d'états, profondeur de pénétration de l'état fondamental
> (prendre $E \approx \qty{0.26}{eV}$). (d) Qu'advient-il du nombre d'états
> liés quand $V_0 \to \infty$, et de leurs énergies~?

**Verdict: native.** Infinitive imperatives (`Montrer`, `compter`, `prendre`)
— the French exercise register used by all 31 chapters — and `Qu'advient-il
de…~?` rather than the flat `Que se passe-t-il pour…`.

### 5. Solution — ch. 27 sol. 10 *Remplir un réservoir*

> (a) $\dd(mu)/\dd t = \dot m h_0$ s'intègre en $mu = mh_0$~: $c_vT = c_pT_0$,
> $T = \gamma T_0$. […] (d) Le travail de transvasement échauffe le gaz~; un
> remplissage lent dans un bain d'eau laisse sortir la chaleur pour que la
> pression à \qty{20}{\celsius} soit celle voulue.

**Verdict: native.** `s'intègre en` for "integrates to"; subjunctive after
`pour que`; `celle voulue` for "the one wanted". Telegraphic solution style
preserved with French spacing.

## Glossary settled by this pass (chapters 20–31, the new physics)

| English | French | Note |
|---|---|---|
| grating, grating equation | *réseau*, *équation des réseaux* | |
| order (of a grating) | *ordre* | |
| free spectral range | *intervalle spectral libre* (ISL) | `\text{FSR}` → `\text{ISL}` in the displays too |
| resolving power | *pouvoir de résolution* | not *résolution* alone |
| finesse, Fabry–Pérot etalon | *finesse*, *étalon de Fabry--Pérot* | |
| blazed grating, blaze angle | *réseau blazé*, *angle de blaze* | the loanword French opticians use |
| Airy disc | *tache d'Airy* | not *disque* |
| dark field, phase contrast | *fond noir*, *contraste de phase* | |
| spatial filtering, Fourier plane | *filtrage spatial*, *plan de Fourier* | |
| seeing (astronomy) | *seeing*, in «~guillemets~» at first use | the term French astronomers keep |
| stimulated / spontaneous emission | *émission stimulée* / *spontanée* | |
| population inversion, pumping | *inversion de population*, *pompage* | |
| gain clamping, small-signal gain | *verrouillage du gain*, *gain petit signal* | |
| output coupler | *coupleur de sortie* | |
| waist, Rayleigh length | *col*, *longueur de Rayleigh* | |
| case hardening (carburising) | *cémentation* | |
| drive-in / predeposition (doping) | *redistribution* / *prédépôt* | the French microelectronics terms |
| random walk | *marche au hasard* | Book 3's form, not *marche aléatoire* |
| fin, fin efficiency | *ailette*, *efficacité d'ailette* | |
| heat sink, thermal paste | *dissipateur*, *pâte thermique* | |
| effusivity, penetration depth | *effusivité*, *profondeur de pénétration* | |
| black body, emissivity, exitance | *corps noir*, *émissivité*, *exitance* | |
| greenhouse effect, forcing, albedo | *effet de serre*, *forçage*, *albédo* | |
| degree-days | *degrés-jours*, `\unit{K.jour}` | |
| open system, control volume | *système ouvert*, *volume de contrôle* | |
| shaft work, flow work | *travail d'arbre*, *travail de transvasement* | the standard French pair |
| throttle, nozzle, diffuser | *détendeur*, *tuyère*, *diffuseur* | |
| quality (of wet steam) | *titre* | |
| reheat, cross-disperser | *resurchauffe*, *disperseur croisé* | |
| COP (cooling / heating) | `\mathrm{COP}_{\text{froid}}` / `_{\text{chaud}}` | |
| free energy / free enthalpy | *énergie libre* / *enthalpie libre* | Helmholtz / Gibbs |
| Maxwell relations, Legendre transform | *relations de Maxwell*, *transformée de Legendre* | |
| supercooled, superheated | *surfondu*, *surchauffé* | |
| equal-area construction | *construction des aires égales* | |
| freeze-drying | *lyophilisation* | |
| scale height | *hauteur d'échelle* | |
| partition function | *fonction de partition* | |
| Schottky anomaly, equipartition | *anomalie de Schottky*, *équipartition* | |
| adiabatic demagnetisation | *désaimantation adiabatique* | |
| wave function, Born's rule | *fonction d'onde*, *règle de Born* | |
| wave packet, spreading | *paquet d'ondes*, *étalement* | |
| stationary state, Bohr frequency | *état stationnaire*, *fréquence de Bohr* | |
| infinite / finite well | *puits infini* / *fini* | |
| tunnelling, tunnel splitting | *effet tunnel*, *dédoublement tunnel* | |
| quantum dot | *boîte quantique* | Book 3's form, reused |
| scanning tunnelling microscope | *microscope à effet tunnel* | |
| work function | *travail de sortie* | for a metal surface (Book 3's *travail d'extraction* is the photoemission sense) |

## Term-link layer

`tools/term_config/book4_fr.py` was a verbatim copy of `book3_fr.py` when this
pass started. It is now a **curation of this book**, and what it had to say
that neither `book3_fr.py` nor `book4_en.py` says:

* **`NOT_A_TERM` still cannot be translated word for word.** The English
  default carries `"law of"`, which never fires because English writes
  *Fourier's law*, *Fick's law*, *Curie's law* — French writes *loi de
  Fourier*, and translating the default word for word would silently delete
  every one. `"loi"`, `"lois"`, `"méthode"`, `"énoncé"` are deliberately
  absent; `"théorème"` stays, exactly as English's `"theorem"` does.
* **Book 3's two `EXTRA` restorations had to be *removed*, not kept.**
  `théorème de Gauss` and `théorème d'Ampère` point at `thm:b1:…` labels that
  live in Book 3; Book 4 has no such labels, so a link there would be an
  undefined reference. Chapter 10 names both in passing and leaves them
  unlinked, exactly as `book4_en.py` does. The seed would have shipped them.
* **`solide` is the homograph English does not have, and it had to be
  DROPped, not STOPped.** English defines *rigid body* — two words, a term of
  art its own prose then avoids, so `book4_en.py` links it **once** in the
  whole volume. French defines \emph{solide}, which is also the state of
  matter of chapters 6, 25 and 29, the ordinary adjective, and the head of
  *le son dans les solides*. Left in, it linked **57 times, 29 of them in
  chapter 1 alone**, where the word is on every line. `STOP` does not help,
  because a STOPped word is still linked inside its defining chapter.
  `champ des vitesses (solide)`, `moment cinétique (solide)` and `énergie
  cinétique (solide)` survive as terms of their own.
* **`book4_en.py`'s five stops, in French:** `laser`, `seuil` (threshold),
  `absorption`, `efficacité` (efficiency), `permanent` (steady). Each was
  checked to be a bare harvested term before being stopped.
* **`DROP` mirrors English term for term:** `quantifiées`, `quatre niveaux`,
  `trois niveaux`, `eulérienne` (English: `quantised`, `four-level`,
  `three-level`, `Eulerian`), plus the itemize head `Compresseur, pompe,
  turbine`, whose three nouns are linked individually.
* **`EXTRA`** adds the lowercase `détendeur` and `tuyère`, exactly as
  `book4_en.py` adds lowercase `throttle` and `nozzle`.
* **The 92 English `\index{}` keys of chapters 21–31 had to be translated
  first.** The harvester reads `\index{}`, so with English keys in the tree
  the French book would have carried an English index *and* a set of terms
  that can never match French prose. Chapters 1–19 already had French keys;
  20 too; 21–31 did not, and now do.
* `AMBIG_POLICY = "drop"` — the university convention (books 3–5).

Result: **1 365 links, 1.11× English's 1 231**, with the same shape by target.

| Target kind | EN | FR |
|---|---:|---:|
| `def` | 578 | 610 |
| `prop` | 390 | 457 |
| `thm` | 207 | 242 |
| `ex` | 35 | 36 |
| `rem` | 19 | 19 |
| `cor` | 1 | 1 |
| `met` | 1 | 0 |
| **total** | **1 231** | **1 365** |

`python3 tools/link_defined_terms.py --book 4 --lang fr --check` reports
*every file matches what the config generates*.

### Omterm target parity

144 French target labels against 143 English. Every divergence accounted for.

**In English, not in French (2 labels, 2 English links):**

| Label | EN links | Why |
|---|---:|---|
| `def:b2:rigid-body-mechanics:solid` | 1 | *solide*, DROPped for the reason above. English's single link is the cost of parity; the alternative was 57. |
| `met:b2:rigid-body-mechanics:incline` | 1 | EN *rolling down an incline*; the French bodies say *qui roule sur un plan incliné* in running prose, so the noun phrase *roulement sur un plan incliné* occurs only at its own method box. |

**In French, not in English (3 labels, 20 French links):**

| Label | FR links | Why |
|---|---:|---|
| `thm:b2:potential-wells-tunneling:tunnel` | 15 | English prose says *tunnelling* (the gerund) where French must say *effet tunnel* (the noun phrase that is also its `\index{}` key), so the English term never matches its own chapter. |
| `prop:b2:dispersion-wave-packets:lossy` | 4 | *condition de Heaviside* is a fixed phrase in French; English varies between *Heaviside condition* and *distortionless line*. |
| `def:b2:heat-conduction:flux` | 1 | *flux thermique*; English writes *thermal flux* only at the definition. |

**Largest per-target gaps** (all read and checked against their targets):

| Label | EN | FR | Why |
|---|---:|---:|---|
| `def:b2:fluid-kinematics:euler` | 43 | 54 | three French terms (*ligne de courant*, *trajectoire*, *écoulement stationnaire*) against three English ones that are rarer in prose (*streamline*, *pathline*, *steady flow*). |
| `prop:b2:feedback-oscillators:lockin` | 4 | 14 | French says *détection synchrone* every time; English alternates *lock-in*, *lock-in amplifier*, *synchronous detection*. |
| `thm:b2:wave-interfaces:snell` | 6 | 15 | *réflexion totale* (two words) against *total internal reflection* (three), which English shortens to *TIR* or to a pronoun. |
| `def:b2:michelson:instrument` | 7 | 14 | French has one-word nouns, *séparatrice* and *compensatrice*, where English needs *beam splitter* and *compensating plate*. |
| `def:b2:feedback-oscillators:loop` | 20 | 14 | the one gap the other way: English *feedback* is one word and everywhere; French splits it into *rétroaction* and *gain de boucle*. |

## Why not 100

1. **A French-only line-wrap defect of my own making, and it took two passes
   to fix properly.** French elides (`l'`, `d'`, `qu'`, `n'`) where English
   does not, and when a source line ends on the apostrophe TeX turns the
   newline into a space: *d' entropie*, *l' énergie*. I found the class,
   confirmed it in the PDF with `pdftotext`, and fixed all 130 sites — 104
   elisions, 21 lines that *began* with punctuation (`. Sa propre largeur`,
   `~; une couche…`), 5 that split a hyphenated word (*demi-* /
   *millimètre*) — by terminating the offending line with `%`.

   That fix was *correct* and *wrong*. Correct, because `%` eats the newline
   and the rendered PDF came back clean. Wrong, because chapters 01–17 of this
   same tree, and the whole shipped Book 3 fr, carry **zero** line-continuation
   `%`: the house style is to rewrap. And a trailing `%` hides the defect from
   the one-line `grep` that finds it — which is exactly what happened when the
   coordinator swept the tree and saw 103 live elisions that were in fact
   already neutralised. All 130 sites are now **rewrapped** in house style (the
   elided fragment moved down onto its word, the punctuation pulled up, the
   hyphen carried down), the tree carries **0** line-continuation `%`, and the
   result is verified two ways: a `%`-agnostic source sweep, and `pdftotext`
   over the rebuilt book. A **131st** site turned up after that — an orphaned
   comma inside an indented `\item` (`24-particle-diffusion.tex:575`,
   printing *que voyez-vous , et quelle*), missed because my own published
   sweep anchored the punctuation at column 0. It is fixed, and the regex in
   *For the next translator* is now indentation-aware.
   The one end-of-line apostrophe that remains is
   `$\dd/\dd t\int n^2 = 2D\int nn''` inside mathematics, where the newline is
   whitespace and there is nothing to fix.

   The English canon cannot produce this class of defect, so no census and no
   gate in the project looks for it — see the note to the next translator.
2. **The link layer runs 11 % above English and cannot be brought to 1.00×.**
   The excess is structural: French repeats a noun phrase where English uses a
   pronoun, a gerund or an abbreviation (*effet tunnel*, *détection
   synchrone*, *réflexion totale*). Forcing parity would mean stopping terms
   that are genuinely defined and genuinely repeated.
3. **`\index{}` keys are French but not alphabetised for French.** The index
   sorts on raw UTF-8, so *émissivité* files after *z*. English has the same
   behaviour and no edition of any book in this project fixes it; noted so the
   next pass does not rediscover it.
4. **The `%` comments inside TikZ pictures stay English** across the whole
   edition (as in every other language). Invisible on the page, and changing
   them would break `id_apply`'s byte-identical guarantee for drawing code.

## Handed back to the coordinator

1. **RESOLVED (coordinator).** `frontmatter/image-credits-book4.fr.tex` now
   reads `\emph{Allée de von Kármán dans les nuages}`; re-measured after the
   rebuild, the book has **0 overfull boxes**.
2. **RELAYED (coordinator).** The English canon writes TeX accent escapes.
   `parts/bachelor-2/04-viscous-flows.tex:484` and
   `frontmatter/image-credits-book4.tex:11` carry `von K\'arm\'an`. Copied
   through, that fails `check_translation.sh`'s accent-escape gate in **every**
   Latin-script edition; the French copy now writes `von Kármán` in UTF-8.
   Dutch, Spanish and Portuguese each inherited it; Portuguese had already
   failed gate 6 on it. Still worth fixing in the canon itself.
3. **`\qty{}` worklist: all 17 sites confirmed.** Twelve in running text were
   rewritten in-patch (`lines/mm` → `traits/mm`, `day` → `jour`, `K.day` →
   `K.jour`, `days` → `jours`, …); five inside `$…$` were kept byte-identical
   for the math census and post-sed'd (`{fringe}` → `{frange}`, `{day}` →
   `{jour}`). Two more that were not on the list turned up and were fixed the
   same way: `{kWh/day}` → `{kWh/jour}` and `{kg/yr}` → `{kg/an}`.
   `\qty{25}{images/s}` and `\qty{1}{cent}` (the musical interval) are correct
   French and were left alone. Zero non-ASCII inside any
   `\qty{}`/`\unit{}`/`\num{}` argument, and `nullfont` stays at 60.
4. **RESOLVED (coordinator).** `\addlegendentry{}` was the blind spot
   `\legend{}` used to be — 31 sites in the canon, invisible to every gate.
   The regex is now `\\(?:legend|addlegendentry)` in `check_latin_prose.py`,
   `check_hindi_prose.py`, `check_arabic_prose.py` and `id_apply.py`'s draw
   census, so the 9 sites this book had to post-`sed` (`long fin`,
   `even`/`odd`, `Sun,`/`Earth,`, `(shifted)`, `air`/`helium alone`, and the
   decibel ladder of ch. 7) can be named as ordinary ranges from now on. Still
   open: a bare `\foreach \l/\t in {…}` label list is not blanked either
   (ch. 7's decibel ladder is one), so that one still needs a post-write edit.
5. **The elision defect is French-specific — I checked the other six.**
   Sweeping every Book 4 tree with the `%`-agnostic regex, the only
   end-of-line apostrophes outside French are TeX closing quotes (`` '' ``) in
   nl (5), es (2), id (4) and the shared `nn''` math line of
   `solutions/*/24-particle-diffusion.tex`; ar and hi are clean. **No other
   edition has this defect**, and the shipped Book 3 fr is clean too (its four
   hits are `f_1'`, `A'`, `T'` — math primes). Any language that elides or
   takes clitics — French, Italian, Catalan — is exposed; the rest are not.

## For the next translator of this book

* **Never end a source line on a French elision — and fix it by rewrapping,
  not with `%`.** `d'`, `l'`, `qu'`, `n'`, `s'`, `j'` at end of line become
  `d' entropie` on the page. Nothing in the project catches it: `id_apply`'s
  censuses compare structure, gate 9 compares the twin's fragments, and the
  LaTeX log is silent. The three sweeps are

  ```sh
  grep -nE "['’]%?$"                          …   # elision left at end of line
  grep -nE '^[[:space:]]*([.,;)?!]|~[;:?!])'  …   # punctuation orphaned onto the next line
  grep -nE '[A-Za-zÀ-ÿ]-%?$'                  …   # hyphenated word split across lines
  ```

  Three details, each of which hid a real site in this book. The `%?` in two
  of them, because a `%`-terminated line is fixed but still matches the naive
  pattern and no reviewer can tell the two apart. The `~[;:?!]` alternative,
  because French-spaced punctuation at line start is invisible to a plain
  `^[.,;)?!]` — 7 of this book's 21 sites. And `[[:space:]]*`, because an
  orphaned comma inside an indented `\item` does not sit at column 0 — that was
  the 131st and last site found. Terminating the line with `%` *does* fix the
  page — but it is not this project's house style (chapters 01–17 and the
  whole of Book 3 fr carry zero line-continuation `%`), and it makes the
  defect invisible to the plain `grep`, so the next reviewer cannot tell a
  fixed line from a broken one. Move the elided fragment down onto its word
  (`… mais` / `d'entropie`), pull an orphaned `.` or `~;` back up, and carry
  the hyphen down with its second half. Only mathematics may keep an
  end-of-line apostrophe: inside `$…$` the newline is whitespace.
* **Translate the `\index{}` keys before generating the links.** The harvester
  reads them; leaving them English gives an English index and a term list that
  cannot match French prose.
* **Keep English line breaks exactly where they fall *inside* math spans.**
  The math census compares span text including its newlines, and `\qty{}`
  arguments that sit inside `$…$` are frozen by it — translate those by a
  post-write `sed`, never with `!math`, which opts the whole file out of the
  most valuable census in the tool.
* **Start a replaced range on the `\begin{env}[…]` line** whenever the
  environment has an optional title. Off-by-one here was the single most
  frequent rejection of the pass.
* **`\emph` adjacency is a census.** Dropping an `\emph{}` that English has —
  even one that reads oddly in French, such as *les particules
  \emph{descendent} le gradient* — rejects the whole file.
* **Generate the links only after the last body is written**, and diff the
  target set *and* the per-target counts against English before believing the
  config: the Book 3 seed produced 1 419 links with two dead `thm:b1:` targets
  in it, and the distance from there to 1 365 with 144 live targets is
  entirely `STOP`/`DROP` curation.
