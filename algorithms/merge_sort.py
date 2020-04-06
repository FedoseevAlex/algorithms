from typing import List
from itertools import zip_longest


def merge_sort(array: List[int]) -> List[int]:
    if len(array) >= 2:
        mid = len(array) // 2
        left = merge_sort(array[:mid])
        right = merge_sort(array[mid:])
        return merge(left, right)
    else:
        return array


def merge_sort_iterative(array: List[int]) -> List[int]:
    queue = [[elem] for elem in array]
    counter = 0

    while len(queue) > 1:
        first, second, *queue = queue
        merged = merge(first, second)
        queue.append(merged)
        counter += 1
    print("total merges", counter)

    return queue[0]


def merge(first: List[int], second: List[int]) -> List[int]:
    result = list()

    while True:
        if not first and not second:
            break

        if not first:
            result.extend(second)
            second.clear()
        elif not second:
            result.extend(first)
            first.clear()
        elif first[0] < second[0]:
            result.append(first[0])
            first = first[1:]
        else:
            result.append(second[0])
            second = second[1:]

    return result
