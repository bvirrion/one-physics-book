# One Physics Book

<p align="center">
  <a href="https://www.one-course.com">
    <img src="assets/one-course-logo.svg" alt="One Course — one-course.com" width="420">
  </a>
</p>

*The One Physics Book to Rule Them All.*

> **One Physics Book** is part of the **One Course** project — one coherent
> course covering each subject from kindergarten to the end of the bachelor's
> degree. Discover the whole project at
> **[www.one-course.com](https://www.one-course.com)**.

A series of physics books, written in English for readers anywhere in the
world, with the ambition of covering everything **from kindergarten to the
end of the bachelor's degree** — as one coherent course, published in
several volumes:

1. **Primary & Middle School Physics** — Grades 1–9;
2. **High School Physics** — Grades 10–12;
3. **University Physics — Year 1**;
4. **University Physics — Year 2**;
5. **University Physics — Year 3**.

The contents follow the old French physics programs: the physics parts of
the collège and lycée « S » (scientifique) track for the school years, the
PCSI and PC\* classes préparatoires for the first two university years, and
a Licence 3 de physique for the third. Unlike those programs, this course
is **physics only** (no chemistry), and the early grades — where French
schools taught no physics — are covered by age-adapted chapters so that the
course truly starts in Grade 1.

The style is concise and rigorous: courses built from **definitions,
examples, propositions, theorems and methods**, with derivations whenever
they are accessible at the given level (results admitted without proof are
explicitly marked), followed by graded **exercises with full solutions**
collected at the end of each book.

## Current status

🚧 **Structure established, content in progress.** All five books build,
with every chapter present as a titled placeholder; course text, figures,
exercises and solutions are being written.

## Building the books

Requirements: a TeX Live installation with `latexmk` (packages used:
`tcolorbox`, `pgfplots`, `amsthm`, `cleveref`, `imakeidx`, …).

```sh
make            # or just: latexmk — builds all books
```

The PDFs are produced at

```
build/one_physics_book_1_primary_middle_school.pdf
build/one_physics_book_2_high_school.pdf
build/one_physics_book_3_university_year_1.pdf
build/one_physics_book_4_university_year_2.pdf
build/one_physics_book_5_university_year_3.pdf
```

`make clean` removes auxiliary files, `make distclean` removes the whole
`build/` directory. To build a single book, e.g.\
`latexmk one_physics_book_2_high_school.tex`.

## Repository layout

```
one_physics_book_<N>_*.tex   entry file per book (N = series number)
styles/onephysics.sty        packages, theorem environments, macros
styles/lang/<lang>.tex       UI strings (en for now)
frontmatter/                 title page, preface (shared layout)
parts/<year>/part.tex        shared structure for a school year
parts/<year>/NN-*.tex        English chapter
parts/<year>/solutions/      solutions, one file per chapter
```

## Contributing

Contributions are welcome — new chapters and years, corrections, better
derivations, additional exercises, figures. Please read
[CONTRIBUTING.md](CONTRIBUTING.md) for the structure, environments and
style conventions of the project.

## Contributors

- Benjamin Virrion
- Fable 5 (Anthropic's Claude)

## License

Not yet decided.
