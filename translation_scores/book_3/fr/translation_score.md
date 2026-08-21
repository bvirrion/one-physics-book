# One Physics Book 3 (University, Year 1) — French edition: self-score

**Date:** 2026-08-21
**Quality bar:** *native academic* (the bar of `translation_instruction.md`).
**Sense/structure reference:** the English canon (`parts/bachelor-1/*.tex`) for
content. **French is the reference edition for this book**, so there is no FR
twin to lean on: the register comparands used were the French Books 1–2 of
this series (`parts/grade-*/fr/`) for settled physics vocabulary — *travail
d'extraction*, *potentiel d'arrêt*, *longueur d'onde de de Broglie*,
*quantification* — and `../one-math-book/parts/bachelor-1/fr/` for the
university lecture register.

## Overall: **96 / 100**

| Dimension | Score | Note |
|---|---:|---|
| **Register** (academic French, weighted) | **96** | Standard French *cours de licence* voice: narrative present in the chapter openings, `Montrer que…` / `En déduire…` / `Établir…` infinitive imperatives in exercise stems, `Considérons…` / `On note…` / `Orientons…` in proofs and definitions. No `nous allons montrer` padding, no English clause order. |
| **Terminology** (weighted) | **96** | Settled glossary below; every `\index{}` key equals its visible term. No sense swaps found on sampling (*champ* ≠ *field* as in a farm, *moment* is the moment of a force and is stoplisted where it means "the moment when", *foyer* is the optical focus and never the hearth of ch. 24). |
| **MT-artifact freedom** (weighted) | **96** | Residual-English sweep over all 60 files returns **zero** English tokens in visible text; the only English left in the tree is inside `%` comments, which the whole edition keeps in English by convention (as does `28-magnetostatics.tex` in every other language). |
| Structure | **100** | `check_translation.sh bachelor-1 fr` **PASSED**. Every body written as line-range replacements on the English canon through `tools/id_apply.py`, so labels, `\cref` targets, `\begin{solution}{key}`, `\qty{}{}`, `\foreach`, `xtick=` and every math display are byte-identical to English. |
| LaTeX hygiene | **99** | 0 errors, 0 undefined references, **0 overfull boxes**, 0 "invalid in math mode", 0 TeX accent escapes, 0 zero-width/bidi characters, 0 non-ASCII inside `\qty{}`/`\unit{}`/`\num{}`. |
| Cross-references | **100** | Ordered `\label{}` sequence diffs to **zero lines** against English across bodies and solutions. 12 exercises + 1 weekend problem per chapter, one solution each. |
| Figures | **98** | Drawing code byte-identical to English (enforced by `id_apply`'s `draw` census); only node text, axis labels and `{\small …}` captions translated. Two node strings shortened in ch. 28 to clear an overfull picture. |
| Solutions | **96** | All 30 solution files translated; `\textbf{n.}` numbering and every number preserved; headers read `\section*{Chapitre \ref{ch:…} --- <titre>}` with the `ch:…` slug unchanged. |
| Defined-term links | **96** | 2 430 `\omterm` links against English's 2 342 (**1.04×**; the finished Spanish edition landed at 1.02×). Target-set parity table below. |

**Overall 96**, weighted toward register + terminology + MT-artifact freedom.

## What this session produced

This was the last leg of the edition. Chapters 01–29 (bodies + solutions) were
already on disk, all written through `tools/id_apply.py`. This pass added:

1. **Chapter 30, *Introduction à la physique quantique*** — body (70 line-range
   replacements) and solutions (38), the longest chapter in the book.
2. **`tools/term_config/book3_fr.py`** — curated from `book3_en.py`, then the
   whole French link layer generated (2 430 links across 60 files).
3. **The five overfull boxes** left over from the earlier passes, plus the one
   chapter 30 introduced — all six cleared by rewording French prose, never by
   touching the mathematics.

No `--force-classes` and no per-range `!class` opt-out was used anywhere: all
108 ranges of chapter 30 passed every one of `id_apply`'s ten structural
censuses (labels, envs, solutions, emph adjacency, index count, ordered
math-span sequence, drawing code, per-range delimiters, brace balance, omterm)
against the English twin on the first or second attempt. `--no-gate` was used,
as instructed, because census 11 is `check_indonesian_prose.py` and means
nothing for a French target.

## Build gates

Measured with `grep -a` — pdfTeX writes the log as ISO-8859, and a plain
`grep -c` treats it as binary, prints nothing and exits 1, which reads as "0"
and is not a count.

| Gate | Result |
|---|---|
| `bash tools/check_translation.sh bachelor-1 fr` | **PASSED** |
| `latexmk one_physics_book_3_university_year_1_fr.tex` | exit 0, 349 pages (EN 332) |
| `grep -ac '^!'` | **0** |
| `grep -aci 'undefined'` | **0** |
| `grep -ac 'Overfull'` | **0** (EN 0) |
| `grep -ac 'invalid in math mode'` | **0** |
| `grep -ac 'Underfull'` | 32 (EN 33) — the series norm |
| `grep -ac 'nullfont'` | 65 — **identical in every edition including English**; it is pgfplots measuring `xmin=0.01` on the three log-axis figures, not a defect |

## Structural mirror

| Count | EN | FR |
|---|---:|---:|
| Chapter bodies | 30 | 30 |
| Solution files | 30 | 30 |
| `\begin{exercise}` | 360 | 360 |
| `\begin{problem}` | 30 | 30 |
| `\begin{solution}` | 390 | 390 |
| `\label{}` multiset diff | — | **0 lines** |

## Sampled passages

Five samples across the whole book, young-to-hard, including chapters not
written in this session.

### 1. Chapter opening — ch. 20 *Théorie cinétique et gaz parfait* (not this session)

> L'air d'une salle de classe pèse autant qu'un homme adulte et contient plus
> de molécules qu'il n'y a de grains de sable sur Terre, chacune filant à la
> vitesse d'une balle de fusil et heurtant ses voisines dix milliards de fois
> par seconde. Personne ne peut en suivre une~; personne n'en a besoin.

**Verdict: native.** `qu'il n'y a de` with the expletive *ne*, the participial
`chacune filant…` chain, and the two-clause `Personne… ; personne…` are French
constructions, not renderings of English ones. Concision matches the source.

### 2. Definition — ch. 22 *Système, transformation* (not this session)

> Une \emph{transformation} le fait passer d'un état d'équilibre à un autre.
> Elle est \emph{quasi statique} si le système traverse une succession d'états
> d'équilibre (assez lentement pour que $P$ et $T$ soient définis partout), et
> \emph{réversible} si, de plus, inverser les conditions extérieures inverse le
> chemin suivi.

**Verdict: native.** Subjunctive after `assez lentement pour que`, the
adverbial `si, de plus,` inserted between commas, and *quasi statique* written
unhyphenated as French thermodynamics writes it.

### 3. Proof — ch. 16 *Forces centrales* (not this session)

> La partie~1 est le \cref{cor:b1:angular-momentum:central}. La force est
> conservative et aucune autre force n'agit, donc $E_m$ se conserve~; […] Le
> terme $mC^2/2r^2$ […] joue le rôle d'une \emph{barrière centrifuge} répulsive
> dans le problème radial, auquel s'applique l'analyse à une dimension du
> \cref{ch:b1:work-and-energy}.

**Verdict: native.** The relative `auquel s'applique…` with inversion is a
written-French move an MT pass does not produce; the article before `\cref` is
correct throughout.

### 4. Exercise stem — ch. 30 ex. 12 *L'énergie de point zéro* (this session)

> (a) Pour un oscillateur harmonique $E = p^2/2m + \tfrac12m\omega^2x^2$,
> prendre $\Delta x\,\Delta p = \hbar/2$ et minimiser $E \approx \dots$ par
> rapport à $\Delta x$~: montrer que $E_{\min} = \hbar\omega/2$ […] (c)
> L'hélium liquide ne gèle jamais sous la pression atmosphérique~: estimer
> l'énergie de point zéro d'un atome d'hélium localisé à …

**Verdict: native.** Infinitive imperatives (`prendre`, `minimiser`,
`montrer que`, `estimer`) — the French exercise register, and the one the
other 29 chapters already use. `par rapport à` for "over", not the calque
`sur`.

### 5. Solution header + solution — ch. 30 (this session)

> \section*{Chapitre \ref{ch:b1:quantum-introduction} --- Introduction à la
> physique quantique}
>
> $h\nu$~: \qty{100}{MHz}~: … Laser~: $1240/633 = \qty{1.96}{eV} = …$, donc
> $10^{-3}/3.1 \times 10^{-19} = 3.2 \times 10^{15}$ photons par seconde.

**Verdict: native.** Header localized, `ch:…` slug untouched; French
punctuation spacing (`~:`, `~;`) applied to the telegraphic solution style the
English uses, which is exactly what the other 29 French solution files do.

## Chapter 30 glossary (the new vocabulary this pass settled)

| English | French | Note |
|---|---|---|
| photon, Planck's constant | *photon*, *constante de Planck* | as Book 2 ch. 15 already fixed |
| photoelectric effect | *effet photoélectrique* | |
| work function | *travail d'extraction* | Book 2 term, reused |
| stopping potential | *potentiel d'arrêt* | Book 2 term, reused |
| threshold | *seuil* (`fréquence seuil`, `longueur d'onde seuil`) | |
| Compton scattering | *diffusion Compton* | |
| matter wave, de Broglie wavelength | *onde de matière*, *longueur d'onde de de Broglie* | the doubled *de de* is correct and is what Book 2 writes |
| wave–particle duality | *dualité onde--corpuscule* | |
| wavefunction, probability density | *fonction d'onde*, *densité de probabilité* | |
| uncertainty principle | *principe d'incertitude* | |
| Bohr radius | *rayon de Bohr* | |
| infinite well, ground state | *puits infini*, *état fondamental* | |
| quantized / quantization | *quantifiée* / *quantification* | **not** *quantisée* |
| energy levels, spectral lines | *niveaux d'énergie*, *raies spectrales* | |
| quantum dot | *boîte quantique* | |
| gap (of a semiconductor) | *bande interdite* | |
| hole | *trou* | in «~guillemets~» at first use, as English does |
| tunnel effect | *effet tunnel* | |
| hydrogen-like | *hydrogénoïde* | |
| zero-point energy | *énergie de point zéro* | |
| "Year 2 volume" | *volume de deuxième année* | the settled cross-volume form in all 30 chapters |

## Term-link layer

`tools/term_config/book3_fr.py` is a **curation**, not a translation of
`book3_en.py`. What it had to say that English did not:

* **`NOT_A_TERM` cannot be translated word for word.** The English default
  carries `"law of"`, which never fires because English writes *Gauss's law*,
  *Bessel's method*, *Clausius statement* — and English therefore links two
  dozen named results. French writes *loi de Gauss*, *méthode de Bessel*,
  *énoncé de Clausius*, so a literal translation of the default silently
  deletes every one of them. `"loi"`, `"lois"`, `"méthode"` and `"énoncé"` are
  deliberately absent; `"théorème"` stays, exactly as English's `"theorem"`
  does (neither edition links *théorème de Millman*). Getting this wrong cost
  88 links and 5 target labels on the first generation.
* **The French homographs**, each read in context before being stopped:
  *tension* (rope pull, chs. 12–19 / voltage, chs. 6–10 & 27 — one word, two
  definitions, no chapter order can place it), *couple* (torque / "un couple
  de forces", "le couple électron--trou"), *capacité* (capacitance / ordinary
  capacity / the head of *capacité thermique*), *solide* (rigid body, ch. 19 /
  state of matter, chs. 20–25 / the adjective), *foyer* (optical focus / the
  hearth of a boiler), *cœur* (fibre core / the Earth's, a cable's, a
  transformer's).
* **`centrale` had to be DROPped, not STOPped**: it is harvested as the
  feminine adjective of *force centrale conservative*, but on its own French
  reads it as a power station, which ch. 24 mentions on nearly every page.
* **`masse` needed no rule**, although it is the same clash English has
  between *mass* and electrical *ground*: the book never defines it bare.
* `AMBIG_POLICY = "drop"` — the university convention (books 3–5).

Result: **2 430 links, 1.04× English's 2 342**, with the same shape by target
(def 1 704, prop 324, thm 304, cor 37, ex 33, rem 20, met 8).

### Omterm target parity

Not a byte-identical set, and it cannot be: the two languages harvest their
notions from different index strings. Every divergence is accounted for.

**In English, not in French (3 labels, 6 English links):**

| Label | EN links | Why |
|---|---:|---|
| `ex:b1:systems-of-points:rolling` | 3 | EN *rolling without slipping*; the French bodies say *roule sans glisser* in the running prose, so the noun phrase *roulement sans glissement* occurs only in its own chapter. |
| `prop:b1:charged-particles:efield` | 2 | EN *accelerating voltage*; French says *tension accélératrice* only at the definition and *tension d'accélération* elsewhere. |
| `prop:b1:filters-transfer-functions:highpass1` | 1 | EN writes the full noun phrase *high-pass filter* (its one link is the loudspeaker-crossover caption); French writes the elliptic bare noun *passe-haut* on all 13 of its occurrences, so the two-word term *filtre passe-haut* appears only at its own definition. Naming bare *passe-haut* in `EXTRA` was tried and rejected: 13 links where English has 1. |

`thm:b1:electrostatics-gauss:gauss` (12 EN links) and
`thm:b1:magnetostatics:ampere` (3) were in this list too — English calls them
*laws*, French calls them *théorèmes*, and `NOT_A_TERM` ate them. Both are
restored by hand in `EXTRA`, which is why they no longer appear here.

**In French, not in English (9 labels, 25 French links):**
`mirrors-thin-lenses:lensconj` (8, from *relation de Descartes* / *relation de
Newton*), `units-dimensions:regression` (6, from *régression linéaire* /
*moindres carrés*), `electrostatics-gauss:gravity` (2, *champ de
gravitation*), `magnetostatics:three` (2, *champ d'un solénoïde* / *d'une
spire* / *d'un fil rectiligne*), `point-kinematics:harmonic` (2, *mouvement
harmonique*), `second-law-entropy:clausiuskelvin` (2, *énoncé de Clausius* /
*de Kelvin*), `charged-particles:hall` (1, *effet Hall*),
`central-forces:conics` (1, *lois de Kepler*), `systems-of-points:rotation`
(1, *liaison pivot*). Each is a notion the French bodies name with a fixed
phrase where English varies its wording; all are correct links to the right
statement, and each was checked against its target.

## Overfull boxes cleared

All six were French prose running longer than English around an unbreakable
formula or inside a fixed-width picture. None was fixed by touching
mathematics.

| File | Fix |
|---|---|
| `fr/21-fluid-statics.tex` | parenthetical moved out of the lead clause: *…ne transmet pas de force tangentielle~: la force de pression est normale, sinon le fluide s'écoulerait.* |
| `fr/23-second-law-entropy.tex` | *ne change qu'infinitésimalement* → *ne change que de façon infinitésimale* (adds a break point). |
| `fr/28-magnetostatics.tex` | two TikZ node strings shortened (*tourne pour aligner* → *tourne et aligne*; *les lignes vont du N au S* → *du N vers le S*) — the picture itself was 13 pt over. |
| `solutions/fr/03-mirrors-thin-lenses.tex` | *En différentiant Descartes* → *Différentions Descartes*. |
| `solutions/fr/08-sinusoidal-impedance.tex` | *en multipliant à l'intérieur par $C\omega$~:* → *en multipliant sous la racine par $C\omega$, il vient* — gives TeX a break before the long radical. |
| `solutions/fr/13-work-and-energy.tex` | *sous forme d'énergie cinétique en $\sigma$~:* → *en énergie cinétique à la distance $\sigma$, cela donne* — same reason. |

## Why not 100

1. **Three English link targets have no French counterpart** (6 links). Closing
   them means either naming a shorter French form, which over-links, or editing
   the prose of chapters 9, 17 and 19 to insert a noun phrase French would not
   naturally use there. Both are worse than the gap.
2. **French says *théorème* where English says *law*.** `NOT_A_TERM` is a
   substring filter, so *théorème de Gauss* and *théorème d'Ampère* have to be
   restored by hand in `EXTRA`; a future chapter that adds a linkable
   *théorème de …* will need the same manual entry, and nothing gates it.
3. **The chapter-30 register is one deliberate register-notch below the older
   French quantum chapter of Book 2.** Book 2 ch. 15 opens on a heat lamp and a
   sunburn; ch. 30 here opens on ultraviolet light and a clean metal, because
   the English canon does. That is fidelity, not a defect — but a French
   lecturer writing this chapter from scratch would probably have opened
   differently.
4. **`\index{}` keys are French but not alphabetised for French.** The index
   sorts on raw UTF-8, so *élasticité* files after *z*. English has the same
   behaviour and no edition of any book in this project fixes it; it is noted
   here so the next pass does not rediscover it.
5. **The `%` comments inside TikZ pictures stay English** across the whole
   edition (as in every other language). Invisible on the page, and changing
   them would break `id_apply`'s byte-identical guarantee for drawing code.

## For the next translator of this book

* **Write every body through `tools/id_apply.py`.** Chapter 30 is 573 lines
  and 70 ranges; three censuses caught real mistakes during this pass (a math
  span whose internal newline had moved, a range that would have changed the
  `\emph`/`\index` adjacency, a `\[` covered without its `\]`). Splitting the
  work into three range files and concatenating them into **one stanza** before
  applying is the right workflow — `id_apply` rebuilds each target file from
  English every time, so applying two stanzas for the same file in sequence
  silently discards the first.
* **Keep English line breaks exactly where they fall *inside* math spans.**
  The math census compares span text including its newlines.
* **`\qty{}{}` arguments must stay ASCII.** `dB/décade` is the trap in this
  book; the tree is clean of it now.
* **Generate the links only after the last body is written**, and check the
  count against English before believing the config: an empty
  `book3_fr.py` produced 3 968 links (1.7×), and the difference between that
  and 2 430 is entirely `STOP`/`DROP` curation.
