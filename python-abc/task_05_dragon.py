#!/usr/bin/python3

"""
create class
"""


from abc import ABC, abstractmethod


class SwimMixin:
    """
    code
    """

    def swim(self):
        print(f"The creature swims!")


class FlyMixin:
    def fly(self):
        print(f"The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print(f"The dragon roars!")
