package main

import (
	"fmt"
)

/*
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104
*/

type TestCase struct {
	Prices   []int
	Expected int
}

var testCases = []TestCase{
	{
		Prices:   []int{7, 1, 5, 3, 6, 4},
		Expected: 5,
	},
	{
		Prices:   []int{7, 6, 4, 3, 1},
		Expected: 0,
	},
	{
		Prices:   []int{2, 4, 1},
		Expected: 2,
	},
}

func main() {
	for i, tc := range testCases {
		result := maxProfit(tc.Prices)
		if tc.Expected != result {
			fmt.Printf("Test case %d failed: %d != %d", i, result, tc.Expected)
			return
		}
	}
}

// just try to get value of maximum profit
func maxProfit(prices []int) int {
	min, maxProfit := -1, 0
	for _, price := range prices {
		if price < min || min < 0 {
			min = price
		}
		if maxProfit < price-min {
			maxProfit = price - min
		}
	}
	if maxProfit > 0 {
		return maxProfit
	}
	return 0
}
