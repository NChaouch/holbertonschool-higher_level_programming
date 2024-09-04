#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        string = ""
        # Check if number is divisible by both 3 and 5
        if number % 3 == 0 and number % 5 == 0:
            string = "FizzBuzz"
        elif number % 3 == 0:  # Check if number is divisible by 3
            string = "Fizz"
        elif number % 5 == 0:  # Check if number is divisible by 5
            string = "Buzz"
        else:
            string = str(number)  # If false, just print the number

        print(string, end=" ")

# Call the function to display result


fizzbuzz()
