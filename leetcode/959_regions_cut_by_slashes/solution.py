"""
959. Regions Cut By Slashes

An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/',
'\', or blank space ' '. These characters divide the square into contiguous regions.
Given the grid grid represented as a string array, return the number of regions.
Note that backslash characters are escaped, so a '\' is represented as '\\'.


Example 1:
Input: grid = [" /","/ "]
Output: 2

Example 2:
Input: grid = [" /","  "]
Output: 1

Example 3:
Input: grid = ["/\\","\\/"]
Output: 5


Explanation: Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.

Constraints:
n == grid.length == grid[i].length
1 <= n <= 30
grid[i][j] is either '/', '\', or ' '.
"""
from typing import List

# There is an euler formula that could help solve this task
# v - e + f = 2, where
# v - number of vertices
# e - number of edges
# f - number of faces (aka regions)
# We can transform it to: f = 2 + e - v
# So let's try to count number of edges and vertices and after that we could try to apply the formula.

def solution(grid: List[str]) -> int:
    print_grid(grid)
    edges = set()
    vertices = set()



    return len(edges) - len(vertices) + 2

def print_grid(grid: List[str]):
    print("-" * (len(grid[0]) + 2))
    for row in grid:
        print("|" + row + "|")
    print("-" * (len(grid[0]) + 2))

if __name__ == "__main__":
    test_cases = [
        ([" /","/ "], 2),
        ([" /","  "], 1),
        (["/\\","\\/"], 5),
        (["/\\/\\", "\\/\\/", "/\\/\\", "\\/\\\\"], 12),
        (["   ", "   ", "   "], 1),
        ([" /\\"," \\/","\\  "], 4),
        (["/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\","/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\","/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\","/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\","/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\","/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\","/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\","/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\","/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\","/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\","/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\","/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\","/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\","/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\","/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\","/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\","/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\","/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\","/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\","/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\","/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\","/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\","/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\","/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\","/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\","/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\","/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\","/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\","/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\","/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\"], 0),
        (["/\\/\\  /\\/\\  /\\/\\","/\\/\\  /\\/\\  /\\/\\","/\\/\\  /\\/\\  /\\/\\","/\\/\\  /\\/\\  /\\/\\","/\\/\\  /\\/\\  /\\/\\","/\\/\\  /\\/\\  /\\/\\","/\\/\\  /\\/\\  /\\/\\","/\\/\\  /\\/\\  /\\/\\","/\\/\\  /\\/\\  /\\/\\","/\\/\\  /\\/\\  /\\/\\","/\\/\\  /\\/\\  /\\/\\","/\\/\\  /\\/\\  /\\/\\","/\\/\\  /\\/\\  /\\/\\","/\\/\\  /\\/\\  /\\/\\","/\\/\\  /\\/\\  /\\/\\","/\\/\\  /\\/\\  /\\/\\"], 12),
    ]

    some_failed = False
    for test_case_num, (*args, expected_result) in enumerate(test_cases):
        result = solution(*args)
        try:
            assert expected_result == result, f"Test case {test_case_num} failed: {expected_result=} {result=}"
        except AssertionError as e:
            some_failed = True
            print(e)
        else:
            print(f"Test case {test_case_num} passed")


    if not some_failed:
        print("All tests passed!")
