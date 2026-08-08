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
    'one_physics_book_2_high_school_ar.tex',
    'one_physics_book_3_university_year_1.tex',
    'one_physics_book_4_university_year_2.tex',
    'one_physics_book_5_university_year_3.tex',
);
# Hindi editions (*_hi.tex) need XeLaTeX for OpenType Devanagari, and Arabic
# editions (*_ar.tex) need LuaLaTeX for babel's Lua bidi engine (bidi=basic); every other
# edition builds with pdfTeX. The choice is made per *source file*, inside the
# command latexmk runs, and deliberately not by setting $pdf_mode:
#
#   * a command-line engine flag beats the rc file, and the release workflow
#     calls `latexmk -pdf <root>` for every book, so any $pdf_mode this file
#     sets is overwritten before the Hindi entry is compiled;
#   * scanning @ARGV only worked while the .tex files were the whole command
#     line -- the workflow puts options in front of them.
#
# Both routes sent the Hindi books through pdflatex, where the guard in
# styles/onephysics.sty stops the build ("Hindi editions require XeLaTeX").
# Dispatching on %S is immune to both, because latexmk hands the routine the
# file it is actually compiling.
#
# The books' many TikZ/pgfplots figures also exceed pdfTeX's default main
# memory (5M words), hence the raised runtime limits.
$pdflatex = 'internal op_compile %O %S';
$xelatex  = 'internal op_compile %O %S';
$lualatex = 'internal op_compile %O %S';

sub op_compile {
    my @args = @_;
    my $source = pop @args;
    my @engine = $source =~ /_hi\.tex$/
        ? ('xelatex', '-interaction=nonstopmode', '-halt-on-error')
        : $source =~ /_ar\.tex$/
        ? ('lualatex', '-interaction=nonstopmode', '-halt-on-error')
        : ('pdflatex',
           '-cnf-line=main_memory=12000000',
           '-cnf-line=extra_mem_top=6000000',
           '-cnf-line=extra_mem_bot=6000000',
           '-interaction=nonstopmode', '-halt-on-error');
    return system(@engine, @args, $source);
}
$makeindex = 'makeindex %O -o %D %S';
