from typing import List


def merge_sort(array: List[int]) -> List[int]:
    if len(array) > 2:
        mid = len(array) // 2
        left = merge_sort(array[:mid])
        right = merge_sort(array[mid:])
        return merge(left, right)
    elif len(array) == 2:
        return [min(array), max(array)]
    else:
        return array


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
            result.append(first.pop(0))
        else:
            result.append(second.pop(0))

    return result
