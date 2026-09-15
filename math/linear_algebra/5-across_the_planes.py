#!/usr/bin/env python3
"""Module to add two 2D matrices."""


def add_matrices2D(mat1, mat2):
    """Adds two 2D matrices element-wise.
    Args:
        mat1 (list): first matrix
        mat2 (list): second matrix
    Returns:
        list: new matrix or None if shapes differ
    """
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    # nested comprehension addition
    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))]
            for i in range(len(mat1))]
