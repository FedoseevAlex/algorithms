"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
You are giving candies to these children subjected to the following requirements:
1. Each child must have at least one candy.
2. Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies to the children.
 
Example 1:
Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:
Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
 
Constraints:
n == ratings.length
1 <= n <= 2 * 10^4
0 <= ratings[i] <= 2 * 10^4
"""

"""
How to solve:

We have an invariant that should stand. And I think we should try to enforce it iteratively.
OR
Try to use dynamic programming for that.

"""

class Solution:
    def candy(self, ratings: list[int]) -> int:
        candies = [1] * len(ratings)

        self.traverse(ratings, candies)
        candies = candies[::-1]
        ratings = ratings[::-1]
        self.traverse(ratings, candies)

        return sum(candies)
        
    def traverse(self, ratings: list[int], candies: list[int]):
        for idx in range(len(ratings)):
            forward_idx = idx+1 if idx < len(ratings) - 1 else None

            curr = ratings[idx]
            forward = ratings[forward_idx] if forward_idx is not None else -float("inf")

            candies[idx] = candies[idx]
            forward_c = candies[forward_idx] if forward_idx is not None else -float("inf")

            if curr > forward and candies[idx] <= forward_c and forward_idx is not None:
                candies[idx] = max(candies[idx], candies[forward_idx]) + 1

            if curr < forward and candies[idx] >= forward_c and forward_idx is not None:
                candies[forward_idx] += (candies[idx] - candies[forward_idx]) + 1


if __name__ == "__main__":
    test_cases = [
        ([1,0,2], 5),
        ([1,2,2], 4),
        ([1,2,87,87,87,2,1], 13),
    ]
    s = Solution()
    for ratings, expected in test_cases:
        result = s.candy(ratings)
        assert result == expected, f"{result=}, {expected=}, {ratings=}"

    print("Success!")

