package main

import (
	"fmt"
)

/*
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
n == nums.length
1 <= n <= 5 * 10^4
-109 <= nums[i] <= 109


Follow-up: Could you solve the problem in linear time and in O(1) space?
*/

type TestCase struct {
	Nums     []int
	Expected int
}

var testCases = []TestCase{
	{
		Nums:     []int{3, 2, 3},
		Expected: 3,
	},
	{
		Nums:     []int{2, 2, 1, 1, 1, 2, 2},
		Expected: 2,
	},
	{
		Nums:     []int{1, 1, 1, 1, 1, 1, 8},
		Expected: 1,
	},
	{
		Nums:     []int{1, 2, 1, 2, 1, 2, 1},
		Expected: 1,
	},
	{
		Nums:     []int{2, 1, 2, 2, 1, 2, 1},
		Expected: 2,
	},
}

func main() {
	for i, tc := range testCases {
		result := majorityElement(tc.Nums)
		if result != tc.Expected {
			fmt.Printf("Test case %d failed: %v != %v", i, result, tc.Expected)
			return
		}
	}
}

// bulletproof solution
func majorityElement(nums []int) int {
	counter := map[int]int{}
	for _, num := range nums {
		counter[num]++
		if counter[num] > len(nums)/2 {
			return num
		}
	}

	return -1
}

// Boyer-Moore Majority Voting Algorithm
// func majorityElement(nums []int) int {
// 	candidate := 0
// 	votes := 0
// 	for _, num := range nums {
// 		if votes == 0 {
// 			candidate = num
// 		}
// 		if num == candidate {
// 			votes++
// 		} else {
// 			votes--
// 		}
// 	}
// 	return candidate
// }
