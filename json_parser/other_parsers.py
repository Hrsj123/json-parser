import re


def other_parsers(string: str, end: int) -> int:
    number_pattern = r"-?(([1-9]\d*)\.?\d*|0\.\d+|0)([eE][-+]?\d+)?"
    boolean_pattern = r"(true|false)"
    null_pattern = r"null"
    pattern = rf"({number_pattern}|{boolean_pattern}|{null_pattern})"
    regex = re.compile(pattern)
    if (match := regex.match(string, end)) is None:
        raise Exception(f"Parsing error at position {end}")
    else:
        return match.end()
