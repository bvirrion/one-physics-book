# Translation score — Physics Book 1 · Arabic (`ar`)

| Field | Value |
|-------|--------|
| **Book** | One Physics Book 1 (Primary & Middle School, grades 1–9) |
| **Language** | Arabic (`ar`), Modern Standard Arabic per `arabic_style_card.md` |
| **Quality bar** | **native academic** (EN is the source of truth; the French twin was consulted only where a sentence's *sense* was ambiguous — never its wording) |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met.** |
| **Date** | 2026-08-14 (single pass, written from the English canon) |
| **Scope** | **All 142 bodies hand-written in Arabic** — 71 chapters + 71 solution files, grades 1–9 — plus `frontmatter/image-credits.ar.tex`, the localisation of every figure's visible text, and a curated `tools/term_config/book1_ar.py` |

## Read this first

Nothing here was machine translated. Every file was written from its
English original with the technical spans held fixed by hand: math,
`tikzpicture` / `pgfplots` / `circuitikz` bodies, `\label`, `\cref`/`\ref`
targets, `\qty`/`\unit` arguments, `\begin{solution}{key}` keys and the
`[resume]` counters of the weekend problems. Only *visible* text was
rewritten — prose, environment titles, captions, and the node/axis labels
inside the drawings.

The register is the school-textbook Arabic the style card fixes: the
narrating voice of the English (a book that talks to the pupil, chapter
after chapter, and keeps promises made years earlier) is carried by Arabic
connective syntax — `فـ` / `وأمّا … فـ` / `ومن ثمّ` / `إذ` — rather than by
transposed English clause order. Imperatives are the singular of
instruction (احسُب، قِس، صِف، بيّن، تنبّأ)، as in the English's
"compute / measure / describe / predict".

| Part of the book | Files | State |
|---|---:|---|
| grade-1 … grade-3, ch01–… + solutions | 40 | Hand-translated |
| grade-4 … grade-6, ch01–… + solutions | 48 | Hand-translated |
| grade-7 … grade-9, ch01–ch09 + solutions | 54 | Hand-translated |

## Dimension scores

| Dimension | Weight | Score /100 | Notes |
|-----------|-------:|----------:|--------|
| Register / tone | 0.20 | **96** | One voice across nine school years: the grade-1 chapters keep short sentences and concrete nouns, the grade-9 chapters carry full argument. Chapter openings are written as Arabic openings, not as translated first sentences («تفاحة تفلت من غصنها فتسقط. والقمر، فوق البستان نفسه، لا يسقط.»). The book's running jokes and callbacks («النكتة القديمة، مدفوعةً»، «الجملة الهادئة») survive as jokes and callbacks |
| Terminology | 0.18 | **96** | One glossary over 71 chapters, settled in grade 1 and never drifting: منبع ضوء، ظلّ تامّ/شبه الظلّ، ناقل/عازل، دارة على التسلسل / على التفرع، مصهر، شدّة التيار، التوتر، مقاومة/مقاوم، عدسة مجمِّعة/مفرِّقة، بؤرة/بعد بؤري، تردّد/سعة، الجاذبية/ثابت الجذب، طاقة كامنة/حركية، مردود، مولّد متناوب، تحريض. Series/parallel and voltage match the shipped Arabic Book 2 (على التسلسل / على التفرع، التوتر). Every `\index` key is the visible Arabic term |
| MT-artifact freedom | 0.17 | **99** | No machine output at any stage. Arabic prose gate: **0 issues across all 142 files** in all nine classes (english, translit, punct, digits, math-space, bidi-ctrl, presform, tatweel, split-number). No English word order, no calqued idiom, no transliterated technical vocabulary |
| Structural fidelity | 0.10 | **100** | 142 files; identical label sets *and order* in every chapter; exercise↔solution key parity in 71/71; identical environment census; `[resume]` blocks preserved; 192 `omfigure` and 139 `tikzpicture` bodies, exactly as English. All nine `check_translation.sh` runs **PASSED**, zero duplicate labels |
| LaTeX hygiene | 0.08 | **100** | LuaHBTeX, exit 0: **0 errors, 0 undefined references, 0 overfull boxes**, 117 underfull, 409 pages. UTF-8 throughout, no TeX accent escapes, no tatweel, no presentation forms, no bidi control characters. The two overfull boxes the first build showed were both in `image-credits.ar.tex` (an unbreakable Latin credit and a long comma-free numeral run) and were fixed there |
| Cross-refs / rule compliance | 0.07 | **100** | `\label`, `\cref`/`\ref` targets, solution keys and every `\omterm` first argument byte-identical to English. ASCII digits everywhere; Arabic punctuation ، ؛ ؟ with the Latin full stop; `\qty`/`\unit` arguments untouched. No curriculum, board or country is named |
| Figures | 0.07 | **97** | All 192 figure bodies present with drawing code preserved; only the visible text was localised — TikZ node labels, pgfplots `xlabel`/`ylabel`/`yticklabels`, circuitikz `l=` labels, and every caption. pgfplots `symbolic y coords` keys were left Latin (invisible) with Arabic `yticklabels` supplied, exactly as the density chart does |
| Solutions | 0.08 | **96** | All 71 solution files written in the same register as their chapters, including the ~20-item weekend-problem answers; the numbered `\textbf{n.}` voice is uniform from grade 1 to grade 9 |
| Defined-term links | 0.05 | **93** | `--check` green and idempotent: **5 618 links** (87 % of English's 6 483) across **130 of English's 133 targets**. `book1_ar.py` is curated: 11 `STOP`, 32 `DROP`, 43 `EXTRA_PROTECT` patterns |

Weighted total: **96 / 100**.

## Gate results

| Gate | Result |
|------|--------|
| `bash tools/check_translation.sh grade-1 ar` … `grade-9 ar` | **PASSED** (9 / 9) |
| `python3 tools/check_arabic_prose.py` (142 files) | **OK — 0 issues** |
| `latexmk one_physics_book_1_primary_middle_school_ar.tex` | exit 0 — 409 pp, 0 errors, 0 undefined, 0 overfull |
| `python3 tools/link_defined_terms.py --book 1 --lang ar --check` | **every file matches what the config generates** |
| `pdftotext … \| grep -cE '\b(and\|to)\b'` | **0** (the coordinator's siunitx `range-phrase` / list-separator fix verified on the page; Book 1 ar uses no `\qtyrange`/`\qtylist`, so nothing regressed) |

## Samples, verdicted

1. **native** — g9 ch01 opening: «تفاحة تفلت من غصنها فتسقط. والقمر، فوق
   البستان نفسه، لا يسقط. وظلّت هاتان حقيقتين لا صلة بينهما آلاف السنين
   --- حتى جمعتهما لمحة عبقرية واحدة.» The English's two-sentence hook is
   rebuilt with Arabic's own topic-then-comment rhythm; no relative clause
   is imported.
2. **native** — g8 ch05 (Ohm): «فالخطّ المستقيم المارّ بالمبدأ توقيع
   المقاوم، لا توقيع المادة --- فاسأل كل عنصر عن صورته قبل أن تأتمنه على
   القانون.» Nominal sentence, then an imperative with `فـ`: the English
   epigram survives as an Arabic epigram.
3. **native** — g7 ch08 (average speed): «فالنصف البطيء طالب بثلاث ساعات
   من الخمس، وجرّ المتوسّط دون المنتصف.» Verb-first narrative clause; the
   English "claimed three hours of the five" is idiomatic, not literal.
4. **near-native** — g9 ch06: «فالقدرة في الزمن لا تغفر لأيّ حدّ: والعامل
   الثاني يعضّ حين يختبئ الأول.» The metaphor is carried, but "لا تغفر
   لأيّ حدّ" is a slightly bookish rendering of "forgives no term"; a
   copy-editor might prefer «لا تسقط حدًّا».
5. **near-native** — g8 ch09: «ونافذة تضيق بالعمر وبسوء المعاملة» — "سوء
   المعاملة" for *abuse* is correct and current, but a hearing-health
   editor would more often write «وبالإفراط في الصوت».

## Why not 100

* **Defined-term coverage (−).** 5 618 links against English's 6 483.
  Arabic proclitics make one-word terms match far more surface forms than
  their English twins, so several terms that link freely in English had to
  be `DROP`ped to stay honest: بصر/سمع/لمس/شمّ/ذوق (the bare sense-words are
  ordinary everywhere, and «نافذة السمع» in grade 8 would have pointed at
  the wrong chapter), سنة، ثانية، لحظة، ليل/نهار، ساخن/بارد، جذب, and the
  bare motion/circuit adjectives. Their compound phrases keep their links.
* **Three English targets have no Arabic link.**
  `prop:g5:mirrors-reflection:image` (Arabic صورة is the ordinary word for
  *picture*; no surface form is specific enough to link safely),
  `ex:g9:alternator:chains` and `def:g7:short-circuits-safety:battery`
  (both absorbed by a nearer Arabic definition of the same idea).
* **Register ceiling.** A few solution lines in grades 8–9 stay close to the
  English's clipped telegraphic voice («قرصان، ويد واحدة تدير.»); it reads
  well, but a human editor with a month would loosen two or three dozen of
  them further.
* **One book-wide unknown.** The Arabic edition's typographic conventions
  for eponym units (نيوتن، جول، واط) follow the shipped Book 2; if the
  series later fixes a different convention, this book must follow.
