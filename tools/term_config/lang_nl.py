"""Dutch morphology.

Plurals are -en or -s. Dutch writes compounds solid (golflengte), and the word
boundary deliberately refuses to match inside one: linking "lengte" inside
"golflengte" would be wrong. Dutch coverage is therefore thinner than English
by construction -- declare the compounds you want linked in EXTRA instead of
loosening the boundary.
"""
WORD_TAIL = r'(?:e?[ns])?'
TAIL_ON_EVERY_WORD = False
HEAD = r'(?:[^\W\d_]+-)?'
DERIVE = False
