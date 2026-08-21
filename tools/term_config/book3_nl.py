"""Book 3 -- nl. Curation only; the rules live in tools/termlink/.

Curated 2026-08-21 against the English curation (`book3_en.py`), which this
file follows term for term wherever the two languages agree, plus the
homographs Dutch makes on its own.

The Dutch bodies (parts/bachelor-1/nl) write their accents as raw UTF-8, so
the terms below are spelled the same way. `lang_nl.py` puts the plural tail
on the last word only, so "centrale kracht" already matches "centrale
krachten" and no plural has to be declared here.

Dutch runs *thinner* than English by construction: it writes solid what
English writes as two words ("knooppuntregel", "impulsmomentstelling",
"rechterhandregel", "tweelichamenprobleem"), and harvest.py only takes an
\\index entry that contains a space -- a Dutch compound hides its own head.
Nothing is restored by hand for those, because the English twins are named
results that English drops through NOT_A_TERM anyway.

The Dutch-only traps, each read in context before being kept or dropped:

* *weerstand* is the resistor and the resistance of chapters 6--10 and the
  drag of a fluid in chapters 12 and 18 ("lineaire weerstand", "kwadratische
  weerstand", "weerstand tegen snelheidsveranderingen"). Stopped;
  "inwendige weerstand" survives as a term of its own.
* *capaciteit* is the capacitance of chapter 27 and the ordinary capacity of
  a compressor (ch. 24) or of a fibre link (ch. 2). Stopped.
* *massa* is the mass of mechanics and the electrical ground of chapter 6
  ("virtuele massa", "massa (nulpotentiaal)"), on top of being one of the
  bare nouns English stops anyway.
* *versterking* is the op-amp gain, the gain of a filter and the ordinary
  amplification; "openlusversterking" is a compound and survives.
* *spanning* looked like the French *tension* trap -- rope tension and
  voltage in one word -- but Dutch calls the rope's pull "spankracht", a
  compound, so bare "spanning" is the electrical quantity everywhere in this
  book and stays linked.
* *koppel* is the torque of chapter 15 and nothing else here (chs. 15, 27,
  28, 29 read in full), so unlike French's *couple* it stays linked.
"""

# Dutch translation of the default NOT_A_TERM keywords.
#
# The English default carries "law of" -- "Gauss's law", "Lenz's law" never
# match it, so English links two dozen named laws. Dutch writes "wet van
# Gauss", "wet van Lenz", so a literal "wet van" would silently delete every
# one of them; it is deliberately absent, and so is bare "wet" (which would
# also swallow "wetten van Kirchhoff" and, as a substring, "wetenschap").
# "stelling" stays, exactly as English's "theorem" does: neither edition
# links "stelling van Millman" / "Millman's theorem".
NOT_A_TERM = ("stelling", "lemma", "ongelijkheid", "formule", "criterium",
              "principe", "identiteit", "regel", "paradox", "probleem")

# Ordinary language in this register, or a word whose sense elsewhere in the
# book is not the sense its definition gives it. (A STOPped word is still
# linked inside the chapter that defines it.)
STOP = {
    # the bare nouns of mechanics and thermodynamics: from chapter 12 on they
    # are on every page and a link on each is noise. Every compound
    # ("centrale kracht", "hoeksnelheid", "kinetische druk", "verloren
    # arbeid", "latente warmte", ...) survives as a term of its own.
    "kracht", "massa", "snelheid", "versnelling", "impuls",
    "druk", "temperatuur", "warmte", "Warmte", "arbeid",
    # the unit (kinetic theory) vs the sliding bar of the Laplace rails
    "bar",
    # moment of a force (ch. 15) vs "op dat moment", "voor het moment"
    "moment",
    # the optical image (ch. 3) vs the mirror image of the symmetry chapters
    "beeld",
    # op-amp and filter gain (chs. 9--10) vs ordinary amplification
    "versterking",
    # flux of the electric field (ch. 26) vs the magnetic flux (ch. 29)
    "flux",
    # the SI unit (ch. 1) vs "per eenheid van lengte", "eenheid van tijd"
    "eenheid",
    # physical dimension (ch. 1) vs "de dimensies van de zaal", "in één
    # dimensie"
    "dimensie",
    # thermodynamic transformation (ch. 22) vs ordinary usage elsewhere
    "toestandsverandering",
    # the objective of an instrument (ch. 4) vs the adjective
    "objectief",
    # THE Dutch homograph: the resistor and the drag of a fluid are one word
    "weerstand",
    # capacitance (ch. 27) vs the capacity of a compressor or of a link
    "capaciteit",
}

NO_CAPITAL = {
    # capitalized, these are the physicists, not the units
    "newton", "joule", "watt", "pascal", "kelvin", "tesla", "hertz",
    "coulomb", "volt", "ampère", "ohm", "henry", "farad", "weber",
}

EXTRA = {
    # NOT_A_TERM's "stelling" is right for "stelling van Millman" and its
    # dozen siblings, which English does not link either -- but the notion
    # English calls *Ampère's law* and links heavily is a *stelling* in
    # Dutch. Restored by hand so the two editions carry the same link.
    "stelling van Ampère": "thm:b1:magnetostatics:ampere",

    # --- Dutch solid compounds -------------------------------------------
    # English writes these as two words, so its \index entry contains a
    # space and harvest.py takes it; Dutch welds them and the entry is
    # skipped. One entry per English link target, so that no notion English
    # links is left bare in Dutch.
    "schijnkracht": "thm:b1:non-inertial-frames:dynamics",
    "centrifugaalkracht": "thm:b1:non-inertial-frames:dynamics",
    "corioliskracht": "thm:b1:non-inertial-frames:dynamics",
    "meesleepkracht": "thm:b1:non-inertial-frames:dynamics",
    "coriolisversnelling": "thm:b1:non-inertial-frames:composition",
    "meesleepversnelling": "thm:b1:non-inertial-frames:composition",
    "uittredepupil": "prop:b1:optical-instruments:telescope",
    "laplacekracht": "thm:b1:magnetostatics:laplace",
    "traagheidsmoment": "prop:b1:angular-momentum:inertia",
    "spanningsdeler": "prop:b1:dc-circuits:dividers",
    "stroomdeler": "prop:b1:dc-circuits:dividers",
    "uittree-arbeid": "prop:b1:quantum-introduction:photoelectric",
    "remspanning": "prop:b1:quantum-introduction:photoelectric",
    "eindsnelheid": "prop:b1:newton-dynamics:terminal",
    "ottokringproces": "prop:b1:heat-engines:otto",
    "compressieverhouding": "prop:b1:heat-engines:otto",
    "stirlingkringproces": "prop:b1:heat-engines:stirling",
    "dieselkringproces": "prop:b1:heat-engines:diesel",
    "belastingslijn": "met:b1:dc-circuits:loadline",
    "werkpunt": "met:b1:dc-circuits:loadline",
    "grondtoestand": "prop:b1:quantum-introduction:box",
    "schmitttrigger": "prop:b1:operational-amplifier:schmitt",
    "verschilversterker": "prop:b1:operational-amplifier:sumdiff",
    "sommeerversterker": "prop:b1:operational-amplifier:sumdiff",
    "normaalkracht": "prop:b1:newton-dynamics:friction",
    "cyclotronfrequentie": "thm:b1:charged-particles:bfield",
    "drukmiddelpunt": "prop:b1:fluid-statics:wall",
    "massaspectrometer": "prop:b1:charged-particles:spectrometer",
    "snelheidsfilter": "prop:b1:charged-particles:spectrometer",
    "wegverschil": "prop:b1:wave-propagation:pathdiff",
    "RLC-kring": "prop:b1:transient-regimes:rlc",
    "RC-kring": "prop:b1:transient-regimes:rcrl",
    "RL-kring": "prop:b1:transient-regimes:rcrl",
    "waterstofatoom": "prop:b1:quantum-introduction:hydrogen",
    "zwaartekrachtveld": "prop:b1:newton-dynamics:weight",
    "schaalhoogte": "prop:b1:fluid-statics:atmosphere",
    "symmetrievlak": "prop:b1:electrostatics-gauss:symmetry",
    "antisymmetrievlak": "prop:b1:electrostatics-gauss:symmetry",
    "Hohmann-transfer": "prop:b1:central-forces:hohmann",
    "kwantumdot": "ex:b1:quantum-introduction:dot",
    "punteffect": "ex:b1:potential-capacitors:point",
    "perkenwet": "cor:b1:angular-momentum:central",
    "debroglie-golflengte": "thm:b1:quantum-introduction:debroglie",
    "neumann-inductie": "rem:b1:induction:twofaces",
    "lorentz-inductie": "rem:b1:induction:twofaces",
    "versnelspanning": "prop:b1:charged-particles:efield",
    "tunneleffect": "rem:b1:quantum-introduction:rest",
    "equipotentiaalvlak": "prop:b1:potential-capacitors:reading",
    "hoogdoorlaatfilter": "prop:b1:filters-transfer-functions:highpass1",
    "bohrstraal": "ex:b1:quantum-introduction:hsize",
    "relaxatieoscillator": "ex:b1:operational-amplifier:astable",
    "wervelstroom": "ex:b1:induction:eddy",

    # --- inflected attributive adjectives ---------------------------------
    # Dutch adds -e to an attributive adjective after a definite article
    # ("het lineaire netwerk"), and lang_nl.py puts its tail on the last
    # word only, so the inflected form has to be declared beside the base.
    "aardse stelsel": "def:b1:non-inertial-frames:earth",
    "geocentrische stelsel": "def:b1:non-inertial-frames:earth",
    "roterende stelsel": "def:b1:non-inertial-frames:frames",
    "eenatomige gas": "prop:b1:kinetic-theory:Ugas",
    "elektrische vermogen": "thm:b1:dc-circuits:kirchhoff",
    "gemiddelde vermogen": "thm:b1:sinusoidal-impedance:power",
    "gereduceerde oog": "def:b1:optical-instruments:eye",
    "kritische punt": "prop:b1:phase-changes:PTdiagram",
    "kritische regime": "thm:b1:transient-regimes:regimes",
    "pseudoperiodieke regime": "thm:b1:transient-regimes:regimes",
    "lineaire netwerk": "def:b1:dc-circuits:linear",
    "lineaire regime": "def:b1:operational-amplifier:ideal",
    "quasistationaire regime": "def:b1:dc-circuits:arqs",
    "sinusvormige signaal": "def:b1:wave-propagation:signal",
}

DROP = {
    # bare adjectives harvested from definitions that merely use them; the
    # phrases they came from ("ideaal gas", "ideale operationele
    # versterker", "lineair netwerk", "lineair regime", "centrale kracht",
    # "conservatieve kracht") all survive as terms of their own.
    "ideale", "lineair", "conservatief",
    # "centraal" and "centraal conservatief" are the bare adjective harvested
    # from "centrale conservatieve kracht"; on its own Dutch reads "centraal"
    # as "central" in the ordinary sense (centrale verwarming, het centrale
    # idee), which the thermodynamics chapters use.
    "centraal", "centraal conservatief",
}

DERIVED = {}
PRIMARY_OK = set()

EXTRA_PROTECT = [
    # the drag of the air, not the electrical component (bare "weerstand" is
    # stopped anyway, but the compound must never be broken into)
    r'\bluchtweerstand\b',
]

AMBIG_POLICY = "drop"          # the university convention (books 3, 4, 5)
