"""Book 4 -- nl. Curation only; the rules live in tools/termlink/.

Curated 2026-08-22 against the English curation (`book4_en.py`), which this
file follows term for term wherever the two languages agree, plus the
homographs and the compounding that Dutch makes on its own.

The file that stood here before was a verbatim copy of `book3_nl.py`, kept
only as a seed; every one of its 67 `EXTRA` entries pointed at a Book 3
label (`thm:b1:...`) that does not exist in Book 4 and would have emitted an
undefined reference. They are all gone: what follows is Book 4's own
curation, checked against Book 4's 801 labels.

The Dutch bodies (parts/bachelor-2/nl) write their accents as raw UTF-8, so
the terms below are spelled the same way. `lang_nl.py` puts the plural tail
on the last word only, so "gaussische bundel" already matches "gaussische
bundels" and no plural has to be declared here.

Dutch runs *thinner* than English by construction: it welds into one word
what English writes as two ("golfpakket", "dopplereffect", "grenslaag",
"driftsnelheid", "tunneleffect"), and `harvest.py` only takes an \\index
entry that contains a space -- a Dutch compound hides its own head. Every
`EXTRA` below restores exactly one such target: the list was built by
diffing the Dutch target set against the English one
(`--terms | awk '{print $NF}' | sort -u`, then `comm`), never by guesswork.

The Dutch-only traps, each read in context before being kept or dropped:

* *weerstand* is the electrical resistance of ch. 10, the drag of ch. 04
  and the thermal resistance of ch. 25 -- STOPped, so each chapter keeps
  its own sense and only the qualified compounds link.
* *druk*, *kracht*, *moment*, *massa*, *snelheid*, *arbeid*, *flux*,
  *impuls* are ordinary words in this register long before any chapter
  defines a qualified version of them.
* *rendement* is the cycle efficiency of ch. 27, the fin efficiency of
  ch. 25 and the isentropic efficiency of the same chapter (English STOPs
  "efficiency" for the same reason).
* *drempel* is the laser threshold of ch. 23 and the threshold of hearing
  of ch. 07.
* *stationair* is the steady flow of ch. 27, the steady state of ch. 23 and
  the stationary states of ch. 30.
* *absorptie* is the absorption of light of ch. 23, of sound of ch. 07 and
  of heat of ch. 26.
"""

STOP = {
    # English STOPs, term for term
    "laser", "drempel", "stationair", "rendement", "absorptie",
    # Dutch words that are ordinary language in this register
    "arbeid", "druk", "kracht", "massa", "moment", "snelheid",
    "temperatuur", "versnelling", "versterking", "weerstand", "flux",
    "impuls", "capaciteit", "eenheid", "dimensie", "beeld", "bar",
    "warmte", "Warmte", "vermogen", "straling", "spanning", "stroom",
    # "lager" is the bearing of ch. 01 and the comparative "lower"
    # everywhere else -- twenty wrong links before it was STOPped
    "lager",
}

NO_CAPITAL = {
    # capitalized, these are the physicists, not the units
    "newton", "joule", "watt", "pascal", "kelvin", "tesla", "hertz",
    "coulomb", "volt", "ampère", "ohm", "henry", "farad", "weber",
}

# One entry per target that the English harvest reaches and the Dutch one
# cannot, because the Dutch name is a single welded word (or a hyphenated
# one) and harvest.py skips any \index entry without a space.
EXTRA = {
    "wrijvingskegel": "rem:b2:rigid-body-mechanics:reading",
    "rolwrijving": "prop:b2:rigid-body-mechanics:power",
    "continuïteitsvergelijking": "thm:b2:fluid-kinematics:continuity",
    "venturimeter": "prop:b2:euler-bernoulli:venturi",
    "venturi-effect": "prop:b2:euler-bernoulli:venturi",
    "pitotbuis": "prop:b2:euler-bernoulli:pitot",
    "draagkracht": "prop:b2:euler-bernoulli:lift",
    "magnuseffect": "prop:b2:euler-bernoulli:lift",
    "grenslaag": "prop:b2:viscous-flows:bl",
    "weerstandscoëfficiënt": "prop:b2:viscous-flows:drag",
    "weerstandscrisis": "prop:b2:viscous-flows:drag",
    "peltonturbine": "prop:b2:flow-balances:pelton",
    "raketvergelijking": "prop:b2:flow-balances:pelton",
    "dopplereffect": "thm:b2:sound-waves:doppler",
    "groepssnelheid": "prop:b2:dispersion-wave-packets:group",
    "zwevingen": "prop:b2:dispersion-wave-packets:group",
    "wienbrugoscillator": "prop:b2:feedback-oscillators:wien",
    "wiennetwerk": "prop:b2:feedback-oscillators:wien",
    "hysteresecomparator": "prop:b2:feedback-oscillators:schmitt",
    "schmitttrigger": "prop:b2:feedback-oscillators:schmitt",
    "bemonstering": "thm:b2:feedback-oscillators:shannon",
    "antialiasingfilter": "thm:b2:feedback-oscillators:shannon",
    "kwantisatie": "rem:b2:feedback-oscillators:quantization",
    "analoog-digitaalomzetter": "rem:b2:feedback-oscillators:quantization",
    "driftsnelheid": "ex:b2:charges-currents-conduction:drift",
    "huideffect": "thm:b2:waves-in-media:skin",
    "reflectiecoëfficiënt": "thm:b2:wave-interfaces:normal",
    "transmissiecoëfficiënt": "thm:b2:wave-interfaces:normal",
    "impedantieaanpassing": "thm:b2:wave-interfaces:normal",
    "stralingsweerstand": "ex:b2:dipole-radiation:antenna",
    "halvegolfdipool": "ex:b2:dipole-radiation:antenna",
    "rayleighverstrooiing": "prop:b2:dipole-radiation:rayleigh",
    "verstrooiingsdoorsnede": "prop:b2:dipole-radiation:rayleigh",
    "thomsonverstrooiing": "prop:b2:dipole-radiation:rayleigh",
    "fresnelgetal": "rem:b2:diffraction:fresnelnumber",
    "schaalhoogte": "prop:b2:boltzmann-factor:barometric",
    "tunneleffect": "thm:b2:potential-wells-tunneling:tunnel",
    "airyschijf": "prop:b2:diffraction:airy",
    "antireflectielaag": "prop:b2:wave-interfaces:optics",
    "bolgolf": "prop:b2:sound-waves:spherical",
    "coaxkabel": "prop:b2:dispersion-wave-packets:coax",
    "coherentielengte": "prop:b2:scalar-light-model:coherence",
    "coherentietijd": "prop:b2:scalar-light-model:coherence",
    "fotonenflux": "prop:b2:scalar-light-model:intensity",
    "fouriertransformatiespectroscopie": "prop:b2:michelson:measure",
    "fraunhoferbuiging": "def:b2:diffraction:huygens",
    "geluidssnelheid": "thm:b2:sound-waves:equation",
    "golfplaatje": "prop:b2:plane-waves-polarization:plates",
    "golftrein": "prop:b2:scalar-light-model:coherence",
    "golfvergelijking": "thm:b2:waves-on-strings:equation",
    "hechtvoorwaarde": "prop:b2:viscous-flows:density",
    "hoofdmaximum": "thm:b2:gratings:nwaves",
    "impulsflux": "thm:b2:flow-balances:momentum",
    "oppervlaktestroom": "prop:b2:maxwell-equations:boundary",
    "poyntingvector": "thm:b2:poynting-vector:poynting",
    "puntwervel": "ex:b2:fluid-kinematics:planeflows",
    "rotatievector": "thm:b2:rigid-body-mechanics:field",
    "staandegolfverhouding": "prop:b2:wave-interfaces:coax",
    "stralingsdruk": "prop:b2:poynting-vector:wave",
    "telegraafvergelijkingen": "prop:b2:dispersion-wave-packets:coax",
    "traagheidsmoment": "prop:b2:rigid-body-mechanics:kinetic",
    "tralievergelijking": "prop:b2:gratings:equation",
    "transmissielijn": "prop:b2:dispersion-wave-packets:coax",
    "transversaliteit": "thm:b2:plane-waves-polarization:wave",
    "verplaatsingsstroom": "thm:b2:maxwell-equations:maxwell",
    "wegverschil": "thm:b2:two-wave-interference:formula",
    "wisselstroomweerstand": "ex:b2:waves-in-media:skinuses",
    "zwaartekrachtsgolfdetector": "rem:b2:michelson:history",
    # the four devices of ch. 27 are introduced capitalised in an itemize;
    # link the lowercase nouns, as book4_en.py does for throttle/nozzle
    "straalpijp": "prop:b2:open-systems:devices",
    "smoorventiel": "prop:b2:open-systems:devices",
    "warmtewisselaar": "prop:b2:open-systems:devices",
}

DROP = {
    # harvest artefacts: the capitalised heads of the ch. 27 itemize, whose
    # lowercase nouns are restored through EXTRA above
    "Compressor, pomp, turbine", "Straalpijp", "Smoorventiel",
    "Warmtewisselaar",
    # bare adjectives that harvest picks up from a title
    "volmaakt", "ideale", "lineair", "centraal",
}

EXTRA_PROTECT = [
    # "luchtweerstand" must not be cut into "lucht" + "weerstand"
    r"\bluchtweerstand\b",
]

AMBIG_POLICY = "drop"          # the university convention (books 3, 4, 5)
