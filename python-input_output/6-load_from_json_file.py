#!/usr/bin/python3

"""
define prototype
"""


import json


def load_from_json_file(filename):
    """
    code
    """

    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)  # load file on json
