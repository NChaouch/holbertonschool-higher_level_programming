#!/usr/bin/python3
def print_last_digit(number):
    last_dg = abs(number) % 10
    print(last_dg, end="")
    return last_dg
