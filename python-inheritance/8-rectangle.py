#!/usr/bin/python3

"""
create class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    code
    """

    def __init__(self, width, height):
        """
        rectangle initialize
        """

        # str "width" if is error (msg error)
        self.integer_validator("width", width)
        # if succes the value of width is give to private att __width
        self.__width = width
        self.integer_validator("height", height)
        # if succes the value of height is give to private att __height
        self.__height = height
