import pytest

from algorithms import heap

testdata = [
    range(5, 1, -1),
    range(15, 1, -1),
    range(50, 1, -1),
    range(150, 1, -1),
    range(1000, 1, -1),
    range(100000, 1, -1),
]


@pytest.mark.timeout(15)
@pytest.mark.parametrize("numbers", testdata)
def test_simple(numbers):
    heap_arr = list(numbers)
    heap.heapify(heap_arr)

    for idx, elem in enumerate(numbers, start=1):
        assert elem == heap.pop(heap_arr), f"Broke at {idx}/{len(numbers)} elements"
