"""Book 2 -- es. Curation only; the rules live in tools/termlink/.

Every key is optional: anything left out falls back to the defaults in
tools/link_defined_terms.py (empty sets, AMBIG_POLICY "drop").

Spanish costs this book two curation problems English does not have:
homographs the English text keeps apart with two different words
("tension" and "voltage" are both *tensión*; "power" and "power of ten"
are both *potencia*), and bare adjectives harvested out of a phrase whose
feminine singular is ordinary language (*absoluta*, *delgada*, *estable*).
"""

NOT_A_TERM = ()

# Words that name something else in ordinary prose, or whose sense in the
# book is not the sense the definition gives them. (A STOPped word is still
# linked inside the chapter that defines it.)
STOP = {
    # harvested from the velocity-vector definition (g12 kinematics), but the
    # word runs from grade 10 on, almost always before that definition
    # exists. "velocidad media", "velocidad del sonido" survive as phrases.
    "rapidez",
    # radiation sense (g11 nucleus) is right in the nuclear chapters and
    # wrong in the relativity chapter, where prose "gamma" is the dilation
    # factor. "radiación gamma" survives as a phrase.
    "gamma",
    # standing-wave node (g12 sound); the circuits chapters use "nodo" for a
    # junction in Kirchhoff's sense.
    "nodo", "nodos",
    # the fundamental of a note (g12 sound); elsewhere the adjective is
    # ordinary -- and "interacción fundamental", "estado fundamental" are
    # terms of their own.
    "fundamental",
    # harvested from "trabajo motor" (g11); bare "motor" is the engine,
    # from the rocket's to the electric one. The phrase survives.
    "motor",
    # oscilloscope gain (g10 signals); "ganancia" is also the ordinary gain
    # of anything -- resolution, energy, speed.
    "ganancia",
    # THE Spanish homograph: rope tension (g10 inertia) and electrical
    # voltage (g11 circuits) share one word, so no chapter ordering can place
    # it right -- every mechanics chapter of grade 12 would link to the
    # voltage definition. Linked only inside its two defining chapters.
    "tensión",
    # ordinary words of the register, never harvested bare in the current
    # text but kept here as a guard if a later edit defines them alone.
    # ("fuerza", "energía", "trabajo", "campo" and "onda" are deliberately
    # NOT here: they are harvested, they are unambiguous in Spanish, and
    # English links them book-wide -- stopping them cost 600 links of
    # coverage for nothing.)
    "real", "normal", "uniforme", "velocidad",
}

NO_CAPITAL = {
    # capitalized, these are the physicists, not the units. The other SI
    # units are spelled differently in Spanish (julio/Joule, voltio/Volt,
    # culombio/Coulomb, hercio/Hertz, ohmio/Ohm, faradio/Farad,
    # henrio/Henry, becquerelio/Becquerel), so they carry no such clash.
    "newton", "pascal", "kelvin", "tesla",
}

EXTRA = {}            # manual {term: label}; overrides every rule

DROP = {
    # bare feminine adjective harvested from the diving method ("presión
    # absoluta"); it also opens "temperatura absoluta" and "incertidumbre
    # absoluta", where a link to the pressure method would be wrong. All
    # three full phrases survive as terms of their own.
    "absoluta",
    # display form with math in it; never matches prose. The dilation theorem
    # is reachable through "dilatación del tiempo".
    "factor $\\gamma$ (gamma)",
    # bare adjective from "lente delgada"; "lámina delgada", "capa delgada"
    # have nothing to do with optics. The lens phrases survive.
    "delgada",
    # bare adjectives from the equilibrium proposition; "núcleo inestable",
    # "plomo estable", "órbita estable" are everywhere. "equilibrio estable"
    # and "equilibrio inestable" survive.
    "estable", "inestable",
    # ordinary words of the register, harvested from definitions that merely
    # use them: "vertical" (from the weight definition), "segundo" (from the
    # SI-units definition -- but "el segundo postulado", "el segundo
    # término" are ordinals), "en reposo" (from the reference-frame
    # definition, though the phrase means "motionless" everywhere),
    # "escapa" (the ordinary verb: argon escapes the lava).
    "vertical",
    "segundo",
    "en reposo", "reposo",
    "escapa",
}

DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"   # a spiral curriculum re-defines its terms
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40

EXTRA_PROTECT = [
    # mechanics' drag, not the electrical quantity
    r'resistencia del aire',
    # "potencia" is both power and a mathematical power
    r'potencias? de (?:diez|dos)',
    # the spring's compression, not the acoustic one
    r'compresión máxima',
    # the Sun's core is neither an optical-fibre core nor an atomic nucleus
    r'núcleo del Sol',
    # a full-court basketball shot, not an electric or magnetic field
    r'campo entero',
]
