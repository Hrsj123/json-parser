from setuptools import find_packages, setup

setup(
    name="py-json-checker",
    version="0.0.1",
    packages=find_packages("json_parser"),
    # install_requires=[],
    entry_points={
        "console_scripts": [
            "check-json=json_parser.main:_cli",
        ]
    },
)
