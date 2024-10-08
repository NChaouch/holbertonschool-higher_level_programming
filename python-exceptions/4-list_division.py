#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for p in range(list_length):
        try:
            result.append(my_list_1[p] / my_list_2[p])
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except (TypeError, ValueError):
            print("wrong type")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            pass
    return result
