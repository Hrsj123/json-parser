**JSON Validator**

This Python project validates the syntax of JSON strings or files. It performs lexical analysis to break down the JSON into tokens and syntactic analysis to ensure it adheres to correct JSON grammar. This project is built by referencing Python's built-in `json` module.

**Features:**

- Validates basic JSON syntax (objects, arrays, key-value pairs)
- Provides informative error messages for common syntax errors

**Usage:**

```
from json_parser import check_json

string = '{"key": "value"}'
check_json(string)          # Returns True or throws `Exception` error
```
