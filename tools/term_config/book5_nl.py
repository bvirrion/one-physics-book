"""Book 5 -- nl. Curation only; the rules live in tools/termlink/.

Curated 2026-09-03 against Book 5's own harvest, from the coordinator's
seed (which carried `STOP`/`EXTRA_PROTECT` from `book4_nl.py` and emptied
`EXTRA`/`DROP` on purpose).

What was checked, and what came of it:

* `EXTRA` was rebuilt from scratch by diffing this edition's target set
  against English's --
      python3 tools/link_defined_terms.py --book 5 --lang <l> --terms \
        | awk '{print $NF}' | sort -u
  then `comm`-ing the two sorted lists. Twenty-nine targets the English
  harvest reaches were unreachable in Dutch, and every one of them for the
  same structural reason: `harvest.py` only takes an `\\index` entry that
  contains a space, and Dutch welds into one word what English writes as
  two -- *starkeffect*, *lengtekrimp*, *toestandsdichtheid*, *bandkloof*,
  *nulpuntsenergie*, *bose-einsteincondensatie*. The entries below restore
  exactly those targets, one term per target (two or three where English
  itself offered several names for the same statement), each term taken
  from an `\\index` key this edition actually writes. Nothing was guessed:
  every label was checked to exist in Book 5.

* `DROP` stays empty: the Dutch harvest produced no artefact terms.

* `STOP` -- the tail of five (*spin*, *metaal*, *gebeurtenis*,
  *observabele*, *gat*) is `book5_en.py`'s own stoplist rendered in Dutch
  and is doing real work: each is an `\\index` key here and each collides
  with an ordinary word of the register (the quantum spin of ch. 12 against
  a spinning star in chs. 25--27; the band-theory metal of ch. 24 against
  scrap metal in ch. 22; the spacetime event of ch. 04 against counted
  events in chs. 16 and 26; the Hermitian observable of ch. 08 against the
  adjective; the semiconductor hole of ch. 24 against the black hole of
  ch. 27). The words carried from `book4_nl.py` were each re-tested against
  this book's harvest: not one of them is a Book 5 term, so none of them
  removes a link here. They are kept as a guard for the ordinary vocabulary
  they name (*druk*, *kracht*, *massa*, *straling*, *temperatuur*, ...),
  which this volume uses constantly in its plain sense.

* `EXTRA_PROTECT` -- the seed's `\\bluchtweerstand\\b` masked a Book 4
  collocation (aerodynamic drag). The string does not occur anywhere in
  Book 5's Dutch bodies, so the pattern protected nothing; it is removed
  rather than carried, exactly the failure mode the seed's docstring warns
  about (a mask written for one book silently deleting another's links).

Do not translate the `"law of"` entry of the shared `NOT_A_TERM` default:
it never fires on English, but its literal translation (*wet van*) would
swallow every named law in the book.
"""

STOP = {
    # Ordinary vocabulary of this register, carried from book4_nl.py and
    # re-tested against Book 5's harvest: none is a term here, so none of
    # them deletes a link; they guard the plain senses.
    "Warmte", "absorptie", "arbeid", "bar", "beeld", "capaciteit",
    "dimensie", "drempel", "druk", "eenheid", "flux", "impuls", "kracht",
    "lager", "laser", "massa", "moment", "rendement", "snelheid",
    "spanning", "stationair", "straling", "stroom", "temperatuur",
    "vermogen", "versnelling", "versterking", "warmte", "weerstand",
    # Book 5's own stoplist (book5_en.py) in Dutch -- these five ARE index
    # keys here, and each is stopped for a reason that survives translation.
    "spin", "metaal", "gebeurtenis", "observabele", "gat",
}

NO_CAPITAL = {
    # carried from book4_nl.py.
    "ampère", "coulomb", "farad", "henry", "hertz", "joule", "kelvin",
    "newton", "ohm", "pascal", "tesla", "volt", "watt", "weber",
}

# One entry per target the English harvest reaches and the Dutch one cannot,
# because the Dutch name is a single welded word and harvest.py skips
# space-less \index entries. Built by comm(1) on the two target sets.
EXTRA = {
    # relativity
    "lorentztransformatie": "thm:b3:relativistic-kinematics:lorentz",
    "inertiaalstelsel": "thm:b3:relativistic-kinematics:postulates",
    "tijdrek": "prop:b3:relativistic-kinematics:dilation",
    "eigentijd": "prop:b3:relativistic-kinematics:dilation",
    "lengtekrimp": "prop:b3:relativistic-kinematics:contraction",
    "eigenlengte": "prop:b3:relativistic-kinematics:contraction",
    "lichtkegel": "rem:b3:relativistic-kinematics:causality",
    "koplampeffect": "prop:b3:covariant-electromagnetism:wavevector",
    "energiefunctie": "prop:b3:lagrangian-mechanics:energy",
    # quantum mechanics
    "onzekerheidsrelatie": "thm:b3:quantum-formalism:uncertainty",
    "waarschijnlijkheidsstroom": "prop:b3:schrodinger-three-dimensions:current",
    "toestandsdichtheid": "prop:b3:schrodinger-three-dimensions:counting",
    "nulpuntsenergie": "thm:b3:harmonic-oscillator:spectrum",
    "bolfuncties": "prop:b3:quantum-angular-momentum:harmonics",
    "baankwantumgetal": "prop:b3:quantum-angular-momentum:harmonics",
    "bohrmagneton": "prop:b3:quantum-angular-momentum:magnetic",
    "zeemaneffect": "prop:b3:quantum-angular-momentum:magnetic",
    "blochbol": "prop:b3:spin-two-level:bloch",
    "waterstofatoom": "thm:b3:hydrogen-atom:levels",
    "bohrstraal": "thm:b3:hydrogen-atom:levels",
    "hoofdkwantumgetal": "thm:b3:hydrogen-atom:levels",
    "balmerreeks": "prop:b3:hydrogen-atom:series",
    "lymanreeks": "prop:b3:hydrogen-atom:series",
    "storingsrekening": "thm:b3:perturbation-theory:corrections",
    "starkeffect": "ex:b3:perturbation-theory:stark",
    "verstrooiingsamplitude": "thm:b3:scattering-theory:amplitude",
    "bornbenadering": "thm:b3:scattering-theory:born",
    "impulsoverdracht": "thm:b3:scattering-theory:born",
    # statistical physics
    "fermi-energie": "thm:b3:quantum-statistics:fermi",
    "ontaardingsdruk": "thm:b3:quantum-statistics:fermi",
    "bose-einsteincondensatie": "thm:b3:quantum-statistics:bec",
    "curietemperatuur": "thm:b3:phase-transitions:meanfield",
    "isingmodel": "thm:b3:phase-transitions:meanfield",
    "gemiddeldeveldtheorie": "thm:b3:phase-transitions:meanfield",
    # matter
    "langevinfunctie": "prop:b3:electromagnetism-in-matter:langevin",
    "oriëntatiepolarisatie": "prop:b3:electromagnetism-in-matter:langevin",
    "madelungconstante": "prop:b3:crystalline-solids:madelung",
    "cohesie-energie": "prop:b3:crystalline-solids:madelung",
    "bandkloof": "thm:b3:electrons-in-solids:bloch",
    "bandenstructuur": "thm:b3:electrons-in-solids:bloch",
    "depletiezone": "prop:b3:electrons-in-solids:junction",
    # subatomic and the universe
    "bindingsenergie": "prop:b3:nuclear-physics:binding",
    "ijzerpiek": "prop:b3:nuclear-physics:binding",
    "baryongetal": "prop:b3:particle-physics:conservation",
    "leptongetal": "prop:b3:particle-physics:conservation",
    # --- welded Dutch compounds whose English name is two words, so the
    # English harvest links them and `harvest.py` drops the Dutch. Same
    # comm(1) discipline as above, applied term by term rather than target
    # by target; nothing here links a notion English leaves unlinked.
    "P-golf": "prop:b3:continuum-elasticity:waves",
    "S-golf": "prop:b3:continuum-elasticity:waves",
    "eigentrillingen": "prop:b3:lagrangian-mechanics:modes",
    "elasticiteitsmodulus": "thm:b3:continuum-elasticity:hooke",
    "snelheidssamenstelling": "prop:b3:relativistic-kinematics:addition",
    "energie--impulsbetrekking": "thm:b3:relativistic-dynamics:relation",
    "massadefect": "thm:b3:relativistic-dynamics:emc2",
    "drempelenergie": "prop:b3:relativistic-dynamics:threshold",
    "veldinvarianten": "prop:b3:covariant-electromagnetism:invariants",
    "larmorprecessie": "prop:b3:spin-two-level:larmor",
    "rabi-oscillatie": "prop:b3:spin-two-level:rabi",
    "hyperfijnstructuur": "ex:b3:spin-two-level:hyperfine",
    "verwisselingswisselwerking": "prop:b3:identical-particles:exchange-force",
    "faseverschuiving": "thm:b3:scattering-theory:partial",
    "verstrooiingslengte": "thm:b3:scattering-theory:partial",
    "rutherfordverstrooiing": "ex:b3:scattering-theory:rutherford",
    "grondpostulaat": "thm:b3:microcanonical-ensemble:postulate",
    "boltzmannverdeling": "thm:b3:canonical-ensemble:boltzmann",
    "toestandssom": "thm:b3:canonical-ensemble:boltzmann",
    "zwartestraling": "thm:b3:photons-phonons:planck",
    "landautheorie": "prop:b3:phase-transitions:landau",
    "metaalbinding": "rem:b3:crystalline-solids:bonds",
    "vanderwaalsbinding": "rem:b3:crystalline-solids:bonds",
    "röntgendiffractie": "prop:b3:crystalline-solids:bragg",
    "millerindices": "prop:b3:crystalline-solids:bragg",
    "driftsnelheid": "prop:b3:electrons-in-solids:drude",
    "p--n-junctie": "prop:b3:electrons-in-solids:junction",
    "kettingreactie": "prop:b3:nuclear-physics:fission",
    "stabiliteitsvallei": "prop:b3:nuclear-physics:semf",
    "alfaverval": "rem:b3:nuclear-physics:modes",
    "bètaverval": "rem:b3:nuclear-physics:modes",
    "gammaverval": "rem:b3:nuclear-physics:modes",
    "deeltjesdetector": "rem:b3:particle-physics:machines",
    "higgsdeeltje": "rem:b3:particle-physics:higgs",
    "sterstructuur": "prop:b3:astrophysics:hydrostatic",
    "neutronenster": "prop:b3:astrophysics:compact",
    "chandrasekharmassa": "prop:b3:astrophysics:compact",
    "schwarzschildstraal": "prop:b3:astrophysics:compact",
}

DROP = set()

# The seed's \bluchtweerstand\b masked a Book 4 collocation that does not
# occur in Book 5; a mask that protects nothing is a mask that can only
# cost links later, so it is gone.
#
# What replaces it is a Dutch morphology accident, found by counting the
# generated surface forms: `lang_nl.py` inflects the term *ket* (Dirac's
# ket, def:b3:quantum-formalism:state) to "keten", which is the ordinary
# Dutch word for *chain*. Unmasked it produced 38 links -- decay chains,
# the photon--baryon chain, polymer chains, the Ising chain -- every one
# of them pointing at the wrong definition, and no census sees it. English
# never links "ket" at all.
EXTRA_PROTECT = [
    r"\bketens?\b",
]

AMBIG_POLICY = "drop"          # the university convention (books 3, 4, 5)
