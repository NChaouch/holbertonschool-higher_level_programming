#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # if key exist his value change, if is not exist a new pair is added
    a_dictionary.update({key: value})
    return a_dictionary
