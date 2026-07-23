"""Book 2 -- pt. High-school physics: AMBIG_POLICY nearest-preceding."""

NOT_A_TERM = ("teorema", "lema", "desigualdade", "fórmula", "critério",
              "princípio", "identidade", "regra", "lei de", "lei da",
              "paradoxo", "problema")

STOP = {
    "real", "normal", "nó", "repouso", "uniforme", "velocidade",
    "força", "energia", "trabalho", "campo", "onda",
}

NO_CAPITAL = {
    "newton", "joule", "watt", "pascal", "kelvin", "tesla", "hertz",
    "coulomb", "volt", "ampère", "ohm", "becquerel", "henry", "farad",
}

EXTRA = {}
DROP = set(STOP)
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40
EXTRA_PROTECT = []
