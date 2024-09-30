#!/usr/bin/python3

"""
define prototype
"""


import json


def save_to_json_file(my_obj, filename):
    """
    code
    """

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)  # dump = for write (obj) json on file
