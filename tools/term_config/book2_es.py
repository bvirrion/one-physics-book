"""Book 2 -- es. Curation only; the rules live in tools/termlink/.

High-school physics: AMBIG_POLICY nearest-preceding for school spiral.
"""

NOT_A_TERM = ("teorema", "lema", "desigualdad", "fórmula", "criterio",
              "principio", "identidad", "regla", "ley de", "ley de la",
              "paradoja", "problema")

STOP = {
    "real", "normal", "nodo", "reposo", "uniforme", "velocidad",
    "fuerza", "energía", "trabajo", "campo", "onda",
}

NO_CAPITAL = {
    "newton", "joule", "watt", "pascal", "kelvin", "tesla", "hertz",
    "coulomb", "volt", "amperio", "ohm", "becquerel", "henry", "faradio",
}

EXTRA = {}
DROP = set(STOP)
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40
EXTRA_PROTECT = []
