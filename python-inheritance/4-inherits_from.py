#!/usr/bin/python3

"""
define the prototype
"""


def inherits_from(obj, a_class):

    """
    conditions
    """

# if obj is a subclass of a_class
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True  # if both conditions are true
    return False
