package main

import (
	"fmt"
)

/*
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

```
int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
```
If all assertions pass, then your solution will be accepted.

Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
*/

type TestCase struct {
	Nums      []int
	Val       int
	Expected  []int
	ExpectedK int
}

var testCases = []TestCase{
	{
		Nums:      []int{3, 2, 2, 3},
		Val:       3,
		Expected:  []int{2, 2},
		ExpectedK: 2,
	},
	{
		Nums:      []int{0, 1, 2, 2, 3, 0, 4, 2},
		Val:       2,
		Expected:  []int{0, 1, 4, 0, 3},
		ExpectedK: 5,
	},
}

func main() {
	for i, tc := range testCases {
		k := removeElement(tc.Nums, tc.Val)
		result := compareSlicesBeginsWith(tc.Nums, tc.Expected)
		if !result {
			fmt.Printf("removeElement: Test case %d failed: %v != %v", i, tc.Nums, tc.Expected)
			return
		}
		if k != tc.ExpectedK {
			fmt.Printf("removeElement: Test case %d failed: %d != %d", i, tc.ExpectedK, k)
			return
		}
	}
}

func compareSlicesBeginsWith(slice, prefix []int) bool {
	for i := 0; i < len(prefix); i++ {
		if slice[i] != prefix[i] {
			return false
		}
	}
	return true
}

// initial solution
func removeElement(nums []int, val int) int {
	notVals := 0
	for s, e := 0, len(nums)-1; s <= e; {
		if nums[s] == val {
			nums[s], nums[e] = nums[e], nums[s]
			e--
			continue
		}
		s++
		notVals++
	}
	return notVals
}
