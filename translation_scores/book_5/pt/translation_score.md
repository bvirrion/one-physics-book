# One Physics Book 5 (University, Year 3) --- Portuguese edition: self-score

**Date:** 2026-09-03
**Variety:** Brazilian Portuguese (`pt` = pt-BR across the whole series).
**Quality bar:** *native academic* (the bar of `translation_instruction.md`) ---
prose a Brazilian physics lecturer would have written, not prose a Brazilian
physicist can decode.
**Sense/structure reference:** the English canon (`parts/bachelor-3/*.tex`) for
content, labels and every formula; the Portuguese Book 4
(`parts/bachelor-2/pt/`) for the university register, the settled glossary and
the term-link conventions (`AMBIG_POLICY = "drop"`). The six sibling editions
of this same book were being written concurrently in the same working tree and
were **not** consulted.

## Overall: **96 / 100**

| Dimension | Score | Note |
|---|---:|---|
| Register (academic Brazilian Portuguese, weighted) | 96 | Narrative present in the chapter openings, impersonal-imperative in methods and exercise stems (*calcule*, *mostre*, *deduza*, *estime*, *compare*, *explique*) --- the same 3rd-person imperative without the pronoun that `parts/bachelor-2/pt` uses, and no `-se` passive imperative in either. Subject pronouns dropped: **0** occurrences of the MT tell *"Nós temos / Nós podemos / Nós vamos"* across the 54 files. Direct address (*você*, *o seu vizinho*) only where English addresses the reader, exactly as Book 4 pt does. |
| Terminology (weighted) | 96 | Glossary below, continuous with Book 4 pt. All 302 `\index{}` calls resolve to **297 distinct Portuguese keys --- the English count exactly**; the only five keys left byte-identical to English are *bra*, *ket*, *spin*, *metal*, *quark*, *supernova* (Portuguese spells them the same). |
| MT-artifact freedom (weighted) | 95 | Gate 9 over all 54 files: **0 title hits, 0 multi-word (tier-1) hits**. The 58 remaining hits are all one-word true cognates or Portuguese abbreviations (*orb*, *rot*, *lab*, *exc*, *osc*, *loc*, *esc*, *vap*, *vib*, *liq*, *fus*, *conf*, *sep*, *nuc*, *grav*, *molar*, *ideal*, *total*, *extra*, *spin*, and the nodes *face $\perp x$*, *$\varphi$ real*, *quarks*, *metal*). The coordinator's sharper census (`\text{}` contents byte-identical to English), **re-run over bodies *and* solutions** after its first pass was found to have read only the chapter bodies, reports Portuguese **clean**: `const`, `ideal`, `molar`, `total`, `spin`, `Coulomb`, `(Dulong--Petit)` and the abbreviations `conf`, `grav`, `e,crit` --- correct Portuguese, proper names, or standard abbreviations. |
| Structure | 100 | `check_translation.sh bachelor-3 pt` green. All 54 files written as line-range replacements on the English canon through `tools/id_apply.py`, so labels, `\cref` targets, solution keys, every math span, every `\qty{}{}`/`\num{}`/`\unit{}` and all drawing code are byte-identical to English. 27 chapters, 324 exercises, 27 weekend problems, 351 solutions --- the English counts exactly. `\text{}` count 1 682 and environment optional titles 754: both identical to English. |
| LaTeX hygiene | 100 | 0 errors, 0 undefined references, **0 overfull boxes**, 0 *"invalid in math mode"*; nullfont **10**, i.e. the English build's own baseline, not one above it. UTF-8 accents only; no non-ASCII character inside any `\qty{}`/`\unit{}`/`\num{}` argument. |
| Cross-references | 100 | Every `\cref`/`\ref` target byte-identical to English; 12 exercises + 1 weekend problem per chapter, one solution each, keyed by the English labels. |
| Figures | 97 | Drawing code untouched; only node text, axis labels, `\legend`/`\addlegendentry` and captions translated. All 11 prose-bearing legend sites of the coordinator's Census 2 are translated (chs. 1, 10, 14, 18, 20, 21); all 49 `\foreach` lists left byte-identical per Census 3. Not 100 because four figure strings are legitimately untranslatable single words (see below). |
| Solutions | 96 | All 27 solution files translated; `\textbf{n.}` numbering and every number, unit and formula preserved. |
| Term links | 96 | **970 links over 103 targets** against English's 916 over 100 (1.06x). **Every one of English's 100 targets is reached**; the three extra are explained below. Includes the *dilatação* homograph fix (three wrong links removed) described under "The term-link curation". |

## What was produced in this run

- 27 chapter bodies and 27 solution files in `parts/bachelor-3/pt/` and
  `parts/bachelor-3/solutions/pt/`, drafted chapter-by-chapter (body, then its
  solutions twin, then `id_apply` green before starting the next).
- `tools/term_config/book5_pt.py` --- curated from this edition's own harvested
  term list against `book5_en.py`, replacing the `book4_pt.py` seed.
- This score file.

Nothing outside those paths was edited. `one_physics_book_5_university_year_3_pt.tex`
and `frontmatter/image-credits-book5.pt.tex` were read and found correct; they
needed no change.

## Checks

```
bash tools/check_translation.sh bachelor-3 pt        -> TRANSLATION GATE: PASSED
python3 tools/check_orphan_lines.py parts/bachelor-3/pt parts/bachelor-3/solutions/pt
                                                     -> orphan English lines: 0
python3 tools/check_latin_prose.py parts/bachelor-3/pt parts/bachelor-3/solutions/pt
                                                     -> 0 title, 0 multi-word; 58 one-word cognates
python3 tools/link_defined_terms.py --book 5 --lang pt --check
                                                     -> CHECK: every file matches
latexmk -g one_physics_book_5_university_year_3_pt.tex
  grep -ac '^!'                   -> 0
  grep -aci undefined             -> 0
  grep -ac Overfull               -> 0        (316 pages; English 302; fr 323, nl 320, es 322)
  grep -ac 'invalid in math mode' -> 0
  grep -ac nullfont               -> 10       (identical in the English build:
                                               a shared style-file artifact,
                                               not a defect)
  distinct pt sources in the .fls -> 54       (27 + 27: the book really is
                                               reading the Portuguese tree)
```

The `.fls` count is the honesty check: a missing translated file would fall
back to English and still build green, so 54/54 is what proves the Portuguese
tree is the one being typeset.

## The term-link curation

`book5_pt.py` was rebuilt rather than inherited. What the audit found:

- **`STOP` was a five-word Book 4 carryover** (*absorção*, *eficiência*,
  *estacionário*, *laser*, *limiar*). Re-running the harvest with `STOP`
  emptied showed Book 5 defines none of them: the entries were inert, not
  masking, and were dropped. The seed also carried *buraco* and *lacuna* for
  English's STOPped *hole*; neither is harvested either (the semiconductor
  hole is `\emph{lacuna}` in two definitions, so `AMBIG_POLICY = "drop"`
  already removes it, and *buraco* only occurs inside *buraco negro*). The
  four that do change the harvest --- *spin*, *metal*, *evento*, *observável*
  --- are kept, matching `book5_en.py` word for word.
- **`NOT_A_TERM` had to be translated**, and the `"law of"` entry deliberately
  *not*: `harvest.py` tests plain substring containment, so a literal
  *"lei de"* would have deleted every named-law link in the book (Planck's,
  Bragg's, Hubble's, Hooke's, Curie--Weiss) with no gate complaint. Translating
  the rest cost one target (*princípio de exclusão de Pauli*,
  `cor:b3:identical-particles:pauli`) --- which is exactly what English's
  `"principle"` costs the English edition, so this is parity, not loss.
- **`EXTRA` stays empty, and this was checked rather than assumed**: the
  Portuguese harvest reaches every target the English harvest reaches (and
  nine more), so there is no English link this edition cannot make.
- **`MAX_TERM_WORDS`/`MAX_TERM_CHARS` deliberately absent.** Book 4 set 5/40
  because `book4_en.py` did; `book5_en.py` sets neither, and a cap here would
  drop Portuguese terms the English edition keeps.
- **`DERIVED`**: nine stem-changing plurals (`-ão` -> `-ões`, `-al` -> `-ais`)
  that `lang_pt.py`'s per-word tail `(?:e?s)?` cannot produce, each verified to
  occur with word boundaries in this edition's own corpus.
- **`EXTRA_PROTECT`**: two Portuguese collocations English cannot produce.
  *ação* is a Book 5 term (the Lagrangian action of ch. 1) and English links
  *action* too --- but the English canon writes *at work* where this edition
  writes **em ação** (eleven sites, chs. 5--26, none of them the action), so
  without the guard the edition would carry eleven links English does not have.
  *rede* is the crystal lattice of ch. 23, and **rede de cinco fendas** (a
  diffraction grating, in ch. 23's own solutions) is the other sense sitting
  inside the defining chapter, where a `STOP` would not have protected it.

- **`STOP` gained a fifth entry after delivery: *dilatação*.** This is the one
  real defect the first pass shipped, and no gate in the repository could see
  it: the link was well-formed, the word was real Portuguese, and the twin
  comparison compares *text*, not *targets*. English splits the sense three
  ways --- *strain*, *dilation*, *expansion* --- and never links *dilatation*
  to the strain target at all; Portuguese has one word, so `lang_pt.py`
  morphology pointed all three senses at `def:b3:continuum-elasticity:strain`:
  nine occurrences against English's three. Six were the strain sense; three
  were **wrong**:

      pt/04-relativistic-kinematics.tex:294            -> TIME dilation
      pt/04-relativistic-kinematics.tex:592            -> TIME dilation
      solutions/pt/16-microcanonical-ensemble.tex:167  -> THERMAL expansion

  The frequency census (a target linked far more often than its English twin)
  is what surfaced it; credit to the French agent, which predicted the
  collision for Portuguese from its own.

Result: **970 links, 103 targets, all 100 of English's reached.** The three
extra (`ex:b3:lagrangian-mechanics:hoop`,
`prop:b3:relativistic-kinematics:addition`, `rem:b3:crystalline-solids:bonds`)
are places where the Portuguese wording of a definition happens to be a cleaner
noun phrase than the English one and so harvests where English does not.

### What the *dilatação* `STOP` actually did (verified, not assumed)

`STOP` is documented as unreliable in both directions, so both halves were
checked against the regenerated tree rather than inferred:

- **The defining chapter kept its links.** All three chapter-3 *dilatação*
  links survive (`pt/03:47`, `pt/03:308`, `solutions/pt/03:17`), together with
  the two *tensor de deformações* and one *campo de deslocamentos* links that
  mirror English exactly. The target goes 9 -> 6.
- **The three wrong sites are now unlinked --- they were NOT redirected.**
  This is worth stating plainly because the suggested fix assumed redirection:
  the term that carries `prop:b3:relativistic-kinematics:dilation` is the
  two-word *dilatação do tempo*, and none of the three sites writes those
  words (they read `(dilatação)`, `dilatação \emph{experimental}` and
  `(dilatação térmica)`). The time-dilation target's count is **29 before and
  29 after**, unchanged.
  Unlinking is nevertheless the *correct* outcome and not a loss: English
  links none of those three sites either, so redirection would have added
  three links English does not have.
- **Nothing else moved.** The regenerated totals differ only in `def`
  (594 -> 591); `prop` 210, `thm` 129, `ex` 30, `rem` 10 are identical, and
  `--check` is green.
- **The residual 6-vs-3 gap on the strain target is density, not collision.**
  English's three links there are *strain tensor* x2 and *displacement field*
  x1; Portuguese mirrors those three and adds three correct-sense *dilatação*
  links inside the defining chapter, a word English simply never links.

Two further suspects flagged by the census were checked and left alone, since
a high count is a style difference and only a wrong target is a defect:
`prop:b3:spin-two-level:rabi` (9 vs 4) and `prop:b3:nuclear-physics:binding`
(5 vs 3) are places where this edition repeats *ressonância magnética* and
*energia de ligação* in full where the English writes "it" or "the gap".

The canon's 11 inherited TeX accent escapes (`Panth\'eon`, `Segr\`e`,
`Amp\`ere`, `\aa ngstr\"om`, `\O rsted`) were checked for in this tree:
`grep -rnP "\\\\['\`^\"~=.]\{?[a-zA-Z]"` over all 54 files returns **0
files** --- every one was already rewritten as a UTF-8 Portuguese form during
drafting.

## Sampled passages, verdicted

**1. Ch. 9 opening (course prose) --- native.**

> Quase nada na natureza é exatamente um oscilador harmônico, e quase tudo é
> aproximadamente um: qualquer sistema afastado de um equilíbrio estável --- a
> ligação de uma molécula, um átomo num cristal, uma ponte, um modo do campo
> eletromagnético --- sente uma força restauradora proporcional ao
> deslocamento, porque todo potencial suave é uma parábola no fundo do seu poço.

Reads as originally-composed Brazilian academic prose: *afastado de um
equilíbrio estável* for "nudged from stable equilibrium" is idiomatic rather
than glossed, and the em-dash apposition is rebuilt around Portuguese word
order, not carried over.

**2. Ch. 21, Landau theory (technical exposition) --- native.**

> Acima de $T_{\text{c}}$: um único poço em $m = 0$. Abaixo: a origem vira um
> cume e aparecem dois poços simétricos [...] --- a mesma raiz quadrada do campo
> médio, agora só por simetria.

*a origem vira um cume* keeps the register informal-but-precise exactly as the
English "the origin becomes a summit" does; *campo médio* is the settled
Brazilian term.

**3. Ch. 22 weekend problem (imperative register) --- native.**

> Modele o circuito: caminho de ferro $\ell = \qty{1.2}{m}$, [...] Escreva a lei
> de Ampère para $H$ ao longo do laço.

Bare 3rd-person imperative, the same stem form `parts/bachelor-2/pt` uses.

**4. Ch. 25 solutions, item 12 (dense numerical prose) --- native.**

> $\hbar$ (a pressão é quântica), $c$ (o amolecimento relativístico dela), $G$
> (o adversário): um número do tamanho de uma estrela construído com três
> constantes microscópicas.

The English possessive "its relativistic softening" becomes *o amolecimento
relativístico dela* --- the Portuguese solution to a construction that has no
direct equivalent, not a calque.

**5. Ch. 18 opening --- near-native.** *"a moeda que se equilibra"* for "the
currency being balanced" is correct and idiomatic, but a Brazilian author
might have written *"a moeda em disputa"*; the sentence is slightly more
literal than the rest of the edition. One of a handful of places where the
English sentence shape shows through.

## Cross-cutting findings (worth the cohort's attention)

1. **`\index{}` keys were untranslated in ten chapters and nothing caught it.**
   Chapters 18--27 (and two stragglers in 8 and 12) carried 131 English index
   keys into the Portuguese tree: they sit on their own lines, usually just
   after `\label`, so any patch range that starts at the first prose line skips
   them --- and `id_apply` only counts `\index` calls, `check_translation.sh`
   never looks at them, and gate 9 does not read them either. The printed index
   would have been half English. All 131 were translated after the fact; the
   edition now has 297 distinct keys, the English count exactly. **Every other
   edition of this book should run
   `comm -12 <(grep -o '\index{[^}]*}' EN|sort -u) <(grep -o '\index{[^}]*}' PT|sort -u)`
   per file before scoring.**
2. **One orphan English line**, found by the coordinator's
   `check_orphan_lines.py`: `21-phase-transitions.tex:108`, where the
   Portuguese sentence had absorbed the sense of the next English line and that
   line then fell outside every range. Fixed; the gate is now 0. This is the
   Spanish agent's defect class and it is real.
3. **Six English `\qty{}{}` unit arguments** (coordinator's Census 1): the
   three `atoms/m^3` inside math spans were kept byte-identical in the patch
   and then post-edited to `m^{-3}` with the word carried into the surrounding
   Portuguese prose (*densidade atômica*, *átomos*); `euros` is the Portuguese
   plural too, so the three euro sites needed no change at all.
4. **Homograph collisions in `lang_<x>.py` morphology are invisible to every
   gate in the repository.** Portuguese *dilatação* covers English's *strain*,
   *dilation* and *expansion*, so three links landed on the wrong sense with a
   perfectly well-formed `\omterm`, a real word, and a green build. Nothing in
   `check_translation.sh`, gate 9, the twin comparison or `id_apply`'s eleven
   censuses can see it. **The only detector is a per-target link-count diff
   against the English twin**; every edition should run one before scoring, and
   any target running well above its English count deserves a look at the
   actual display texts (high density is fine, a wrong sense is not).
5. **`\text{}` subscripts are invisible to every structural census** (the math
   census blanks them), so English ones survive a green `id_apply`. Fourteen
   were caught by gate 9 and fixed here: `system`/`sys`, `liquid`/`vapour`,
   `folded`, `states`, `rest`, `then`, `band`/`chain`, `singlet`/`triplet`,
   `iron`/`gap`, `peak`, `atom`, `nucleus`, `free`, `proper`, `Earth`.

## Why not 100

- **The four figure strings that stay English-shaped.** `face $\perp x$`,
  `$\varphi$ real`, the `quarks` row label and the `metal` band label are each a
  single word that Portuguese spells identically; gate 9 will keep reporting
  them forever, and no reader is harmed, but the edition cannot claim a clean
  twin-comparison gate.
- **Register drift in a handful of chapter openings** (sample 5 above). The
  translated openings are correct and idiomatic but occasionally track the
  English sentence rhythm more closely than the exercise and solution prose
  does, which was drafted more freely.
- **Link density is 1.06x English**, not 1.00x. Portuguese noun phrases harvest
  slightly more generously than English ones, and although the two
  `EXTRA_PROTECT` guards and the five `STOP` entries remove the worst
  offenders, the edition still links three targets English does not.
- **Three wrong links shipped in the first delivery** and were caught by a
  cross-edition frequency census, not by anything in this edition's own gate
  set. A homograph collision is invisible to every check the repository has;
  the only detector is comparing a target's link count against its English
  twin, and that comparison should have been part of my own hand-off rather
  than the coordinator's.
- **The index defect was found by hand, not by a gate**, ten chapters after it
  started. That it was caught before the build is luck plus a diff, not
  process; an edition scoring itself 100 should not have needed either.
