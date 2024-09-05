#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        # Check if number is divisible by both 3 and 5
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz", end=" ")
        elif number % 3 == 0:  # Check if number is divisible by 3
            print("Fizz", end=" ")
        elif number % 5 == 0:  # Check if number is divisible by 5
            print("Buzz", end=" ")
        else:
            print(number, end=" ")  # If false, just print the number


# Call the function to display result


fizzbuzz()
