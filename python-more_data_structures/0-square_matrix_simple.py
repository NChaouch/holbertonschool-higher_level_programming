#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        # for each row, create a new row where each number is squared.
        new_row = [elmt ** 2 for elmt in row]
        # This new line is added
        new_matrix.append(new_row)
    return new_matrix
