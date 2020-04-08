from random import randint

import pytest

from algorithms import merge_sort as ms


@pytest.fixture
def random_array():
    return [randint(0, 100000) for _ in range(randint(100, 10000))]


test_funcs = [ms.merge_sort, ms.merge_sort_iterative]


@pytest.mark.parametrize("func", test_funcs)
def test_simple(func):
    assert list(range(1, 11)) == func(list(range(10, 0, -1)))


@pytest.mark.repeat(5)
@pytest.mark.parametrize("func", test_funcs)
def test_merge_sort(func, random_array):
    assert func(random_array) == sorted(random_array)
