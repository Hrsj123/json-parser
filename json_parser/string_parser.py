import re

FLAGS = re.VERBOSE | re.MULTILINE | re.DOTALL
STRINGCHUNK = re.compile(r'.*?(?P<terminator>["\n\\\x00-\x1f])', FLAGS)
BACKSLASH = {'"': '"', "\\": "\\", "/": "/", "b": "\b", "f": "\f", "n": "\n", "r": "\r", "t": "\t"}


def _decode_uXXXX(string: str, pos: int):  # s = "uxxxx"
    esc = string[pos + 1 : pos + 5]  # esc = "xxxx"
    if len(esc) == 4 and esc[1] not in "xX":
        try:
            return int(esc, 16)
        except ValueError:
            pass
    raise Exception("Invalid \\uXXXX escape")


def string_parser(string: str, end: int) -> int:
    start = end - 1

    while True:
        chunk = STRINGCHUNK.match(string, end)
        if chunk is None:
            raise Exception(f"Unterminated string starting at {start}")
        #
        end = chunk.end()
        terminator = chunk.group("terminator")
        #
        if terminator == '"':
            return end  # End of string!
        elif terminator == "\n":
            raise Exception(f"Unstringified new-line char appeared in the string at {end}")
        elif terminator != "\\":  # Any other control character ([\x00-\x1f])
            raise Exception(f"Invalid control character at {end}: `{terminator}`")
        # If `terminator == backslash`:
        try:
            esc = string[end]  # `string[end]` gives the char after backslash!
        except IndexError:
            raise Exception(f"Unterminated string starting at {start}")
        #
        if esc != "u":
            try:  # eg: `"apples\zmangoes!"`
                BACKSLASH[esc]
            except KeyError:
                raise Exception(f"Invalid \\escape at {end}")
            end += 1
        else:
            _decode_uXXXX(string, end)
            end += 5
