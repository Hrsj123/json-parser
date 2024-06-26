import re


def other_parsers(string, end):
    p1 = r"-?(([1-9]\d*)\.?\d*|0\.\d+|0)([eE][-+]?\d+)?"
    p2 = r"(true|false)"
    p3 = r"null"
    pattern = rf"({p1}|{p2}|{p3})"
    regex = re.compile(pattern)
    if (match := regex.match(string, end)) is None:
        raise Exception(f"Parsing error at position {end}")
    else:
        return match.end()
