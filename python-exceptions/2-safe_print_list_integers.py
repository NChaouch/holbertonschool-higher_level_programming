#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ct = 0
    for p in range(x):
        try:
            print("{:d}".format(my_list[p]), end="")
            ct += 1
        except (ValueError, TypeError):
            continue  # if error continue
    print()  # print the /n
    return ct
