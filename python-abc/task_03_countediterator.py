#!/usr/bin/python3

"""
create class
"""


from abc import ABC, abstractmethod


class CountedIterator:
    """
    code
    """

    def __init__(self, iterable):
        # initialize self.iterable
        self.iterable = iter(iterable)
        # initialize the counter
        self.count = 0

    def __iter__(self):
        # return self for the iterations in code
        return self

    def __next__(self):
        try:
            item = next(self.iterable)  # call for each iteration
            self.count += 1  # iteration
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        return self.count  # num elem iteration
