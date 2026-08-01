"""Expand the book's siunitx vocabulary into KaTeX-renderable LaTeX.

KaTeX has no siunitx support, so \\qty, \\num, \\unit, \\qtyrange,
\\qtylist and \\ang are rewritten here, mirroring what siunitx prints with
the book's setup (styles/onephysics.sty: per-mode=symbol,
output-decimal-marker={.}, range-units=single, everything else default:
thin-space products, digit groups of 3 from 5 digits, English range/list
phrases, repeated list units).

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
}

SI_COMMANDS = {"qty": 2, "num": 1, "unit": 1, "ang": 1,
               "qtyrange": 3, "qtylist": 2}


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
    v = value.strip()
    if "\\pm" in v:
        lo, hi = v.split("\\pm", 1)
        return format_number(lo) + " \\pm " + format_number(hi)
    m = re.fullmatch(r"([+-]?)(\d*(?:\.\d+)?)(?:[eE]([+-]?\d+))?", v)
    if not m or (not m.group(2) and m.group(3) is None):
        raise ParseError(f"unsupported siunitx number {value!r}")
    sign, mantissa, exponent = m.groups()
    out = "-" if sign == "-" else ""
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
    while i < len(s):
        c = s[i]
        if c == "\\":
            m = re.match(r"\\([a-zA-Z]+)", s[i:])
            name = m.group(1)
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
            m = re.match(r"\^(\{[^{}]*\}|[+-]?\d)", s[i:])
            if not m:
                raise ParseError(f"unsupported exponent in unit {body!r}")
            exp = m.group(1).strip("{}")
            out.append(f"^{{{exp}}}")
            i += m.end()
        elif c in ".~":
            out.append("\\,")
            i += 1
        elif c == "/":
            out.append("/")
            i += 1
        elif c in " \t":
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
    return "" if unit_body.lstrip().startswith("\\degree") else "\\,"


def expand_command(name, args):
    """One siunitx call -> LaTeX."""
    if name == "num":
        return format_number(args[0])
    if name == "unit":
        return format_unit(args[0])
    if name == "ang":
        return format_number(args[0]) + "{}^{\\circ}"
    if name == "qty":
        value, unit = args
        number = format_number(value)
        if "\\pm" in value:
            # siunitx brackets an uncertainty before its unit
            number = f"({number})"
        return number + _sep(unit) + format_unit(unit)
    if name == "qtyrange":
        lo, hi, unit = args
        # range-units=single: one unit after the upper bound
        return (format_number(lo) + "\\text{ to }" + format_number(hi)
                + _sep(unit) + format_unit(unit))
    if name == "qtylist":
        values, unit = args
        # siunitx default list-units=repeat: unit after every value
        rendered = [format_number(v) + _sep(unit) + format_unit(unit)
                    for v in values.split(";")]
        if len(rendered) == 1:
            return rendered[0]
        return ("\\text{, }".join(rendered[:-1])
                + "\\text{ and }" + rendered[-1])
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


def expand(tex):
    """Rewrite every siunitx call inside a math string."""
    out = []
    i = 0
    while i < len(tex):
        m = re.compile(r"\\(qtyrange|qtylist|qty|num|unit|ang)(?![a-zA-Z])"
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
        expanded = expand_command(m.group(1), args)
        if _in_text(tex, m.start()):
            expanded = f"${expanded}$"
        out.append(expanded)
        i = j
    return "".join(out)
