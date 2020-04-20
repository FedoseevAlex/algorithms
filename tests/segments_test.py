from random import randint

import pytest

from algorithms import segments as seg


@pytest.fixture
def random_array():
    return [randint(0, 100000) for _ in range(randint(100, 50000))]


def test_simple():
    array = list(range(5, 0, -1))
    array.extend([2] * 2)
    control = sorted(array)
    seg.quick_sort(array)
    assert array == control


@pytest.mark.repeat(5)
def test_sort_random(random_array):
    array = random_array.copy()
    seg.quick_sort(array)
    assert array == sorted(random_array)


test_data = [
    ([(0, 9), (6, 8)], (1, 6, 11), [1, 2, 0]),
    ([(0, 5), (7, 10)], (1, 6, 11), [1, 0, 0]),
]


@pytest.mark.parametrize('array, points, control', test_data)
def test_segments(array, points, control):
    assert seg.segments(array, points) == control
