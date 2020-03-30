import heapq
from operator import neg
from random import shuffle

import pytest

from algorithms import heap


def test_base():
    arr = []
    heap.insert(arr, 200)
    heap.insert(arr, 10)
    assert heap.pop_max(arr) == 200
    heap.insert(arr, 5)
    heap.insert(arr, 500)
    assert heap.pop_max(arr) == 500


def test_case_1():
    arr = []
    heap.insert(arr, 200)
    heap.insert(arr, 10)
    heap.insert(arr, 5)
    heap.insert(arr, 500)
    heap.pop_max(arr)
    heap.pop_max(arr)
    heap.pop_max(arr)
    heap.pop_max(arr)


def test_case_2():
    arr = []
    heap.insert(arr, 10)
    heap.insert(arr, 10)
    heap.insert(arr, 8)
    heap.pop_max(arr)
    assert arr == [10, 8]


def test_case_3():
    arr = []
    heap.insert(arr, 2)
    heap.insert(arr, 3)
    heap.insert(arr, 15)
    heap.insert(arr, 18)
    heap.insert(arr, 12)
    heap.pop_max(arr)
    heap.pop_max(arr)
    heap.pop_max(arr)
    assert arr == [3, 2]


def test_case_4():
    arr = []
    heap.insert(arr, 4)
    heap.insert(arr, 3)
    heap.insert(arr, 0)
    heap.pop_max(arr)
    assert arr == [3, 0]

def test_case_5():
    arr = []
    heap.insert(arr, 53)
    heap.insert(arr, 7)
    heap.insert(arr, 22)
    heap.insert(arr, 6)
    heap.insert(arr, 5)
    heap.insert(arr, 21)
    heap.insert(arr, 20)
    assert heap.pop_max(arr) == 53
    assert heap.pop_max(arr) == 22
    assert heap.pop_max(arr) == 21
    assert heap.pop_max(arr) == 20
    assert heap.pop_max(arr) == 7
    assert heap.pop_max(arr) == 6
    assert heap.pop_max(arr) == 5
