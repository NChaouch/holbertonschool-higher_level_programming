#!/usr/bin/python3

"""
create class
"""


from abc import ABC, abstractmethod
from math import pi  # for calcul


class Shape(ABC):  # for geometric shape method
    """
    code
    """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):

    # initialize of circle
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (self.radius * self.radius) * pi

    def perimeter(self):
        return abs(pi * self.radius) * 2  # for values positive


class Rectangle(Shape):

    # initialize rectangle
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        return (self.width + self.height) * 2


def shape_info(shape):  # for print area and perimeter

    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
