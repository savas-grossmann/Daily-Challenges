# Leetcode 747 - https://leetcode.com/problems/largest-number-at-least-twice-of-others/
from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        maximum = nums_sorted[-1]
        idx = nums.index(maximum)
        del nums_sorted[-1]
        nums = set(nums_sorted)
        for i in nums:
            if 2 * i > maximum:
                return -1
        return idx


if __name__ == '__main__':
    sol = Solution()
    print(sol.dominantIndex([3,2,6,0]))
