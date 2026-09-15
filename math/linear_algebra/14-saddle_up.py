#!/usr/bin/env python3
"""Module for multiplying ndarrays."""
import numpy as np


def np_matmul(mat1, mat2):
    """Performs matrix multiplication.
    Args:
        mat1 (numpy.ndarray): first ndarray
        mat2 (numpy.ndarray): second ndarray
    Returns:
        numpy.ndarray: multiplied array
    """
    # matmul operation
    return np.matmul(mat1, mat2)
