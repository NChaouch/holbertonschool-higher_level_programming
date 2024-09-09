#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    int_max = my_list[0]
    num = 1
    while num < len(my_list):
        if my_list[num] > int_max:
            int_max = my_list[num]
            num += 1
            return int_max
