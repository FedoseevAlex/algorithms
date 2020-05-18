"""
Implementation of algorithm for finding maximum length of non-decreasing sequence
"""
from typing import List


def max_seq(array: List[int]):
    lens = list()
    for i in range(len(array)):
        lens.append(1)
        for j in range(i):
            if (
                array[j] <= array[i]
                and array[i] % array[j] == 0
                and lens[j] + 1 > lens[i]
            ):
                lens[i] += 1

    return max(lens)


if __name__ == "__main__":
    num = input()
    arr = [int(i) for i in input().split()]
    print(max_seq(arr))
