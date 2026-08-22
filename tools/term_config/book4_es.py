"""Book 4 -- es. Curation only; the rules live in tools/termlink/.

Every key is optional: anything left out falls back to the defaults in
tools/link_defined_terms.py (empty sets, AMBIG_POLICY "drop").

Curated 2026-08-22 against Book 4's own Spanish harvest

    python3 tools/link_defined_terms.py --book 4 --lang es --terms

and term for term against the English curation of the same book
(`book4_en.py`), which stops five words -- laser, threshold, steady,
efficiency, absorption -- drops six harvest artefacts and adds two
lowercase device nouns.  The Book 3 seed that used to sit here was Book 3's
curation (mechanics, electrostatics, magnetism, optical instruments) and
most of it was dead weight in a book about rigid bodies, fluids, Maxwell's
equations, physical optics, diffusion, radiation, potentials and quantum
mechanics; what survived is listed below with its Book 4 reason.

Spanish adds four homographs of its own that English never meets:

  * *trayectoria* is the pathline of chapter 2 **and** the ordinary
    trajectory of a particle, a packet's centre, an alpha particle -- the
    word is on nearly every page of the book;
  * *estacionario* is the steady flow of chapters 2 and 27, the stationary
    state of chapter 30 and the standing wave's adjective;
  * *rendimiento* is the fin efficiency of chapter 25, the isentropic
    efficiency of chapter 27, the luminous efficiency of chapter 26 and the
    ordinary "rendimiento" of any machine;
  * *tensión* is the string's tension of chapter 6 and the circuit's
    voltage of chapters 9--10 (only the compound *tensión superficial* is a
    Book 4 term, so the bare word is stopped for safety).
"""

# Ordinary language in this register, or a word whose sense elsewhere in the
# book is not the sense its definition gives it. (A STOPped word is still
# linked inside the chapter that defines it.)
STOP = {
    # --- parity with book4_en.py -------------------------------------
    # "láser" is named in every optics chapter long before ch. 23 defines
    # it; a link on each occurrence would be noise
    "láser",
    # the laser threshold (ch. 23) vs the hearing threshold (ch. 7), a
    # perception threshold (ch. 24), "por encima del umbral"
    "umbral",
    # the steady flow of chs. 2 and 27 vs the adjective everywhere, and vs
    # the stationary states of ch. 30 ("estado estacionario" survives)
    "estacionario",
    # cycle and turbine efficiency (ch. 27) vs fin efficiency (ch. 25),
    # luminous efficiency (ch. 26), motor efficiency, quantum efficiency
    "rendimiento",
    # absorption of light (ch. 23) vs absorption of sound, of heat, of
    # X-rays, and the atmosphere's absorption bands (ch. 26)
    "absorción",
    # --- homographs Spanish creates on its own -----------------------
    # the pathline of ch. 2 vs the trajectory of a particle, of a packet's
    # centre, of an alpha particle: one word in Spanish, two in English
    "trayectoria",
    # the string's tension vs the circuit's voltage; only the compound
    # "tensión superficial" is a Book 4 term
    "tensión",
    # --- ordinary words of this register -----------------------------
    # moment of a force vs "en el momento en que", "por el momento"
    "momento",
    # loop gain (ch. 9) vs the ordinary gain of anything
    "ganancia",
    # the fibre core (ch. 16) and the coaxial core (ch. 8) vs the atomic
    # nucleus of chs. 17 and 31, all "núcleo"
    "núcleo",
    # the optical focus vs "enfocar", "el foco de una fuente"
    "foco",
    # the optical image vs "la imagen de los rayos", "la imagen
    # microscópica", "en la imagen de Lorentz"
    "imagen",
    # the steady flow of ch. 2 vs the steady state of chs. 5, 24 and 27,
    # where the same Spanish words carry the open-system sense that
    # "régimen estacionario" (ch. 27) already links
    "flujo estacionario",
}

NO_CAPITAL = {
    # capitalized, these are the physicists, not the units. The other SI
    # units are spelled differently in Spanish (julio/Joule, voltio/Volt,
    # culombio/Coulomb, hercio/Hertz, ohmio/Ohm, faradio/Farad,
    # henrio/Henry, amperio/Ampère), so they carry no such clash.
    "newton", "pascal", "kelvin", "tesla", "weber",
}

EXTRA = {
    # the devices of ch. 27 are introduced capitalised in an itemize; link
    # the lowercase nouns too (the English curation does the same for
    # "throttle" and "nozzle")
    "tobera": "prop:b2:open-systems:devices",
    "estrangulamiento": "prop:b2:open-systems:devices",
}

DROP = {
    # bare adjectives and harvest artefacts, dropped in book4_en.py too
    # ("quantised", "four-level", "three-level", "Eulerian", "rotation
    # about a fixed", "power of forces on")
    "cuantizadas", "euleriana",
    "tres niveles", "cuatro niveles",
    # the itemize title of ch. 27 harvested whole: a list of three devices,
    # never a noun phrase in prose ("compresor", "bomba" and "turbina"
    # would each need their own entry, and none is wanted)
    "Compresor, bomba, turbina",
}

DERIVED = {}
PRIMARY_OK = set()

EXTRA_PROTECT = [
    # the drag of the air, not the electrical quantity
    r'resistencia del aire',
]

AMBIG_POLICY = "drop"          # the university convention (books 3, 4, 5)
