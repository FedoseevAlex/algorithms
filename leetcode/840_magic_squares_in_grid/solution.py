"""
840. Magic grids In Grid

A 3 x 3 magic grid is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that
each row, column, and both diagonals all have the same sum.
Given a row x col grid of integers, how many 3 x 3 contiguous magic grid subgrids are there?
Note: while a magic grid can only contain numbers from 1 to 9, grid may contain numbers up to 15.


Example 1:
Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
Output: 1
Explanation:
The following subgrid is a 3 x 3 magic grid:
while this one is not:
In total, there is only one magic grid inside the given grid.


Example 2:
Input: grid = [[8]]
Output: 0


Constraints:
row == grid.length
col == grid[i].length
1 <= row, col <= 10
0 <= grid[i][j] <= 15
"""
from typing import List


def solution(grid: List[List[int]]) -> int:
    # You can't have magic square if the grid is too small
    if len(grid) < 3 or len(grid[0]) < 3:
        return 0

    # we'll make the margin of one row and one column from the grid edges
    # there is no point to look for squares there
    magic_squares = 0
    for row in range(1, len(grid)-1):
        for column in range(1, len(grid[1]) -1 ):
            if is_magic(grid, row, column):
                magic_squares += 1
    return magic_squares

def is_magic(grid: List[List[int]], center_row: int, center_column: int) -> bool:
    numbers = set()
    # check that numbers in square belong to [1, 9] range
    # and also save the numbers for the next check
    for row in range(center_row-1, center_row+2):
        for column in range(center_column-1, center_column+2):
            number = grid[row][column]
            if number == 0 or number > 9:
                return False
            numbers.add(grid[row][column])

    # check that square contains all numbers from 1 to 9 only one time
    if numbers != set(range(1, 10)):
        return False

    # check sums for rows, columns and diagonals
    target_sum = sum(grid[center_row][center_column-1:center_column+2])

    # check rows sums
    for row_idx in range(center_row-1, center_row+2):
        if sum(grid[row_idx][center_column-1:center_column+2]) != target_sum:
            return False

    # check column sums
    for column_idx in range(center_column-1, center_column+2):
        if sum(row[column_idx] for row in grid[center_row-1:center_row+2]) != target_sum:
            return False

    # check diagonal sum
    if sum(grid[center_row + idx][center_column + idx] for idx in range(-1, 2)) != target_sum:
        return False

    # check reverse diagonal sum
    if sum(grid[center_row + idx][center_column - idx] for idx in range(-1, 2)) != target_sum:
        return False

    return True


if __name__ == "__main__":
    test_cases = [
        ([[4,3,8,4],[9,5,1,9],[2,7,6,2]], 1),
        ([[8]], 0),
        ([[5,5,5],[5,5,5],[5,5,5]], 0)
    ]

    for test_case_num, (*args, expected_result) in enumerate(test_cases):
        result = solution(*args)
        try:
            assert expected_result == result, f"Test case {test_case_num} failed: {expected_result=} {result=}"
        except AssertionError:
            print(expected_result)
            print(result)
            raise
    print("All tests passed!")
