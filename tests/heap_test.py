import heapq
from random import randint

import pytest

from algorithms import heap

@pytest.mark.repeat(10)
def test_heapq_compare():
    arr = [randint(0, 100000) for _ in range(500)]
    heap_arr = arr.copy()
    heap.heapify(heap_arr)
    heapq_arr = arr.copy()
    heapq._heapify_max(heapq_arr)

    assert heap_arr == heapq_arr


testdata = [
    range(5, 1, -1),
    range(15, 1, -1),
    range(50, 1, -1),
    range(150, 1, -1),
    range(1000, 1, -1),
]


@pytest.mark.parametrize("numbers", testdata)
def test_simple(numbers):
    heap_arr = list(numbers)
    heap.heapify(heap_arr)

    for idx, elem in enumerate(numbers, start=1):
        print(heap_arr)
        assert elem == heap.pop(heap_arr), f"Broke at {idx}/{len(numbers)} elements"


@pytest.mark.timeout(3)
def test_for_time():
    numbers = range(100000, 1, -1)
    heap_arr = list(numbers)
    heap.heapify(heap_arr)

    for idx, elem in enumerate(numbers, start=1):
        assert elem == heap.pop(heap_arr), f"Broke at {idx}/{len(numbers)} elements"


cases = [
    (
        [
            "Insert 200",
            "Insert 10",
            "Insert 5",
            "Insert 500",
            "ExtractMax",
            "ExtractMax",
            "ExtractMax",
            "ExtractMax",
        ],
        [500, 200, 10, 5],
    ),
    (
        [
            "Insert 2",
            "Insert 3",
            "Insert 18",
            "Insert 15",
            "Insert 18",
            "Insert 12",
            "Insert 12",
            "Insert 2",
            "ExtractMax",
            "ExtractMax",
            "ExtractMax",
        ],
        [18, 18, 15],
    ),
    (
        [
            "Insert 2",
            "Insert 3",
            "Insert 15",
            "Insert 18",
            "Insert 12",
            "ExtractMax",
            "ExtractMax",
            "ExtractMax",
        ],
        [18, 15, 12],
    ),
    (["Insert 10", "Insert 10", "Insert 8", "ExtractMax", "ExtractMax",], [10, 10]),
    (["Insert 3", "Insert 0", "ExtractMax", "ExtractMax",], [3, 0]),
    (
        [
            "Insert 53",
            "Insert 7",
            "Insert 22",
            "Insert 6",
            "Insert 5",
            "Insert 21",
            "Insert 20",
            "ExtractMax",
            "ExtractMax",
        ],
        [53, 22],
    ),
    (
        [
            "Insert 304",
            "Insert 255",
            "Insert 146",
            "Insert 29",
            "Insert 157",
            "Insert 96",
            "Insert 105",
            "ExtractMax",
        ],
        [304],
    ),
]


@pytest.mark.parametrize("ops,answer", cases)
def test_cases(ops, answer):
    assert list(heap.make_answer(ops)) == answer


