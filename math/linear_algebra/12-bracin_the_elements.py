#!/usr/bin/env python3
"""Module for element-wise operations using NumPy."""


def np_elementwise(mat1, mat2):
    """Performs element-wise arithmetic.
    Args:
        mat1 (numpy.ndarray): first ndarray
        mat2 (numpy.ndarray or scalar): second ndarray or scalar
    Returns:
        tuple: (sum, difference, product, quotient)
    """
    # element-wise ops
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
