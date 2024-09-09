#!/usr/bin/python3
def no_c(my_string):
    filtr_char = (char for char in my_string if char != 'c' and char != 'C')
    new_str = "".join(filtr_char)
    return new_str
