#!/usr/bin/python3

"""
define prototype
"""


def append_write(filename="", text=""):
    """
    code
    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
