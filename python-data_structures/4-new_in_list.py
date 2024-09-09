#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_new = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return list_new
    list_new[idx] = element
    return list_new
