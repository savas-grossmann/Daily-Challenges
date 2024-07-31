
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#
# Given and int array, find the 2 best indices i and j so array[j] - array[i] is max
# but i < j, return the difference or 0 if its minus.

from typing import List


def maxProfit_slow(self, prices: List[int]) -> int:
    profit = 0
    for i in range(0, len(prices) - 1):
        for j in range(i + 1, len(prices)):
            temp = prices[j] - prices[i]
            if temp > profit:
                profit = temp
    return profit


# The Problem is close to maximum SubArray. We go through the Array and try
# to find the biggest Subarray which will also give us the maximum profit
def maxProfit_fast(self, prices: List[int]) -> int:
    profit, current = 0, 0
    for i in range(1, len(prices)):
        current = max(0, current + (prices[i] - prices[i - 1]))
        profit = max(profit, current)
    return profit


if __name__ == '__main__':
    print(maxProfit_slow(1, [7, 1, 5, 3, 6, 4]))
    print(maxProfit_fast(1, [0, 6, -3, 7]))
