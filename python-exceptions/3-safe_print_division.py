#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        result = None  # if is echec
    finally:
        # print the result if none or success
        print("Inside result: {}".format(result))
        # return the result if none or success
        return result
