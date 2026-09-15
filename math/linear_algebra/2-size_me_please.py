#!/usr/bin/env python3
"""Module to calculate the shape of a matrix."""


def matrix_shape(matrix):
    """Calculates the shape of a matrix.
    Args:
        matrix (list): the matrix
    Returns:
        list of integers: the shape
    """
    shape = []  # store dimensions
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
