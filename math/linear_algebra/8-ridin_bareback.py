#!/usr/bin/env python3
"""Module for matrix multiplication."""


def mat_mul(mat1, mat2):
    """Performs matrix multiplication.
    Args:
        mat1 (list): first matrix
        mat2 (list): second matrix
    Returns:
        list: new multiplied matrix or None
    """
    if len(mat1[0]) != len(mat2):
        return None
    # init result zero matrix
    res = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                res[i][j] += mat1[i][k] * mat2[k][j]
    return res
