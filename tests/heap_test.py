import pytest

from algorithms import heap

testdata = [
    list(range(5)),
    list(range(15)),
    list(range(50)),
    list(range(150)),
    list(range(1000)),
    list(range(100000)),
]


@pytest.mark.parametrize("numbers", testdata)
def test_simple(numbers):
    heap_arr = numbers.copy()
    heap.heapify(heap_arr)

    for idx, elem in enumerate(reversed(numbers), start=1):
        print(heap_arr)
        assert elem == heap.pop(heap_arr), f"Broke at {idx}/{len(numbers)} elements"
