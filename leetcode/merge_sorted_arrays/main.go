package main

import (
	"fmt"
	"sort"
)

/*
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.


Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109


Follow up: Can you come up with an algorithm that runs in O(m + n) time?
*/

type TestCase struct {
	Nums1    []int
	Nums2    []int
	M        int
	N        int
	Expected []int
}

var testCases = []TestCase{
	{
		Nums1:    []int{1, 2, 3, 0, 0, 0},
		M:        3,
		Nums2:    []int{2, 5, 6},
		N:        3,
		Expected: []int{1, 2, 2, 3, 5, 6},
	},
	{
		Nums1:    []int{1},
		M:        1,
		Nums2:    []int{},
		N:        0,
		Expected: []int{1},
	},
	{
		Nums1:    []int{0},
		M:        0,
		Nums2:    []int{1},
		N:        1,
		Expected: []int{1},
	},
	{
		Nums1:    []int{2, 0},
		M:        1,
		Nums2:    []int{1},
		N:        1,
		Expected: []int{1, 2},
	},
}

func main() {
	//for i, tc := range testCases {
	//	merge(tc.Nums1, tc.M, tc.Nums2, tc.N)
	//	result := compareSlices(tc.Nums1, tc.Expected)
	//	if !result {
	//		fmt.Printf("merge: Test case %d failed: %v != %v", i, tc.Nums1, tc.Expected)
	//		return
	//	}
	//}

	//for i, tc := range testCases {
	//	merge2(tc.Nums1, tc.M, tc.Nums2, tc.N)
	//	result := compareSlices(tc.Nums1, tc.Expected)
	//	if !result {
	//		fmt.Printf("merge2: Test case %d failed: %v != %v", i, tc.Nums1, tc.Expected)
	//		return
	//	}
	//}

	for i, tc := range testCases {
		merge3(tc.Nums1, tc.M, tc.Nums2, tc.N)
		result := compareSlices(tc.Nums1, tc.Expected)
		if !result {
			fmt.Printf("merge3: Test case %d failed: %v != %v", i, tc.Nums1, tc.Expected)
			return
		}
	}
}

func compareSlices(a, b []int) bool {
	if len(a) != len(b) {
		return false
	}
	for i := 0; i < len(a); i++ {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}

// initial solution
func merge(nums1 []int, m int, nums2 []int, n int) {
	result := make([]int, 0, n+m)
	nums1Copy := nums1[:m]
	nums2Copy := nums2

	for len(nums1Copy) > 0 && len(nums2Copy) > 0 {
		numToAdd := 0
		switch {
		case nums1Copy[0] <= nums2Copy[0]:
			numToAdd = nums1Copy[0]
			nums1Copy = nums1Copy[1:]
		case nums2Copy[0] <= nums1Copy[0]:
			numToAdd = nums2Copy[0]
			nums2Copy = nums2Copy[1:]
		}
		result = append(result, numToAdd)
	}
	result = append(result, nums1Copy...)
	result = append(result, nums2Copy...)

	copy(nums1, result)
}

func merge2(nums1 []int, m int, nums2 []int, n int) {
	nums1 = append(nums1[m:], nums2...)
	sort.Ints(nums1)
}

// Main idea here is that we are filling nums1 array in reverse order.
// Thus, we can always choose the bigger number for the current position and
// fill the array in correct way.
func merge3(nums1 []int, m int, nums2 []int, n int) {
	var (
		mp = m - 1
		np = n - 1
		kp = n + m - 1
	)

	for np >= 0 {
		if mp >= 0 && nums1[mp] > nums2[np] {
			nums1[kp] = nums1[mp]
			mp--
		} else {
			nums1[kp] = nums2[np]
			np--
		}
		kp--
	}
}
