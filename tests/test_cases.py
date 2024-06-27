from pathlib import Path
from typing import List

import pytest

from json_parser import check_json


@pytest.fixture
def path():
    return "./tests/cases/{}/{}.json"


class TestStep1:
    def test_invalid_json(self, path: str):
        with open(path.format("step1", "invalid")) as f:
            string = f.read()
        with pytest.raises(Exception, match="Parsing error at position \\d+"):
            check_json(string)

    def test_valid_json(self, path: str):
        with open(path.format("step1", "valid")) as f:
            string = f.read()
        assert check_json(string) is True


class TestStep2:
    _invalid_file_list: List[str] = ["invalid", "invalid2"]
    _valid_file_list: List[str] = ["valid", "valid2"]

    @pytest.mark.parametrize("file_name", _invalid_file_list)
    def test_invalid_json(self, path: str, file_name):
        with open(path.format("step2", file_name)) as f:
            string = f.read()
        with pytest.raises(Exception, match="Object's key must be a string starting with `\"`"):
            check_json(string)

    @pytest.mark.parametrize("file_name", _valid_file_list)
    def test_valid_json(self, path: str, file_name):
        with open(path.format("step2", file_name)) as f:
            string = f.read()
        assert check_json(string) is True


class TestStep3:
    def test_invalid_json(self, path: str):
        with open(path.format("step3", "invalid")) as f:
            string = f.read()
        with pytest.raises(Exception, match="Expecting a valid value in key-value pair"):
            check_json(string)

    def test_valid_json(self, path: str):
        with open(path.format("step3", "valid")) as f:
            string = f.read()
        assert check_json(string) is True


class TestStep4:
    _valid_file_list: List[str] = ["valid", "valid2"]

    def test_invalid_json(self, path: str):
        with open(path.format("step4", "invalid")) as f:
            string = f.read()
        with pytest.raises(Exception, match="Expecting a valid value in key-value pair"):
            check_json(string)

    @pytest.mark.parametrize("file_name", _valid_file_list)
    def test_valid_json(self, path: str, file_name):
        with open(path.format("step4", file_name)) as f:
            string = f.read()
        assert check_json(string) is True


@pytest.fixture
def other_path():
    return "./tests/test/{}"


class TestOtherCases:
    _fail_files: List[str] = [
        file.name
        for file in Path("./tests/test/").iterdir()
        if file.is_file() and file.name.startswith("fail")
    ]
    _pass_files: List[str] = [
        file.name
        for file in Path("./tests/test/").iterdir()
        if file.is_file() and file.name.startswith("pass")
    ]

    @pytest.mark.parametrize("fail_file", _fail_files)
    def test_fail_json_cases(self, other_path: str, fail_file: str):
        with open(other_path.format(fail_file)) as f:
            string = f.read()
        with pytest.raises(Exception):
            check_json(string)

    @pytest.mark.parametrize("pass_file", _pass_files)
    def test_pass_json_cases(self, other_path: str, pass_file: str):
        with open(other_path.format(pass_file)) as f:
            string = f.read()
        assert check_json(string) is True
