#!/usr/bin/env python3.8

from unittest import TestCase
from random import shuffle

from insert_sorting import increase_sort, decrease_sort


class InsertionSortTest(TestCase):
    """
    Test for insertion sorting functions
    """

    def test_increasing_sort_static(self):
        """
        Testing insertion sort in increasing order implementation.
        Check result using static array.
        """
        input_array = [3, 1, 4, 5, 2, 6]
        output_array = [1, 2, 3, 4, 5, 6]

        result = increase_sort(input_array)
        self.assertListEqual(output_array, result)

    def test_decreasing_sort_static(self):
        """
        Testing insertion sort in decreasing order implementation.
        Check result using static array.
        """
        input_array = [3, 1, 4, 5, 2, 6]
        output_array = [6, 5, 4, 3, 2, 1]

        result = decrease_sort(input_array)
        self.assertListEqual(output_array, result)

    def test_increasing_sort_random(self):
        """
        Testing insertion sort in increasing order implementation.
        Check result using random shuffled array.
        """
        output_array = list(range(10000)) 
        input_array = output_array.copy()
        shuffle(input_array)

        result = increase_sort(input_array)
        self.assertListEqual(output_array, result)

    def test_decreasing_sort_random(self):
        """
        Testing insertion sort in decreasing order implementation.
        Check result using random shuffled array.
        """
        output_array = list(range(10000, -1)) 
        input_array = output_array.copy()
        shuffle(input_array)

        result = decrease_sort(input_array)
        self.assertListEqual(output_array, result)

