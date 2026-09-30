"""Expand the book's siunitx vocabulary into KaTeX-renderable LaTeX.

KaTeX has no siunitx support, so \\qty, \\num, \\unit, \\qtyrange,
\\qtylist and \\ang are rewritten here, mirroring what siunitx prints with
the book's setup (styles/onephysics.sty: per-mode=symbol,
output-decimal-marker={.}, range-units=single, everything else default:
thin-space products, digit groups of 3 from 5 digits, repeated list units;
range/list phrases are the edition's own, English by default) — plus
\\numrange.

Units are written in siunitx literal shorthand throughout the book
(``m/s``, ``kW.h``, ``\\micro s``, ``s^{-1}``); the handful of macro unit
atoms in use are mapped explicitly — an unknown one raises, keeping the
fail-loudly contract.
"""

import re

from .lexer import ParseError

# Unit macro atoms actually used in the book. \degree carries an empty
# number-unit separator in siunitx (45° not 45 °); model that with NOSEP.
NOSEP = ("{}^{\\circ}",)
UNIT_MACROS = {
    "micro": "\\text{µ}",
    "ohm": "\\Omega",
    "degree": "{}^{\\circ}",
    "celsius": "{}^{\\circ}\\mathrm{C}",
    "degreeCelsius": "{}^{\\circ}\\mathrm{C}",
    "minute": "\\mathrm{min}",
    "gram": "\\mathrm{g}",
    "percent": "\\%",
    "delta": "\\delta",      # dioptre (physics book 3, optics)
    "angstrom": "\\text{\u00c5}",
    "Omega": "\\Omega",
}

# Macro-form units (\milli\second, \giga\bit\per\second — the quant books):
# siunitx joins a prefix to its unit, separates units with a thin space and
# prints \per as "/" (per-mode=symbol). Market units are the
# \DeclareSIUnit's of styles/onequant.sty.
SI_PREFIXES = {
    "pico": "p", "nano": "n", "milli": "m", "kilo": "k", "mega": "M",
    "giga": "G", "tera": "T",
}
SI_UNITS = {
    "second": "s", "metre": "m", "watt": "W", "hour": "h", "hertz": "Hz",
    "bit": "bit", "byte": "B", "decibel": "dB",
    "bp": "bp", "tick": "tick", "share": "sh", "contract": "ct",
    "barrel": "bbl", "mmbtu": "MMBtu", "therm": "th", "bushel": "bu",
    "troyounce": "oz\\,t", "flop": "flop", "msg": "msg",
}

SI_COMMANDS = {"qty": 2, "num": 1, "unit": 1, "ang": 1,
               "qtyrange": 3, "qtylist": 2, "numrange": 2}

# range/list words; the emitter passes the edition's own (LangStrings
# reads them from the \sisetup line of styles/lang/<lang>.tex)
DEFAULT_PHRASES = {"range": " to ", "pair": " and ", "final": " and "}


def _group_digits(digits, from_right):
    if len(digits) < 5:
        return digits
    if from_right:
        parts = [digits[max(0, i - 3):i]
                 for i in range(len(digits), 0, -3)][::-1]
    else:
        parts = [digits[i:i + 3] for i in range(0, len(digits), 3)]
    return "\\,".join(parts)


def format_number(value):
    """siunitx number: decimal point, digit grouping, e-notation,
    \\pm uncertainties."""
    # an explicit \, digit group (1\,528) is input-ignored by siunitx: the
    # number is regrouped by the usual rule (1528, 97 690)
    v = value.strip().replace("\\,", "")
    mu = re.fullmatch(r"([+-]?\d*(?:\.\d+)?)\((\d+)\)", v)
    if mu:
        # compact uncertainty 2.72548(57): printed as written
        return format_number(mu.group(1)) + f"({mu.group(2)})"
    if "\\pm" in v:
        lo, hi = v.split("\\pm", 1)
        if not lo.strip():
            # \qty{\pm 6}{dB}: a signed number, not an uncertainty
            return "\\pm " + format_number(hi)
        return format_number(lo) + " \\pm " + format_number(hi)
    m = re.fullmatch(r"([+-]?)(\d*(?:\.\d+)?)(?:[eE]([+-]?\d+))?", v)
    if not m or (not m.group(2) and m.group(3) is None):
        raise ParseError(f"unsupported siunitx number {value!r}")
    sign, mantissa, exponent = m.groups()
    # siunitx keeps an explicit sign as written (+2.0 stays +2.0)
    out = sign
    if mantissa:
        if "." in mantissa:
            whole, frac = mantissa.split(".")
            out += (_group_digits(whole, True) + "."
                    + _group_digits(frac, False))
        else:
            out += _group_digits(mantissa, True)
    if exponent is not None:
        exp = str(int(exponent))
        power = f"10^{{{exp}}}"
        out += f" \\times {power}" if mantissa else power
    return out


def format_unit(body):
    """siunitx literal unit shorthand -> LaTeX (upright, thin-space
    products, symbol \\per)."""
    out = []
    i, s = 0, body.strip()
    prev_unit = False    # last token was a macro-form unit (\second, \bit)
    while i < len(s):
        c = s[i]
        if c == "\\":
            if s.startswith("\\%", i):
                out.append("\\%")
                i += 2
                continue
            if s.startswith("\\$", i):
                # currency in a unit: \qty{80}{\$/\barrel} -> 80 $/bbl
                out.append("\\$")
                i += 2
                continue
            m = re.match(r"\\([a-zA-Z]+)", s[i:])
            if m and m.group(1) in SI_PREFIXES:
                if prev_unit:
                    out.append("\\,")
                out.append(f"\\mathrm{{{SI_PREFIXES[m.group(1)]}}}")
                prev_unit = False
                i += m.end()
                continue
            if m and m.group(1) in SI_UNITS:
                if prev_unit:
                    out.append("\\,")
                out.append(f"\\mathrm{{{SI_UNITS[m.group(1)]}}}")
                prev_unit = True
                i += m.end()
                continue
            if m and m.group(1) == "per":
                out.append("/")
                prev_unit = False
                i += m.end()
                continue
            prev_unit = False
            if s.startswith("\\,", i):
                # explicit thin-space product (mol\,m^{-2}\,s^{-1})
                out.append("\\,")
                i += 2
                continue
            m = re.match(r"\\([a-zA-Z]+)", s[i:])
            if not m:
                raise ParseError(f"unsupported character {c!r} "
                                 f"in siunitx unit {body!r}")
            name = m.group(1)
            if name in ("sqrt", "omterm"):
                # \sqrt{Hz}; \omterm{label}{unit} = a defined-term link
                # around a unit (renders as the unit itself)
                j = i + m.end()
                groups = []
                for _ in range(2 if name == "omterm" else 1):
                    while j < len(s) and s[j] in " \t\n":
                        j += 1
                    if j >= len(s) or s[j] != "{":
                        raise ParseError(f"\\{name} missing brace group "
                                         f"in siunitx unit {body!r}")
                    depth, k = 1, j + 1
                    while k < len(s) and depth:
                        if s[k] == "{":
                            depth += 1
                        elif s[k] == "}":
                            depth -= 1
                        k += 1
                    if depth:
                        raise ParseError(f"unbalanced braces in siunitx "
                                         f"unit {body!r}")
                    groups.append(s[j + 1:k - 1])
                    j = k
                inner = format_unit(groups[-1])
                out.append(f"\\sqrt{{{inner}}}" if name == "sqrt"
                           else inner)
                i = j
                continue
            if name not in UNIT_MACROS:
                raise ParseError(f"unknown unit macro \\{name} "
                                 f"in siunitx unit {body!r}")
            out.append(UNIT_MACROS[name])
            i += m.end()
        elif c.isalpha():
            j = i
            while j < len(s) and s[j].isalpha():
                j += 1
            out.append(f"\\mathrm{{{s[i:j]}}}")
            i = j
        elif c == "^":
            # exponents, and ionic charges (H^+, Ca^{2+})
            m = re.match(r"\^(\{[^{}]*\}|[+-]?\d|[+-])", s[i:])
            if not m:
                raise ParseError(f"unsupported exponent in unit {body!r}")
            exp = m.group(1).strip("{}")
            out.append(f"^{{{exp}}}")
            i += m.end()
        elif c == "_":
            # chemical formula subscripts (O_2, CO_2)
            m = re.match(r"_(\{[^{}]*\}|\d+|[a-zA-Z])", s[i:])
            if not m:
                raise ParseError(f"unsupported subscript in unit {body!r}")
            out.append(f"_{{{m.group(1).strip('{}')}}}")
            i += m.end()
        elif c in ".~":
            out.append("\\,")
            i += 1
        elif c in "/()'":
            # literal shorthand: J/(kg.K), nV/\sqrt{Hz}; arcmin ' / arcsec ''
            out.append(c)
            i += 1
        elif c in " \t\n":
            i += 1
        elif c.isdigit():
            # e.g. the "2" of a literal "m2" never appears; digits only
            # occur in exponents, handled above
            raise ParseError(f"unsupported character {c!r} "
                             f"in siunitx unit {body!r}")
        else:
            raise ParseError(f"unsupported character {c!r} "
                             f"in siunitx unit {body!r}")
    return "".join(out)


def _sep(unit_body):
    u = unit_body.lstrip()
    # \degree and the arcmin/arcsec marks carry no number-unit separator
    return "" if (u.startswith("\\degree") or u.startswith("'")) else "\\,"


def expand_command(name, args, phrases=None):
    """One siunitx call -> LaTeX."""
    phrases = phrases or DEFAULT_PHRASES
    if name == "numrange":
        lo, hi = args
        return (format_number(lo) + f"\\text{{{phrases['range']}}}"
                + format_number(hi))
    if name == "num":
        return format_number(args[0])
    if name == "unit":
        return format_unit(args[0])
    if name == "ang":
        return format_number(args[0]) + "{}^{\\circ}"
    if name == "qty":
        value, unit = args
        number = format_number(value)
        if "\\pm" in value and value.split("\\pm", 1)[0].strip():
            # siunitx brackets an uncertainty before its unit
            number = f"({number})"
        return number + _sep(unit) + format_unit(unit)
    if name == "qtyrange":
        lo, hi, unit = args
        # range-units=single: one unit after the upper bound
        return (format_number(lo) + f"\\text{{{phrases['range']}}}"
                + format_number(hi)
                + _sep(unit) + format_unit(unit))
    if name == "qtylist":
        values, unit = args
        # siunitx default list-units=repeat: unit after every value
        rendered = [format_number(v) + _sep(unit) + format_unit(unit)
                    for v in values.split(";")]
        if len(rendered) == 1:
            return rendered[0]
        last = phrases["pair" if len(rendered) == 2 else "final"]
        return ("\\text{, }".join(rendered[:-1])
                + f"\\text{{{last}}}" + rendered[-1])
    raise ParseError(f"unknown siunitx command \\{name}")


def _in_text(tex, pos):
    """Whether pos sits inside a \\text{...}-like group (where the
    expansion must be re-wrapped in $...$ — KaTeX supports embedded
    math inside \\text)."""
    stack = []
    i = 0
    while i < pos:
        c = tex[i]
        if c == "\\":
            m = re.match(r"\\(text|textrm|textbf|textit|mbox)\s*\{", tex[i:])
            if m:
                stack.append(True)
                i += m.end()
                continue
            i += 2
            continue
        if c == "{":
            stack.append(False)
        elif c == "}" and stack:
            stack.pop()
        i += 1
    return any(stack)


def expand(tex, phrases=None):
    """Rewrite every siunitx call inside a math string."""
    out = []
    i = 0
    while i < len(tex):
        m = re.compile(r"\\(qtyrange|qtylist|qty|numrange|num|unit|ang)(?![a-zA-Z])"
                       ).search(tex, i)
        if not m:
            out.append(tex[i:])
            break
        out.append(tex[i:m.start()])
        args, j = [], m.end()
        for _ in range(SI_COMMANDS[m.group(1)]):
            while j < len(tex) and tex[j] in " \t\n":
                j += 1
            if j >= len(tex) or tex[j] != "{":
                raise ParseError(
                    f"\\{m.group(1)} missing brace group in {tex!r}")
            depth, k = 1, j + 1
            while k < len(tex) and depth:
                if tex[k] == "{":
                    depth += 1
                elif tex[k] == "}":
                    depth -= 1
                k += 1
            if depth:
                raise ParseError(f"unbalanced braces in {tex!r}")
            args.append(tex[j + 1:k - 1])
            j = k
        expanded = expand_command(m.group(1), args, phrases)
        if _in_text(tex, m.start()):
            expanded = f"${expanded}$"
        out.append(expanded)
        i = j
    return "".join(out)
