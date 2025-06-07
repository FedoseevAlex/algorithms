"""
You are given a string s. It may contain any number of '*' characters. Your task is to remove all '*' characters.
While there is a '*', do the following operation:
- Delete the leftmost '*' and the smallest non-'*' character to its left. If there are several smallest characters, you can delete any of them.
Return the lexicographically smallest resulting string after removing all '*' characters.

Example 1:
Input: s = "aaba*"
Output: "aab"
Explanation:
We should delete one of the 'a' characters with '*'. If we choose s[3], s becomes the lexicographically smallest.


Example 2:
Input: s = "abc"
Output: "abc"
Explanation:
There is no '*' in the string.

Constraints:
- 1 <= s.length <= 105
- s consists only of lowercase English letters and '*'.
The input is generated such that it is possible to delete all '*' characters.
"""
from collections import defaultdict


class Solution:
    def clearStars(self, s: str) -> str:
        result = [(x, False) for x in s]
        seen = defaultdict(list)
        for idx, symbol in enumerate(s):
            if symbol != "*":
                seen[symbol].append(idx)
                continue
            result[idx] = (symbol, True)

            m = min(k for k, v in seen.items() if len(v) != 0)
            idx2 = seen[m].pop()
            result[idx2] = (s[idx2], True)

        return "".join([x for x, deleted in result if not deleted])



if __name__ == "__main__":
    test_cases = [
        # ("abc", "abc"),
        # ("aaba*", "aab"),
        # ("de*", "e"),
        # ("abc*de*fgh*", "defgh"),
        # ("a*b*c*d*", ""),
        # ("abcde*f*", "cdef"),
        # ("abc*", "bc"),
        # ("aaaa***", "a"),
        ("r"*50_000 + "*"*50_000, ""),
        # ("", ""),
    ]
    s = Solution()
    for *args, expected in test_cases:
        result = s.clearStars(*args)
        assert result == expected, f"{result=}, {expected=}, {args=}"

    print("Success!")