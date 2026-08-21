# Translation score — Physics Book 3 · Indonesian (`id`)

| Field | Value |
|-------|--------|
| **Book** | One Physics Book 3 (University, Year 1) — 30 chapters |
| **Language** | Indonesian (`id`) |
| **Quality bar** | **native academic** (English is the source of truth; the `id` editions of Physics 1–2 were the register exemplar, `book2_id.py` and `book3_en.py` the curation exemplars) |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-08-21 |
| **Scope of this pass** | Chapters 27–30 (bodies + solutions, 8 files) translated from the English canon; `tools/term_config/book3_id.py` written and curated from nothing; the whole `\omterm` layer generated and audited over all 60 files; both prose gates and the build brought green over the whole tree. Chapters 1–26 were translated in an earlier run of the same job and were re-audited, not re-translated. |

## Method

Not machine translation and not a hand-rewrite. Every file is a **line-range
patch on the English canon** applied through `tools/id_apply.py`: the
Indonesian replaces named ranges and every line not named is copied
byte-identically. Labels, `\cref` targets, `\begin{solution}{key}`,
`\foreach` lists, `xtick=`, coordinates, `\qty{}{}` and every math display
are therefore *the same bytes as English* and cannot drift.

The applier refuses to write a file that fails any census against its English
twin: ordered labels / environments / `\begin{solution}{}` / `\emph`–`\index`
adjacency / `\index` count / **ordered math spans** / drawing code / per-range
`\[ \]` counts / brace balance / surviving `\omterm` / the Indonesian prose
gate. Every rejection in this pass was a real defect: two moved line breaks
inside inline math (`$\times r/a$` rewritten as *dikalikan* `$r/a$`, which
silently deletes a math span), one dropped `\emph{}` on a defined term
(*fungsi kerja*), and one sentence of nine words that contained no Indonesian
function word. **One stanza per file, always** — the applier rebuilds each
target from English on every run, so splitting a long chapter across two
patch files would discard the first file's work in silence.

## Verdict in one line

Indonesian university-physics prose, written rather than converted:
*potensial elektrostatik*, *sirkulasi*, *permukaan ekuipotensial*, *momen
dipol*, *sangkar Faraday*, *efek ujung runcing*, *kapasitansi*,
*permeabilitas hampa*, *lintasan Ampère*, *gaya Laplace*, *momen magnetik*,
*gaya gerak listrik imbas*, *induktansi bersama*, *arus pusar*, *kumparan
suara*, *efek fotolistrik*, *potensial henti*, *kepadatan peluang*, *asas
ketakpastian*, *jari-jari Bohr*, *keadaan dasar*, *titik kuantum*, *efek
terowongan* — with a link layer that knows *selubung* is a fibre cladding
before it is the envelope of a damped oscillation, *inti* is a fibre core
before it is a nucleus, and *tegangan* is a voltage three times out of four.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Register / tone | **96** | Lecture register, not carried over: «Sebuah medan adalah tiga bilangan di setiap titik; sebuah potensial hanya satu.» «Sebuah jarum kompas berayun ketika kawat di dekatnya mengalirkan arus.» «Gerakkanlah sebuah magnet mendekati sebuah kumparan dan arus mengalir dalam kumparannya; hentikanlah magnetnya dan arusnya berhenti.» «Sinarilah sebuah logam yang bersih dengan cahaya ultraungu dan elektron terlontar keluar seketika.» Definitions open the way an Indonesian lecture opens them (*Yang disebut …*, *Terdapat sebuah fungsi skalar …*, *Misalkan …*); imperatives are `Hitunglah`, `Tunjukkan`, `Simpulkanlah`, `Periksalah`, `Sketsalah`; `sebesar` where English writes *of*. −4: a handful of appositive dashes are kept from English where an Indonesian lecturer might use a colon |
| Terminology | **96** | Named the way an Indonesian physics lecture names it: *kelajuan* vs *kecepatan* held apart, *massa jenis* never *kerapatan*, *usaha* for work, *kalor* vs *suhu* vs *panas* all distinct, *bayangan* (optical image) vs *bayang-bayang* (shadow), *hambatan* (quantity) vs *resistor* (component), *ggl* spelled out once as *gaya gerak listrik*. Chapters 27–30 add *keping* for a capacitor plate, *lilitan* for a single turn and *kumparan* for a coil, *solenoida*/*toroida*, *selongsong* for a cable sheath (so that *selubung* stays the fibre cladding), *pengeras suara*, *kerucut*, *kelos*, *ultraungu*. −4: `trace`/`rank` do not occur here, but `rms`, `dee`, `fret`, `slide` and `loop` are kept English because Indonesian keeps them |
| MT-artifact freedom | **96** | Gate 8 (`check_indonesian_prose.py`) green on all 60 files; `tools/check_latin_prose.py` (twin-comparison) reports only its cognate tiers — *retina*, *sensor*, *magnet*, *anode*, *resistor*, *adiabat*, *isobar*, *seismometer*, *volume*, and the `\text{}` abbreviations *orb*, *spin*, *rot*, *iso*, *loop* — plus one `dup` hit (`fret 5 … fret 12 …` in solutions 5) that is genuinely identical because *fret* is the Indonesian word and the rest is numerals. Two real defects it did catch: `\text{ind}` (induced) in ch. 29, now `\text{imb}`, and the reminder that `\qty{}{}` arguments are invisible to gate 8 — `\qty{1000}{turns/m}` (ch. 29) and `\qty{6.2e9}{protons/s}` (solutions ch. 17) are localized by hand to `lilitan/m` and `proton/s` |
| Structural fidelity | **99** | Exact mirror over 60 files: 89 `definition`, 57 `theorem`, 132 `proposition`, 6 `corollary`, 117 `example`, 48 `remark`, 25 `method`, 2 `notation`, 360 `exercise`, 30 `problem`, 171 `proof`, 390 `solution`, 129 `tikzpicture`, 55 `axis`, 150 `omfigure` — every count identical to English. 360 `exo:` labels EN / 360 ID; 30 `pb:` EN / 30 ID. `check_translation.sh bachelor-1 id`: **PASSED** |
| LaTeX hygiene | **99** | **0 errors, 0 undefined references, 0 overfull boxes, 0 “invalid in math mode”**; 35 underfull vboxes against English's 33; 352 pages against English's 332. `grep -c '/id/'` in the `.fls`: **540** — the Indonesian bodies really are in the build. `nullfont` = 65, the same count as every other edition including English (pgfplots measuring `xmin=0.01` on three log-axis figures) |
| Cross-refs / rule compliance | **99** | `\label`, `\cref`/`\ref` targets and `\begin{solution}{key}` byte-identical to English; solution headers `\section*{Bab \ref{ch:…} --- <judul>}` with the `ch:` slug untouched. **Zero** curriculum, ministry, country or track names; the cross-volume pointer reads «jilid Tahun ke-2». Decimal **point** kept everywhere, in prose and in math. `-nya` attached, reduplication with a bare hyphen, `di`/`ke` separated as prepositions and attached as prefixes (checked by grep: the only `ke dua` is the preposition + numeral in «beralih ke dua benda») |
| Figures | **98** | All 129 `tikzpicture` and 55 `axis` bodies byte-identical to English — coordinates, `\foreach` numerics, `xtick`/`ytick`, `samples`, `\addplot` expressions, options. Only node text, axis labels and `{\small …}` captions localized: *kawat lurus ($I$ menuju pembaca)*, *solenoida (penampang): seragam di dalam*, *persegi panjang Ampère*, *magnet: medan dipol, garisnya dari U ke S* (the magnet poles are **U**/**S**, not N/S), *batang luncur: fluks tumbuh, $\vect F$ mengerem*, *kumparan suara*, *kepadatan peluang $\|\psi\|^2$*, *tingkat hidrogen (skala termampat)* |
| Solutions | **97** | All 360 exercise solutions and all 30 weekend-problem solutions present and native, including the four written in this pass (Millikan's oil drop, the coaxial cable / power line / galvanometer, the bicycle dynamo and loudspeaker, the hydrogen spectrum and the quantum dot) |
| Defined-term links (`\omterm`) | **95** | **2 515 links across 60 files**, 107.4 % of English's 2 342 on the same text — between Portuguese (1.07×) and French (1.04×). **Full target parity**: every English target present in the Indonesian course bodies, plus 15 Indonesian-only targets. Per-target counts audited display by display; the residual excess is two documented one-word-covers-two families, not wrong sense |

## The link layer — what this book cost

`tools/term_config/book3_id.py` did not exist. Curating it from the harvest,
then diffing the **per-target counts** against English (target-set parity
alone proves nothing), found six defects that no gate can see:

1. **`hukum` must NOT be in `NOT_A_TERM` for this book.** `book2_id.py` has
   it, and copying it silently suppressed fourteen named results — *hukum
   Ampère*, *hukum Gauss*, *hukum Faraday*, *hukum Coulomb*, *hukum Lenz*,
   *hukum Snell*, *hukum Kepler*, *hukum Kirchhoff*, *hukum Hooke*, *hukum
   Stokes*, *hukum Biot–Savart*, … — because `harvest.py` tests plain
   substring containment. English's default blocks the *phrase* `"law of"`,
   which never fires on *Ohm's law*; its literal Indonesian translation
   would swallow every named law. The rest of the list translates word for
   word and is symmetric: `theorem`/`teorema`, `rule`/`aturan`,
   `principle`/`asas`, `formula`/`rumus`, `identity`/`identitas`.
2. **`\emph{Lensa} adalah …` cost 76 links.** The capitalized display is a
   separate harvest entry (style card §4b.3), so lowercase `lensa` was not a
   term at all: 10 links where English's `lens` has 64. Fixed at the source,
   `Yang disebut \emph{lensa} adalah …` — the §4c.1 convention. **The check
   is mechanical and worth running on every `id` book**: list every
   capitalized harvest entry whose lowercase twin is *not* a term, and count
   the lowercase form in the corpus. On this book it returned exactly one
   real hit (`Lensa`, 76 occurrences) and two harmless ones (`ARQS`, `SI`).
3. **`okuler` and `objektif` reached nothing.** English harvests *eyepiece*
   (32 links) and *objective* (23); the Indonesian definition spells them
   *lensa okuler* / *lensa objektif*, and the prose then uses the bare heads
   47 and 28 times. Declared in `EXTRA` — the same failure as `gesekan` in
   `book2_id.py`.
4. **`selubung` is a new homograph family.** Fibre cladding (ch. 2), the
   *envelope* of a damped oscillation (chs. 5, 7) and of a beat, a hot-air
   balloon envelope (chs. 20, 21) and a coaxial *sheath* (ch. 26): 15 of 20
   links were the wrong sense against English's 4 for *cladding*. Stoplisted;
   chapter-local links survive. Chapters 27–30 use **`selongsong`** for a
   cable sheath so the collision does not grow.
5. **`titik tanah`** is the electrical ground point of ch. 6 and the
   sub-satellite point of the ground track in ch. 16. Stoplisted.
6. **`panjang gelombang`** generated 38 links English does not have: English
   defines *wavelength* twice and its ambiguity policy drops it, while
   Indonesian spells the de Broglie one differently and kept it. Stoplisted
   for parity.

`tegangan` is **masked, not stoplisted** (§4c.3): voltage 145 times against
27 rope/surface/material tensions, so eighteen `EXTRA_PROTECT` patterns read
off the mechanics chapters keep both senses. After masking, every link to
`def:b1:dc-circuits:voltage` outside chapters 6–10, 14, 17, 26, 27, 29 is
gone.

**Two divergences are deliberate and are not defects** (§4c.4): `lintasan`
covers English's *path* (never linked) and *trajectory* (linked), 62 links
against 13; and several Indonesian compounds are harvested where the English
single word was dropped as ambiguous — *lebar pita* (bandwidth, 18),
*gaya hambat* (drag, 19), *gaya apung* (buoyancy, 15), *pengeras suara* (10).
Every one is right in sense.

## Samples

| # | Passage | Verdict |
|---|---------|---------|
| 1 | Ch. 1 opening (not written in this session): «Di sebuah laboratorium di ruang bawah tanah sebuah bandul berayun, sebuah stopwatch berdetak, dan seorang mahasiswa menuliskan $g = \qty{9.77}{m/s^2}$. Apakah itu nilai yang ``benar''? … Fisika mengukur, dan pengukuran tanpa ketidakpastiannya hanyalah kabar angin.» | **native** |
| 2 | Ch. 20 opening: «Udara di dalam sebuah ruang kelas seberat seorang dewasa, dan memuat lebih banyak molekul daripada butir pasir di Bumi, masing-masing terbang dengan laju peluru senapan dan bertumbukan sepuluh miliar kali tiap sekon dengan tetangganya. Tak seorang pun dapat mengikuti satu di antaranya; tak seorang pun perlu.» | **native** |
| 3 | Ch. 27 definition: «Sebuah penghantar terkucil pada potensial $V$ mengemban muatan $Q$ yang sebanding dengan $V$: $Q = CV$, dengan $C$ yang disebut \emph{kapasitansi}-nya (farad, \unit{F}) … Yang disebut \emph{kapasitor} adalah sepasang penghantar (\emph{keping}) yang mengemban muatan berlawanan $\pm Q$ dan saling berhadapan sehingga medannya terkurung di antara keduanya.» | **native** |
| 4 | Ch. 28 example: «Sebuah kawat \qty{10}{A} pada \qty{1}{cm}: … empat kali medan Bumi --- kompasnya memang berayun. … dengan teras besi berpermeabilitas nisbi $1000$, beberapa tesla akan menyusul seandainya besinya tak menjenuh dekat \qty{2}{T} --- langit-langit setiap elektromagnet.» | **native** |
| 5 | Ch. 30 opening: «Kirimkanlah elektron satu demi satu lewat dua celah dan mereka mendarat sebagai titik, masing-masing di satu tempat --- dan titik-titiknya menumpuk, setelah beribu-ribu, menjadi rumbai sebuah gelombang. Kedua kenyataan itu tak muat dalam fisika dua puluh sembilan bab pertama.» | **native** |
| 6 | Solutions ch. 29 (weekend problem): «Kopel Laplace arus imbasnya melawan putarannya (Lenz); energi lampunya datang dari kaki pengendaranya, sebanyak \qty{5.7}{W}.» | **near-native** — compact to the point of terseness, as the English is |

## Why not 100

* **Link density is 1.07× English**, driven by `lintasan` (62 vs 13) and by
  four Indonesian compounds that survive an ambiguity check English fails.
  Every link is right in sense, but the page is a little busier than the
  English page.
* **Six single English words survive inside `\text{}` and TikZ nodes** as
  abbreviations an Indonesian lecturer would also write (*orb*, *spin*,
  *rot*, *iso*, *loop*, *dee*). Defensible, not invisible.
* **A few appositive em-dash chains** are kept from the English sentence
  rhythm where an Indonesian lecturer might restructure into two sentences.
* **`\qty{}{}` arguments are outside every automated gate.** Two were English
  in the canon and were localized by hand; a third reader would have to
  re-check them by eye, which is not a property a shipped edition should
  have.

## Notes for `indonesian_style_card.md`

The style card is read-only for this agent. These are the decisions this tree
now embodies, for the main session to merge:

1. **`hukum` out of `NOT_A_TERM` for university physics** (item 1 above), with
   the reason: `harvest.py` tests substring containment, so a bare keyword is
   symmetric between the languages and a *phrase* keyword is not.
2. **The capitalized-display check should be a routine, not a warning.** One
   command lists every capitalized harvest entry whose lowercase twin is not
   a term; on this book it found `Lensa` (76 lost links) in one shot.
3. **`selubung`** joins the homograph table: cladding / envelope of a damped
   oscillation / balloon envelope / coaxial sheath. Use **`selongsong`** for
   a cable sheath to keep the two apart.
4. **`okuler` / `objektif`** join the “term whose head the prose drops” family
   next to `gesekan`.
5. **Indonesian TikZ node text runs 15–20 % longer than English**, so a node
   centred under a `scope` can push a two-scope picture overfull where English
   fits. Two of the four chapters written in this pass did; both were fixed by
   shortening the node, never the drawing.
6. **A comma-separated numeral run inside one `$…$` is unbreakable in Latin
   script too.** The Arabic finding generalizes: `$0.02, -0.05, 0.08, …$`
   overflowed once the Indonesian word before it grew. Splitting it into one
   math group per number restores the break points and changes nothing on the
   page.
7. **`\text{}` subscripts are visible text and must be localized** —
   `\text{ind}` → `\text{imb}`, `\text{air}` → `\text{udara}`,
   `\text{enclosed}` → `\text{dalam}`. `tools/check_latin_prose.py` is the
   only gate that sees them.
