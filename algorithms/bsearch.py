from typing import List


def bsearch(arr: List, element: int):
    pos = 0
    end = len(arr) - 1
    while pos <= end:
        mid = (pos + end) // 2
        if arr[mid] > element:
            end = mid - 1
        elif arr[mid] < element:
            pos = mid + 1
        else:
            return mid + 1
    return -1
