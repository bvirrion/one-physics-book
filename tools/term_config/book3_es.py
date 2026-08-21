"""Book 3 -- es. Curation only; the rules live in tools/termlink/.

Every key is optional: anything left out falls back to the defaults in
tools/link_defined_terms.py (empty sets, AMBIG_POLICY "drop").

Curated 2026-08-21 against the English curation (`book3_en.py`), which this
file follows term for term wherever the two languages agree, plus the
homographs Spanish creates on its own: *tensión* is both the rope's tension
and the circuit's voltage, *central* is both the adjective of a central
force and the power station of chapter 24, *par* is both the torque and
"a pair of", *capacidad* is both the capacitance and the ordinary capacity
of a machine, and *cámara* is both the camera of chapter 4 and the cold
chamber of chapter 24.
"""

# Ordinary language in this register, or a word whose sense elsewhere in the
# book is not the sense its definition gives it. (A STOPped word is still
# linked inside the chapter that defines it.)
STOP = {
    # the bare nouns of mechanics and thermodynamics: from chapter 12 on
    # they are on every page, and a link on each is noise. Every compound
    # ("fuerza central", "velocidad angular", "presión cinética", "trabajo
    # perdido", "calor latente", ...) survives as a term of its own.
    "fuerza", "masa", "velocidad", "aceleración",
    "presión", "temperatura", "calor", "trabajo",
    # the Spanish for "momentum", stopped in English for the same reason;
    # "conservación de la cantidad de movimiento" survives.
    "cantidad de movimiento",
    # the unit (kinetic theory) vs the sliding bar of the Laplace rails
    "bar",
    # moment of a force (ch. 15) vs "en el momento en que", "por el momento"
    "momento",
    # the optical image (ch. 3) vs "imagen especular" in the symmetry
    # chapters and "la imagen ondulatoria" in ch. 30
    "imagen",
    # optical focus (ch. 3) vs the verb "enfocar"/"foco" of a light source
    "foco",
    # op-amp gain (ch. 10) vs the ordinary "ganancia" of anything
    "ganancia",
    # fibre core (ch. 2) vs the Earth's core (ch. 26), the coaxial core
    # (ch. 28) and the atomic nucleus (chs. 26--30) -- all "núcleo"
    "núcleo",
    # flux of the electric field (ch. 26) vs the magnetic flux (ch. 29)
    "flujo",
    # the SI unit (ch. 1) vs "vector unitario", "por unidad de longitud"
    "unidad",
    # physical dimension (ch. 1) vs "las dimensiones de la sala", "en una
    # dimensión"
    "dimensión",
    # thermodynamic transformation (ch. 22) vs ordinary usage elsewhere
    "transformación",
    # the objective of an instrument (ch. 4) vs the adjective
    "objetivo",
    # THE Spanish homograph: the rope's tension (mechanics) and the
    # circuit's voltage (chs. 6--10, 27) are one word, so no chapter order
    # can place it right. "divisor de tensión", "fuente de tensión",
    # "tensión de saturación", ... survive.
    "tensión",
    # torque (ch. 15) vs "un par de hilos", "el par de cargas"
    "par",
    # capacitance (ch. 27) vs the ordinary capacity of a compressor, a
    # battery, a pipe. "capacidad calorífica ..." survives.
    "capacidad",
    # the photographic camera (ch. 4) vs the cold chamber of a refrigerator
    # and the bubble chamber of ch. 25
    "cámara",
}

NO_CAPITAL = {
    # capitalized, these are the physicists, not the units. The other SI
    # units are spelled differently in Spanish (julio/Joule, voltio/Volt,
    # culombio/Coulomb, hercio/Hertz, ohmio/Ohm, faradio/Farad,
    # henrio/Henry, amperio/Ampère), so they carry no such clash.
    "newton", "pascal", "kelvin", "tesla", "weber",
}

EXTRA = {}            # manual {term: label}; overrides every rule

DROP = {
    # bare adjectives harvested from definitions that merely use them; the
    # phrases they came from ("gas ideal", "amplificador operacional
    # ideal", "circuito lineal", "régimen lineal", "fuerza central",
    # "fuerza conservativa") all survive as terms of their own.
    "ideal", "lineal", "central", "conservativa",
    # harvested from "\emph{central conservativa}" -- a two-word adjective
    # phrase, never a noun phrase in prose
    "central conservativa",
}

DERIVED = {}
PRIMARY_OK = set()

EXTRA_PROTECT = [
    # the drag of the air, not the electrical quantity
    r'resistencia del aire',
    # a moving-coil meter's "cuadro móvil" is not the optical frame
    r'cuadro móvil',
]

AMBIG_POLICY = "drop"          # the university convention (books 3, 4, 5)
