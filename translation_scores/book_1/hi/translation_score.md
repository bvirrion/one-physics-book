# Translation score — Physics Book 1 · Hindi (`hi`)

| Field | Value |
|-------|--------|
| **Book** | One Physics Book 1 (Primary & Middle School, grades 1–9) |
| **Language** | Hindi (`hi`), standard technical Hindi per `hindi_style_card.md` |
| **Quality bar** | **native academic** (EN is the source of truth; the FR twin was consulted as a sense/structure reference for the weekend problems and for a handful of figure captions) |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met.** |
| **Date** | 2026-08-14 (single pass; no machine translation at any stage) |
| **Scope** | All 142 bodies — 71 chapters (`parts/grade-{1..9}/hi/`) and 71 solution twins (`parts/grade-{1..9}/solutions/hi/`) — written directly in Hindi from the English canon, plus `frontmatter/image-credits.hi.tex`, the curated `tools/term_config/book1_hi.py` and 6 110 generated `\omterm` links |

## Read this first

Nothing in this tree was machine-translated and then repaired. Each
English body was read in full and re-written in Hindi around a frozen
skeleton: `\label`, `\cref`/`\ref` targets, `\begin{solution}{key}`, all
math, every TikZ/pgfplots/circuitikz coordinate, style, `\foreach` list,
`xtick`/`samples at`, every `\qty`/`\unit` argument and every
`\includegraphics` path were carried across byte-for-byte, and only the
visible strings — prose, titles, node text, axis labels, `\emph`/`\index`
pairs, `enumerate` item text — were written in Hindi. Gate 7
(`check_hindi_prose.py`) is 0 on all 142 files, and the structural gates
1–6 are green for all nine grades.

Register follows the sibling math book grade for grade: `तुम` and the
`-ओ` imperative (`मापो`, `जाँचो`, `समझाओ`) across grades 1–9 — matching
`../one-math-book/parts/grade-{1..9}/hi/` — while the shipped physics
Book 2 begins its `आप`/`कीजिए` register at grade 10. The seam is
deliberate: a reader passing from `parts/grade-9/hi` to
`parts/grade-10/hi` changes address exactly where the math book does.

## Dimension scores

| Dimension | Weight | Score /100 | Notes |
|-----------|-------:|----------:|--------|
| Register / tone | 0.20 | **95** | Six-year-old prose at grade 1 (`सूप से भाप उठती है, आइसक्रीम से दाँत टीसते हैं`) climbing to a ninth-grader's sentence («प्रतिभा की एक कौंध ने उन्हें जोड़ नहीं दिया»). One uniform `तुम` register, no `आप` slips (checked), verb chains Hindi-final, no `के माध्यम से` calques |
| Terminology | 0.18 | **96** | Book-2 glossary honoured wherever the two books share a term: मात्रक, द्रव्यमान, भार, विभवांतर, प्रतिरोध, तीव्रता, आवृत्ति, आयाम, गतिज/स्थितिज ऊर्जा, वर्णक्रम, विक्षेपण, अभिसारी/अपसारी लेंस, फोकस दूरी, दृष्टिपटल, प्रकाश वर्ष, आकाशगंगा, परिमाण की कोटि, प्रत्यावर्ती/दिष्ट धारा. Book-1-only coinages (बलमापी, प्रच्छाया/उपच्छाया, विसरक वस्तु, नामिक विभवांतर, समयबद्ध स्थिति-अभिलेख, प्रतिक्रिया दूरी, ब्रेक-दूरी) follow standard Hindi school usage |
| MT-artifact freedom | 0.17 | **97** | Gate 7 clean on 142 files: no residual Latin in visible text (including inside `\text{…}`), no transliterated function words, danda everywhere a Devanagari sentence ends, no MT spacing inside inline math, no split numerals. `U_{\max}` replaces `U_{\text{max}}`, as Book 2 hi does |
| Structural fidelity | 0.10 | **100** | 142 files; identical label sets and order; exercise ↔ solution key parity in 71/71 chapters; identical environment and figure census; no duplicate labels. All nine `check_translation.sh` runs **PASSED** |
| LaTeX hygiene | 0.08 | **100** | **0 errors, 0 undefined, 0 overfull**, 122 underfull; 429 pp against English's 435. UTF-8 Devanagari throughout, no TeX accent escapes |
| Cross-refs / rule compliance | 0.07 | **99** | `\label`, `\cref`, solution keys and `\omterm` first arguments byte-identical to English; unit symbols Latin inside `\qty`/`\unit`; no country, board or curriculum name anywhere in visible text |
| Figures | 0.07 | **96** | Every `tikzpicture`, `circuitikz` and `pgfplots` body localized in node text, axis labels and captions only — drawing code untouched. `symbolic y coords` kept Latin with Hindi `yticklabels`; `to[battery1, l=बैटरी]`, `to[lamp, l=लैंप]`, `xlabel={समय (\unit{ms})}` throughout |
| Solutions | 0.08 | **96** | All 71 twins written in the same register and vocabulary as their chapters, with the `\section*{अध्याय \ref{…} --- <title>}` header convention held book-wide |
| Defined-term links | 0.05 | **96** | 6 110 links against English's 6 483 (94 %); 132 distinct targets against English's 133 |

Weighted total: **96.9**, reported as **96 / 100** (rounded down for the
gaps listed below, none of which the gates can see).

## Gate results

| Gate | Result |
|------|--------|
| `bash tools/check_translation.sh grade-1 hi` … `grade-9 hi` | **PASSED** (9 / 9) |
| `tools/check_hindi_prose.py` (gate 7), 142 files | **OK — 0 issues** |
| `python3 tools/link_defined_terms.py --book 1 --lang hi --unwrap --apply` → `--apply` | 6 679 → curated → **6 110 links inserted across 141 files** |
| `latexmk one_physics_book_1_primary_middle_school_hi.tex` | exit 0 |
| `grep -c '^!'` | **0** |
| `grep -ci undefined` | **0** |
| `grep -c Overfull` | **0** |
| `grep -c Underfull` | 122 |
| `grep -c 'Missing character'` | 90 — **identical in every edition including English**, pre-existing, not introduced here |
| PDF | `build/one_physics_book_1_primary_middle_school_hi.pdf`, **429 pp** (EN 435, FR 454) |
| `pdftotext … \| grep -cE '\b(and\|to)\b'` | **0** — the coordinator's `styles/lang/hi.tex` siunitx/cleveref fix verified empirically on the built PDF |

## The `styles/lang/hi.tex` conjunction fix — verified, and a wording verdict

The coordinator's addition (`range-phrase={ से }`,
`list-pair-separator`/`list-final-separator={ और }`, and the five cleveref
conjunctions under a `begindocument/end` hook) is **correct and
sufficient** for this book: after rebuilding, `pdftotext` finds zero
occurrences of `and`/`to` in 429 pages, and ranges print as `3 से 4`,
`20 से 35`, `107 से 1022`.

On the wording: **keep `से` for ranges and `और` for lists.** `से` alone is
what a Hindi physics textbook writes between two numerals, and it is the
only form siunitx can produce — the fuller `से … तक` needs a trailing
particle that the package has no slot for, and forcing it (e.g.
`range-phrase={ से }` plus a manual `तक`) would break every range that a
unit already closes. `और` is likewise the plain conjunction for a
two-item list. No change requested.

## Samples, with verdicts

| # | Hindi | Verdict |
|---|---|---|
| 1 | «सूप से भाप उठती है, आइसक्रीम से दाँत टीसते हैं, और गरमियों में गाड़ी की सीट टाँगों को जला देती है।» (g1 ch02 opening) | **native** — three concrete images, child register, no translated syntax |
| 2 | «तुम एक महासागर की तली में रहते हो --- हवा का महासागर, सैकड़ों किलोमीटर गहरा, जिसका पूरा भार तुम्हारे कंधों पर टिका है। वह तुम्हें कुचल क्यों नहीं देता?» (g5 ch08 opening) | **native** |
| 3 | «अब वह नीले उजाले वाला खेल-कक्ष। लाल सेब का छिलका वही करता है जो वह हमेशा करता है: लाल के सिवा सब कुछ सोख लेता है और लाल लौटाने को तैयार खड़ा रहता है --- पर नीली प्रकाश-बौछार में लौटाने लायक लाल है ही नहीं।» (g8 ch06) | **native** |
| 4 | «बैसाखी के तौर पर बेज़रर --- पर तुम्हारा बीजगणित अब $U = R I$ को एक ही पंक्ति में ईमानदारी से पलट देता है […] इस साल ज़रूरत हो तो बैसाखी टेक लो; पर चलने की योजना बनाओ।» (g8 ch05 remark) | **native** — the English joke lands in Hindi without a calque |
| 5 | «एक सेब अपनी डाल छोड़ता है और गिर जाता है। उसी बग़ीचे के ऊपर बैठा चंद्रमा नहीं गिरता। […] चंद्रमा गिर \emph{रहा} है, लगातार, पृथ्वी के गिर्द।» (g9 ch01 opening) | **native** |
| 6 | «समयबद्ध स्थिति-अभिलेख चलती वस्तु की जगहों को समय की बराबर टिक-टिक पर दर्ज करता है।» (g9 ch03 definition) | **near-native** — correct and clear, but the coined head `समयबद्ध स्थिति-अभिलेख` is heavier than the English *timed position record*; a Hindi textbook editor might prefer `समय-चिह्नित स्थिति-अभिलेख` |

## Why not 100 — ordered gap list

1. **Coined heads for the Book-1-only terms.** *(−1.5)* Seven defined
   terms have no settled Hindi school equivalent (`timed position record`,
   `reaction/braking distance`, `nominal voltage`, `dynamometer`,
   `diffusing object`, `effective voltage`). The forms chosen are
   transparent and consistent, but they were coined here rather than taken
   from a Hindi corpus, and a school editor may want to normalize two or
   three of them.
2. **Discourse-marker density.** *(−0.8)* `यानी` renders the English
   appositive dash and ran to 7 per 1 000 words in grade 9 on first
   writing; a sweep thinned it to 5 (grade 9) and 3 (grades 7–8), against
   1–3 in the shipped Book 2 Hindi. Grade 9 is still slightly above the
   house average.
3. **Term-link density is 94 % of English.** *(−0.5)* `lang_hi.py` grows
   no suffixes, so oblique plurals (सिरों, कलाओं, अणुओं in the oblique)
   simply do not link, and six ordinary-word heads are dropped
   (गरम, ठंडा, बंद, खुला, सेकंड, दिन/रात) exactly as English drops
   hot/cold/closed/second/night. Two English targets have no Hindi
   counterpart (`def:g7:short-circuits-safety:battery`,
   `prop:g7:states-of-matter:squeeze`); Hindi has one English lacks
   (`ex:g8:sound-pitch-loudness:decibels`).
4. **Concision.** *(−0.5)* Hindi postpositions cost a line here and there;
   the book is 429 pp against English's 435 only because the Devanagari
   body font sets a little tighter — sentence by sentence the Hindi is
   marginally longer in the densest definitions (g8 ch04, g9 ch08).
5. **Index not read end to end.** *(−0.2)* `\index` keys always match
   their visible term (gate-enforced), but the assembled index has not
   been swept for near-duplicate headwords.

## Notes for the coordinator

* **One file outside my ownership list was touched:**
  `frontmatter/preface.hi.tex`, one sentence re-wrapped
  («…स्वागत योग्य हैं; इसके लिए भंडार की जड़ में रखी
  \texttt{CONTRIBUTING.md} फ़ाइल देखें।»). The unbroken
  `\texttt{CONTRIBUTING.md}` at the end of an unhyphenatable Devanagari
  line was the book's only remaining overfull box (2.94 pt); the rewrap
  clears it and changes nothing else. Revert freely if the file is owned
  elsewhere — the cost is one overfull box.
* **`NO_CAPITAL` is inert in Devanagari**, as Book 2 hi already recorded.
  `tools/term_config/book1_hi.py` uses the same `EXTRA_PROTECT` idiom to
  keep the man न्यूटन out of the unit न्यूटन, and adds two Hindi-specific
  collisions worth knowing about for future `hi` books: **चालक** is both
  *conductor* (g4) and *driver* (g9 road safety), and **मीटर** is both the
  SI length unit and the electricity meter by the front door (g9 ch06).
  Both are masked by context patterns.
* `styles/`, `latexmkrc`, `tools/termlink/`, `tools/check_*.py` and every
  other language's files were not touched.

**Handover.** Complete: 142 bodies, image credits, term config, 6 110
links, nine green gates and a 0/0/0 build at 429 pp. The working tree is
left uncommitted for review.
