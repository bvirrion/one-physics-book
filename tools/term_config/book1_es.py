"""Book 1 -- es. Curation only; the rules live in tools/termlink/.

Young-book register: most of the defined vocabulary is also ordinary
Spanish, so a word earns a link only when it means the defined thing in
nearly all of its uses.

The Spanish traps are not the English ones. "medio" is the medium of a
sound, the middle of anything and the half of everything ("media hora",
"medio metro"); "fuente" is a light source and a power supply; "materia"
is matter and a school subject; "peso" is weight and money; "corriente"
is the electric current and the adjective "ordinary"; "potencia" is
electrical power and a mathematical power of ten. The bare adjectives
harvested from Spanish phrases ("uniforme", "recta", "llena") are
ordinary language on every page.
"""

NOT_A_TERM = ("teorema", "lema", "desigualdad", "fórmula", "criterio",
              "principio", "identidad", "regla", "ley de", "paradoja",
              "problema")

STOP = {
    # moon sense in its chapters; "la fase siguiente" of any process
    # elsewhere. "fases" survives -- almost always lunar.
    "fase",
    # magnet sense in its chapters; the Earth's geographic poles and the
    # poles of an alternator elsewhere.
    "polo", "polos",
    # circuit-diagram sense in its chapter; "el símbolo \\unit{A}" and the
    # mathematical symbols elsewhere.
    "símbolo",
    # THE Spanish homograph of this book: the medium a sound travels
    # through (g7) against "medio metro", "en medio de", "por medio de"
    # everywhere else. Linked only inside its own chapter.
    "medio", "medios",
    # the light source (g1) against "fuente de alimentación", "fuente de
    # energía" and the water fountain. The phrases survive.
    "fuente", "fuentes",
    # the electric current (g7) against the adjective ("una lámpara
    # corriente", "el aire corriente"). "corriente eléctrica" survives.
    "corriente",
    # electrical power (g9) against "potencias de diez" and "la potencia
    # de un imán". "potencia eléctrica" survives.
    "potencia",
}

NO_CAPITAL = {
    # capitalized, these are the physicists, not the units
    "newton", "julio", "vatio", "voltio", "amperio", "ohmio", "hercio",
    # sentence-initial these are imperatives ("Mide el filamento"),
    # not the defined nouns
    "mide", "medir", "observa",
}

EXTRA = {}            # manual {term: label}; overrides every rule

DROP = {
    # ordinary adjectives and verbs of the young register
    "caliente", "Caliente", "frío", "Frío",
    "sentido", "sentidos", "vista", "tacto", "olfato", "gusto", "oído",
    # ordinal "segundo" everywhere; the unit survives in "por segundo"
    "segundo", "segundos",
    # "en ese momento", "un instante" -- ordinary time words (the
    # duration definition names them both; "duración" keeps its link)
    "momento", "momentos", "instante", "instantes",
    # bare adjectives; "circuito abierto", "circuito cerrado",
    # "movimiento uniforme", "movimiento variado" survive as phrases
    "abierto", "cerrado", "recta", "rectas", "circular", "uniforme",
    "variado", "llena", "lleno",
    # "este año", "el año pasado": ordinary everywhere. "año luz" survives.
    "año", "años",
    # ordinary time-of-day words; "amanecer", "atardecer" keep their links
    "noche", "Noche", "día", "Día", "días",
    # ordinary verbs harvested from the definitions ("la lámpara se
    # enciende", "el cable se calienta"); the nouns "luz" and "calor"
    # keep their links
    "enciende", "encender", "calienta", "calentar",
}

DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"   # a spiral curriculum re-defines its terms
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40

# NOTE: multi-word patterns use \s+ between words -- a phrase wrapped
# across a source line break must still be protected.
EXTRA_PROTECT = [
    # mechanics' drag (g9 parachutist), not the electrical quantity
    r'resistencia\s+del\s+aire',
    # mathematics' powers, not electric power
    r'potencias?\s+de\s+diez',
    # the buildings, not the quantity P = UI
    r'central(?:es)?\s+(?:eléctrica|hidroeléctrica|nuclear|térmica)\w*',
    # "media hora", "media vuelta": the feminine of "medio", not the mean
    r'\b[Mm]edias?\s+(?:hora|vuelta|altura|manzana|docena|tableta|luna)\w*',
    r'\bhora\s+y\s+media\b',
    # "a medias", "en medio de", "por medio de": ordinary prose
    r'\b(?:a|en|por)\s+medios?\b',
    r'\bmedio\s+(?:de\s+)?(?:campo|tubo|metro|litro|kilo)\w*',
    # the ordinary adjective, not the electric current
    r'\bcorrientes?\s+(?:de\s+aire|abajo|arriba)\b',
    # a book of the series, not the space a body occupies
    r'\b(?:este|el)\s+volumen\b',
    r'\bvolumen\s+de\s+bachillerato\b',
    # headphone loudness, not the space a body occupies
    r'\ba\s+todo\s+volumen\b',
    # the verb ("enciende la luz"), not the phenomenon
    r'\bluz\s+verde\b',
    # "con fuerza", "a la fuerza", "por fuerza": the adverb, not the
    # physical quantity ("una fuerza de", "la fuerza del imán" survive)
    r'\b(?:con|a\s+la|por)\s+fuerza\b',
    # "estación" is the season only in its own chapters: the space
    # station, the train station and the metro stop are all estaciones
    r'estación\s+(?:espacial|tripulada|de\s+tren)',
    r'[Ll]a\s+estación\s+y\s+la\s+tripulación',
    r'a\s+la\s+estación\s+en\s+su',
    r'la\s+estación,\s+la\s+gravedad',
    r'suelos\s+de\s+las\s+estaciones',
    r'entre\s+estaciones',
    # the underground railway, not the unit of length
    r'trayecto\s+de\s+metro',
]
