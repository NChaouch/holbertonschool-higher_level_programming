#!/usr/bin/python3
# ensure the following code only run when the file is executed directly
if __name__ == "__main__":
    # Import the function add from file add_0.py
    from add_0 import add

    a = 1  # De©ine variable a
    b = 2  # De©ine variable b

    # Calculate the sum of the function import add from add_0.py
    result = add(a, b)

    # display the result of the function
    print("{} + {} = {}".format(a, b, result))
