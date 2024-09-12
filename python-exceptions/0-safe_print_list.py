#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ct = 0
    try:
        while True:
            if ct < x:  # num of element to print if less x
                print(my_list[ct], end="")
                ct += 1
            else:
                break  # if ct is no longer less than x
    except IndexError:  # if  index that does not exist in the list
        pass  # ignore
    print()  # nothing and /n
    return ct  # return true
