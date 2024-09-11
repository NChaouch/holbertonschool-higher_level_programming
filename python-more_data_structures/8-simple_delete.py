#!/usr/bin/python3
def simple_delete(a_dictionary, key=[]):
    if key in a_dictionary:
        del a_dictionary[key]  # if key is present delete
    return a_dictionary  # return if dictionary is modified or not
