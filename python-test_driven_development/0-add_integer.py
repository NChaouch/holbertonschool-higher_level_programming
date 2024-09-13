#!/usr/bin/python3
"""
    Return the sum of two integers.

    This function takes two arguments, `a` and `b`, which can be either
    integers or floats. If either argument is a float, it will be converted
    to an integer before the addition. By default, `b` is set to 98 if not
    provided.

    Parameters:
        a (int or float): The first number to be added. Must be an integer
                          or a float.
        b (int or float, optional): The second number to be added. Must be
                                    an integer or a float. Defaults to 98.

    Returns:
        int: The result of adding `a` and `b` as integers.

    Raises:
        TypeError: If `a` or `b` is not an integer or a float.

    Examples:
        >>> add_integer(3, 5)
        8
        >>> add_integer(4.6, 2)
        6
        >>> add_integer(10)
        108
    """


def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
