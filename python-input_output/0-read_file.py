#!/usr/bin/python3

"""
define prototype
"""


def read_file(filename=""):
    """
    code read file
    """

    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
