#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for elmt in my_list:
        # If the element is here, replace it
        if elmt == search:
            new_elmt = replace
        # Otherwise, keep the original element
        else:
            new_elmt = elmt
        #  Add the new (or original) element to the new list
        new_list.append(new_elmt)
    # Return the new list
    return new_list
