#!/usr/bin/python3

"""
class Rectangle creation
"""


class Rectangle:

    """
    initialize width and height at 0
    """

    number_of_instances = 0
    print_symbol = "#"  # initialize #

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        rectangle = ""
        line = []  # initialize line empty
        for line in range(self.height):
            rectangle += str(self.print_symbol) * self.width  # if true calcul
            if line != (self.height - 1):  # -1 if different
                rectangle += '\n'  # print \n if true or false
        return rectangle  # return rectangle if true or false

    def __repr__(self):
        # return str Rectanngle with values update
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod  # belong to class
    def bigger_or_equal(rect_1, rect_2):
        # check if object is an instance of class
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() >= rect_2.area():  # for obtain surface area
            return rect_1  # if area is greater or equal rect_2
        return rect_2
