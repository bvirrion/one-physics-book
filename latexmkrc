# latexmk configuration for the One Physics Book series
$pdf_mode = 1;              # pdflatex
$out_dir = 'build';
# One entry file per book; each PDF is named after its entry file
# (build/one_physics_book_<N>_<slug>.pdf).
@default_files = (
    'one_physics_book_1_primary_middle_school.tex',
    'one_physics_book_2_high_school.tex',
    'one_physics_book_2_high_school_fr.tex',
    'one_physics_book_2_high_school_nl.tex',
    'one_physics_book_2_high_school_es.tex',
    'one_physics_book_2_high_school_pt.tex',
    'one_physics_book_2_high_school_hi.tex',
    'one_physics_book_3_university_year_1.tex',
    'one_physics_book_4_university_year_2.tex',
    'one_physics_book_5_university_year_3.tex',
);
# The books' many TikZ/pgfplots figures exceed pdfTeX's default main
# memory (5M words); raise the runtime limits.
$pdflatex = 'pdflatex -cnf-line=main_memory=12000000 -cnf-line=extra_mem_top=6000000 -cnf-line=extra_mem_bot=6000000 -interaction=nonstopmode -halt-on-error %O %S';
# Hindi editions (*_hi.tex) need XeLaTeX for OpenType Devanagari. Entry files
# carry "% !TEX program = xelatex"; also force the engine when the jobname
# ends in _hi so a bare `latexmk file_hi.tex` works without relying on the
# magic-comment scan order.
$xelatex = 'xelatex -interaction=nonstopmode -halt-on-error %O %S';
# Hindi editions need XeLaTeX (OpenType Devanagari). Detect from @ARGV
# (latexmk puts the requested .tex files there when the rc file is read).
# Also honor a bare jobname without .tex and any path prefix.
for my $arg (@ARGV) {
    if ($arg =~ /_hi(\.tex)?$/) {
        $pdf_mode = 5;  # xelatex
        last;
    }
}
$makeindex = 'makeindex %O -o %D %S';
