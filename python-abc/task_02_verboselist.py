#!/usr/bin/python3

"""
create class
"""


from abc import ABC, abstractmethod


class VerboseList(list):  # derived class from list
    """
    code
    """

    def append(self, item):  # for add one element in list
        super().append(item)  # call method from parent class list for add
        print(f"Added {[item]} to the list.")

    def extend(self, iter):  # for add more elements in list
        initial_len = len(self)  # measure len of list before add elem
        super().extend(iter)  # add elements
        items_add = len(self) - initial_len  # calcul of rest elem added
        print(f"Extended the list with {[items_add]} items.")

    def remove(self, item):
        if item in self:
            super().remove(item)  # remove item if is here
            print(f"Removed {[item]} from the list.")

    def pop(self, index=-1):  # last elem of the list
        if self:  # check if list is not empty
            item = super().pop(index)  # remove elem (item)
            print(f"Popped {[item]} from the list.")
            return item
