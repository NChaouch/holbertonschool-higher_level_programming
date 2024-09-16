#!/usr/bin/python3

"""
class Square creation
"""


class Square:

    """
    initialize size at 0
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):  # access the value of the private size attribute
        return self.__size

    @size.setter
    # modification of the value of private size attribute
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):  # calcul of the update value (setter)
        return self.__size ** 2
