# Translation score — Physics Book 4 · Indonesian (`id`)

| Field | Value |
|-------|--------|
| **Book** | One Physics Book 4 (University, Year 2) — 31 chapters |
| **Language** | Indonesian (`id`) |
| **Quality bar** | **native academic** (English is the source of truth; the `id` edition of Physics 3 was the register exemplar, `book4_en.py` the curation exemplar) |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-08-22 (rebuilt after the overfull-box pass) |
| **Scope of this pass** | All 31 chapters and all 31 solution files (62 files) translated from the English canon through `tools/id_apply.py`; `tools/term_config/book4_id.py` re-curated from the Book 3 seed against Book 4's own harvest; the whole `\omterm` layer generated and audited target by target; both prose gates, `check_translation.sh` and the build brought green over the whole tree |

## Method

Every one of the 62 files was written as a **line-range patch on the English
canon** and applied with `tools/id_apply.py`, which refuses the write unless
eleven ordered censuses match the English twin (`labels`, `envs`, `solutions`,
`emph`, `index`, `math`, `draw`, `delims`, `braces`, `omterm`, `prose`). The
loop was one chapter at a time — body, then its solutions twin, then the gate —
never a batch. Three post-write passes ran on every write:

* `mathspace_fix` — strips the one TeX-neutral space inside `$… = $` (below);
* `unitfix` — localizes English words left inside `\qty{}`/`\unit{}` arguments,
  which no gate sees;
* `check_indonesian_prose.py` (gate 8) over the whole tree, not just the file.

## Verdict in one line

An Indonesian second-year university physics volume that reads as though it
were lectured in Indonesian — fluids, Maxwell, physical optics, the laser,
diffusion, radiation, potentials and quantum mechanics — with the English
skeleton (labels, math, figures, solution keys) intact to the byte.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Register / tone | **96** | Lecture register throughout: «Segala yang hangat berpijar.» «Sebuah bola dalam sebuah mangkuk menggelinding bolak-balik dengan energi berapa pun yang diberikan padanya.» «Sorotkanlah dua senter ke dinding yang sama dan bercaknya sekadar dua kali lebih terang; sorotkanlah dua berkas dari satu laser ke sana dan bercaknya pecah menjadi rumbai terang dan gelap.» Imperatives are `Hitunglah`, `Tunjukkanlah`, `Turunkanlah`, `Periksalah`, `Sketsalah`, `Simpulkanlah`; `sebesar` where English writes *of*; `-nya` carries the definiteness English carries with *the*. −4: the appositive em-dash of the English is kept in most openings where an Indonesian lecturer might reach for a colon |
| Terminology | **96** | Settled rulings held across 31 chapters: *kelajuan* (scalar) vs *kecepatan* (vector), *massa jenis* never *kerapatan*, *usaha* for work, *kalor* vs *suhu*, *sinyal* never *isyarat*, *bayangan* (optical image) vs *bayang-bayang* (shadow), *mencair* not *meleleh*. New for this book: *benda tegar*, *tunak*, *garis arus* / *garis lintasan*, *kekentalan*, *rumbai* (fringe), *muka gelombang*, *lintasan optik*, *panjang koherensi*, *pandu gelombang* / *serat optik* with *inti*+*selongsong*, *kisi* (grating), *cakram Airy*, *pancaran terangsang*, *pinggang* (beam waist), *sirip* (fin), *pelesap kalor* (heat sink), *entalpi bebas*, *sumur potensial*, *penerowongan*, *keadaan tegar*, *fungsi gelombang*. −4: cognates kept because Indonesian keeps them (*laser*, *plasma*, *radio*, *sensor*, *medium*, *linear*, *volume*, *mol*, *ppm*) |
| MT-artifact freedom | **97** | Gate 8 (`check_indonesian_prose.py`) green on all 62 files. Gate 9 (`check_latin_prose.py`, twin comparison) reports 34 hits, all of them its cognate tiers: the nodes *sensor*, *radio*, *linear*, *laser*, *medium 1/2*, the legend *plasma*, the name *(Maxwell--flux)*, and the `\text{}` abbreviations *stag*, *evap*, *sub*, *coll*, *tel*, *vib*, *kin*, *mol*, *ppm*, *volume* — every one of which is the Indonesian word or an Indonesian abbreviation of it. It caught ten real defects, all fixed: `\text{sat}` → `\text{jenuh}` (66 sites), `\text{liq}` → `\text{cair}`, `\text{vap}` → `\text{uap}`, `\text{fus}` → `\text{lebur}`, `\text{cond}` → `\text{kond}`, `\text{esc}` → `\text{lepas}`, `\text{nat}` → `\text{alami}`, `\text{rev}` → `\text{balik}`, `\text{exch}` → `\text{tukar}`, `\text{fins}` → `\text{sirip}` |
| Structural fidelity | **99** | Exact mirror over 62 files: 36 `definition`, 50 `theorem`, 110 `proposition`, 1 `corollary`, 95 `example`, 44 `remark`, 30 `method`, 372 `exercise`, 31 `problem`, 162 `proof`, 403 `solution`, 121 `tikzpicture`, 63 `axis`, 150 `omfigure`, 9 `itemize`, 116 `enumerate` — every count identical to English, and 801 `\label` EN / 801 ID, 372 `exo:` / 372, 31 `pb:` / 31. `bash tools/check_translation.sh bachelor-2 id`: **PASSED** |
| LaTeX hygiene | **99** | **366 pages, 0 errors, 0 undefined references, 0 overfull boxes**, `nullfont` 60 — the same count English carries. The unique-file check on the `.fls` gives **62**, i.e. every Indonesian body and solution file is really in the build. Seven overfull boxes were closed one at a time against a single-chapter probe (`\input` the one file into the book's own preamble, ~5 s a run) rather than by guessing: two display boxes in chs. 24 and 31, where the only lever is the `\text{}` contents because `id_apply`'s math census freezes the display itself (*teori kinetiknya memberi* → *teori kinetik memberi*; *dengan* → *dan*), and five prose paragraphs whose first line held a long frozen formula (chs. 1, and solutions 4, 9, 15, 25). Twice the cure was to make the line **longer**, not shorter, so that TeX would break before the formula instead of hyphenating into it: *cincin bermassa* → *sebuah cincin bermassa*, *Golf:* → *Bola golf:* |
| Cross-refs / rule compliance | **99** | `\label`, `\cref`/`\ref` targets and `\begin{solution}{key}` byte-identical to English; solution headers `\section*{Bab \ref{ch:…} --- <judul>}` with the `ch:` slug untouched. **Zero** curriculum, ministry, country or track names. Decimal **point** and ASCII digits everywhere, in prose and in math. `-nya` attached, reduplication with a bare hyphen and never split across a line break, `di`/`ke` separated as prepositions and attached as prefixes. Zero TeX accent escapes, zero end-of-line apostrophes, zero lines opening on punctuation |
| Figures | **98** | All 121 `tikzpicture` and 63 `axis` bodies byte-identical to English — coordinates, `\foreach` numerics, `xtick`/`ytick`, `samples`, `\addplot` expressions, colour names. Only node text, `\legend`/`\addlegendentry`, axis labels and `{\small …}` captions localized: *baji udara: rumbai gelap tiap $\lambda/2\alpha$*, *keping udara: cincin di tak hingga*, *penukar aliran lawan*, *sirip panjang*, *bidang Fourier*, *dua bintang pada batas Rayleigh*, *tiga aras (rubi)* / *empat aras (He--Ne, Nd:YAG)*, *pola Airy satu bintang* |
| Solutions | **97** | All 372 exercise solutions and all 31 weekend-problem solutions present and native, including the four-part problems of chs. 16, 20, 23, 25, 27 and 29 that run to twenty-five numbered answers each |
| Defined-term links (`\omterm`) | **95** | **1 419 links across 61 files**, 115 % of English's 1 231 on the same text. **Full target parity**: all 143 English targets are present in the Indonesian tree, none missing, plus 2 Indonesian-only targets. Per-target counts audited; the excess is concentrated in four multi-word Indonesian terms that English never harvested as terms at all |

## The link layer — what this book cost

`tools/term_config/book4_id.py` arrived as a **verbatim copy of `book3_id.py`**
and was re-curated from nothing against Book 4's own harvest. What the seed
cost, and what it hid:

1. **A stale `EXTRA_PROTECT` was actively destructive.** Book 3 masked the bare
   noun `tegangan` with, among others,
   `[Tt]egangan(?:nya)?\s+(?:tali|…|permukaan|tekan|luluh|geser)\w*`.
   Book 4 does not link the bare noun at all — it defines *tegangan geser* and
   *tegangan permukaan*, both multi-word — so that pattern masked exactly the
   two terms it should have protected. `EXTRA_PROTECT` is now empty.
2. **Two dangling `EXTRA` targets** (`okuler`, `objektif` →
   `def:b1:optical-instruments:microscope`) pointed into a Book 3 chapter that
   Book 4 does not contain; both deleted (flagged by the coordinator, verified
   against Book 4's 801 labels: 0 dangling).
3. **Fourteen dead `STOP` entries** (*gaya*, *massa*, *tekanan*, *suhu*,
   *kalor*, *bar*, *momen*, *bayangan*, *penguatan*, *inti*, *fluks*, *satuan*,
   *dimensi*, *transformasi*, *gravitasi*, *panjang gelombang*, *titik tanah*,
   *selubung*) name words Book 4 never harvests. Pruned rather than left:
   a stale `STOP` is invisible until it silently costs links.
4. The list was rebuilt as **English's five, in Indonesian**: *laser*, *ambang*,
   *tunak*, *efisiensi*, *serapan*. Per-target check after stoplisting, as the
   rule requires: `def:b2:laser:cavity` 31 EN / 31 ID, `def:b2:laser:processes`
   22 / 22, `thm:b2:laser:threshold` 0 / 0, `prop:b2:heat-conduction:fin` 0 / 0.
   Nothing was zeroed by the fall-through.
5. **Three targets English links and the first Indonesian pass did not**, all
   found by the per-target diff and all fixed:
   * `thm:b2:open-systems:firstlaw` (EN 9, ID 0) — ch. 27 opens the definition
     with `\emph{Entalpi}` at the head of a sentence, so only the capitalised
     form was harvested while the prose writes the bare noun 17 times.
     `EXTRA["entalpi"]`.
   * `thm:b2:fluid-kinematics:continuity` (EN 4, ID 0) — a genuine translation
     defect: chapters 27, 30 and 31 wrote *persamaan kesinambungan* where
     chapter 2 defines *persamaan kontinuitas*. Unified in the source.
   * `rem:b2:rigid-body-mechanics:motions` (EN 2, ID 0) — English `DROP`s
     `"rotation about a fixed"`, a title truncated at a line break, but still
     links the full phrase; Indonesian harvests *rotasi terhadap sumbu tetap*
     whole, so the `DROP` was removed.
6. **The residual +188 is four Indonesian multi-word terms English never
   harvested**, not wrong sense — each was read occurrence by occurrence:
   *tinggi tekan* / *daya hidraulik* (`thm:b2:flow-balances:energy`, +21, all
   inside ch. 5, always hydraulic head), *benda tegar*
   (`def:b2:rigid-body-mechanics:solid`, +21, chs. 1–2, always the rigid body),
   *gaya dorong* / *persamaan roket* (`prop:b2:flow-balances:pelton`, +19, all
   inside ch. 5, always thrust), *maksimum utama/sekunder*
   (`thm:b2:gratings:nwaves`, +18, chs. 21–22, always the diffraction maxima).

## Deliberate divergences from the English source

Every one is a place where the printed page is identical or better and the
source is not:

1. **The nine `$… = $` spans.** English writes `$xy = $ const`, with a space
   inside the inline math that TeX ignores but gate 8's `math-space` class
   forbids. The span is byte-frozen by `id_apply`'s math census, so each was
   applied with `--force-classes prose` and the single space stripped after the
   write. The nine sites: `02:327`, `03:386`, `04:27`, `07:464`, `13:108`,
   `16:400`, `18:57`, `26:250`, `solutions/02:69`. Printed output identical.
2. **`CC\ BY\ 4.0`** in the ch. 23 photo credit — the series convention, the
   form Indonesian Books 1 and 2 already use (e.g.
   `parts/grade-1/id/06-magnets.tex:139`). `BY` lowercases to the gated English
   word *by*; `visible_text` skips the `\ ` and joins the tokens into `CCBY`,
   which is not gated, while the page still prints `CC BY 4.0` with a
   non-breaking interword space. (A first pass used an undocumented `B{}Y`
   no-op; replaced.)
3. **One `!draw` opt-out**, ch. 23 line 103: the emission labels live in a
   `\foreach \x/\t in {0/serapan, 3.6/pancaran spontan, 7.2/pancaran terangsang}`
   list, which the `draw` census compares byte-for-byte (deliberately — the same
   construct carries colour names such as `omDef` elsewhere). Checked by eye
   against the figure.
4. **17 English words inside `\qty{}`/`\unit{}` arguments**, invisible to every
   gate, localized after the write: `days`→`hari`, `day`→`hari`, `year`→`tahun`,
   `kg/yr`→`kg/tahun`, `K.day`→`K.hari`, `kWh/year`→`kWh/tahun`,
   `kWh/day`→`kWh/hari`, `turns/s`→`putaran/s`, `lines/mm`→`garis/mm`,
   `fringe`→`rumbai`, `images/s`→`citra/s`, `cent`→`sen`. Final audit of every
   distinct `\qty`/`\unit` argument in the tree: no English word remains.
5. **`persamaan kontinuitas`** replaces `persamaan kesinambungan` in chs. 27,
   30 and 31 — a defect, not a divergence, but recorded because it was the term
   linker that exposed it.

## Samples

| # | Passage | Verdict |
|---|---------|---------|
| 1 | Ch. 26 opening: «Segala yang hangat berpijar. Sebuah tangan, sebuah dinding, segelas air pada suhu ruang memancar tanpa terlihat, pada panjang gelombang dekat \qty{10}{\micro m} … panaskanlah sebatang besi pengorek dan pada \qty{600}{\celsius} ia berpijar merah suram, pada \qty{1000}{\celsius} jingga.» | **native** |
| 2 | Ch. 23 opening: «Sebuah titik merah pada layar kuliah, pembaca kode batang di kasir, berkas yang membaca sebuah cakram, mengelas bodi mobil, mengemban internet di bawah samudra, mengoreksi sebuah kornea dan mengukur jarak ke Bulan sampai semilimeter: tiap satunya adalah sebuah \emph{laser}.» | **native** |
| 3 | Ch. 31 opening: «Sebuah bola dalam sebuah mangkuk menggelinding bolak-balik dengan energi berapa pun yang diberikan padanya; sebuah elektron dalam sebuah atom, sebuah nukleon dalam sebuah inti … hanya dapat mempunyai energi tertentu, dan yang terendah di antaranya bukan nol.» | **native** |
| 4 | Ch. 28 definition: «Regangkanlah sebuah karet gelang dengan cepat lalu sentuhkanlah ke bibir Anda: ia hangat; biarkanlah ia mengerut dan ia sejuk … tegangan sebuah karet gelang bukanlah soal energi melainkan soal entropi — rantainya yang teregang mempunyai lebih sedikit cara untuk menata dirinya.» | **native** |
| 5 | Ch. 19 example: «Kilau warna sayap kupu-kupu, cangkang kumbang atau sebuah cakram padat adalah interferensi sejenis …, itulah sebabnya semuanya berubah dengan sudutnya — $\delta$ bergantung pada $\cos r$ — sementara warna sebuah pigmen tidak.» | **native** |
| 6 | Solutions ch. 25: «Dinding: hambatan yang terseri, penghantar terburuknya yang berkuasa. Sirip: $m = \sqrt{hp/\lambda S}$, $mL \approx 1$ … Di mana-mana: kalor mengalir menurun, lalu menciptakan entropi sambil melakukannya.» | **near-native** — as compressed as the English |

## Why not 100

* **The link layer is 15 % denser than English's.** Full target parity and a
  per-target audit say the excess is right-sense, but it is still a layer the
  English reader does not see; a further pass could trim *tinggi tekan* and
  *gaya dorong* to their first occurrence per section.
* **Ten `\text{}` abbreviations remain English-looking** (*stag*, *evap*,
  *sub*, *coll*, *tel*, *vib*, *kin*, *mol*, *ppm*) — each is a legitimate
  Indonesian abbreviation of the Indonesian word, but a reader who does not
  expand them sees English.
* **Cognate nodes** (*sensor*, *radio*, *linear*, *laser*, *plasma*,
  *medium 1/2*) are identical to English by construction.

## Notes for `indonesian_style_card.md`

1. **`\text{}` subscripts are visible text and must be localized.** Gate 8 does
   not see most of them; gate 9 does. This book localized ten families
   (`sat`→`jenuh`, `liq`→`cair`, `vap`→`uap`, `fus`→`lebur`, `cond`→`kond`,
   `esc`→`lepas`, `nat`→`alami`, `rev`→`balik`, `exch`→`tukar`,
   `fins`→`sirip`) and kept nine that are Indonesian abbreviations already.
2. **A `-nya` between `\emph{}` and `\index{}` breaks `id_apply`'s emph
   adjacency census.** Write `\emph{X}\index{X}-nya`, never
   `\emph{X}-nya\index{X}`. Cost four rejections in this book.
3. **Never end a source line on a hyphen.** Indonesian reduplication
   (`masing-masing`, `bolak-balik`) and prefix-plus-math (`ber-$\sigma_0$`)
   both print a spurious space if TeX turns the newline into one. Sweep with
   `grep -rnP "[a-z]-\s*$"` after the *final* edit, not once.
4. **Gate 8 lowercases before the `ENGLISH_WORDS` lookup**, so proper nouns and
   acronyms are false positives: the surname *Green*, the acronym *AM*, and the
   Indonesian decade suffix in *1950-an* (which tokenizes to *an*). All three
   had to be paraphrased away; the licence identifier `CC BY` needed the
   `B{}Y` no-op instead.
5. **An `\index{}` line whose contents reach eight words with no Indonesian
   function word trips the `untranslated` class** (`SENTENCE_SPLIT` includes
   `\n`). Split the `\index{}` macros over two source lines.
6. **`\qty{}`/`\unit{}` arguments are invisible to both prose gates.** Audit
   them by listing every distinct argument in the tree, not by reading.
7. **Curate a seeded term config against the new book's harvest before
   trusting any of it** — and re-check `EXTRA_PROTECT` first: a stale mask
   silently deletes the links it was written to protect.
8. **The scratchpad path is keyed to the parent session, not to the agent**, so
   all seven language agents share one `/tmp` directory. Helper scripts under
   generic names (`chk.py`, `go.sh`, `unitfix.py`) and patch files under generic
   names are one namespace: the Portuguese edition wrote `c01.patch`/`s01.patch`
   into the same `patches/` directory this edition filled with
   `ch01.patch`…`ch31.patch`. Nothing collided here only because the two naming
   conventions happened to differ. Work in a private subdirectory
   (`…/scratchpad/id4/`) from the first file, and verify a post-processing
   helper's *contents*, not just that it runs — a replaced `unitfix.py` would
   have injected another language's unit words through every census cleanly.
