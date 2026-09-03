# One Physics Book 5 (University, Year 3) — French edition: self-score

**Date:** 2026-09-03
**Quality bar:** *native academic French* (the bar of `translation_instruction.md`).
**Sense/structure reference:** the English canon (`parts/bachelor-3/*.tex` and
`parts/bachelor-3/solutions/*.tex`), followed line-range by line-range through
`tools/id_apply.py`; no `--force-classes` anywhere in the book.
**Register comparands:** the shipped French Books 3 and 4
(`parts/bachelor-1/fr/`, `parts/bachelor-2/fr/`) — used not only for
terminology but, after the coordinator's question, for the *instruction
register* itself (see "Register: the Book 4 twin" below), and
`../one-math-book/parts/bachelor-1/fr/` for the lecture voice.

## Overall: **96 / 100**

| Dimension | Score | Note |
|---|---:|---|
| **Register** (academic French, weighted) | **95** | Now the exact three-way split of the shipped French Book 4: **infinitive** in exercise, problem and `method` instructions (*Montrer que…*, *Calculer…*, *Vérifier…*, *En déduire…*), **imperative-vous** in reader-addressing narrative (*Glissez une feuille de plastique…*, *Chauffez de l'eau d'un degré…*, *Pointez un radiotélescope…*), **first-person plural** in proofs (*Posons…*, *Développons…*, *Multiplions…*). French punctuation spacing (`~:`, `~;`, `~?`, `~!`) and «~guillemets~» throughout. Not a 96: the whole book was first written in imperative-vous and only converted after the coordinator asked; the split is right now, but it was not designed in. |
| **Terminology** (weighted) | **96** | All 302 `\index{}` calls are French and each equals its visible term; 297 distinct keys against English's 297. Checked against the shipped French Books 3–4: *pression de dégénérescence*, *bande interdite*, *paramètre d'ordre*, *vallée de stabilité*, *séquence principale*, *zone de déplétion*, *fond diffus cosmologique*, *masse invariante*, *nombre baryonique*. No sense swaps found on sampling. |
| **MT-artifact freedom** (weighted) | **92** | The shipped tree is clean: gate 9 returns **0 multi-word `text` fragments**, `check_orphan_lines.py` returns **0**, and every `\text{…}` span in the book holds French. But it got there late. Twenty-four visible-prose fragments survived the *first* clean full build — 3 `[Partial proof]` titles, 4 `\text{…}` spans inside frozen displays, 14 English `\text{}` subscripts (`\text{iron}`, `\text{nucleus}`, `\text{proper}`, `\text{Earth}`, …) and 1 orphan English line — and the last 15 of those were found by the coordinator, not by me. |
| Structure | **98** | `check_translation.sh bachelor-3 fr` **PASSED**. All 54 files written as line-range replacements on the English canon through `id_apply.py`. **One** per-range opt-out in the whole book, `@@ 57-58 !draw` in `15-scattering-theory.tex` — justified below. |
| LaTeX hygiene | **100** | 0 errors, 0 undefined references, **0 overfull boxes** (EN 0), 0 "invalid in math mode", 0 TeX accent escapes, 0 non-ASCII inside `\qty{}`/`\unit{}`/`\num{}`, 0 line-continuation `%`. |
| Cross-references | **100** | The ordered `\label{}` multiset is **byte-identical** to English: 621 labels, the diff of the two sorted lists is empty. `\ref`/`\cref` slugs untouched; solution headers localised to `\section*{Chapitre \ref{ch:…} --- <titre>}`. |
| Figures | **98** | 118 `omfigure`, 82 `tikzpicture`, 36 `includegraphics` — identical to English. Drawing code byte-identical (enforced by `id_apply`'s `draw` census on 53 of the 54 files); only node text, `\addlegendentry{}`, axis labels and `{\small …}` captions translated. All 11 prose-bearing legend sites of the coordinator's Census 2 are French. |
| Solutions | **98** | All 27 solution files translated; `\textbf{n.}` numbering and every number, unit and symbol preserved; 25-item weekend answers complete in every chapter. |
| Defined-term links | **96** | **981** `\omterm` links against English's 916 (**1.07×**), after three French-only homograph collisions were found and closed (45 wrong links removed — see below). Every one of English's 100 target labels is still reached; French additionally reaches 9 (109 used). The residual 1.07× is prose length. |

**Overall 96**, weighted toward register, terminology and MT-artifact freedom.
Measured on the tree **as it stands after the last edit**: after the
coordinator's 15 defects and the 9 further English `\text{}` spans I found
alongside them, after the register conversion and the narrative restoration,
after the homograph census and the final `--unwrap`/`--apply`/`--check` link
cycle, and after the
rebuild that followed all of it.

## Register: the Book 4 twin

The coordinator asked which register the exercise stems use and whether it
matches `parts/bachelor-2/fr`. The honest first answer was **no**. The book
was drafted with the *imperative-vous* (`Montrez que…`, `Calculez…`), and the
French Books 3 and 4 do not use it there: `parts/bachelor-2/fr` contains 77
`-ez` tokens in the whole volume (mostly *assez*, *nez*, *chez*) against 123
`(a) <Infinitif>` exercise stems, and `parts/bachelor-1/fr` 33 against 11.
Book 5 fr had ~1 900 imperative forms. That is a total mismatch, so it was
converted. What Book 4 fr actually does, and what Book 5 fr now does:

| Context | Book 4 fr | Book 5 fr (now) |
|---|---|---|
| exercise / problem instructions | infinitive — *Montrer que…*, *comparer…*, *vérifier…* | infinitive — **Montrer 98**, Calculer 55, Vérifier 23, Écrire 22, Comparer 20, Expliquer 19… |
| `method` steps | infinitive — *Lister les ordres…*, *ajouter…* | infinitive — *Compter les modes…*, *les occuper avec…*, *intégrer* |
| proofs | first-person plural — *Appliquons…*, *Différentions…* | first-person plural — *Posons…*, *Développons…*, *Multiplions…*, *Remplissons…*, *Résolvons…* |
| chapter openings, reader-addressing narrative | imperative-vous — *Regardez une roue de bicyclette…*, *Inclinez un disque compact…* | imperative-vous — *Glissez une feuille de plastique…*, *Chauffez de l'eau d'un degré…*, *Pointez un radiotélescope…*, *Dépouillez la matière…* |

The conversion was scripted with an explicit irregular-verb table
(*écrivez→écrire*, *obtenez→obtenir*, *déduisez→déduire*, *convertissez→
convertir*, *résolvez→résoudre*, …), a protected list for the genuine
second-person narration Book 4 also keeps (*vous avez jamais touché*, *vous
entendez deux chocs*, *vous construisez un télescope*), and a rule for the
~150 clitic imperatives (*Déduisez-en* → *En déduire*, *évaluez-la* →
*l'évaluer*, *rappelez-vous* → *rappeler*, *servez-vous-en* → *s'en servir*).
Then **32 narrative sites** that the sweep had over-converted were restored
to the imperative by hand, and **5 proof openings** put into the *nous* form.
Residual imperative forms in instructions: **0**. Subject infinitives that
were already correct were left alone (*Mesurer une tige en mouvement, c'est
repérer…*, *Échanger deux particules identiques ne doit rien changer*,
*Compter les états quantiques… donne*, *Joindre des noyaux légers paie…*).

## Build gates

Measured with `grep -a`: pdfTeX writes the log as ISO-8859, and a plain
`grep -c` treats it as binary, prints nothing and exits 1 — which reads as
"0" and is not a count.

| Gate | Result |
|---|---|
| `.fls` honesty check (`grep -o 'parts/bachelor-3/\(solutions/\)\?fr/[^ ]*' … \| sort -u \| wc -l`) | **54 / 54** — the build really reads the French tree |
| `bash tools/check_translation.sh bachelor-3 fr` | **PASSED** |
| `python3 tools/check_orphan_lines.py …` | **0** |
| `latexmk -g one_physics_book_5_university_year_3_fr.tex` | exit 0, **323 pages** (EN 302) |
| `grep -ac '^!'` | **0** |
| `grep -aci 'undefined'` | **0** |
| `grep -ac 'Overfull'` | **0** (EN 0) |
| `grep -ac 'invalid in math mode'` | **0** |
| `grep -ac 'nullfont'` | **10** — exactly the English baseline; a *rise* above 10 would mean a non-ASCII character reached a `\qty{}`/`\unit{}`/`\num{}` argument |
| `grep -ac 'Underfull'` | 36 — the series norm |
| `python3 tools/check_latin_prose.py` (gate 9) | 85 hits: **0 multi-word `text`**, 1 multi-word `node` (a proper name), 1 `title`, 83 one-word cognates |
| French elision sweep (three greps, **run after the last edit**) | **0 / 0 / 0** |
| `grep -rnP "\\\\['\`^\"~=.]\{?[a-zA-Z]"` (gate 6, TeX accent escapes) | **0** — the 11 the English canon carried are UTF-8 here (*Panthéon*, *Segrè*, *Ampère* ×3, *ångström* ×4, *Ørsted*) |
| `python3 tools/link_defined_terms.py --book 5 --lang fr --check` | every file matches what the config generates |

### Structural parity with the English canon

| Quantity | French | English |
|---|---:|---:|
| files | 54 | 54 |
| `\label{}` (ordered multiset) | 621 | 621 — **identical** |
| `\index{}` calls / distinct keys | 302 / 297 | 302 / 297 |
| environment optional titles | 622 | 622 |
| `\text{…}` spans | 1 682 | 1 682 |
| `omfigure` / `tikzpicture` / `includegraphics` | 118 / 82 / 36 | 118 / 82 / 36 |
| `\omterm` links / distinct targets | 981 / 109 | 916 / 100 |

### The French elision sweep

The one defect class that is French-only and invisible to every automatic
gate: a line ending on an apostrophe, on a hyphen inside a compound, or
beginning with punctuation renders with a spurious space (`l’ hydrogène`,
`demi- micromètre`). Three greps over all 54 files, run after the last edit:

```
grep -rnP "['’]\s*$"                      → 0
grep -rnE "^\s*([.,;:)?!]|~[;:?!])"       → 0   (TikZ `.. controls` excluded)
grep -rnE "[a-zà-ÿ]-\s*$"                 → 0
```

Two real hits were found and **rewrapped, never patched with a trailing `%`**:
`11-hydrogen-atom.tex` (`un demi-\nmicromètre`) and, earlier in the run,
`14-identical-particles.tex` (`doivent-\nelles`). The tree contains zero
line-continuation `%`.

### Gate 9 in detail

| Class | Hits | Verdict |
|---|---:|---|
| `text` (multi-word) | **0** | — |
| `node` (multi-word) | 1 | `23-crystalline-solids.tex` `van der Waals $\sim -1/r^6$` — a proper name plus mathematics. |
| `title` | 1 | `26-particle-physics.tex` `Leptons, quarks, hadrons` — the three words are spelt identically in French. |
| `node-1word` | 21 | True cognates and mathematics: `libration`, `rotation`, `translation`, `saturation`, `positronium`, `continuum $\rho(E)$`, `section $S$, $\sigma = F/S$`, `face $\perp x$`. |
| `text-1word` | 62 | Math subscripts French spells the same or standard abbreviations: `\text{orb}`, `\text{osc}`, `\text{boson}`, `\text{fermion}`, `\text{singlet}`, `\text{eff}`, `\text{vib}`, `\text{rms}`, `\text{gap}`. |

## Homograph collisions: the morphology census

The coordinator's Dutch case (*ket* inflected to *keten*, the ordinary word
for *chain*, 38 wrong links) generalises, and French has the same disease in
a worse form: it pluralises in `-s`, and it has **one word where English has
two**. Counting the generated `\omterm` surface forms per target and dividing
by the English twin's count found three collisions that no gate, no census and
no build can see, because every wrong link is a well-formed link to a real
label:

| French term | wrongly linked to | wrong links | why English never collides |
|---|---|---:|---|
| **contrainte** | `def:b3:lagrangian-mechanics:coordinates` (ch. 1 *constraint*) | **27**, all in chapter 3, where the word means *stress* — including the definition line `\emph{tenseur des \omterm{…coordinates}{contraintes}}`, i.e. the **stress tensor** pointing at *generalized coordinates* | English says *constraint* and *stress* |
| **dilatation** | `def:b3:continuum-elasticity:strain` (ch. 3 elastic dilatation) | **5** — *dilatation du temps* (ch. 4, ×3) and *dilatation thermique* (chs. 16, 23) | English says *dilation*, *expansion*, *strain* |
| **bras** | `def:b3:quantum-formalism:state` (Dirac *bra*) | **3** — the spiral **arms** of a galaxy (chs. 12, 27) and *bras de fer* (ch. 14); the French plural of *bra* **is** the word for *arms* | English never links *bras* at all |

All three are now in `STOP`, which keeps a term linked inside the chapter that
defines it and nowhere else. The result is exactly right: chapter 1 keeps its
8 *contrainte* links, chapter 3 keeps its 4 *dilatation* links and gains
nothing false, chapter 3's stress still links through the multi-word terms
*tenseur des contraintes* / *vecteur contrainte*, chapter 4 keeps its 18
*dilatation du temps* links to `prop:b3:relativistic-kinematics:dilation`, and
*bras* links nowhere. The cost is ~10 legitimate cross-chapter *contrainte*
links in chapters 2, 9 and 16 — a density loss taken deliberately to buy a
correctness gain.

Total links fell 1 026 → **981** (1.12× → **1.07×** English). The nine targets
French reaches and English does not were re-checked and are **not** collisions:
they are named results whose French rendering recurs where English paraphrased
(*règle de Born*, *théorème de Liouville*, *règle d'or de Fermi*, *théorème de
Noether*, *principe d'exclusion de Pauli*, *liaison covalente* / *métallique*,
*théorème spin--statistique*, *composition des vitesses*). Worst remaining
ratio: 2.33× on a 7-link target (*moment conjugué*, a genuine term English
does not link).

## The single opt-out: `15-scattering-theory.tex`, `@@ 57-58 !draw`

`id_apply.py`'s `draw` census blanks node text with

```python
NODE_TEXT = re.compile(r"node\s*(\[[^\]]*\])?\s*(\([^)]*\))?\s*(at\s*\([^)]*\))?\s*\{")
```

The `at\s*\([^)]*\)` group stops at the **first** closing parenthesis, so it
cannot match a `calc`-library coordinate that itself contains parentheses.
The detector label of the scattering figure is exactly that:

```latex
\node[omProp, anchor=west, font=\footnotesize] at ($(35:3.4)+(0.25,0)$)
  {detector, $\dd\Omega$};
```

The census therefore refuses to blank `{detector, $\dd\Omega$}`, and a
translation of those two lines fails the `draw` check even though nothing but
the label changed. The range-scoped `!draw` was taken in preference to leaving
the label in English or to a file-wide `--force-classes draw`. The two
opted-out lines were then diffed by hand against English: coordinates,
options and `rotate around` are byte-identical; only `detector` became
`détecteur`.

## Sampled passages (verdicts)

**1. `01-lagrangian-mechanics.tex`, chapter opening — *native*.**

> Les forces qui tiennent un système --- tiges, rails, articulations --- ne
> travaillent pas, et pourtant la méthode de Newton nous oblige à les traîner
> dans tout le calcul.

Idiomatic verb choice (*traîner*), French apposition dashes, no calque of
"drag them through".

**2. `19-quantum-statistics.tex`, theorem body — *native*.**

> À $0 < T \ll T_{\text{F}} = E_{\text{F}}/k_{\text{B}}$, seuls les électrons
> situés à $\sim k_{\text{B}}T$ de la surface de cette \emph{mer de Fermi}
> peuvent répondre à quoi que ce soit~: la fraction $\sim T/T_{\text{F}}$ est
> la clé maîtresse du comportement métallique.

*Clé maîtresse*, *à quoi que ce soit* — the French idiom, not the English shape.

**3. `22-electromagnetism-in-matter.tex`, chapter opening — *native*, and the
register model.**

> Glissez une feuille de plastique entre les armatures d'un condensateur
> chargé et la tension chute, comme si de la charge était apparue de nulle
> part.

Imperative-vous, exactly as `parts/bachelor-2/fr` opens its chapters
(*Inclinez un disque compact sous une lampe…*).

**4. `25-nuclear-physics.tex`, exercise 2 — *native*, infinitive register.**

> La densité universelle. (a) À partir de $R = r_0A^{1/3}$, montrer que la
> densité nucléaire est indépendante de $A$ et l'évaluer.

The Book 4 fr stem shape, including the clitic infinitive *l'évaluer* where
the draft had *évaluez-la*.

**5. `27-astrophysics.tex`, chapter opening — *near-native*.**

> l'univers lui-même est un système thermique en refroidissement dont la
> photographie de nourrisson --- le fond diffus cosmologique --- est le corps
> noir le plus parfait jamais mesuré.

*Photographie de nourrisson* is faithful and readable, but a French
astrophysicist would more likely write *la photographie de l'univers enfant*.
Understood on first reading; slightly translated in feel. This is the register
ceiling.

## Why not 100

1. **Twenty-four English fragments survived the first clean build**, and the
   coordinator found 15 of them. Three `[Partial proof]` optional titles
   (ch. 20, 21, 22), four `\text{…}` prose spans frozen inside `\[…\]`
   (`(and cyclic)`, `integer spin`, `half-integer spin`, `(dilute gas)`),
   fourteen English `\text{}` subscripts (`\text{iron}`, `\text{nucleus}`,
   `\text{atom}`, `\text{proper}`, `\text{Earth}`, `\text{free}`,
   `\text{system}`, `\text{hence}`, `\text{then}`) and one orphan English line
   (`06-covariant-electromagnetism.tex`, *"wire's line charge in the new frame
   is"*). All are fixed; nine more that the coordinator's list did not include
   were found in the same sweep and fixed too (`\text{liquid}`,
   `\text{vapour}`, `\text{ideal}`, `\text{gas}`, `\text{peak}`,
   `\text{folded}`, `\text{chain}`, `\text{band}`, `\text{molar}`). The
   process failed before the gates did.
2. **The instruction register was wrong for the whole first draft** and was
   corrected only after the coordinator asked. It is right now, and verified
   verb by verb against `parts/bachelor-2/fr`, but a book should not need a
   1 900-form sweep at the end.
3. **Three homograph collisions shipped 45 wrong links** through every green
   gate (*contrainte*, *dilatation*, *bras*), and I only looked for them after
   the coordinator described the Dutch *keten* case and named the method. The
   surface-form frequency table against the English twin should be a standing
   step, not a rescue.
4. **One `!draw` opt-out** where the tool should not have needed one.
6. **Two overfull boxes needed rewording**, not just rewrapping (the Liouville
   proof's velocity-field sentence gained *le couple*; the Rutherford
   paragraph gained *au potentiel en*), and one section title was shortened
   (*et l'hydrogène* for *et l'atome d'hydrogène*) to clear 2.5 pt.

## Cross-edition findings (reported to the coordinator)

* **`NODE_TEXT` cannot match a `calc` coordinate.** Affects every edition at
  `15-scattering-theory.tex:57--58`; each will need the same range-scoped
  `!draw`, or the regex fixed once in `tools/id_apply.py`.
* **Unnamed-line English is invisible to every gate but gate 9 and the new
  orphan check.** Book 5's English has three `[Partial proof]` optional titles
  (ch. 20, 21, 22) one line above their proof bodies, and four prose
  `\text{…}` spans inside displays (ch. 10 `(and cyclic)`, ch. 14
  `integer spin` / `half-integer spin`, ch. 18 `(dilute gas)`).
* **English `\text{}` subscripts are the largest silent class.** Gate 9 buries
  them in tier-2 one-word noise. The productive census is the coordinator's:
  diff each edition's `\text{}` contents against the English twin and keep
  only the words that are not words of the target language. In this edition
  that census found 23 sites; every structural gate was green throughout.
* **Morphology can invent a homograph, and the only detector is the
  frequency table.** French needed three `STOP` entries English needs none of;
  the census that finds them is: count `\omterm` surface forms per target,
  divide by the English twin's count, and read every target whose ratio is
  implausible. Romance and Germanic editions should all run it — *contrainte*
  (constraint/stress) and *dilatation* (strain/dilation/expansion) are one
  word in Spanish, Portuguese and Italian too.
* **The canon's TeX accent escapes were a French problem above all.** Zero
  remain in this edition — the 11 sites (*Panthéon*, *Segrè*, *Ampère* ×3,
  *ångström* ×4, *Ørsted*) were written UTF-8 when the ranges were translated,
  which is why gate 6 never fired here.
* **Instruction register is not checked by anything.** Books 3 and 4 fr are
  infinitive in exercises and imperative-vous in narrative; nothing in the
  toolchain compares a new edition against its own Book 4 twin, and a
  uniformly-imperative book passes every gate. A one-line count
  (`grep -c '(a) [A-Z][a-zéè]*ez'` against `(a) [A-Z][a-zéè]*er`) would have
  caught it on day one, in any Romance edition.
