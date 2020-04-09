from random import randint


def quick_sort(array, start=None, end=None):
    if start is None:
        start = 0

    if end is None:
        end = len(array) - 1

    if start >= end:
        return

    separator = partition(array, start, end)
    quick_sort(array, start, separator - 1)
    quick_sort(array, separator + 1, end)


def partition(array, start, end):
    rand_index = randint(start + 1, end)
    array[start], array[rand_index] = array[rand_index], array[start]

    pivot = start
    separator = start
    right = start

    while right < end:
        right += 1
        if array[right] > array[pivot]:
            continue
        separator += 1
        array[right], array[separator] = array[separator], array[right]
    array[separator], array[pivot] = array[pivot], array[separator]
    return separator


if __name__ == '__main__':
    segment_num, _ = map(int, input().split())
    segments = list()
    for idx in segment_num:
        segments.append(tuple(map(int, input().split())))
    points = list(map(int, input().split()))
