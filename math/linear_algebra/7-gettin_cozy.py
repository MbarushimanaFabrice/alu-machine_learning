#!/usr/bin/env python3
"""Module to concatenate two 2D matrices."""


def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenates two 2D matrices along a specific axis.
    Args:
        mat1 (list): first matrix
        mat2 (list): second matrix
        axis (int): axis for concatenation
    Returns:
        list: new matrix or None
    """
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        # copy inner arrays and concat
        return [row[:] for row in mat1] + [row[:] for row in mat2]
    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        # concat rows
        return [mat1[i][:] + mat2[i][:] for i in range(len(mat1))]
    return None
