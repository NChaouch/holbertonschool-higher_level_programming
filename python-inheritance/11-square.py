#!/usr/bin/python3

"""
create class
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    code
    """

    def __init__(self, size):
        """
        Square initialize
        """

        # str "size" if is error (msg error)
        self.integer_validator("size", size)
        # if success the value of size is give to private att __size
        self.__size = size

    def area(self):  # Calcul area of Square
        return self.__size ** 2

    def __str__(self):
        return (f"[Square] {self.__size}/{self.__size}")
