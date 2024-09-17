#!/usr/bin/python3

"""
class Rectangle creation
"""


class Rectangle:

    """
    initialize width and height at 0
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):  # access the value of the private width attribute
        return self.__width

    @width.setter
    # modification of the value of private width attribute
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property  # access the value of the private height attribute
    def height(self):
        return self.__height

    @height.setter
    # modification of the value of private height attribute
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
