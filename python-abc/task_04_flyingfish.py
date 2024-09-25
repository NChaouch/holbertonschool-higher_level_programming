#!/usr/bin/python3

"""
create class
"""


from abc import ABC, abstractmethod


class Fish:
    """
    code
    """

    def swim(self):
        print(f"The fish is swimming")

    def habitat(self):
        print(f"The fish lives in water")


class Bird:
    def fly(self):
        print(f"The bird is flying")

    def habitat(self):
        print(f"The bird lives in the sky")


class FlyingFish(Fish, Bird):
    def fly(self):
        print(f"The flying fish is soaring!")

    def swim(self):
        print(f"The flying fish is swimming!")

    def habitat(self):
        print(f"The flying fish lives both in water and the sky!")
