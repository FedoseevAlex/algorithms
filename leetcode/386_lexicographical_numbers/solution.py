"""
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.
You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

Example 1:
Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]

Example 2:
Input: n = 2
Output: [1,2]
 
Constraints:
1 <= n <= 5 * 104
"""
from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        curr = 1
        for _ in range(n):
            result.append(curr)

            if curr * 10 <= n:
                curr *= 10
            else:
                while curr % 10 == 9 or curr >= n:
                    curr //= 10
                curr += 1

        return result


if __name__ == "__main__":
    test_cases = [
        (13, list(map(int, sorted(map(str, range(1, 13 + 1)))))),
        (2, list(map(int, sorted(map(str, range(1, 2 + 1)))))),
        (100,list(map(int, sorted(map(str, range(1, 100 + 1)))))),
        (1000,list(map(int, sorted(map(str, range(1, 1000 + 1)))))),
        (50_000,list(map(int, sorted(map(str, range(1, 50_000 + 1)))))),
        # (, )
    ]
    s = Solution()
    for *args, expected in test_cases:
        result = s.lexicalOrder(*args)
        assert result == expected, f"{args=}\n\n{result=}\n\n{expected=}"

    print("Success!")