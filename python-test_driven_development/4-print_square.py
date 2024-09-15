#!/usr/bin/python3
"""
Functionprints a square with the character #.
"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        Size: The size length of the square (int).

    Raises:
        TypeError: if size is not an integer.
        ValueError: if size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for ct in range(size):
        print(size * "#")