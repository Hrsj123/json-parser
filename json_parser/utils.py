import argparse
from sys import stdin

FILEPATH = "filepath"


def arg_parser() -> dict:
    DESCRIPTION = "A command-line utility to check is an input json is valid or not"
    EPILOG = f'{"-" *(len(DESCRIPTION) // 2 - 2)} END {"-" *(len(DESCRIPTION) // 2 - 2)}'

    parser = argparse.ArgumentParser(
        prog="check-json",
        description=DESCRIPTION,
        epilog=EPILOG,
    )

    parser.add_argument(FILEPATH, help="The filepath where the file exists", nargs="?")
    args = parser.parse_args()

    file_path = vars(args)[FILEPATH]
    is_file_valid = file_path

    json_string = ""
    if is_file_valid:
        with open(file_path) as f:
            json_string = f.read()
    else:
        print("Enter the input json string: ")
        json_string = stdin.buffer.read().decode("utf-8")

    return json_string
