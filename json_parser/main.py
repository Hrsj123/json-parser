import re

from .other_parsers import other_parsers
from .string_parser import string_parser
from .utils import arg_parser

FLAGS = re.VERBOSE | re.MULTILINE | re.DOTALL
WHITESPACE = re.compile(r"[ \t\n\r]*", FLAGS)
WHITESPACE_STR = " \t\n\r"


def object_parser(string: str, end: int) -> int:
    next_char = string[end : end + 1]
    if next_char:
        # white-space
        if next_char in WHITESPACE_STR:
            end = WHITESPACE.match(string, end).end()
            next_char = string[end : end + 1]
        #
        if next_char == "}":
            return end + 1
        elif next_char != '"':
            raise Exception("Object's key must be a string starting with `\"`")
    end += 1  # Marks the first char of the first key in the current object!

    while True:
        # "key"
        end = string_parser(string, end)
        # white-space
        next_char = string[end : end + 1]
        if next_char in WHITESPACE_STR:
            end = WHITESPACE.match(string, end).end()
            next_char = string[end : end + 1]
        # ":"
        if next_char != ":":
            raise Exception("Key should be followed by `:` in an object")
        end += 1
        # white-space
        next_char = string[end : end + 1]
        if next_char in WHITESPACE_STR:
            end = WHITESPACE.match(string, end).end()
            next_char = string[end : end + 1]
        # "value"
        try:
            end = main(string, end)
        except Exception:
            raise Exception("Expecting a valid value in key-value pair")
        # white-space
        next_char = string[end : end + 1]
        if next_char in WHITESPACE_STR:
            end = WHITESPACE.match(string, end).end()
            next_char = string[end : end + 1]

        # After key-value pair:  [`}` or `,`]
        if next_char == "}":
            end += 1
            return end
        elif next_char != ",":
            raise Exception("Comma `,` should appear after each key-value pair")
        end += 1
        # white-space
        next_char = string[end : end + 1]
        if next_char in WHITESPACE_STR:
            end = WHITESPACE.match(string, end).end()
            next_char = string[end : end + 1]
        if next_char != '"':
            raise Exception("Object's key must be a string starting with `\"`")
        end += 1


def array_parser(string: str, end: int) -> int:
    next_char = string[end : end + 1]
    if next_char in WHITESPACE_STR:
        end = WHITESPACE.match(string, end).end()
        next_char = string[end : end + 1]
    while True:
        if next_char == "]":
            return end + 1
        elif next_char != ",":
            end = main(string, end)
            next_char = string[end : end + 1]
            if next_char in WHITESPACE_STR:
                end = WHITESPACE.match(string, end).end()
                next_char = string[end : end + 1]
            if next_char not in [",", "]"]:
                raise Exception("Each term in array should be seprarted by a `,`")
            if next_char == ",":
                end += 1
                next_char = string[end : end + 1]
                if next_char == "]":
                    raise Exception("Each `,` should be followed by an element")
        else:
            raise Exception("Unexpected `,` appeared in the array")


def main(string: str, end: int = 0) -> int:
    if string[end : end + 1] in WHITESPACE_STR:
        end = WHITESPACE.match(string, end).end()
    #
    if string[end:].startswith("{"):
        end = object_parser(string, end + 1)
    elif string[end:].startswith("["):
        end = array_parser(string, end + 1)
    elif string[end:].startswith('"'):
        end = string_parser(string, end + 1)
    else:  # Other data types!
        end = other_parsers(string, end)
    return end


def check_json(string: str):
    string = string.strip()  # TODO: Due to this operation, `pos` values will be inaccurate!
    length = len(string)
    res = main(string)
    if type(res) is int and res == length:
        # print("Valid JSON")
        return True
    else:
        raise Exception(f"Unknown characters after pos: {res}")


def _cli():
    json_string = arg_parser()
    res = check_json(json_string)
    print(res)
