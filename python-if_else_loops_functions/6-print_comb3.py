#!/usr/bin/python3
for first_dg in range(10):
    # ensures that the second digit is always greater than the first.
    for second_dg in range(first_dg + 1, 10):
        pair = f"{first_dg}{second_dg}"

        if first_dg == 8:
            print(pair)
        else:
            print(pair, end=", ")
