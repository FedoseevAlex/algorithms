#!/usr/bin/env python3.8
from random import shuffle

"""
Insertion sort algorithm

Example for array [3, 2, 4, 1]:
    On each iteration we compare array[i] and array[j]. 
    While array[j] > array[i] and j > 0, j is decremented.
    After the index j for which the condition above is false is found
    then array[i] is inserted to j index.
    [3, 2, 4, 1] ->
     ^
     i 
     j

    [3, 2, 4, 1] ->
        ^
        i
        j

    [2, 3, 4, 1] -> [2, 3, 4, 1] ->
           ^            ^  ^
           i            j  i
           j

    [2, 3, 4, 1] -> [2, 3, 4, 1] -> [2, 3, 4, 1]
              ^            ^  ^         ^     ^
              i            j  i         j     i
              j

    [1, 2, 3, 4]
"""


def increase_sort(array: list) -> list:
    """
    This function implement insert sorting algorithm.
    Result array is sorted in increasing order.
    """
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j - 1] > array[i]:
            j -= 1
        array.insert(j, array.pop(i))
    return array


def decrease_sort(array: list) -> list:
    """
    This function implement insert sorting algorithm.
    Result array is sorted in decreasing order.
    """
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j - 1] < array[i]:
            j -= 1
        array.insert(j, array.pop(i))
    return array

