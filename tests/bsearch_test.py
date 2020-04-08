from random import randint

import pytest

from algorithms import bsearch


test_data = [
        ([1, 5, 8, 12, 13], [8, 1, 23, 1, 11], [3, 1, -1, 1, -1]),
]
@pytest.mark.parametrize('array,elements,control', test_data)
def test_cases(array, elements, control):
    results = list()

    for element in elements:
        result = bsearch.bsearch(array, element)
        results.append(result)

    assert results == control


@pytest.mark.repeat(100)
def test_simple():
    array = sorted(set(randint(0, 100) for _ in range(10)))
    elements = set(randint(0, 100) for _ in range(10))

    for element in elements:
        if element in array:
            assert array.index(element) + 1 == bsearch.bsearch(array, element)
        else:
            assert bsearch.bsearch(array, element) == -1
