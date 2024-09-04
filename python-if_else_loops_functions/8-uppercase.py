#!/usr/bin/python3
def uppercase(str):
    for character in str:
        # check if the char is a lowercase letter
        if 'a' <= character <= 'z':
            # Convert the char to upper
            uppercase_character = chr(ord(character) - 32)
        else:
            # guard the char if is not lowercase letter
            uppercase_character = character
        # display char without \n
        print("{}".format(uppercase_character), end="")

    # display new line after convert the string
    print()
