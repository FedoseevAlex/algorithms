package main

import (
	"fmt"
	"slices"
)

/*
Given n points on a 2D plane where points[i] = [xi, yi],
Return the widest vertical area between two points such that no points are inside the area.
A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height).
The widest vertical area is the one with the maximum width.
Note that points on the edge of a vertical area are not considered included in the area.

Example 1:
Input: points = [[8,7],[9,9],[7,4],[9,7]]
Output: 1

Example 2:
Input: points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
Output: 3


Constraints:
n == points.length
2 <= n <= 105
points[i].length == 2
0 <= xi, yi <= 109

*/

type TestCase struct {
	Input    [][]int
	Expected int
}

var testCases = []TestCase{
	{
		Input:    [][]int{{8, 7}, {9, 9}, {7, 4}, {9, 7}},
		Expected: 1,
	},
	{
		Input:    [][]int{{3, 1}, {9, 0}, {1, 0}, {1, 4}, {5, 3}, {8, 8}},
		Expected: 3,
	},
}

func main() {
	for i, tc := range testCases {
		result := maxWidthOfVerticalArea(tc.Input)
		if tc.Expected != result {
			fmt.Printf("Test case %d failed: %d != %d", i, result, tc.Expected)
			return
		}
	}
}

func maxWidthOfVerticalArea(points [][]int) int {
	xCoordinates := []int{}
	for _, point := range points {
		xCoordinates = append(xCoordinates, point[0])
	}

    slices.Sort(xCoordinates)


    maxDistance := 0
    for i := 0; i < len(xCoordinates) - 1; i++ {
        distance := xCoordinates[i+1] - xCoordinates[i]
        if distance > maxDistance {
            maxDistance = distance
        }
    }

	return maxDistance
}
