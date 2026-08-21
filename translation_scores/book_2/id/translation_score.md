# Translation score — Physics Book 2 · Indonesian (`id`)

| Field | Value |
|-------|--------|
| **Book** | One Physics Book 2 (High School, grades 10–12) |
| **Language** | Indonesian (`id`) |
| **Quality bar** | **native academic** (EN is the source of truth; the `pt` edition of the same book was the method exemplar for term curation, the math `id` edition the register exemplar) |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-08-21 |
| **Scope of this pass** | Full translation of all 70 bodies (35 chapters + 35 solution files) from the English canon, by line-range patch; a curated `tools/term_config/book2_id.py` (was a 24-line seed with every set empty); a regenerated `\omterm` layer; one appended word in `tools/check_indonesian_prose.py`. |

## Method

Not machine translation and not a hand-rewrite. Every file is a **line-range
patch on the English canon**: the Indonesian replaces named ranges, and every
line not named is copied byte-identically. Labels, `\cref` targets,
`\begin{solution}{key}`, `\foreach` lists, `xtick=`, coordinates, `\qty{}{}`
and every math display are therefore *the same bytes as English* and cannot
drift.

The applier refuses to write a file that fails any census against its English
twin: ordered labels / environments / `\begin{solution}{}` / `\emph`–`\index`
adjacency / `\index` count / **ordered math spans** / drawing code / per-range
`\[ \]` counts / brace balance / surviving `\omterm` / the Indonesian prose
gate. Every rejection in this pass was a real defect, never a false alarm —
the classes that fired most were *envs* (a range that swallowed its
`\end{...}`), *math* (a moved line break inside a formula) and *prose*
(`english: 'The'` on an environment title started one line too late, exactly
the failure the brief predicts).

## Verdict in one line

Indonesian high-school physics prose, written rather than converted:
*momentum*, *kerangka acuan inersial*, *gaya pemulih*, *berat semu*,
*percepatan sentripetal*, *laju terminal*, *pseudoperiode*, *tetapan
peluruhan*, *defek massa*, *energi ikat tiap nukleon*, *potensial henti*,
*fungsi kerja*, *waktu diri*, *pemuluran waktu*, *pengerutan panjang* — with
a link layer that knows *tegangan* is two quantities, *inti* is a fibre core
before it is a nucleus, and *berat* is sometimes just an adjective.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Exact mirror: 35 chapters, 35 solution files, **525 `exo:` labels EN / 525 ID**, **35 `pb:` EN / 35 ID**, **560 `solution` environments EN / 560 ID**, and per-environment parity across the board (180 `definition`, 31 `theorem`, 83 `proposition`, 159 `example`, 119 `remark`, 38 `method`, 2 `notation`, 525 `exercise`, 35 `problem`, 67 `proof`, 149 `tikzpicture`, 6 `circuitikz`, 34 `axis`, 137 `omfigure`). `check_translation.sh grade-10/11/12 id`: **PASSED**, three times |
| Terminology | **96** | School-textbook register throughout, and the physics is named the way an Indonesian textbook names it: *gerak lurus berubah beraturan*, *gerak melingkar beraturan*, *kerangka Frenet*, *kekekalan momentum*, *koefisien gesekan*, *bidang miring*, *hukum jatuh bebas Galileo*, *sudut lontar*, *jangkauan*, *waktu terbang*, *hari sideris*, *setengah sumbu panjang*, *tetapan waktu*, *rezim pseudoperiodik/aperiodik*, *penghalang Coulomb*, *reaksi berantai*, *massa kritis*, *batang kendali*, *panjang gelombang de Broglie*, *keserentakan*. `sebesar` where English writes *of*; every quantity named with symbol and unit. −4 for two lexical choices that cost link parity: the book says *laju* for speed where the defined term is *kelajuan*, and *periode/frekuensi* are re-defined in the circular-motion chapter only after an edit forced by the audit |
| Register / tone | **96** | Written Indonesian, not carried over: «Amatilah sebuah mobil menempuh bundaran dengan tetap \qty{30}{km/h}: jarum penunjuknya tidak pernah bergerak, namun setiap penumpang merasa tertarik ke samping.» «Selundupkanlah sebuah timbangan badan ke dalam lift.» «Putarlah tombol berat sebuah radio loteng dan stasiunnya berbaris melewati jarumnya.» English appositive dashes kept where Indonesian also uses them; imperatives in the `-lah` form the register expects (*Tunjukkan*, *Perhatikanlah*, *Hitunglah*, *Simpulkanlah*) |
| LaTeX hygiene | **98** | **0 errors, 0 undefined references, 0 overfull boxes**; 136 underfull vboxes against English's 129. `latexmk -g` from a cleared `.aux` **converges** and exits 0 — see "The page-count oscillation" below. `grep -c '/id/'` in the `.fls`: **630** — the Indonesian bodies really are in the build, not English falling through |
| Cross-refs / rule compliance | **99** | `\label`, `\cref`/`\ref` targets and `\begin{solution}{key}` byte-identical to English. **Zero** curriculum, ministry, country or track names; cross-volume pointers read «jilid Tahun ke-1», «jilid universitasnya». Decimal **point** kept everywhere, in prose and in math, per the series convention. `-nya` attached, reduplication with a bare hyphen, `di`/`ke` separated as prepositions and attached as prefixes (checked by eye and by grep: no split prefix survives) |
| Defined-term links (`\omterm`) | **95** | `--check` **green and idempotent**: **4 652 links across 70 files**, all matching what `book2_id.py` generates — 103.4 % of English's 4 497 on the same text. **Full target-set parity: every one of English's 203 targets is present**, plus 3 Indonesian-only targets. Per-target counts audited term by term; the residual gaps are lexical, not wrong-sense, and are listed below |
| Figures | **98** | All 149 drawing bodies byte-identical to English — coordinates, `\foreach` numerics, `xtick`/`ytick`, `samples`, `\addplot` expressions, `circuitikz` component names and options. Only node text, legends, axis labels and `{\small …}` captions localized (*tampak atas*, *tampak belakang*, *mengorbit / lepas / jatuh*, *pseudoperiodik ($R$ kecil)*, *parabola (tanpa udara)*, *muon lahir pada \qty{15}{km}*) |
| Solutions | **97** | All 525 exercise solutions plus all 35 weekend-problem solutions present and native; headers `\section*{Bab \ref{ch:…} --- <judul>}` with `ch:` slugs untouched |
| MT-artifact freedom | **97** | Gate 8 (`check_indonesian_prose.py`) green over all 70 files: no residual English word, no untranslated sentence, no untranslated environment title, no split enclitic, no math-space or reduplication-space defect. The gate caught four real defects during the pass (an untranslated `\begin{remark}[The jumping rail]`, `diode` for *dioda*, the chemical symbol `Am` reading as English "am", and `\text{ISS}` inside a formula) — all fixed at the source |

## Terminology decisions and homographs — for `indonesian_style_card.md`

The style card is read-only for this agent. These are the decisions the Book 2
tree now embodies, for the main session to merge.

### Physics glossary settled in this pass (grades 10–12)

| English | Indonesian | Note |
|---|---|---|
| momentum | *momentum* | not *pusa*, not *impuls* |
| inertial reference frame | *kerangka acuan inersial* | g12 ch06; *kerangka inersial* in the relativity chapter, matching English's two definitions |
| restoring force | *gaya pemulih* | |
| apparent weight | *berat semu* | |
| free-body diagram | *diagram benda bebas* | |
| coefficient of friction | *koefisien gesekan* | but the ordinary word is *gesekan* |
| inclined plane | *bidang miring* | *bidang* is legitimate here: it is a plane, not a field |
| centripetal / tangential / normal acceleration | *percepatan sentripetal / tangensial / normal* | |
| uniform rectilinear motion | *gerak lurus beraturan* | |
| uniformly accelerated motion | *gerak lurus berubah beraturan* | |
| uniform circular motion | *gerak melingkar beraturan* | |
| chronophotograph | *kronofotografi* | |
| projectile | *proyektil* | reserved; *peluru* is a bullet, and both occur in the same exercise |
| launch angle / range / time of flight | *sudut lontar / jangkauan / waktu terbang* | |
| terminal speed | *laju terminal* | |
| stiffness (of a spring) | *kekakuan* | |
| damping / pseudo-period | *peredaman / pseudoperiode* | |
| forced oscillations / natural frequency / resonance | *osilasi paksa / frekuensi alami / resonansi* | |
| isochronism | *isokronisme*, adj. *isokron* | |
| capacitance / inductance / time constant | *kapasitansi / induktansi / tetapan waktu* | |
| smoothing / timing circuit | *penghalusan / sirkuit pewaktu* | |
| pseudo-periodic / aperiodic regime | *rezim pseudoperiodik / aperiodik* | |
| work / conservative force / potential energy | *usaha / gaya konservatif / energi potensial* | elastic: *energi potensial elastis* |
| energy diagram / turning point | *diagram energi / titik balik* | |
| stable / unstable equilibrium | *kesetimbangan mantap / goyah* | |
| escape speed | *laju lepas* | |
| ellipse / focus / semi-major axis | *elips / fokus / setengah sumbu panjang* | |
| perihelion / aphelion / sidereal day | *perihelion / aphelion / hari sideris* | |
| geostationary orbit | *orbit geostasioner* | |
| decay constant / exponential decay / half-life | *tetapan peluruhan / peluruhan eksponensial / waktu paruh* | |
| mass defect / binding energy per nucleon | *defek massa / energi ikat tiap nukleon* | |
| fission / fusion / fissile / chain reaction / critical mass | *fisi / fusi / fisil / reaksi berantai / massa kritis* | |
| moderator / control rod / Coulomb barrier / plasma | *moderator / batang kendali / penghalang Coulomb / plasma* | |
| photon / Planck's constant / photoelectric effect | *foton / tetapan Planck / efek fotolistrik* | |
| threshold frequency / work function / stopping potential | *frekuensi ambang / fungsi kerja / potensial henti* | |
| energy level / ground state / excited state / ionization | *tingkat energi / keadaan dasar / keadaan tereksitasi / ionisasi* | |
| stimulated emission / matter wave / de Broglie wavelength | *pancaran terangsang / gelombang materi / panjang gelombang de Broglie* | |
| event / proper time / time dilation / length contraction | *peristiwa / waktu diri / pemuluran waktu / pengerutan panjang* | |
| relativity principle / simultaneity | *asas kerelatifan / keserentakan* | special relativity = *kerelatifan khusus* |
| mass–energy equivalence | *kesetaraan massa--energi* | |

### Homographs the link layer had to be taught (new for the card)

1. **`tegangan`** — voltage *and* rope tension, exactly as `tensão` is for
   `pt`. Not stoplisted here: the electrical sense is 3× the commoner, so
   stoplisting would cost 55 right links to save 17 wrong ones. The
   mechanical uses are masked by `EXTRA_PROTECT` patterns instead
   (`tegangan` + a following `$`, `tali`, `kawat`, `kabel`, `penghela`,
   `kerja`).
2. **`inti`** — the **core of an optical fibre** (g10) before it is the
   nucleus of an atom, the core of the Sun, the core of an electromagnet, or
   *intinya* meaning "essentially". Ungoverned it shipped **119 links, 8 of
   them right**. Stoplisted (chapter-local links survive).
3. **`berat`** — the weight of a body *and* the adjective "heavy"
   (*peredaman berat*, *inti yang berat*, *lebih berat*). Adjectival uses
   masked in `EXTRA_PROTECT`.
4. **`hambatan`** — electrical resistance *and* aerodynamic drag
   (*hambatan udara*, *gaya hambatan*). 20 wrong links before masking.
5. **`gravitasi`** — one word for English's *gravity* (never linked) and
   *gravitation* (linked), and defined twice on top of that: 78 links
   against English's 14. Stoplisted; *gaya gravitasi* and *interaksi
   gravitasi* survive as terms of their own.
6. **`diam`** — "at rest", harvested from the reference-frame definition,
   against the ordinary adjective on every page: 102 links, ~15 right.
7. **`mantap`** — stable equilibrium *and* the ordinary "steady" (a steady
   current, a steady gigawatt). Same shape: `tipis` (thin lens / thin air),
   `seragam` (uniform field / marching in step), `lolos` (escape speed / any
   escaping), `mutlak` (absolute pressure / any absolute).
8. **Unit names spelled like the physicists** — *newton, joule, coulomb,
   ohm, watt, henry, becquerel, pascal, kelvin, tesla, volt, ampere, hertz,
   farad, sievert, curie*. Indonesian has no *julio/voltio* escape, so
   capitalized forms are excluded via `NO_CAPITAL`. `Newton` alone shipped
   **23 wrong links** (`hukum Newton`, `Newton tidaklah keliru`).
9. **`sekon`** — *not* ambiguous, but stoplisted anyway: English never links
   "second" (its ordinal would fire), and linking all 137 Indonesian
   occurrences would put a fifth of the book's links on one unit definition.
10. **`peluru` vs `proyektil`** — a bullet and a projectile share a word in
    everyday Indonesian; ch07 needs both in the same exercise, so
    *proyektil* is reserved for the physics object.
11. **`sinyal` vs `isyarat`** — both are correct Indonesian for *signal*;
    the series' defined term is *sinyal* (g10), so 13 occurrences of
    *isyarat* introduced in grades 11–12 were harmonized.

## Gate-list words appended to `tools/check_indonesian_prose.py`

Append-only, per the shared-file protocol; no rule was rewritten.

* **`ID_MARKERS`, two blocks** (39 + 23 words): ordinary Indonesian function
  and quantity words — *sekitar, kira-kira, saat, ketika, seluruh, setelah,
  selama, terhadap, menurut, sebesar, sepanjang, melalui*, the numerals
  *satu…sepuluh, puluh, ratus, ribu, juta, miliar*, *semesta, bintang,
  planet-planet, sebagai, supaya, hingga*; then the classifiers *seorang,
  seekor, sehelai, sebutir, sebatang, selembar* and *disebut, dinamakan,
  terletak, berada, titik, garis, sudut, bidang, lensa, bayangan, arah,
  bentuk, ukuran, jumlah, bagian, keadaan, getaran*. Each fired on correct
  Indonesian prose where a numeral-and-quantity sentence runs past eight
  words without touching any marker already listed. Every word is
  unambiguously Indonesian, so the class still cannot excuse an English
  sentence.
* **`ALLOWED`, one word**: `he` — the chemical symbol for helium. Figure
  labels set the mass number in math and leave the symbol outside it
  (`{$^{4}$He}` on the binding-energy curve), so the symbol reaches the
  gate as a bare word. Only the one symbol that collides with an English
  word is listed; a genuine English sentence containing "he" still fires on
  its other words and on the sentence-density rule.

## The page-count oscillation — resolved

The brief flagged that, with the English bodies falling through, the smoke
build oscillated by one page between passes (the `Solusi hlm.` page-number
feedback loop) and `latexmk` exited 12 with "needed too many passes". **With
the real Indonesian bodies it converges.** `latexmk -g` from a cleared
`.aux`: exit 0, one `Rerun` request, **374 pages**, and a second `latexmk`
run reports "Nothing to do". English is 350 pages: Indonesian runs +6.9 %
long, which is the usual cost of *yang*-clauses and of `ber-`/`me-` prefixed
verbs against English's bare stems.

## Samples, verdicted

**1 — ch12 ch01 opening (native).**
«Putarlah tombol berat sebuah radio loteng dan stasiunnya berbaris melewati
jarumnya: sebuah suara, biola, desis, lalu sebuah suara lagi. Di balik
papannya tidak ada motor dan tidak ada komputer --- sebuah kumparan, sebuah
kapasitor yang kepingnya bersilang dan diputar tombolnya, dan seuntai kawat
antena.»
Verdict: **native**. `Di balik papannya` for "behind the panel", the
appositive list without a copula, `seuntai kawat` with the right classifier.

**2 — ch16 opening (native).**
«Setiap satelit GPS membawa jam atom yang tepat sampai satu sekon dalam tiga
juta tahun --- dan sebelum peluncurannya, para insinyur dengan sengaja
melarasnya keliru: jika dibiarkan jujur, jam itu akan bertambah 38
sepersejuta sekon tiap hari.»
Verdict: **native**. *melarasnya keliru* (detune) and *jika dibiarkan jujur*
are written Indonesian, not glossed English.

**3 — ch09 method (native).**
«Jangan pernah mengukur satu osilasi saja: jalankanlah pengukur waktunya saat
bebannya melintasi garis tegak (paling cepat, paling mudah ditimbang),
hitunglah $N = 50$ osilasi, lalu bagilah dengan $N$ --- galat tanggapan
\qty{0.2}{s} menjadi \qty{4}{ms} pada $T_0$.»
Verdict: **native**. The imperative chain in `-lah`, `galat tanggapan` for
"reaction error".

**4 — ch14 solution 9c (near-native).**
«Tidak ada longsoran neutron: tiap fusinya dibeli oleh tumbukannya sendiri,
dan hilangnya pengurungan mendinginkan plasmanya lalu memadamkan apinya.»
Verdict: **near-native**. *dibeli oleh tumbukannya sendiri* keeps the English
metaphor; an Indonesian physicist would more likely write *dibayar dengan
tumbukannya sendiri*. Kept for series voice.

**5 — ch08 caption (native).**
«Seluruh mekanisme sebuah orbit: kecepatannya menyinggung, gayanya menuju
pusatnya --- gravitasi tidak pernah memperlambat satelitnya, ia hanya
membelokkan lintasannya, selamanya.»
Verdict: **native**.

No sample in the book reads as MT.

## Why not 100 — the honest gaps

1. **`laju` vs `kelajuan` (−39 links on `def:g12:kinematics-2d:velocity`).**
   English links its "speed" 38 times to the velocity definition. The
   Indonesian tree says *laju* 356 times and *kelajuan* rarely; the defined
   display is *kelajuan*, so the ordinary word reaches nothing. Adding
   *laju* as a term would link all 356, including *laju perubahan momentum*
   and *laju peluruhan*, where the link would be plainly wrong. Left as is:
   the sense is right on the page, the link is missing.
2. **`lintasan` (+75 on `def:g10:relative-motion:trajectory`).** Indonesian
   has one word where English has *path* (never linked) and *trajectory*
   (linked). Every one of the 101 links is right in sense; only the count
   diverges.
3. **Six more targets diverge by 10–29 links** — *waktu paruh* (+29),
   *gelombang* (+19), *saling meniadakan* (+18), *satuan/meter/kilogram*
   (+13), *medan* (+13), *kerangka tanah* (+12) — all the same shape: one
   Indonesian word covering two English ones, or an Indonesian phrase used
   more often than its English twin. None is wrong-sense.
4. **`aktivitas` (−16).** 27 occurrences against English's 33 "activity";
   the difference is prose, not curation.
5. **Two source edits were needed to restore link parity**, and both are
   real translation defects the audit exposed: `\emph{Daya}` and
   `\emph{Periode}` were capitalized at the start of their defining
   sentence, which makes each a *separate harvest entry* that bypasses the
   ambiguity resolution — English's "power" splits 61/59 across its two
   definitions, the Indonesian *daya* was landing 114/10 until the display
   was lowercased. Anyone adding a definition to this tree should write the
   `\emph{term}` lowercase and mid-sentence.
6. **136 underfull vboxes** against English's 129: seven pages where the
   longer Indonesian prose leaves a looser column. Cosmetic.
7. **Two overfull boxes had to be fixed by rewording**, not by translation
   choice: an inline `\dfrac` preceded by *Matahari:* (9 characters where
   English has *Sun:*) could not fit, and became a two-line display; and a
   ratio line in the orders-of-magnitude solutions was 1 pt over and gained
   the word *Nisbah*. Both edits are in the Indonesian tree only.
