#!/usr/bin/python3

"""
create class
"""


class Student:
    """
    code
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        result = {}
        for attr in attrs:
            if hasattr(self, attr):  # check if attr is here
                result[attr] = getattr(self, attr)  # get the value of attr
        return result
