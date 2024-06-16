# Leetcode 2099 - https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/
from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        for x in range(len(nums) - k):
            lowest = min(nums)
            nums.remove(lowest)
        return nums


# if __name__ == '__main__':
#    sol = Solution()
#    nums = [-1,-2,3,4]
#    k = 3
#    print(sol.maxSubsequence(nums, k))
