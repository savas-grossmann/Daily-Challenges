# Leetcode 137 - https://leetcode.com/problems/single-number-ii/
from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        for i in count:
            if count[i] == 1:
                return i


if __name__ == '__main__':
    sol = Solution()
    print(sol.singleNumber([0,1,0,1,0,1,99]))