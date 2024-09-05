#!/usr/bin/python3

# Import the function add from the file add_0.py
from add_0 import add

# Define the variables a and b
a = 1
b = 2

# Ensure the following code only runs when the file is executed directly
if __name__ == "__main__":
    # Calculate the result of the addition
    result = add(a, b)

    # Display the result using string formatting
    print("{} + {} = {}".format(a, b, result))
