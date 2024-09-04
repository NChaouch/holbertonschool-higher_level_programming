#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        string = ""
        if number % 3 == 0:  # check if number is divisible by 3
            string += "Fizz"
        if number % 5 == 0:
            string += "Buzz"
        if number % 3 != 0 and number % 5 != 0:
            string = str(number)
        print(string, end=" ")


# call the function for display result
fizzbuzz()
