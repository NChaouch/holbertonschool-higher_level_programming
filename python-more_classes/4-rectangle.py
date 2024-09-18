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
        elif value < 0:
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
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):  # calcul area of update values of width and height(setter)
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        #  if not 0, calcul perimeter of update values of witdth and height
        return (self.__width + self.__height) * 2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")  # if equal 0 str empty
        #  if not equal 0 return str with ###
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        # return str Rectanngle with values update
        return f"Rectangle({self.__width}, {self.__height})"
