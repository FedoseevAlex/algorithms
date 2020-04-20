"""
https://stackoverflow.com/questions/36972714/implementing-3-way-quicksort
"""
from operator import itemgetter
import bisect
from typing import List
from random import randint


def quick_sort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1

    if start >= end:
        return

    left, right = partition(array, start, end)
    quick_sort(array, start, left)
    quick_sort(array, right, end)


def partition(array, start, end):
    # random_index = randint(start + 1, end)
    # array[start], array[random_index] = array[random_index], array[start]

    pivot = array[start]
    left = start
    right = end
    i = start

    while i <= right:
        if array[i] > pivot:
            array[i], array[right] = array[right], array[i]
            right -= 1
            i -= 1
        elif array[i] < pivot:
            array[left], array[i] = array[i], array[left]
            left += 1
        i += 1
    return left - 1, right + 1


def segments(segs: List, points: List[int]):
    results = list()
    starts = list(map(itemgetter(0), segs))
    ends = list(map(itemgetter(1), segs))
    quick_sort(starts)
    quick_sort(ends)

    for point in points:
        left = bisect.bisect_right(starts, point)
        right = bisect.bisect_left(ends, point)
        results.append(abs(left - right))
    return results


if __name__ == "__main__":
    segment_num, _ = map(int, input().split())
    segs = list()
    for _ in range(segment_num):
        segs.append(tuple(map(int, input().split())))
    points = list(map(int, input().split()))

    print(*segments(segs, points))
