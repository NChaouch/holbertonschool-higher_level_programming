#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary.keys()):  # sorted by alphabetic order
        print("{}: {}".format(key, a_dictionary[key]))
