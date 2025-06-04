"""
You are given a string word, and an integer numFriends.

Alice is organizing a game for her numFriends friends. There are multiple rounds in the game, where in each round:
- word is split into numFriends non-empty strings, such that no previous round has had the exact same split.
- All the split words are put into a box.
Find the lexicographically largest string from the box after all the rounds are finished.

Example 1:
Input: word = "dbca", numFriends = 2
Output: "dbc"
Explanation: 
All possible splits are:
"d" and "bca".
"db" and "ca".
"dbc" and "a".

Example 2:
Input: word = "gggg", numFriends = 4
Output: "g"
Explanation: 
The only possible split is: "g", "g", "g", and "g".

Constraints:
- 1 <= word.length <= 5 * 103
- word consists only of lowercase English letters.
- 1 <= numFriends <= word.length

Approach:
Since we are looking the max substring we can find the max letter (#1)
and take the maximum window from this max symbol.
Thus we can reduce the number of iterations needed.
Time complexity seems to be the O(n) in the worst case.
"""

class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word

        max_window = len(word) - numFriends + 1
        m = max(word) #1
        result = ""
        for i in range(len(word)):
            if word[i] != m:
                continue
            result = max(result, word[i: i+max_window])
        return result


if __name__ == "__main__":
    test_cases = [
        ("dbca", 2, "dbc"),
        ("gggg", 4, "g"),
        ("aann", 2, "nn"),
        ("gh", 1, "gh"),
        ("b", 1, "b"),

    ]
    s = Solution()
    for test_case_num, (word, num_friends, expected_result) in enumerate(test_cases):
        result = s.answerString(word, num_friends)
        assert expected_result == result, f"Test case {test_case_num} failed: {expected_result=} {result=}"
    print("All tests passed!")