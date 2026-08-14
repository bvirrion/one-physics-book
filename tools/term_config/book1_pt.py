"""Book 1 -- pt. Curation only; the rules live in tools/termlink/.

Young-book register (cf. book1_en.py): most of the defined vocabulary is
also ordinary Portuguese, so a word earns a book-wide link only if it
means the defined thing in nearly all of its uses. Everyday furniture
words are DROPped (their compound phrases survive as terms of their
own); words that are honest terms inside their own chapter and ordinary
language elsewhere are STOPped.

Brazilian Portuguese adds four curation problems the English text does
not have:

* homographs the English keeps apart with two different words: *meio* is
  the sound's medium and also "half/middle/by means of"; *sentido* is a
  sense of the body and also the direction of a current; *intensidade*
  is the current's intensity and also the magnitude of a force;
* one term colliding with a function word: *nós* is both the junctions
  of a circuit and the pronoun "we/us";
* unit names spelled exactly like the physicists they honour (newton,
  joule, watt, volt, ampère, ohm, hertz), separated only by the capital;
* ordinary words that happen to be terms elsewhere in the book: *grama*
  (gram, but also "grass"), *volume* (the space a body occupies, but
  also a volume of this series), *estação* (season, but also a station).
"""

STOP = {
    # honest in its chapter, ordinary emphasis elsewhere ("observe que")
    "observação", "observar", "Observar",
    # equilibrium sense in its chapter; "as contas se equilibram" and
    # ordinary "uma dieta equilibrada" elsewhere
    "equilibrada",
    # moon sense in its chapter; "as duas fases da queda" of any process
    # elsewhere
    "fase", "fases",
    # magnet sense in its chapters; the Earth's geographic poles and the
    # rotor's poles elsewhere. "polo norte", "polo sul" survive.
    "polo", "polos",
    # circuit-diagram sense in its chapter; "o símbolo \\unit{A}" and the
    # math symbols elsewhere
    "símbolo",
    # THE Portuguese collision of this book: *meio* is the sound's medium
    # (g7) and, everywhere else, "half", "the middle", "by means of" --
    # "no meio do túnel", "por meio de", "meia-cana". Linked inside the
    # chapter that defines it.
    "meio",
    # the current's intensity (g8-02) -- but "de intensidade" also names
    # the magnitude of a force (g9 gravitation) and "intensidade sonora"
    # the loudness of a sound. The two phrases survive as terms.
    "intensidade",
    # the junctions of a parallel circuit -- and the pronoun "we/us",
    # which this book uses on nearly every page ("a luz chega até nós").
    "nós",
    # Portuguese has ONE word where English alternates two: *lâmpada* is
    # both the "bulb" English links and the "lamp" English leaves alone.
    # Linked book-wide it carried 504 links against English bulb's 228 --
    # 7 % of the whole layer on a single word, and the page read visibly
    # bluer than the English one. Linked inside the chapter that defines
    # it; the phrases "lâmpada de filamento", "lâmpada indicadora" and
    # the circuit terms around it keep their own links.
    "lâmpada",
}

NO_CAPITAL = {
    # capitalized, these are the physicists, not the units; Portuguese
    # spells the two alike ("a lei de Ohm", "dois ohms").
    "newton", "newtons", "joule", "joules", "watt", "volt", "ampère",
    "ohm", "hertz",
    # sentence-initial these are imperatives ("Medir uma intensidade",
    # "Observar o mundo"), not the defined nouns
    "medir", "observar",
}

EXTRA = {}            # manual {term: label}; overrides every rule

DROP = {
    # ordinary adjectives of the register, harvested from the gentle
    # grade-1/2 definitions; linking them everywhere is noise
    "quente", "Quente", "frio",
    # the five senses: "sentido" is above all the direction of a current
    # or of a motion in this book; the others are ordinary nouns
    # ("à vista", "ao toque"). English drops exactly the same set --
    # sense/senses/sight/touch/smell/taste -- and keeps "hearing", so
    # "audição" is deliberately NOT dropped here: it is what keeps
    # def:g1:five-senses:senses reachable, as it does in English.
    "sentido", "visão", "tato", "olfato", "paladar",
    # the unit -- but "segundo" is also the ordinal ("o segundo ramo")
    # and a conjunction; the unit survives through "por segundo" prose
    "segundo",
    # "naquele instante" -- ordinary time word
    "instante",
    # bare adjectives; "circuito aberto", "circuito fechado",
    # "trajetória retilínea", "trajetória circular", "movimento
    # uniforme" and "movimento variado" survive as phrases
    "aberto", "fechado", "retilínea", "circular", "uniforme", "variado",
    # "neste ano", "no ano que vem", "nove anos": ordinary everywhere;
    # "ano-luz" and "o ano e as estações" survive
    "ano",
    # ordinary time-of-day words used constantly ("o dia a dia", "hoje à
    # noite"); "nascer do sol" and "pôr do sol" keep their links
    "dia", "noite",
}

DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"   # a spiral curriculum re-defines its terms
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40

# Two rules hold for EVERY pattern below:
#   * NEVER consume a `$` -- match it with a lookahead. The list is one
#     alternation scanned left to right, so eating an opening $ leaves
#     the inline-math rule pairing the closing $ with the next formula's
#     opening one, and the mask runs inside out to end of file.
#   * NEVER write a literal space -- always `\s+`. The list is compiled
#     with re.S and real prose wraps across source lines.
EXTRA_PROTECT = [
    # mechanics' drag, not the electrical quantity
    r'resistência\s+do\s+ar',
    # the kettle's and the toaster's heating element, not the quantity R
    r'resistência\s+d[aeo]\s+(?:chaleira|torradeira|aquecimento)',
    # mathematics' powers, not electric power
    r'potências?\s+de\s+(?:dez|dois)',
    # the electricity bill, not the phenomenon
    r'conta\s+de\s+luz',
    # a volume of this series, not the space a body occupies
    r'volumes?\s+do\s+ensino\s+médio',
    r'volume\s+do\s+(?:primeiro|segundo|terceiro)\s+ano',
    # grass, not the unit of mass
    r'a\s+grama\s+é\s+verde',
    # stations of every other kind, not the seasons of the year
    r'estaç(?:ão|ões)\s+(?:espacial|espaciais|de\s+medida)',
    r'(?:entre|duas|quatro)\s+estações',
    # the iron core of an electromagnet and the deep core of a planet,
    # not the nucleus of an atom
    r'núcleos?\s+de\s+ferro',
    r'núcleo\s+(?:profundo|d[oa]\s+(?:Terra|Sol|usina))',
    # the orbital period of a satellite, not the period of an
    # alternating voltage
    r'período\s+orbital',
    # the verb ("ligar/desligar o interruptor"), not the component
    r'interruptor\s+(?:aberto|fechado)\s+d[eo]\s+teste',
    # adverbial "com força" = hard, strongly ("entortam com força",
    # "sacodem com força demais"), not the measured quantity
    r'com\s+força',
]
