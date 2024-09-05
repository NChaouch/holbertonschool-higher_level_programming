#!/usr/bin/python3
import sys

if __name__ == "__main__":
    number_args = len(sys.argv) - 1

    if number_args == 0:
        print("0 arguments.")
    elif number_args == 1:
        print("1 argument:")
    else:
        print(f"{number_args} arguments:")

    for ct in range(1, len(sys.argv)):
        print(f"{ct}: {sys.argv[ct]}")
