#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    # found key dictio of witch the value is greater
    return max(a_dictionary, key=a_dictionary.get)
