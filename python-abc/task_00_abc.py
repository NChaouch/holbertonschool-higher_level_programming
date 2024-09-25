#!/usr/bin/python3

"""
create class
"""


from abc import ABC, abstractmethod


# abstract class 'Animal' inherits from ABC
class Animal(ABC):

    """
    code
    """

    @abstractmethod
    def sound(self):
        pass  # use for derived classes


# inherits from 'Animal' abstract class
class Dog(Animal):
    # method sound for class Dog
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"
