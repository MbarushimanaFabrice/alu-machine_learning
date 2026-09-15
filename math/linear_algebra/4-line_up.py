#!/usr/bin/env python3
"""Module to add two arrays element-wise."""


def add_arrays(arr1, arr2):
    """Adds two arrays element-wise.
    Args:
        arr1 (list): first array
        arr2 (list): second array
    Returns:
        list: new array or None if shapes differ
    """
    if len(arr1) != len(arr2):
        return None
    # add element-wise
    return [arr1[i] + arr2[i] for i in range(len(arr1))]
