#!/usr/bin/python3
for first_dg in range(10):
    # ensures that the second digit is always greater than the first.
    for second_dg in range(first_dg + 1, 10):
        if first_dg == 8 and second_dg == 9:
            print(f"{first_dg}{second_dg}")
        else:
            print(f"{first_dg}{second_dg}", end=", ")
