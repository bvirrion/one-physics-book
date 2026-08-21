# One Physics Book 3 (University, Year 1) --- Portuguese edition: self-score

**Date:** 2026-08-21
**Variety:** Brazilian Portuguese (`pt` = pt-BR across the whole series).
**Quality bar:** *native academic* (the bar of `translation_instruction.md`).
**Sense/structure reference:** the English canon (`parts/bachelor-1/*.tex`) for
content and labels; the Portuguese Books 1--2 of this series
(`parts/grade-*/pt/`) and `../one-math-book/parts/bachelor-1/pt/` for the
university register and for the term-link conventions
(`AMBIG_POLICY = "drop"`). **No French twin of Book 3 existed at scoring
time** --- `parts/bachelor-1/fr/` was being written concurrently by a sibling
agent in the same working tree and carried no generated links --- so French was
not used as a reference here; the Spanish edition of the same book, finished
earlier the same day, was used only to calibrate link density and the
`\text{...}` convention.

## Overall: **96 / 100**

| Dimension | Score | Note |
|---|---:|---|
| Register (academic Brazilian Portuguese, weighted) | 96 | Narrative present in the chapter openings; imperative/impersonal instructions in the methods and exercise stems (*escreva*, *deduza*, *verifique*, *isole*), as a Brazilian lecture text does. Subject pronouns are dropped throughout: **zero** occurrences of the MT tell *"Nós temos / Nós podemos"* in 60 files. |
| Terminology (weighted) | 96 | Settled glossary below; index keys equal the visible terms (checked mechanically: 0 mismatches over every `\emph{...}\index{...}` pair). |
| MT-artifact freedom (weighted) | 96 | Four residual-English defects were found by a purpose-built sweep and fixed (below). After the fix, an English-word scan, an English-suffix scan and a function-word-density scan over the reduced visible text of all 60 files return no true positive. |
| Structure | 100 | `check_translation.sh` green; every body was written as line-range replacements on the English canon through `tools/id_apply.py`, so labels, `\cref` targets, solution keys, `\qty{}{}`, `\foreach`, `xtick=` and every math display are byte-identical to English. |
| LaTeX hygiene | 99 | 0 errors, 0 undefined references, 0 overfull boxes, 0 *"invalid in math mode"*; UTF-8 accents only; no accented word inside any `\qty{}{}` unit argument. |
| Cross-references | 100 | Every `\cref`/`\ref` target byte-identical to English; 12 exercises + 1 weekend problem per chapter, one solution each. |
| Figures | 98 | Drawing code untouched; only node text, axis labels and captions translated. One caption node was shortened (not redrawn) to clear the last overfull box. |
| Solutions | 96 | All 30 solution files translated; `\textbf{n.}` numbering and every number preserved. |
| Term links | 96 | 2 509 links (English 2 342 = 1.07x; Spanish 2 400 = 1.02x). 200 distinct targets against English's 194; four English targets missing, ten extra. |

## What was produced in this run

The 60 bodies already existed (written in two earlier, spend-limited runs of
this same job). This run added the missing half of the deliverable:

- `tools/term_config/book3_pt.py` --- curated from the harvested Portuguese
  term list, **not** translated from `book3_en.py`; 2 509 links generated,
  where the uncurated stub would have produced 4 133.
- The native-register / residual-English pass over the whole tree (below).
- The last overfull box cleared.
- This score file.

## Checks

```
bash tools/check_translation.sh bachelor-1 pt        -> TRANSLATION GATE: PASSED
python3 tools/link_defined_terms.py --book 3 --lang pt --check
                                                     -> CHECK: every file matches
latexmk one_physics_book_3_university_year_1_pt.tex
  grep -ac '^!'                  -> 0
  grep -aci undefined            -> 0
  grep -ac Overfull              -> 0        (340 pages; English 332, Spanish 345)
  grep -ac 'invalid in math mode'-> 0
  grep -ac nullfont              -> 65       (identical in English: pgfplots
                                              measuring xmin=0.01 on the three
                                              log-axis figures, not a defect)
```

Omterm **target** parity with English: 194 distinct targets in the English
course bodies, 200 in the Portuguese. The four English targets missing here
(`def:b1:kinetic-theory:equilibrium`, `ex:b1:systems-of-points:rolling`,
`prop:b1:filters-transfer-functions:highpass1`, `prop:b1:units-dimensions:pi`)
are all cases where the *same* term maps to the *same* label in both
configurations, but the Portuguese phrase does not happen to recur outside the
solutions files; coverage is at or above English everywhere else.

## The curation (`tools/term_config/book3_pt.py`)

This is where Portuguese and English part company, and the file documents each
decision in place. The short version:

**Stopped in English, *not* needed in Portuguese** --- *objetiva* keeps its 23
links (English must stop "objective" because it is also an adjective);
*câmera* needs no stop (Portuguese spells the cold *câmara* differently, where
Spanish had to stop *cámara*); *torque* is the Brazilian word for the moment of
a force, so the Spanish clash on *par* never arises; *capacitância* is not
*capacidade*, so the Spanish clash on *capacidad* never arises either.

**Needed in Portuguese, absent in English** --- *sinal* is the signal of ch. 5
and, about as often, the algebraic sign (*"cargas de mesmo sinal"*,
*"verifique o sinal"*): no pattern list separates *"o sinal de teste"* from
*"o sinal de $q$"*, so it is stopped and linked only inside ch. 5. *casca* is
both the cladding of an optical fibre (ch. 2) and the spherical shell of
chs. 21, 26, 27. *núcleo* is the fibre core, the Earth's core, the coaxial
core, the iron core and the atomic nucleus, all one word.

**A French stop that Portuguese does not need.** The French edition had to stop
*solide*; Portuguese names the rigid body *corpo rígido*, so bare *sólido* is
never harvested as a term at all and its 26 ordinary uses (*estado sólido*,
*esfera sólida*, *ângulo sólido*) cannot be mislinked. The label
`def:b1:systems-of-points:solid` is reached through *corpo rígido* 4 times,
against English's 3. Likewise French had to **DROP** *centrale* (the power
station) rather than stop it: the Brazilian power station is a *usina*, so bare
*central* is dropped here only as a stray adjective.

**The one homograph that was *not* stopped** --- *tensão* is both the rope's
tension and the circuit's voltage, exactly the trap that made Spanish stop
*tensión* and lose most of its 120 "voltage" links (Spanish ships 34). Here the
mechanical sense was enumerated instead: it occupies about twenty sites in
chs. 12--15, 21 and 25, each masked by an `EXTRA_PROTECT` pattern, so the
electrical uses of chs. 5--10, 17 and 26--29 keep **121** links, matching
English's 120 on "voltage". Verified afterwards by listing every surviving
`\omterm{def:b1:dc-circuits:voltage}` in chapters 11--25: all seventeen are the
electrical sense.

**`NOT_A_TERM` had to be translated, minus one entry --- and this was verified
label by label, not assumed.** The shared default is English (`theorem`,
`lemma`, `principle`, ...) and is inert against a Portuguese index, so without
translation the tree harvests 26 *"teorema de ..."*, *"princípio de ..."*,
*"regra da ..."* entries that English never links (English has **zero**
`\omterm` displays containing *theorem*, *principle*, *rule*, *formula*,
*inequality*, *criterion* or *identity* --- checked, all zero). The test in
`harvest.py` is plain **substring containment, not position**, so a bare
keyword fires in both languages whatever the word order, and the two editions
stay symmetric.

The trap is the single *phrase* in the default, `law of`, which **is**
position-dependent and so never fires on English's own possessive form: English
links **70** named-law displays. Portuguese puts the keyword first --- *lei de
Ohm* --- so a literal `lei de` would have caught every one of them and deleted
the lot, silently, with no complaint from any of the eight gates. It is
deliberately absent, and this edition ships **77** named-law links against
English's 70. `método` and `enunciado` are out for the same reason: the English
default carries neither *method* nor *statement*, so *método de Bessel*,
*método de Silbermann*, *enunciado de Clausius* and *enunciado de Kelvin* stay
linkable, as their English twins are.

The suppression was then audited exhaustively. It costs 32 links across 17
files, and **zero target labels**: of the 26 suppressed terms, 18 point at
labels that are equally unreachable in English (0 links there, 0 here ---
English's own filter suppresses the same class), and the remaining 8 point at
labels still reached through another term at a count **at or above** English's
(`thm:b1:work-and-energy:ke` 51 vs 47, `thm:b1:newton-dynamics:laws` 19 vs 16,
`prop:b1:systems-of-points:twobody` 4 vs 4, `thm:b1:fluid-statics:archimedes`
2 vs 2, `prop:b1:fluid-statics:atmosphere` 3 vs 3,
`thm:b1:potential-capacitors:conductor` 2 vs 2, `thm:b1:heat-engines:carnot`
1 vs 1). For contrast, the French edition of this same book lost 88 links and
5 target labels outright by translating the list literally.

`NOT_A_TERM` is also **subject- and level-specific**, not merely
language-specific: `book2_pt.py`, the school book, leaves it empty and is right
to, because a spiral curriculum re-links its result names on purpose. It was
checked here, not copied.

**Sanity, per chapter.** Link counts per chapter run at 0.85--1.15 of English
except in the chapters where a single Portuguese word covers two English ones
(ch. 11 *velocidade* for "velocity" *and* "speed"; ch. 18 *referencial* for
"frame" *and* "reference frame"; ch. 30 *comprimento de onda*, which English
cannot link at all because the shared harvester skips single-word index entries
outside a `definition` and "wavelength" is one word). No label carries a
runaway count: the densest is *tensão* at 121, against English's 120.

## Sampled passages

1. **`parts/bachelor-1/pt/01-units-dimensions.tex`, opening** ---
   *"Num laboratório de subsolo um pêndulo oscila, um cronômetro dispara e um
   estudante escreve $g = \qty{9.77}{m/s^2}$. […] A física mede, e uma medida
   sem a sua incerteza é um boato."*
   **Verdict: native.** The inversion *"Num laboratório de subsolo um pêndulo
   oscila"* is Portuguese word order, not an English calque, and *"é um boato"*
   carries the English aphorism instead of glossing it.

2. **`parts/bachelor-1/pt/18-non-inertial-frames.tex`, opening** ---
   *"Em pé num ônibus que faz uma curva à esquerda, você se inclina para a
   direita, empurrado por uma força que ninguém exerce. […] como se uma mão
   invisível a fizesse girar."*
   **Verdict: native.** *Em pé*, *faz uma curva*, the imperfect subjunctive
   after *como se* --- a machine produces *"como se uma mão invisível fazia".*

3. **`parts/bachelor-1/pt/24-heat-engines.tex`, method "Auditar uma máquina"**
   --- *"localize a criação (diferenças finitas de temperatura nos trocadores,
   atrito, estrangulamento, compressão não quase-estática) […] Um componente
   que não cria entropia não vale a pena melhorar."*
   **Verdict: native.** *trocadores*, *estrangulamento* are the Brazilian
   engineering terms, and *"não vale a pena melhorar"* is idiom, not gloss.

4. **`parts/bachelor-1/pt/27-potential-capacitors.tex`, theorem "Propriedades
   de um condutor em equilíbrio"**, item 4 --- *"Uma cavidade dentro de um
   condutor, vazia de carga, tem $\vect E = \vect 0$ e $V$ uniforme, aconteça o
   que acontecer fora (gaiola de Faraday)."*
   **Verdict: native.** *"aconteça o que acontecer"* is the Portuguese
   concessive; MT renders "whatever happens outside" as *"o que quer que
   aconteça do lado de fora"*. Items 1--3 of the same theorem are
   **near-native**: correct and terse, as clipped as the English, where a
   Brazilian textbook would add a little connective tissue. Deliberate --- the
   series' house style is the telegraphic statement.

5. **`parts/bachelor-1/pt/30-quantum-introduction.tex`, opening** ---
   *"Envie elétrons um a um por duas fendas e eles chegam como pontos, cada um
   num lugar --- e os pontos se acumulam, aos milhares, nas franjas de uma
   onda."*
   **Verdict: native.** *um a um*, *aos milhares*, *se acumulam* are idiom, not
   glosses of "one at a time", "over thousands", "build up".

6. **`parts/bachelor-1/solutions/pt/16-central-forces.tex`, item 3** ---
   *"As moléculas de um gás, a algumas centenas de metros por segundo, têm uma
   cauda da distribuição de velocidades acima de \qty{2.4}{km/s}; em tempos
   geológicos o gás da Lua vazou para o espaço."*
   **Verdict: native.** *vazou para o espaço* is the ordinary verb a Brazilian
   physicist uses; post-edited MT reaches for *"escapou"* or *"fugiu"*.

## Faults found and fixed in this run

Everything below was found by mechanical sweeps written for this pass, not by
re-reading 60 files: a curated English-word scan, an English-suffix scan and a
function-word-density scan over `visible_text()`; a title / `\text{}` / TikZ-node
comparison against the English twin; and a repeated-word scan.

- **Three untranslated environment titles**, ch. 11 --- `[Derivatives of the
  local basis]`, `[Velocity and acceleration in cylindrical coordinates]`,
  `[Velocity in spherical coordinates]`. These are invisible to every existing
  gate: the optional argument of `\begin{...}[...]` is *masked* by
  `tools/termlink/protect.py`, it carries no accent for gate 6 to miss, and
  Portuguese is written in the same alphabet as the source, so a forgotten
  title looks exactly like a correct one.
- **One duplicated English line left in the prose**, ch. 27 theorem *Energia de
  um capacitor*: the English *"the work needed to carry the charge from one
  plate to the other"* stood immediately above its own Portuguese translation.
  Deleted.
- **One untranslated `\text{}` inside a display**, ch. 29 --- *"(no load
  losses, no magnetizing current)"*, now *"(sem perdas em vazio, sem corrente
  magnetizante)"*.
- **Fourteen English `\text{}` subscripts** --- `fluid`, `immersed`, `imm`,
  `out`, `inside`, `core`, `air`, `circuit`, `enclosed`, `enc`, `static`,
  `own`, `in`, `i.e.` --- localised to *fluido, imerso, im, saída, int, núcleo,
  ar, circuito, enlaçada, enl, est, próprio, int, isto é,* and one `sh` to
  *der*, matching the prose's *"resistor em derivação"*. (`\text{watts}`,
  `\text{joules}`, `\text{ohms}` were **kept**: unlike Spanish, which needs
  *vatios/julios/ohmios*, those are the correct Portuguese plurals.) This
  follows the shipped Spanish edition, which localises `\text{}` and leaves
  `\mathrm{}` alone.
- **`(magnet)` in a TikZ node**, ch. 29, now *(ímã)*.
- **`de de Broglie`**, ch. 30 (index entry and two prose sites): correct but
  ugly. Now *de De Broglie*, with an `EXTRA` entry linking the whole six-word
  phrase to the de Broglie theorem --- one word over `MAX_TERM_WORDS`, so the
  harvester had been dropping it and the inner *comprimento de onda* linked to
  the sinusoidal wave of ch. 5 (right notion, wrong statement). This restores
  the English target `thm:b1:quantum-introduction:debroglie`.
- **`46\% da da Lua`**, ch. 18 --- grammatical but unreadable; now *"46% da
  contribuição lunar"*.
- **The last overfull box** (17.58 pt, ch. 28, the magnet/couple figure): the
  two caption nodes of the two `scope`s, both centred, had grown longer than
  their English originals and pushed the `tikzpicture` past `\textwidth`.
  Fixed by shortening the two Portuguese node texts (*"linhas de N contornando
  até S"* -> *"linhas de N a S"*, *"gira para alinhar"* -> *"gira e alinha"*).
  No drawing coordinate and no mathematics touched.

## Variety check (pt-BR, no European forms)

Swept mechanically over all 60 files: *elétron* 100 / *eletrão* 0; *próton* 52
/ *protão* 0; *nêutron* 8 / *neutrão* 0; *hidrogênio*, *fenômeno*, *nanômetro*,
*cronômetro* (never *-ónio/-ómetro*); *tela* 32 / *ecrã* 0; *trem* 68 /
*comboio* 0; *ônibus* 6 / *autocarro* 0; *usina* 16 / *central elétrica* 0;
*geladeira* / *refrigerador* (both, correctly split between the everyday and
the technical register); *ímã* 40 / *íman* 0; *empuxo* 22 / *impulsão* 0;
*capacitor* 176 (the component) against *condensador* 10 (only the condenser of
the ch. 24 refrigeration cycle --- correct, not a slip); *quantidade de
movimento* 29 / *momento linear* 0; *tensão* / *voltagem* 0; no `-ct-`/`-cç-`
pre-1990 spellings; *"está a fazer"* (European progressive) 0 occurrences ---
every hit of *"está a"* is a distance (*"está a \qty{1.2}{m}"*).

## Settled terminology

**Optics** raio de luz · dioptro · normal · ângulo limite · reflexão total ·
casca / núcleo (fibra) · abertura numérica · desvio mínimo · espelho
côncavo/convexo · lente delgada · vergência · distância focal · aumento
transversal/angular · medida algébrica · condições de Gauss · estigmatismo ·
objetiva / ocular · intervalo óptico · lupa · luneta · pupila de saída ·
poder coletor de luz · profundidade de campo · número f · acomodação ·
ponto próximo / ponto remoto · critério de Rayleigh.
**Signals & circuits** sinal · celeridade · onda progressiva / estacionária ·
comprimento de onda · dupla periodicidade · batimentos · fem · convenção
gerador / receptor · lei das malhas / dos nós · divisor de tensão / de
corrente · ponte de Wheatstone · teorema de Millman · modelo de Thévenin /
de Norton · regime transitório / permanente · regime pseudoperiódico /
crítico / aperiódico · decremento logarítmico · amplitude complexa · fasor ·
impedância / admitância · reatância · valor eficaz (RMS) · fator de potência ·
fator de qualidade · banda passante · diagrama de Bode · passa-baixa /
passa-alta / passa-faixa · cascata · efeito de carga · amp. op. ·
realimentação · curto-circuito virtual / terra virtual · gatilho de Schmitt ·
slew rate · produto ganho--largura de banda.
**Mechanics** ponto material · referencial · abscissa curvilínea · base de
Frenet · aceleração normal / tangencial · quantidade de movimento ·
atrito seco / fluido · reação normal · rolamento sem deslizamento ·
trabalho / potência de uma força · energia potencial · pontos de retorno ·
oscilador amortecido · oscilações forçadas · momento (torque) ·
braço de alavanca · momento de inércia · teorema de Huygens ·
pêndulo físico / de torção · força central · barreira centrífuga ·
velocidade areolar · transferência de Hohmann · referencial baricêntrico ·
teoremas de Koenig · massa reduzida · força de arrastamento / de Coriolis ·
pêndulo de Foucault · seletor de velocidades · frequência ciclotrônica ·
raio de Larmor · efeito Hall.
**Thermodynamics** gás perfeito · livre caminho médio · pressão cinética ·
capacidade térmica a volume / a pressão constante · entalpia ·
transformação quase-estática / isocórica / monobárica / adiabática ·
expansão de Joule · relação de Mayer · coeficiente adiabático ·
termostato · entropia criada / trocada · desigualdade de Clausius ·
enunciado de Kelvin / de Clausius · diagrama entrópico · máquina térmica ·
rendimento · coeficiente de desempenho · bomba de calor · refrigerador ·
ciclo de compressão de vapor · fluido refrigerante · trabalho perdido ·
regra da alavanca · título (fração mássica de vapor) · calor latente ·
pressão de vapor saturante · super-resfriamento / superaquecimento ·
ponto de orvalho · umidade relativa · isotermas de Andrews.
**Electromagnetism & quantum** carga elementar · lei de Gauss ·
superfície de Gauss · plano de simetria / de antissimetria ·
potencial eletrostático · condutor em equilíbrio · teorema de Coulomb ·
gaiola de Faraday · poder das pontas · capacitor plano / cilíndrico /
esférico · dipolo elétrico · lei de Biot--Savart · curva amperiana ·
espira · solenoide · momento magnético · força de Laplace / de Lorentz ·
trilhos de Laplace · lei de Faraday · lei de Lenz · autoindutância ·
indutância mútua · correntes de Foucault · indução de Neumann / de Lorentz ·
efeito fotoelétrico · função trabalho · potencial de corte ·
espalhamento Compton · onda de matéria · comprimento de onda de De Broglie ·
função de onda · densidade de probabilidade · princípio da incerteza
(kept distinct from *incerteza de medida*, which ch. 1 reserves for
metrology) · poço infinito · estado fundamental · níveis de energia ·
ponto quântico.

## Why not 100

- **`\mathrm{}` subscripts are mathematics and stay byte-identical to
  English**, by construction and by the convention every edition of this series
  follows (English, Spanish and Portuguese carry the *same* 24 `\mathrm{}`
  strings in the *same* counts). A Brazilian reader therefore meets
  `S_{\mathrm{created}}`, `S_{\mathrm{exch}}`, `\mathrm{out}`, `\mathrm{in}`
  and `\mathrm{eff}` in chapters 22--24 as English abbreviations. Only
  `\text{}` subscripts, which the applier does allow to change, were localised.
  Changing this is a *series-wide* decision, not a Portuguese one --- see
  "shared files" below.
- **`\qty{}{yr}`** (chs. 16, 30) prints an English abbreviation for the year.
  It is inside a unit argument, where an accented or translated word is a
  fatal-class bug (the `dB/década` trap), so English, Spanish and Portuguese
  all keep it. Same series-wide caveat.
- The series' statement style is deliberately telegraphic; a few enumerated
  theorem items (chs. 21, 27) read *correct and terse* rather than *written in
  Portuguese first*.
- Four English `\omterm` targets do not recur in the Portuguese course bodies
  (listed above), and ten Portuguese ones have no English counterpart --- an
  artefact of which index entry the shared harvester can see in each language
  (it skips single-word index entries outside a `definition`, which costs
  English "wavelength" and gains Portuguese "comprimento de onda").
- The 60 bodies were drafted in two earlier sessions of this job. They were
  swept mechanically here (residual English by word list, by suffix and by
  function-word density; every environment title, `\text{}` and TikZ node
  compared against its English twin; repeated words; European-Portuguese
  forms; unit arguments; overfull boxes) and sampled by hand across young and
  hard chapters, but not re-read line by line.

## Shared files a maintainer may want to change (nothing was touched here)

- `tools/check_translation.sh` has **no Latin-script prose gate**. Portuguese,
  Spanish, French, Dutch and Indonesian are all written in the source's own
  alphabet, and only Indonesian has one (`tools/check_indonesian_prose.py`,
  gate 8). The four defects above --- three English environment titles, one
  duplicated English line, one English `\text{}` and fourteen English
  subscripts --- passed every gate and built cleanly. Two cheap, generic
  additions would have caught all of them, in every Latin-script edition at
  once: (a) compare every `\begin{env}[title]`, `\text{...}` and TikZ
  `node {...}` against its English twin and report the ones that are
  byte-identical *and* contain lowercase letters (a handful of false positives:
  tikz option lists, `resume`, proper nouns, abbreviations); (b) run the
  existing `visible_text()` reduction against a curated list of English words
  that are not words of the target language. Both are ~40 lines on top of
  `check_hindi_prose.visible_text`.
