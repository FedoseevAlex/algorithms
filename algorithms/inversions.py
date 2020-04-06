from typing import List


def get_inversions(array: List[int]) -> List[int]:
    if len(array) >= 2:
        mid = len(array) // 2
        left_inversions, left = get_inversions(array[:mid])
        right_inversions, right = get_inversions(array[mid:])
        merged_inversions, merged = merge(left, right)
        return merged_inversions + left_inversions + right_inversions, merged
    return 0, array


def merge(first: List[int], second: List[int]) -> List[int]:
    result = list()
    inversions = 0

    while True:
        print(first, second)
        if not first and not second:
            break

        if not first:
            result.extend(second)
            second.clear()
        elif not second:
            result.extend(first)
            first.clear()
        elif first[0] <= second[0]:
            result.append(first.pop(0))
        else:
            inversions += len(first)
            result.append(second.pop(0))
        print(inversions)

    return inversions, result
