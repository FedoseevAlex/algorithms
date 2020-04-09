from random import randint

import pytest

from algorithms import segments as seg


@pytest.fixture
def random_array():
    return [randint(0, 100000) for _ in range(randint(100, 10000))]


def test_simple():
    array = list(range(10, 0, -1))
    seg.quick_sort(array)
    assert list(range(1, 11)) == array


@pytest.mark.repeat(5)
def test_merge_sort(random_array):
    array = random_array.copy()
    seg.quick_sort(array)
    assert array == sorted(random_array)
