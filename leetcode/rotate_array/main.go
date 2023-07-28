package main

import (
	"fmt"
)

/*
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Constraints:
1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105


Follow up:
Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
*/

type TestCase struct {
	Nums     []int
	Steps    int
	Expected []int
}

var testCases = []TestCase{
	{
		Nums:     []int{1, 2, 3},
		Steps:    2,
		Expected: []int{2, 3, 1},
	},
	{
		Nums:     []int{1, 2, 3, 4, 5, 6, 7},
		Steps:    3,
		Expected: []int{5, 6, 7, 1, 2, 3, 4},
	},
	{
		Nums:     []int{-1, -100, 3, 99},
		Steps:    2,
		Expected: []int{3, 99, -1, -100},
	},
	{
		Nums:     []int{-1},
		Steps:    2,
		Expected: []int{-1},
	},
	{
		Nums:     []int{1, 2, 3},
		Steps:    5,
		Expected: []int{2, 3, 1},
	},
}

func compareSlices(first, second []int) bool {
	if len(first) != len(second) {
		return false
	}
	for i := 0; i < len(first); i++ {
		if first[i] != second[i] {
			return false
		}
	}
	return true
}

func main() {
	for i, tc := range testCases {
		rotate(tc.Nums, tc.Steps)
		if !compareSlices(tc.Nums, tc.Expected) {
			fmt.Printf("Test case %d failed: %v != %v", i, tc.Nums, tc.Expected)
			return
		}
	}
}

// first solution O(N) space complexity and O(N) time complexity
//func rotate(nums []int, k int) {
//	k = k % len(nums)
//	result := make([]int, 0, len(nums))
//	result = append(result, nums[len(nums)-k:]...)
//	result = append(result, nums[:len(nums)-k]...)
//	copy(nums, result)
// }

// second solution O(1) extra space and O(N^2) time complexity
// func rotate(nums []int, k int) {
// 	k = k % len(nums)
// 	for i := 0; i < k; i++ {
// 		last := nums[len(nums)-1]
// 		for j := len(nums) - 1; j > 0; j-- {
// 			nums[j] = nums[j-1]
// 		}
// 		nums[0] = last
// 	}
// }

// third solution O(1) space complexity and O(N) time complexity
func rotate(nums []int, k int) {
	reverse := func(arr []int) {
		for i := 0; i < len(arr)/2; i++ {
			arr[i], arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]
		}
	}

	k = k % len(nums)
	reverse(nums[:len(nums)-k])
	reverse(nums[len(nums)-k:])
	reverse(nums)
}
