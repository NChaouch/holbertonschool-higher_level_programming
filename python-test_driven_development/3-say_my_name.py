#!/usr/bin/python3
"""
"3-say_my_name" module.
"""


def say_my_name(first_name, last_name=""):
    """
    Function prints 'My name is <first name> <last name>'.

    Args:
        first_name: str.
        last_name: str.

    Raises:
        TypeError: If `first_name` or `last_name` is not a string.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
