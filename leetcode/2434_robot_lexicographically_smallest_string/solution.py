"""
You are given a string s and a robot that currently holds an empty string t. Apply one of the following operations until s and t are both empty:

- Remove the first character of a string s and give it to the robot. The robot will append this character to the string t.
- Remove the last character of a string t and give it to the robot. The robot will write this character on paper.

Return the lexicographically smallest string that can be written on the paper.

Example 1:
Input: s = "zza"
Output: "azz"
Explanation: Let p denote the written string.
Initially p="", s="zza", t="".
Perform first operation three times p="", s="", t="zza".
Perform second operation three times p="azz", s="", t="".

Example 2:
Input: s = "bac"
Output: "abc"
Explanation: Let p denote the written string.
Perform first operation twice p="", s="c", t="ba". 
Perform second operation twice p="ab", s="c", t="". 
Perform first operation p="ab", s="", t="c". 
Perform second operation p="abc", s="", t="".

Example 3:
Input: s = "bdda"
Output: "addb"
Explanation: Let p denote the written string.
Initially p="", s="bdda", t="".
Perform first operation four times p="", s="", t="bdda".
Perform second operation four times p="addb", s="", t="".
 

Constraints:
- 1 <= s.length <= 10^5
- s consists of only English lowercase letters.


Can't solve this shit...
Okay, I did it with editorial.......................

Greedy algorighm suits this task. 
First, we're always pushing letters to stack (t).
On every iteration we are finding minimum of the rest string and popping from stack to result all symbols
that are less than our minimum symbol.

So we are always pushing from the string to stack
AND
on every step we are updating the minimum symbol from the rest string
AND
pushing everything that is less then minimum in stack to result


Thus, we are always find minimum from the string and trying to push everyghing that less or equal to the result.
Doing so we are maintaining lexicographical minimum.

pizdec
"""

from collections import Counter
from string import ascii_lowercase

def get_min(cnt: Counter) -> str:
    for l in ascii_lowercase:
        if cnt.get(l, 0) == 0:
            continue
        break
    return l

class Solution:
    def robotWithString(self, s: str) -> str:
        cnt = Counter(s)
        t = []
        m = get_min(cnt)
        result = []
        for c in s:
            cnt[c] -= 1
            t.append(c)
            m = get_min(cnt)
            while t and t[-1] <= m:
                result.append(t.pop())

        return "".join(result)


if __name__ == "__main__":
    test_cases = [
        ("zza", "azz"),
        ("bac", "abc"),
        ("bdda", "addb"),
        ("bydizfve", "bdevfziy"),
        ('vzhofnpo','fnohopzv'),
        ('a' + 'z'*10000 + 'a', "aa" + 'z' * 10000),
        #  ("", "", "", ""),
    ]
    s = Solution()
    for *args, expected in test_cases:
        result = s.robotWithString(*args)
        assert result == expected, f"{result=}, {expected=}, {args=}"

    print("Success!")