# One Physics Book 5 (University, Year 3) --- Indonesian edition: self-score

**Date:** 2026-09-03
**Quality bar:** *native academic* (the bar of `translation_instruction.md`),
modern lecture register --- the ruling settled for the Indonesian editions in
`indonesian_style_card.md`.
**Sense/structure reference:** the English canon (`parts/bachelor-3/*.tex`)
for content; `parts/bachelor-2/id/` for the Indonesian university register and
the settled terminology; `book5_en.py` for the stop-list reasoning carried
into `book5_id.py`.

## Overall: **96 / 100**

| Dimension | Score | Note |
|---|---:|---|
| Register (academic Indonesian, weighted) | 97 | Uniform `-lah` imperative across all 54 files (2 800 forms), **matching `parts/bachelor-2/id` exactly** --- see *Register, checked not assumed*. Definitions use `\emph{term}` lowercase mid-sentence so the harvest registers one entry, not two. |
| Terminology (weighted) | 96 | Settled glossary below. Every `\text{}` subscript that carries a word was localised (`besi`, `celah`, `cair`, `uap`, `inti`, `diri`, `pita`, `rantai`, `puncak`, `sistem`, `keadaan`, `terlipat`, `tambahan`, `bebas`, `dalam`, `perangkap`, `lambat`, `diam`, `rasa`, `tetapan`, `dahulu`, `Bumi`, `Bose`/`Fermi`); Latin abbreviations kept by convention (`const`, `max`, `int`, `orb`, `osc`, `tot`, `rad`, `lab`, `esc`, `deg`, `conf`, `grav`). |
| MT-artifact freedom (weighted) | 96 | No calqued word order found on sampling; every TikZ node, axis label, `\legend`, `\addlegendentry`, caption and environment optional title is Indonesian (swept mechanically against the English twins --- see *Checks*). Orphan-line sweep: **0**. |
| Structure | 100 | `check_translation.sh` green; all 54 files written as line-range replacements on the English canon through `tools/id_apply.py`, so labels, `\cref` targets, solution keys, `\qty{}{}`, `\foreach`, `xtick=` and every math display are byte-identical to English. |
| LaTeX hygiene | 99 | 0 errors, 0 undefined, 0 overfull, 0 "invalid in math mode"; `nullfont` at the English baseline of 10; UTF-8 accents only (`Ampère`, `Segrè`, `Ørsted`), none inside a unit argument. |
| Cross-references | 100 | Every `\cref`/`\ref` target byte-identical to English; 12 exercises + 1 weekend problem per chapter, one solution each. |
| Figures | 98 | Drawing code untouched; only node text, axis labels, legends and captions translated. One `!draw` opt-out was needed in ch. 15 (below). |
| Solutions | 97 | All 27 solution files translated; `\textbf{n.}` numbering and every number preserved. |

## What was produced

- `parts/bachelor-3/id/01`--`27` and `parts/bachelor-3/solutions/id/01`--`27`
  --- **54 files, 21 744 lines** (English: 21 296), every one applied as
  `id_apply` line ranges, so all eleven censuses (labels, envs, solutions,
  emph, index, math, draw, delims, braces, omterm, prose) passed on write.
- `tools/term_config/book5_id.py` --- audited and curated, not left as the
  seed. See *Term configuration* below.
- `translation_scores/book_5/id/translation_score.md` --- this file.
- Build: **329 pages**, `0` errors, `0` undefined, `0` overfull
  (English: 302 pages).
- No file outside the four paths above was touched. The entry file
  `one_physics_book_5_university_year_3_id.tex` and
  `frontmatter/image-credits-book5.id.tex` already existed and needed
  no change.

## Checks

```
bash tools/check_translation.sh bachelor-3 id      -> TRANSLATION GATE: PASSED
                                                     (indonesian prose gate: OK, 54 files)

python3 tools/check_latin_prose.py parts/bachelor-3/id parts/bachelor-3/solutions/id
  -> 61 findings in 54 files, ALL reviewed:
       1 x tier 1 (node)  : 'van der Waals $\sim -1/r^6$'  -- a proper name plus
                            mathematics; correct to keep, as in every edition
       4 x tier 2 (node)  : 'neutron', 'proton', 'positronium...', '$\varphi$ real'
      56 x tier 2 (text)  : orb, osc, sep, esc, deg, conf, grav, const, boson,
                            fermion, singlet, triplet, molar, total, spin, atom,
                            ideal, Coulomb -- Indonesian words or kept abbreviations

python3 tools/check_orphan_lines.py parts/bachelor-3/id parts/bachelor-3/solutions/id
  -> orphan English lines: 0

\text{} identical-to-English census, run over BOTH directories
  -> 22 sites, all legitimate (const, boson, fermion, singlet, triplet, molar,
     total, spin, atom, ideal, Coulomb, grav, conf, (Dulong--Petit))

grep -rnP "\\\\['`^\"~=.]\{?[a-zA-Z]" parts/bachelor-3/id parts/bachelor-3/solutions/id
  -> 0   (three inherited `Amp\`ere` were found and converted to UTF-8 `Ampère`)

latexmk -g one_physics_book_5_university_year_3_id.tex
  '^!' lines             -> 0        (329 pages)
  undefined              -> 0
  Overfull               -> 0
  "invalid in math mode" -> 0
  nullfont               -> 10       (= the English build's own count)

grep -oa 'parts/bachelor-3/\(solutions/\)\?id/[0-9a-z-]*\.tex' build/...fls | sort -u | wc -l
  -> 54                             (the build really read all 54 Indonesian files)

python3 tools/link_defined_terms.py --book 5 --lang id --unwrap --apply
python3 tools/link_defined_terms.py --book 5 --lang id --apply
  -> 954 links across 52 files      (English: 916 -- 1.04x)
python3 tools/link_defined_terms.py --book 5 --lang id --check
  -> CHECK: every file matches what the config generates

\omterm targets reached: comm -23 <English's 100> <this edition's 124>  -> empty
\index{} occurrences: 302 (English: 302); unique keys 298 vs English 297
```

## Register, checked not assumed

The coordinator asked which register the exercise stems use and whether it
matches the Book 4 Indonesian twin. Measured, not assumed:

| | `parts/bachelor-2/id` (Book 4) | `parts/bachelor-3/id` (this book) |
|---|---:|---:|
| `-lah` imperative forms | 2 187 | 2 800 |
| bare imperatives without `-lah` | 2 | 0 |
| commonest `(a)` stems | *Tentukanlah*, *Tunjukkanlah*, *Turunkanlah*, *Tuliskanlah* | *Tunjukkanlah*, *Hitunglah*, *Tuliskanlah*, *Periksalah* |

Same register, same suffix, same politeness level; the two books differ only
in which verbs their physics calls for. Nothing diverged and nothing needed
converting.

## Term configuration (`tools/term_config/book5_id.py`)

The seed was audited item by item against Book 5's own Indonesian harvest.

- **`NOT_A_TERM` added.** The shared default is English-only and
  `harvest.py` matches it as a *substring*, so English's `theorem`,
  `formula`, `principle` and `rule` silently block *Noether's theorem*,
  *the Sackur--Tetrode formula*, *Hamilton's principle*, *the Born rule*.
  Indonesian puts the result-name in front, so without an Indonesian list
  this edition would have linked **fourteen** result names English does not.
  Two heads are deliberately absent: `hukum`, because the English default
  blocks only `law of X` and therefore keeps Bragg's, Hooke's, Hubble's,
  Planck's, Dulong--Petit's and the radioactive-decay law (all six of which
  Indonesian writes `hukum X`); and `lema`/`aturan`, which are substrings of
  the ordinary Book 5 terms *interaksi le**ma**h* and *parameter
  keter**atura**n* --- with a substring matcher those two are not
  conservative, they are destructive.
- **`STOP` pruned.** The five carried-over Book 4 words (`Ambang`,
  `Efisiensi`, `Laser`, `Serapan`, `Tunak` and their lowercase twins) match
  no defined term anywhere in Book 5; the harvest drops exactly four
  entries, all of them Book 5's own. Every inert entry was removed. English
  STOPs five words and Indonesian drops four: the difference is correct, not
  a miss --- English's *observable* is a bare noun, while this edition writes
  the defined term *besaran teramati*, which is multi-word and so is never
  matched by the bare `teramati`.
- **`EXTRA` stays empty, and this was checked.** Diffing the two `--terms`
  target sets, `comm -23 en id` is empty: every English target is reached.
- **`EXTRA_PROTECT` stays empty, and this was checked too.** After the Dutch
  *ket* -> *keten* collision, the generated `\omterm` surface forms were
  counted and their frequency table compared against English's:
  `kristal`+`kristalnya` 31 vs `crystal` 29, `kisi`+`kisinya` 25 vs
  `lattice` 25, `spin` 31 vs `spin`+`spins` 36, `peristiwa` 19 vs `events`
  18. No Indonesian term is implausibly ahead of its English twin, so no
  mask is needed. The seed's `EXTRA_PROTECT` was already empty, so the
  brief's warning about a carried-over mask did not apply to `id`.

## Settled glossary (the decisions a reviewer should check first)

| English | Indonesian | Note |
|---|---|---|
| free energy | energi bebas | |
| partition function | fungsi partisi | grand: *fungsi partisi besar* |
| chemical potential | potensial kimia | |
| degeneracy pressure | tekanan kemerosotan | *merosot* for *degenerate* throughout |
| band gap | celah pita | |
| doping / donor / acceptor | pendopingan / donor / akseptor | *jenis-n*, *jenis-p* |
| hole (semiconductor) | lubang | STOPped: black hole in ch. 27 |
| superfluid / superconductor | adiluncur / adikonduktor | |
| condensate | kondensat | *memampat* for *to condense* |
| lattice | kisi | *sel satuan*, *tetapan kisi* |
| cohesive energy | energi kelekatan | |
| hysteresis / remanence / coercivity | histeresis / keteringatan / kekoersifan | |
| reluctance | keengganan | magnetic circuit |
| nuclide / binding energy / mass defect | nuklida / energi ikat / cacat massa | |
| valley of stability | lembah kemantapan | |
| quark flavours | atas, bawah, aneh, pesona, dasar, puncak | letters u/d/s/c/b/t kept |
| confinement | pengurungan | |
| standard candle | lilin baku | |
| main sequence | deret utama | |
| proper time | waktu diri | `t_{\text{diri}}` |
| order parameter | parameter keteraturan | |
| universality / critical exponent | kesemestaan / eksponen genting | *genting* for *critical* |
| nucleation | pengintian | |

## Sampled passages, verdicted

Five passages were read back cold against the English and judged as if by an
Indonesian physicist who had not seen the source.

1. **ch. 17, opening (`17-canonical-ensemble.tex:3--19`).**
   *"Sistem terkucil adalah khayalan seorang teoretikus: cuplikan yang
   sebenarnya duduk dalam termostat, ruangan, samudra udara --- yakni dalam
   sentuhan dengan sebuah tandon yang menetapkan bukan energinya melainkan
   suhunya."* --- **native.** The `bukan ... melainkan` correlative is the
   idiomatic Indonesian answer to English's *not ... but*; a machine renders
   it *tidak ... tetapi*, which is grammatical and flat.

2. **ch. 19, theorem (`19-quantum-statistics.tex:56--61`).**
   *"yakni sebuah tekanan pada nol mutlak, yang murni berasal kuantum ---
   kekakuan gas elektron tiap logam dan penopang bintang mati."* ---
   **native.** Verbless apposition after `yakni`, which is how Indonesian
   technical prose delivers a definition mid-sentence.

3. **ch. 24, definition (`24-electrons-in-solids.tex:151--168`).**
   *"Karena itu muncullah pemisahan besar itu: logam menghantar lebih buruk
   ketika dipanaskan ..., semikonduktor lebih baik ...--- yakni satu
   pembalikan tanda yang mengenali kelas sebuah bahan dalam satu
   pengukuran."* --- **native.** `muncullah` (the `-lah` focus particle on a
   verb, not an imperative) is a register marker no MT system produces.

4. **solutions ch. 22, item 19 (`solutions/id/22-...:19`).**
   *"Melipatduakan $e$ membagi dua $B$ lalu membagi empat gayanya ...
   tetapi $P = RI^2$ menjadi empat kali lipat: celah dibayar dengan kalor
   tembaga."* --- **native.** The verbal nouns `melipatduakan` /
   `membagi dua` / `membagi empat` are the compact Indonesian idiom for
   *doubling* / *halves* / *quarters*.

5. **ch. 26, problem stem (`26-particle-physics.tex:404--409`).**
   *"dikabeli secara berkebetulan --- yakni satu cacahan hanya ketika
   keduanya menyala dalam \qty{100}{ns}."* --- **near-native.**
   *dikabeli secara berkebetulan* for *wired in coincidence* is
   understandable and correct but reads as a coinage; a working Indonesian
   particle physicist would more likely say *dirangkai dalam mode
   koinsidensi*. Kept for consistency with the rest of the chapter, which
   avoids unassimilated loans. This is the kind of site that keeps the
   register score at 97 rather than 100.

## Why not 100

1. **One `!draw` opt-out (ch. 15, line 57).** `id_apply`'s `NODE_TEXT`
   pattern cannot match a `\node ... at ($(35:3.4)+(0.25,0)$)` --- the
   nested parentheses defeat it --- so translating that node's
   `{detector, $\dd\Omega$}` required suppressing the `draw` census for the
   file. It was verified by hand with `draw_bodies()` that this is the only
   drawing difference in the file, but a hand check is weaker than a census.
2. **Three `!prose` opt-outs, all of them now obsolete.** Chapter 20,
   `solutions/18` and `solutions/26` were written with the prose census
   suppressed because gate 8's `math-space` rule was false-positiving on the
   English canon's own `$... = $ const` idiom --- a conflict with the math
   census, which requires that span byte-identical. In each case the span
   was then post-edited by hand: `$\lambda_{\max}T = $ const` became
   `$\lambda_{\max}T = \text{tetapan}$`, `$k_{\text{B}}T\ln n(h) + mgh = $
   const` became `... = \text{tetapan}$`, and `$\Delta^{++} = $ uuu` became
   `$\Delta^{++} =$ uuu`. Those three inline spans are therefore the only
   places in the book where the mathematics is not byte-identical to English
   --- deliberately, because the alternative was to leave the English word
   *const* standing in Indonesian prose. The coordinator has since fixed the
   rule, so the opt-outs are no longer needed; the whole tree passes the
   fixed gate. The result is right, but the route to it was taken on a wrong
   signal.
3. **A handful of naturalised coinages.** *dikabeli secara berkebetulan*
   (above), *keteringatan* for *remanence*, *kekoersifan* for *coercivity*,
   *adiluncur* for *superfluid*: all defensible, all consistent with Book 4
   Indonesian, none of them the word a specialist would reach for first.
4. **This edition is the longest of the run so far (329 pp against
   English's 302, +8.9 %).** Indonesian's agglutination and its habit of
   marking definiteness with `-nya` genuinely lengthen prose, and Book 4
   Indonesian ran longest too --- but part of the excess is my own
   preference for the explicit `yakni ...` apposition where a bare colon
   would do. Nothing is wrong; it is simply not as tight as it could be.
5. **Three overfull boxes existed in the first clean build** (ch. 10 proof;
   `solutions/01` items (b) and 15) and were cured by rewrapping the prose
   *before* the break, then re-verified with a single-file probe and a full
   rebuild. They are gone, but they were mine, not inherited.

## For the coordinator: gate-8 word-list requests

Reported, not edited, per the brief.

1. **`be`** (in `ENGLISH_FUNCTION` / `ENGLISH_WORDS`) fires on
   `\bar n_{\text{BE}}` --- the standard Bose--Einstein subscript, which
   lowercases to `be`. It blocked ch. 18 twice, including a line of the
   English canon that no patch range touches. Worked around here by writing
   `\bar n_{\text{Bose}}` and `\bar n_{\text{Fermi}}`, which is arguably
   clearer anyway, but the rule will bite every edition that keeps `BE`.
   Suggest skipping tokens that are ALL-CAPS in the source.
2. **The `-s`/`-es` plural rule fires on ALL-CAPS acronyms.** `ISS`
   lowercases to `iss`, is stripped to `is`, and `is` is a listed word.
   Same suggested fix as (1): do not apply the plural/suffix rules to a
   token that was ALL-CAPS.
3. **`1900-an` / `1890-an`** --- the Indonesian decade suffix. The tokeniser
   splits on the hyphen and reports the residue `an` as English. Suggest
   treating `<digits>-an` as one token. Worked around by rewriting as
   *pada awal abad kedua puluh* / *sepanjang dasawarsa 1890*.
4. **The `untranslated` rule fires on `\index{}`-only lines.** A line such
   as `\index{ikatan van der Waals}\index{ikatan kovalen}\index{ikatan
   logam}` is eight visible words with no function word, because index keys
   are noun phrases by construction. Worked around by splitting such lines
   with a `%` continuation (ch. 23 and ch. 25). Suggest skipping lines whose
   visible text comes entirely from `\index{}`.
