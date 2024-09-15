#!/usr/bin/python3

"""
This contains the matrix_divided function
"""


def matrix_divided(matrix, div):

    """Divides all elements of a matrix by div and returns a new matrix.

    Args:
        matrix: a list of lists of integers or floats.
       div: a number (integer or float) to divide the matrix by.

    Raises:
        TypeError: if the matrix is not a list of lists of integers/floats,
                   if the rows of the matrix are not the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is 0.

    Returns:
        A new matrix with all elements divided by div,
        rounded to 2 decimal places.
    """

    # Check if matrix is a list of lists (integers or floats)
    if not isinstance(matrix, list) or not all(
        isinstance(row, list) for row in matrix
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    # Check if all rows are the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element by div and round to 2 decimal places
    return [[round(num / div, 2) for num in row] for row in matrix]
