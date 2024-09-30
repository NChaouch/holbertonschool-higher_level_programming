#!/usr/bin/python3

"""
define prototype
"""


def write_file(filename="", text=""):
    """
    code
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
