#!/usr/bin/python3

"""
class Square creation
"""


class Square:

    """
    initialize size and position at 0
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):  # access the value of the private position attribute
        return self.__position

    @position.setter
    # modification of the value of private position attribute
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(number, int) for number in value) or
                not all(number >= 0 for number in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):  # calcul of the update value (size setter)
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()  # print line empty
        else:
            for _ in range(self.__position[1]):  # if size is not 0
                print()
            for _ in range(self.__size):
                # repeat size times because is num of row in square
                print(" " * self.__position[0] + "#" * self.__size)
