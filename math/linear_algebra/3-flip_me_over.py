#!/usr/bin/env python3
"""Module for matrix transposition."""


def matrix_transpose(matrix):
    """Returns the transpose of a 2D matrix.
    Args:
        matrix (list): the 2D matrix
    Returns:
        list: transposed matrix
    """
    # use list comprehension to transpose
    return [[matrix[i][j] for i in range(len(matrix))]
            for j in range(len(matrix[0]))]
