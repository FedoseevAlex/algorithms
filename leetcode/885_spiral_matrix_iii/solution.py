"""
You start at the cell (rStart, cStart) of an rows x cols grid facing east.
The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.
You will walk in a clockwise spiral shape to visit every position in this grid.
Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.).
Eventually, we reach all rows * cols spaces of the grid.
Return an array of coordinates representing the positions of the grid in the order you visited them.

Example 1:
Input: rows = 1, cols = 4, rStart = 0, cStart = 0
Output: [[0,0],[0,1],[0,2],[0,3]]

Example 2:
Input: rows = 5, cols = 6, rStart = 1, cStart = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]

Constraints:
1 <= rows, cols <= 100
0 <= rStart < rows
0 <= cStart < cols
"""
from typing import List


def solution(rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
    path = [[rStart, cStart]]
    size = 1
    while len(path) < rows*cols:
        for row_step, col_step, curr_size in [(0, 1, size), (1, 0, size), (0, -1, size+1), (-1, 0, size+1)]:
            for _ in range(curr_size):
                rStart += row_step
                cStart += col_step
                if rStart < 0 or cStart < 0 or rStart >= rows or cStart >= cols:
                    continue
                path.append([rStart, cStart])
        size += 2
    return path


def _solution(rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
    size = 2
    path = [[rStart, cStart]]
    current_point = [rStart-1, cStart+1]
    while size <= 2 * max(rows, cols):
        down = [[current_point[0]+idx+1, current_point[1]] for idx in range(size)]
        path += down
        current_point = path[-1]

        left = [[current_point[0], current_point[1]-idx-1] for idx in range(size)]
        path += left
        current_point = path[-1]

        up = [[current_point[0]-idx-1, current_point[1]] for idx in range(size)]
        path += up
        current_point = path[-1]

        right = [[current_point[0], current_point[1]+idx+1] for idx in range(size)]
        path += right
        current_point = path[-1]

        size += 2
        current_point = [current_point[0]-1, current_point[1]+1]
    answer = []
    for x, y in path:
        if x < 0 or y < 0 or x >= rows or y >= cols:
            continue
        answer.append([x, y])
    return answer

if __name__ == "__main__":
    test_cases = [
        (1, 4, 0, 0, [[0,0],[0,1],[0,2],[0,3]]),
        (5, 6, 1, 4, [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]),
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
