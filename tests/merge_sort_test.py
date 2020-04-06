from random import randint

import pytest

from algorithms import merge_sort as ms


@pytest.fixture
def random_array():
    return [randint(0, 100000) for _ in range(randint(100, 10000))]

def test_simple():
    assert list(range(1, 11)) == ms.merge_sort(list(range(10, 0, -1)))


@pytest.mark.repeat(100)
def test_merge_sort(random_array):
    assert ms.merge_sort(random_array) == sorted(random_array)
