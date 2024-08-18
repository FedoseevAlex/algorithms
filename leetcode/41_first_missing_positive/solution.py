"""
41. First Missing Positive
https://leetcode.com/problems/first-missing-positive

Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.
You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Example 2:
Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.


Constraints:
1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
"""

def normal_solution(nums: list[int]):
    nums_set = set(nums)
    for n in range(1, len(nums) + 2):
        if n not in nums_set:
            return n

def solution(nums: list[int]):
    n = len(nums)
    idx = 0
    while idx < n:
        correct_idx = nums[idx] - 1
        if 0 < nums[idx] < n and nums[idx] != nums[correct_idx]:
            nums[idx], nums[correct_idx] = nums[correct_idx], nums[idx]
        else:
            idx += 1

    for idx, n in enumerate(nums, start=1):
        if idx != n:
            return idx


if __name__ == "__main__":
    test_cases = [
        ([1], 2),
        ([3,4,-1,1], 2),
        ([1,2,0], 3),
        ([7,8,9,11,12], 1),
    ]

    for test_case_num, (*args, expected_result) in enumerate(test_cases):
        result = normal_solution(*args)
        try:
            assert expected_result == result, f"Test case {test_case_num} failed: {expected_result=} {result=}"
        except AssertionError:
            print(expected_result)
            print(result)
            raise
    print("All tests passed!")
