#!/usr/bin/python3

"""
class Suare creation
"""


class Square:

    """
    initialize size at 0
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        calcul and return the area of the square (int)
        """
        # attribute private equal size square ** 2 (in square)
        return self.__size ** 2
