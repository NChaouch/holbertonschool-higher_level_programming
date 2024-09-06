#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    # get the last figit of the division
    last_dg = number % 10

else:  # for number negative
    last_dg = -(abs(number) % 10)

print(f"Last digit of {number} is {last_dg} ", end="")

if last_dg > 5:
    print("and is greater than 5")

elif last_dg == 0:
    print("and is 0")

else:
    print("and is less than 6 and not 0")
