#!/usr/bin/env python3
from random import shuffle

def sort(array):
    """
    This function implement insert sorting algorithm.
    Example for array [3, 2, 4, 1]:
        On each iteration we compare array[i] and array[j]. 
        While array[j] > array[i] and j > 0, j is decremented.
        After the index j for which the condition above is false is found
        then array[i] is inserted to j index.
        [3, 2, 4, 1] ->
         ^
         i 
         j

        [3, 2, 4, 1] ->
            ^
            i
            j

        [2, 3, 4, 1] -> [2, 3, 4, 1] ->
               ^            ^  ^
               i            j  i
               j

        [2, 3, 4, 1] -> [2, 3, 4, 1] -> [2, 3, 4, 1]
                  ^            ^  ^         ^     ^
                  i            j  i         j     i
                  j

        [1, 2, 3, 4]
    """

    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j - 1] > array[i]:
            j -= 1
        array.insert(j, array.pop(i))
    return array

if __name__ == '__main__':
    print('Static test starts...')
    init_array = [3, 5, 4, 6, 2, 1]
    sorted_array = [1, 2, 3, 4, 5, 6]
    result = sort(init_array) 
    assert result == sorted_array, f'{result} != {sorted_array}'
    print('Static test complete')
    
    print('Random test starts...')
    big_array = list(range(10000))
    shuffled = big_array.copy()
    shuffle(shuffled)
    assert sort(shuffled) == big_array
    print('Random test complete')
