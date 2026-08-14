# Translation score — Physics Book 1 · Brazilian Portuguese (`pt`)

| Field | Value |
|-------|--------|
| **Book** | One Physics Book 1 (Primary & Middle School, grades 1–9) |
| **Language** | Brazilian Portuguese (`pt`) |
| **Quality bar** | **native academic** (EN is the source of truth; the shipped Book 2 `pt` edition was the register and terminology reference, the FR Book 1 tree the structural/sense cross-check where it already existed) |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-08-14 (link-density pass + missing-target audit the same day, after coordinator verification) |
| **Scope of this pass** | First-pass translation written directly from the English canon: all **71 chapters + 71 solution files** (142 files), the front-matter `image-credits.pt.tex`, a curated `tools/term_config/book1_pt.py` (created from scratch) and the generated `\omterm` layer. Nothing was machine-translated and patched; every chapter was drafted at register in one pass, then swept. |

## Verdict in one line

Brazilian school-physics prose that climbs from *bath-time and magnets* to
*gravitação, energia cinética e ordens de grandeza* without changing
translator: children's rhythm in grades 1–3 (*flutua, afunda, quentinho,
mil e um, mil e dois*), a real *ensino fundamental* textbook by grade 9
(*intensidade gravitacional, distância de frenagem, tensão eficaz,
rendimento, ordem de grandeza*), and a term-link layer that knows *meio*
is usually "half", *nós* is usually a pronoun, *grama* is sometimes
grass, and *lâmpada* is one Portuguese word doing two English words' work.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Exact mirror of the English tree: **797 `exo:` labels EN / 797 PT**, **35 `pb:` / 35**, **832 `solution` environments / 832**, **139 `tikzpicture` / 139**, **192 `omfigure` / 192**, **113 definition / 113**, 90 proposition, 259 example, 73 method, 96 remark, 13 `axis`, 62 `includegraphics` — identical on both sides. All nine `check_translation.sh` gates **PASSED** |
| Terminology | **96** | Continuity with the shipped Book 2 `pt` was checked before coining anything: *óptica*, *polo*, *lâmpada*, *pilha*, *densidade*, *altura* (pitch), *intensidade sonora*, *amplitude*, *rendimento*, *frequência*, *tensão*, *amperímetro*, *voltímetro* all match Book 2. Brazilian post-2009 orthography (*polo*, *ideia*, *óptica*). SI unit **names** lower-case in prose (newton, joule, watt, volt, ampère, ohm, hertz); unit **symbols** inside `\qty`/`\unit` byte-identical to English. Deliberate collision-avoidance: *terminais* (not *polos*) for a battery's terminals, *umbra/penumbra* (not *sombra*) for eclipse geometry, *intensidade sonora* (not bare *intensidade*) for loudness |
| Register / tone | **96** | The gradient is the point of this book and it holds. Grade 1: «Um pássaro canta em algum lugar lá em cima. O pão cheira a quentinho.» Grade 9: «Nada nos céus está suspenso. Tudo cai, e erra o alvo.» Counting-seconds idiom localized («mil e um, mil e dois», not the English crocodiles); compass card N/L/S/O; English appositive dashes kept where Portuguese uses them too |
| LaTeX hygiene | **97** | 0 errors, 0 undefined references, **0 overfull boxes**, 154 underfull (EN 121). 0 TeX accent escapes, UTF-8 throughout, no `\end{…>` typos, no duplicate labels, no drafty `...`, no zero-width characters, no ASCII `"` in prose (TeX ``…'' quotes throughout, as Book 2 `pt` does) |
| Cross-refs / rule compliance | **99** | `\label`, `\cref`/`\ref` targets and `\begin{solution}{key}` byte-identical to English; solution headers keep the English `ch:` slug and localize only the chapter word (`\section*{Capítulo \ref{…} --- …}`). **Zero** curriculum, track or country names anywhere in the visible text. Decimal **point** kept throughout, per the series convention, not the Brazilian comma |
| Figures | **98** | All 139 drawing bodies byte-identical to English — coordinates, `\foreach` lists, `xtick`/`ytick`, `samples`, `\addplot` expressions, `circuitikz` component names. Only node text, legends, axis labels and `{\small …}` captions localized (`l=pilha`, `l=lâmpada`, `xlabel={tempo (\unit{ms})}`). `symbolic y coords` keys deliberately left ASCII with translated `yticklabels` |
| Solutions | **97** | All 797 exercise solutions plus all 35 weekend-problem solutions present, keyed identically, and written as answers rather than glosses; the rhyming closer of the g9 motion problem was re-rhymed in Portuguese («Espaços iguais, um ritmo em paz --- força resultante nenhuma o desfaz») rather than translated flat |
| MT-artifact freedom | **97** | Calque sweep (`isso é porque`, `de forma que`, `tomar lugar`, `ao invés de`, gerundismo `vai estar …ndo`, English function words with markup stripped) returns **zero** hits; the two matches it did flag (`no fim do dia`, `em ordem de`) were read in context — the first is literal end-of-day prose, the second was rewritten to `Ordene por velocidade` |
| Defined-term links (`\omterm`) | **96** | `--check` **green**: **6 663 links across 140 files**, all matching what `book1_pt.py` generates — **102.8 % of English's 6 483** on the same text. **200 linkable terms PT / 211 EN**, 10 chapter-local. Target sets are the same size (**133 PT / 133 EN**), one label each way (both explained below). No term dominates the page any more: the heaviest label is *luz* at 487 (English's heaviest is the same concept at 437) |

**Weighted total: 96 / 100.**

### Link-density pass (post-verification)

The first run shipped **7 119** links, 9.8 % over English, with
**504** of them on `def:g3:first-electric-circuit:bulb` alone — 7 % of the
whole layer on one word, because *lâmpada* absorbs both English *bulb*
(linked) and English *lamp* (not linked). `lâmpada` is now **STOPped**:
it links inside the chapter that defines it and nowhere else. Result:

| | before | after | EN |
|---|---:|---:|---:|
| total links | 7 119 | **6 663** | 6 483 |
| `…:bulb` | 504 | **39** | 228 |
| heaviest label | 504 (*lâmpada*) | **487** (*luz*) | 437 (*light*) |
| ratio to EN | 109.8 % | **102.8 %** | — |

The trade-off is real and is the reason this dimension is 96 and not 98:
a Portuguese reader can no longer jump from a grade-8 *lâmpada* to the
grade-3 definition, where an English reader can jump from *bulb*. The
engine links every occurrence or none — there is no first-occurrence
mode — so with one word carrying two English words' worth of text, the
choice was 504 links or 39. A page that reads blue is worse than a jump
the reader can make by the index.

## Structural / build gates

| Gate | Result |
|------|--------|
| `bash tools/check_translation.sh grade-1 … grade-9 pt` | **PASSED** (9/9) |
| `latexmk one_physics_book_1_primary_middle_school_pt.tex` | exit 0 |
| `grep -c '^!'` | **0** |
| `grep -ci 'undefined'` | **0** |
| `grep -c 'Overfull'` | **0** |
| `grep -c 'Underfull'` | 154 (EN 121 — the series norm, and see the caveat below) |
| PDF | `build/one_physics_book_1_primary_middle_school_pt.pdf`, **451 pp** (EN 435, FR 454, AR 450) |
| `python3 tools/link_defined_terms.py --book 1 --lang pt --check` | **green** — every file matches the config (6 663 links; `--unwrap --apply` → `--apply` is idempotent) |
| Exercise ↔ solution invariant | 71/71 chapters diff to zero lines (the gate's own check) |
| Duplicate labels in the `pt/` tree | none |

### Build-environment caveat

This machine has **no Portuguese hyphenation pattern file installed**:

```
Package onephysics Warning: brazilian/portuguese.ldf not found; building
Portuguese without babel. Install texlive-lang-portuguese for hyphenation.
```

The book was therefore typeset with English hyphenation, exactly as the
Book 2 `pt` edition was. Everything that depends on line breaking — the 0
overfull boxes, the 154 underfull ones, the 451-page total — is
**provisional**: install `texlive-lang-portuguese`, rebuild and re-check
the overfull count before printing. No content score depends on it.

## Defined-term links — what Portuguese needed

`tools/term_config/book1_pt.py` was created for this edition, seeded from
`book1_en.py`'s structure and from the Book 2 `pt` config's hard-won
rules. Four problems are specific to Portuguese here.

### `STOP` (word keeps its link inside the chapter that defines it)

| Term | Why |
|---|---|
| `meio` | **the** collision of this book: the sound's *medium* (g7) and, everywhere else, "half", "the middle", "by means of" — *no meio do túnel*, *por meio de*, *meia-cana*. 184 occurrences, a minority of them acoustic |
| `intensidade` | the current's intensity (g8) — but *de intensidade* also names the magnitude of a force (g9 gravitation) and *intensidade sonora* the loudness of a sound. Both phrases survive as terms of their own |
| `nós` | the junctions of a parallel circuit — and the pronoun *we/us*, on nearly every page («a luz que chega até **nós**»). Same collision Book 2 `pt` documented |
| `polo`, `polos` | magnet poles in their chapters; the rotor's poles and the Earth's geographic poles elsewhere. *polo norte* / *polo sul* survive |
| `fase`, `fases` | moon phases in their chapter; «as duas fases da queda» of any process elsewhere |
| `lâmpada` | Portuguese has one word where English alternates two — *bulb* (linked in English) and *lamp* (not linked). Book-wide it carried 504 links; see the density pass above |
| `observação`, `observar`, `equilibrada`, `símbolo` | the English config's stops, with the same reasons |

### `DROP` (ordinary word harvested from a definition that merely uses it)

`quente`/`frio`; `sentido` (in this book *sentido* is above all the
**direction** of a current or a motion, not a sense of the body);
`visão`, `tato`, `olfato`, `paladar` — but **not** `audição`, which is
kept for the same reason English keeps *hearing*: it is what makes
`def:g1:five-senses:senses` reachable (9 links PT / 10 EN);
`segundo` (the unit vs
the ordinal *o segundo ramo*); `instante`; `aberto`, `fechado`,
`retilínea`, `circular`, `uniforme`, `variado` (the compound phrases
*circuito aberto*, *trajetória retilínea*, *movimento uniforme* survive);
`ano` (*ano-luz* survives); `dia`, `noite` (*o dia a dia* is everywhere;
*nascer do sol* and *pôr do sol* survive).

### `NO_CAPITAL`

`newton`, `joule`, `watt`, `volt`, `ampère`, `ohm`, `hertz` — capitalized
these are the physicists, and Portuguese spells the two alike — plus
`medir` and `observar`, whose capitalized forms are the imperatives of
method titles.

### `EXTRA_PROTECT` (all patterns use `\s+`, none consumes a `$`)

*resistência do ar* and *resistência da chaleira/torradeira* (drag and a
heating element, not the quantity *R*); *potências de dez*; *conta de
luz*; *volume do ensino médio* (a volume of this series, not the space a
body occupies); *a grama é verde* (grass, not the gram); *estação
espacial / estações de medida / entre estações* (stations, not seasons);
*núcleo de ferro*, *núcleo da Terra* (cores, not the atomic nucleus);
*período orbital*; and adverbial *com força* ("hard", not the measured
quantity).

### Target-set diff against English — both labels audited

Both editions link **133 distinct targets**. One label differs each way.

* **`def:g7:short-circuits-safety:battery` — EN 24 links, PT 0, and
  honest to leave dark.** English does not reach that definition through
  any Portuguese-reproducible route: its sole carrier is the possessive
  **`battery's`**, which the harvester accepts as a term distinct from
  `battery` because the definition emphasises `\emph{battery's}` and the
  key *batterys* still matches the label leaf *battery*. All 24 English
  links are that one surface form — including ordinary possessive
  mentions such as «the **battery's** push is tiny», which land on
  *Short circuit of the battery* rather than on the battery definition,
  so the English behaviour is itself slightly off-target. Portuguese has
  no possessive form; the only candidate surface is *da pilha*, an
  ordinary prepositional phrase that occurs on nearly every circuit page
  and would mislink the whole book. The pt definition emphasises the
  defined object (`os dois terminais da \emph{pilha}`), mirroring
  English's emphasis without inventing a term. Chapter-level access is
  unaffected: `def:g7:short-circuits-safety:device` (*curto-circuito*)
  is linked and reachable throughout.
* **`ex:g8:sound-pitch-loudness:decibels` — PT 3 links, EN 0.**
  Portuguese's *decibéis* is harvested from the example's own
  `\emph{decibéis}\index{decibel}` pair, and the plural is what the
  prose actually writes; English's *decibels* falls to its own config.
  A gain, not a defect.

## Samples, with verdicts

| # | Sample | Verdict |
|---|--------|---------|
| 1 | «Um pássaro canta em algum lugar lá em cima. O pão cheira a quentinho. A calçada gela os seus pés através da meia.» (g1, five senses) | **native** — written for a Brazilian six-year-old, not carried over from English |
| 2 | «Quem viaja é o revezamento: um padrão de apertos em disparada, passado de fileira em fileira da multidão. Cada molécula apenas se sacode em torno da casa dela.» (g7 solutions, sound) | **native** |
| 3 | «Uma lei, três receitas, a oficina inteira.» (g8, Ohm's law) | **native** — English's clipped apposition survives as Portuguese apposition, not as a subordinate clause |
| 4 | «Nada nos céus está suspenso. Tudo cai, e erra o alvo.» (g9, gravitation) | **native** |
| 5 | «O livro-caixa da montanha-russa: altura gasta compra velocidade, velocidade gasta compra altura de volta.» (g9, energy) | **near-native** — *livro-caixa* for the book's recurring "ledger" metaphor is a translator's coinage; correct and understood, but a Brazilian editor might prefer *balanço* or *contabilidade* in one or two of its ten uses |

No sample in the sweep was judged **MT**.

## Why not 100 — the honest gaps

1. **Three words are STOPped and therefore dark outside their own
   chapters: `lâmpada`, `meio`, `intensidade`.** Each is a genuine
   one-word-for-two collision (*bulb*/*lamp*, *medium*/*half*,
   *intensity*/*magnitude*), and the engine links every occurrence or
   none. `lâmpada` is the costly one: it removes a jump an English
   reader has (39 links vs English *bulb*'s 228). A per-sense `EXTRA`
   map would recover part of all three; the vocabulary model does not
   support sense disambiguation inside one word.
2. **The layer still runs 2.8 % over English (6 663 vs 6 483)**, now for
   one benign reason only: Portuguese repeats nouns where English
   pronominalizes ("the lamp's own light" → «a luz da própria
   lâmpada»). No single label dominates: heaviest is *luz* at 487
   against English *light*'s 437.
3. **Overfull/underfull counts are provisional** — no Portuguese
   hyphenation patterns on this machine (above). The 0 overfull is real
   for *this* build, not for a properly hyphenated one.
4. **Two deliberate conventions may read foreign to a Brazilian
   reader**: the decimal **point** (a series-wide rule, kept), and
   *ampère* with the grave accent (matching the shipped Book 2 `pt`
   edition rather than INMETRO's *ampere*). Consistency across the two
   books won; a national-standards reviewer may disagree.
5. **A handful of coined idioms** carry the English book's recurring
   metaphors — *livro-caixa* (ledger), *raspadinha do atrito* (friction's
   skim), *aposentar a energia* (retire the energy). They are consistent
   and they work; they are also the places where a native editor would
   most plausibly reach for something else.
6. **Register at the seams.** Grades 1–3 and grades 8–9 were written at
   their own registers with confidence; grades 5–6, the hinge where the
   children's voice becomes the textbook's, are the pages I would ask a
   Brazilian teacher to read first.
