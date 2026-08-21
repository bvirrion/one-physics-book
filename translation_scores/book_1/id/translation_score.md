# Translation score — Physics Book 1 · Indonesian (`id`)

| Field | Value |
|-------|--------|
| **Book** | One Physics Book 1 (Primary & Middle School, grades 1–9) |
| **Language** | Indonesian (`id`), Bahasa Indonesia baku per `indonesian_style_card.md` |
| **Quality bar** | **native academic** (English is the sole source of truth; no other edition was consulted) |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met.** |
| **Date** | 2026-08-21 |
| **Scope** | **All 142 bodies written in Indonesian** — 71 chapters + 71 solution files, grades 1–9 — plus the localisation of every figure's visible text and a curated `tools/term_config/book1_id.py` |

## Read this first

Nothing here was machine translated. Every file was produced as a
**line-range patch on the English canon**: each named range was rewritten in
Indonesian and every unnamed line was copied byte-identically, so `\label`,
`\cref`/`\ref` targets, `\begin{solution}{key}`, `\qty`/`\unit` arguments,
math displays, `\foreach` lists, `xtick=` and all coordinate/style options
are physically the same bytes as English and cannot drift. The applier
refused any file that failed a census against its English twin (ordered
labels / environments / solution keys / `\emph`–`\index` adjacency /
`\index` count / ordered math spans / drawing code / per-range `\[ \]`
counts / brace balance / surviving `\omterm` / the prose gate); every one of
the 142 files was written until it passed all eleven.

Only *visible* text was rewritten: prose, environment optional titles,
captions, TikZ `node {…}` text, pgfplots `xlabel=`/`ylabel=`, circuitikz
`l=` labels, `\text{…}` inside math, `\index{}` keys, the drawing code's
`%` comments, and the solution headers (`\section*{Bab \ref{ch:…} --- …}`,
`ch:` slug untouched).

### Register

The English voice — a book that talks to one pupil for nine years and keeps
promises made years earlier — is carried by Indonesian syntax, not by
transposed English clause order. The ladder the style card fixes:

* **grades 1–3** speak to the child directly: `kamu`, short concrete
  sentences, `-lah` imperatives (`lihatlah`, `cobalah`, `peganglah`,
  `berdirilah`), no subordinate stacking;
* **grades 4–6** drop the coaxing `-lah` from running prose and keep it only
  where a step is genuinely being ordered; sentences lengthen, the
  vocabulary becomes technical (`massa jenis`, `pendesakan air`, `penaraan`);
* **grades 7–9** are full textbook prose: `yang`-clauses, `sehingga` /
  `sedangkan` / `melainkan` / `karena itu` chains, the impersonal passive
  (`diukur`, `dinyatakan`, `dibelanjakan`) that Indonesian science writing
  lives on. `-lah` survives there only inside `method` steps, where
  `ukurlah` / `bagilah` / `hitunglah` is ordinary procedural Indonesian, not
  a child register.

The book's running jokes and callbacks survive as jokes and callbacks: the
electron's punchline in the last chapter ("lelucon lama, dibayar"), the
"kalimat yang tenang" of grade 9, the "pemanas yang punya hobi", the
detective's creed, the ladybug that opens grade 1 and returns on the last
page.

| Part of the book | Files | State |
|---|---:|---|
| grade-1 … grade-3, chapters + solutions | 40 | Hand-translated |
| grade-4 … grade-6, chapters + solutions | 48 | Hand-translated |
| grade-7 … grade-9, ch01–ch09 + solutions | 54 | Hand-translated |

## Dimension scores

| Dimension | Weight | Score /100 | Notes |
|-----------|-------:|----------:|--------|
| Register / tone | 0.20 | **96** | One voice across nine school years, with the three-step ladder above. Chapter openings are written as Indonesian openings, not as translated first sentences ("Sebuah apel melepaskan diri dari dahannya lalu jatuh. Bulan, di atas kebun yang sama, tidak."). Definiteness is marked the Indonesian way with `-nya` rather than by importing English articles |
| Terminology | 0.18 | **96** | One glossary over 71 chapters, settled in grade 1 and never drifting — see the table below. Every `\index` key is the visible Indonesian term; all 200 keys are Indonesian, none transliterated English |
| MT-artifact freedom | 0.17 | **98** | No machine output at any stage. `check_indonesian_prose.py`: **0 issues across all 142 files** in all seven classes (english, untranslated, math-space, redup-space, enclitic, split-number, title). No English clause order, no calqued idiom; `di`/`ke` are separated as prepositions and attached as prefixes throughout (checked by eye: 0 wrongly joined, 0 wrongly separated) |
| Structural fidelity | 0.10 | **100** | 142 files; identical label sets *and order* in every chapter; exercise↔solution key parity in 71/71; identical environment census; `[resume]` blocks preserved; the grade-1–5 / grade-6–9 exercise-count contract (9–11 vs 12 + one 13–15-question weekend problem) mirrors English exactly. All nine `check_translation.sh` runs **PASSED**, zero duplicate labels |
| LaTeX hygiene | 0.08 | **100** | pdfTeX, exit 0: **0 errors, 0 undefined references, 0 overfull boxes**, 464 pages. `.fls` shows 1 278 `/id/` inputs, so the Indonesian bodies really are in the build. Decimal separator is a point everywhere, digits ASCII, no accent escapes |
| Cross-refs / rule compliance | 0.07 | **100** | `\label`, `\cref`/`\ref` targets, solution keys and every `\omterm` first argument byte-identical to English. `\qty`/`\unit` arguments untouched; nothing changed inside math. No curriculum, board or country is named; no `SD`/`SMP`/`SMA` as institution labels; no English glosses in parentheses |
| Figures | 0.07 | **97** | All 192 figure bodies present with drawing code preserved; only visible text was localised — TikZ node labels, pgfplots `xlabel`/`ylabel`/`symbolic coords`, circuitikz `l=` labels, `\foreach` label lists, and every caption. Three node labels were shortened after the first build so their pictures fit the text block |
| Solutions | 0.08 | **96** | All 71 solution files written in the same register as their chapters, including the 12–15-item weekend-problem answers; the numbered `\textbf{n.}` voice is uniform from grade 1 to grade 9 |
| Defined-term links | 0.05 | **94** | `--check` green and idempotent: **6 799 links** (104.9 % of English's 6 483) across **133 targets**, the same count as English. `book1_id.py` curated from scratch: 10 `STOP` entries, 38 `DROP` entries, 9 `NO_CAPITAL` entries, 13 `EXTRA_PROTECT` patterns |

Weighted total: **96 / 100**.

## Gate results

| Gate | Result |
|------|--------|
| `bash tools/check_translation.sh grade-1 id` … `grade-9 id` | **PASSED** (9 / 9) |
| `python3 tools/check_indonesian_prose.py` (142 files) | **OK — 0 issues** |
| `latexmk -g one_physics_book_1_primary_middle_school_id.tex` | exit 0 — **464 pp, 0 errors, 0 undefined, 0 overfull** |
| `grep -c '/id/' …_id.fls` | **1 278** |
| `link_defined_terms.py --book 1 --lang id --unwrap --apply` → `--apply` → `--check` | **every file matches what the config generates** |

## Defined-term link audit

| | English | Indonesian |
|---|---:|---:|
| Links | 6 483 | **6 799** (+4.9 %) |
| Distinct targets | 133 | **133** |
| Median per-target difference | — | **2 links** |
| Targets within ±20 % of the English count | — | 93 / 134 |

**Target-set diff — one swap, both explained.**

* English-only `def:g7:short-circuits-safety:battery` (24 links). English
  harvests that target from `\emph{battery's}`, a possessive that its
  morphology treats as a *different word* from "battery". Indonesian writes
  `baterainya`, which the `-nya` tail folds back into the grade-3 term
  `baterai`; the 24 links therefore land on
  `def:g3:first-electric-circuit:battery` — the chapter that actually
  defines a battery. A better link, not a lost one.
* Indonesian-only `ex:g8:sound-pitch-loudness:decibels` (3 links): the
  decibel ladder, which the English harvest happens not to reach.

**The one large density difference** is `ex:g2:measuring-time:clock`
(en 73, id 238). Indonesian `jam` is *hour*, *clock* and *watch* in one
word; English links only "hours" there. Every one of the 238 is the same
semantic family as the target (the clock example of grade 2), so this is
density, not wrong sense. `berjam-jam` ("for hours", adverbial) and the
`kilowatt-jam` compound are protected out.

**Wrong-sense links hunted and removed** (each verified by reading the
display/target pairs in the applied tree, not by trusting the totals):

| Word | Was | Fix |
|---|---|---|
| `menarik` | 86 links to the grade-1 **magnet** definition — but in this book it draws a current, hauls a rope, pulls a lever, and also means *interesting* | `DROP` |
| `kutub` | from grade 5 on, bare `kutub` is overwhelmingly the **battery terminal** (English says "terminal" there), yet it linked to the magnetic-pole definition | `STOP` (as English stops "pole"/"poles"; `kutub utara` / `kutub selatan` survive) |
| `tahun`, `panas`, `dingin`, `sekon`, `saat`, `malam`, `siang`, `lurus`, `melingkar`, `beraturan`, `berubah`, `terbuka`, `tertutup`, `indra`, `penglihatan`, `perabaan`, `penciuman`, `pengecapan` | ordinary vocabulary, ~900 links between them | `DROP` (the English config drops each of their English twins) |
| `Massa jenis` | the grade-7 definition opened with the term, so the **capitalised** display became a separate harvest entry pointing always at grade 7, even inside grade 6 | fixed in the source (`Yang disebut \emph{massa jenis}…`) |
| `Osiloskop` | likewise capitalised-only, so every lowercase `osiloskop` in running text went unlinked | fixed in the source (`Sebuah \emph{osiloskop}…`) |

## Terminology decisions — for `indonesian_style_card.md`

These are the rulings this book had to make; the main session should merge
them into §3 (Physics glossary) and §4 (homographs). They are consistent
with the Book 2 (`id`) glossary wherever the two books overlap.

| English | Indonesian | Note |
|---|---|---|
| light source | sumber cahaya | |
| shadow / umbra / penumbra | bayang-bayang / umbra / penumbra | `bayangan` is reserved for the **optical image**; `bayang-bayang` is the shadow. Kept apart in all 71 chapters |
| image (optical), real image | bayangan, bayangan nyata | |
| conductor / insulator | penghantar / isolator | thermal insulator: `isolator kalor` |
| series / parallel circuit | rangkaian seri / rangkaian paralel | matches Book 2 |
| switch / bulb / battery | sakelar / bohlam / baterai | battery **terminal** is `kutub` — see the homograph note below |
| short circuit | korsleting | verb: `mengorsletingkan`, adj. `terkorsleting` |
| fuse / circuit breaker | sekring / pemutus arus | |
| current, current intensity | arus, kuat arus | `kuat arus`, not `intensitas` |
| voltage, effective/nominal voltage | tegangan, tegangan efektif / tegangan nominal | |
| resistance / resistor | hambatan / resistor | |
| DC / AC | arus searah / arus bolak-balik | the abbreviations DC and AC are kept, as in Indonesian practice |
| power / energy / joule / watt | daya / energi / joule / watt | |
| kilowatt-hour | kilowatt-jam | |
| heat vs temperature vs hot | kalor / suhu / panas | never interchanged: `kalor` is the transferred quantity, `suhu` the reading, `panas` the sensation |
| melting / freezing / boiling / evaporation / condensation / sublimation | peleburan / pembekuan / pendidihan / penguapan / pengembunan / sublimasi | verbs: `mencair`, `membeku`, `mendidih`, `menguap`, `mengembun`. **`mencair`, not `meleleh`** — settled in grade 1 and swept through the whole book |
| mass / weight | massa / berat | `berat` is the force; `massa` never carries the sense "heavy" |
| density | massa jenis | not `kerapatan` |
| volume / displacement (water) | volume / pendesakan air | |
| force / newton / dynamometer | gaya / newton / dinamometer | |
| speed, average / instantaneous | kelajuan, kelajuan rata-rata / kelajuan sesaat | `kelajuan` (scalar), not `kecepatan` — Book 1 never needs the vector |
| trajectory / uniform / varied motion | lintasan / gerak beraturan / gerak berubah | |
| kinetic / potential energy | energi kinetik / energi potensial | |
| efficiency / renewable | efisiensi / terbarukan | |
| gravitation / gravitational constant / gravitational strength | gravitasi / tetapan gravitasi / kuat gravitasi | |
| orbit / axis / leap year | orbit / sumbu / tahun kabisat | |
| lens: converging / diverging | lensa cembung / lensa cekung | (not `konvergen`/`divergen`) |
| focal point / focal length | titik fokus / jarak fokus | |
| transparent / translucent / opaque | bening / baur / buram | one-word set, chosen so the three sort cleanly in a method's four steps |
| diffusion (of light) / primary source | pembauran / sumber primer | a diffusing object is a `benda pembaur` |
| spectrum / dispersion | spektrum / dispersi | |
| frequency / period / amplitude / pitch / loudness | frekuensi / perioda / amplitudo / nada / kenyaringan | |
| infrasound / ultrasound / decibel | infrasonik / ultrasonik / desibel | |
| medium (of sound) | medium | plural mentioned once as `media` |
| alternator / turbine / transformer / induction | alternator / turbin / trafo / induksi | |
| oscilloscope / sinusoid / peak voltage | osiloskop / sinusoid / tegangan puncak | |
| atom / nucleus / electron / order of magnitude | atom / inti / elektron / orde besaran | |
| light-year | tahun cahaya | |
| reaction / braking / stopping distance | jarak tanggap / jarak pengereman / jarak berhenti | |
| the marching current ("the march") | arak-arakan (verb `berarak`) | the book's running metaphor for the current; chosen over `pawai` because `berarak` gives the verb the metaphor needs |
| the relay (of sound) | estafet (verb `mengestafet`) | |

## Homographs met, and how they were handled

| Word | Senses | Ruling |
|---|---|---|
| `air` | **water** (Indonesian) vs English *air* | English *air* is `udara`. The two never meet; the prose gate deliberately does not flag `air` |
| `kutub` | magnetic **pole** vs battery **terminal** | Both senses are correct Indonesian and both are used. Because the terminal sense dominates from grade 5 on, bare `kutub` is `STOP`ped in the link config; `kutub utara` / `kutub selatan` remain terms |
| `menarik` | **attracts** vs **is interesting** vs **draws** (a current), **hauls** (a rope) | Used freely in prose; `DROP`ped from the link harvest — it cannot mean the magnet definition often enough to earn a link |
| `tegangan` | **voltage** vs rope/surface **tension** | Voltage throughout Book 1; `tegangan permukaan` protected |
| `berat` | **weight** (noun) vs **heavy** (adjective) | Both used; the adjectival collocations (`lebih berat`, `paling berat`, `terlalu berat`, …) are protected out of the link layer |
| `gaya` | **force** vs **style/manner** | `dengan gaya` ("with style", grade 9's orbiting cannonball) protected |
| `jam` | **clock** vs **hour** vs **watch** | One word, one target; see the link audit |
| `bayangan` / `bayang-bayang` | optical **image** vs **shadow** | Held strictly apart |
| `daya` / `usaha` | **power** / (mechanical) **work** vs everyday *capacity* / *effort* | Book 1 needs only `daya` = power; `usaha` is never used in the physics sense here, so no collision |
| `sisi` | **side** of a shape vs *aspect* | No physics term in Book 1 claims it |

## Words appended to the shared gate lists

Only `ID_MARKERS` was touched, append-only, with a reason per word. Nine
words were added — each of them unambiguously Indonesian (English spells
every one of them differently), so the `untranslated` class can still not
excuse an English sentence; each had fired on correct grade-1–9 prose where
a list-heavy or subordinate-clause sentence runs past eight words without
touching a marker already listed:

`dalam`, `kalau`, `begitu`, `saja`, `sesuatu`, `selalu`, `melainkan`,
`walaupun`, `meskipun`.

Nothing was added to `NOT_GATED` or `ALLOWED`, and no existing rule was
rewritten.

One convention worth recording: the required CC credit is written
`CC\ BY\ 4.0`. `visible_text` skips `\ ` and joins the tokens into `CCBY`,
which is not gated, while the page still renders `CC BY 4.0` with a
non-breaking interword space. Used in the four chapters that carry a
Commons photograph.

## Samples, verdicted

**1 — grade 2, chapter opening (native).**

> Sebuah jungkat-jungkit tergantung mendatar dengan seorang anak di tiap
> ujungnya. Menara balok berdiri --- tambah satu balok, dan ia runtuh.
> Seorang akrobat berjalan di atas tali yang lebih tipis daripada
> sepatunya. Ketiganya sedang memainkan permainan yang sama dan dalam:
> permainan keseimbangan, tempat gaya saling meniadakan dan tidak ada yang
> bergerak.

Three short concrete sentences, then one long one that names the idea — the
English rhythm, rebuilt with Indonesian means (`tempat` as a relative of
place, not a translated "where").

**2 — grade 6, a definition (native).**

> Yang disebut \emph{lintasan} sebuah benda yang bergerak adalah garis yang
> digambar oleh perjalanannya --- jalan yang ditorehkannya melalui ruang.

`Yang disebut … adalah …` is the standard Indonesian defining frame, and it
also keeps the term out of sentence-initial position so the link harvest
sees a lowercase display. This pattern was used deliberately throughout.

**3 — grade 8, chapter opening (native).**

> Satu pertanyaan telah mengekori seluruh kisah kelistrikannya: sebagian
> komponen membiarkan arak-arakannya menyerbu, yang lain mencekiknya
> menjadi rembesan --- lampu membelah tegangan secara tidak sama, kawat
> tipis menghangat, yang tebal tetap sejuk.

The English colon-and-dash architecture survives because Indonesian tolerates
it; the metaphor (`arak-arakan`, `menyerbu`, `rembesan`) is carried by
Indonesian words that actually collocate.

**4 — grade 9, an example (near-native).**

> Bohlam leluhur yang berpijar: lima persen cahaya, sembilan puluh lima
> persen kehangatan --- sebuah pemanas yang punya hobi.

"A heater with a hobby" lands, and `bohlam leluhur` for "the ancestor bulb"
reads naturally. Marked near-native only because `yang punya` is a shade
more colloquial than the surrounding prose; `yang mempunyai hobi` would be
stiffer and worse.

**5 — grade 7, a method step (native).**

> isilah alat suntik plastik dengan udara, tutup mulutnya dengan ujung
> jari, lalu doronglah penghisapnya: ia mengalah --- kamu dapat memaruh
> ruang udaranya, sambil merasakan perlawanan yang kenyal.

Procedural `-lah` on the first and last verb of the step, bare imperative in
the middle: the ordinary rhythm of an Indonesian lab instruction, not
`-lah` on every verb.

## Why not 100

* **Link density is 4.9 % above English, and one target is 3× English.**
  `jam` (hour/clock/watch) alone accounts for +165 of the +316. It is the
  right target, but the density is higher than a reader needs. Reducing it
  further would mean either stopping `jam` outright — losing the target and
  the parity — or a long list of collocation protections; I judged the
  trade-off not worth it and recorded it here instead. (−2 on the link
  dimension.)
* **Two morphological asymmetries remain in the link layer**, both benign
  and both documented above: the `baterainya` fold and the decibel ladder.
* **Two near-synonyms live side by side in grade 2** — `keseimbangan`
  (balance, the everyday game) and `kesetimbangan` / `setimbang`
  (equilibrium, the physics state), mirroring the English "balance" vs
  "equilibrium". They are correct and deliberate, but an Indonesian reader
  meeting both in one chapter title has to work slightly harder than the
  English reader does. (−1 on terminology.)
* **`-nya` density.** This edition marks definiteness with `-nya` far more
  often than a newspaper would — it is what carries the English definite
  article and the book's habit of pointing back at the object under
  discussion ("lampunya", "arak-arakannya"). It reads as textbook
  Indonesian, but a native editor might thin it in the grade-8/9 chapters.
  (−2 on register.)
* **Figure captions inside `omfigure` for the AI illustrations** are single
  long lines in the English source and were kept as single long lines; they
  are correct but are the one place where the Indonesian runs noticeably
  longer than the English. No box overflows.
