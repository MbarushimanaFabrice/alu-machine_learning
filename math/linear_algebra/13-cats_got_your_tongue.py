#!/usr/bin/env python3
"""Module for concatenating ndarrays."""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Concatenates two ndarrays along a specific axis.
    Args:
        mat1 (numpy.ndarray): first ndarray
        mat2 (numpy.ndarray): second ndarray
        axis (int): axis
    Returns:
        numpy.ndarray: concatenated array
    """
    # concatenate arrays
    return np.concatenate((mat1, mat2), axis=axis)
