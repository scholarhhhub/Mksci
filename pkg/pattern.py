# from ast import pattern
from nis import match
import pregex
from pregex.core.classes import AnyLetter, AnyDigit, AnyFrom, AnyWhitespace
from pregex.core.quantifiers import Optional, AtLeastAtMost, AtMost
from pregex.core.operators import Either
from pregex.core.groups import Capture
from pregex.core.pre import Pregex
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
