# from ast import pattern
from nis import match
from pregex.classes import AnyLetter, AnyDigit, AnyFrom, AnyWhitespace
from pregex.quantifiers import Optional, AtLeastAtMost, AtMost
from pregex.operators import Either
from pregex.groups import Capture
from pregex.pre import Pregex
import re


def get_doc_pattern(key):
    pre: Pregex = (
        "<%"
        + Optional(AtMost(AnyWhitespace(), 2))
        + key
        + Optional(AtMost(AnyWhitespace(), 2))
        + "%>"
    )
    regex = pre.get_pattern()
    return pre, regex


def replace_with_pattern(pattern, value, text):

    return re.sub(pattern, value, text)


if __name__ == "__main__":  # pragma: no cover
    key = "project:name"
    value = "Mksci"
    pre, pat = get_doc_pattern(key)
    text = "<%  project:name %>"
    print(replace_with_pattern(pat, value, text))

    matches = pre.get_matches(text)
    print(matches)
