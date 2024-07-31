# Leetcode 75 - https://leetcode.com/problems/sort-colors/
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = {0: 0, 1: 0, 2: 0}
        for i in nums:
            counter[i] += 1
        index = 0
        for i in counter:
            nums[index:index+counter[i]] = [i] * counter[i]
            index += counter[i]
        #print(nums)


if __name__ == '__main__':
    sol = Solution()
    sol.sortColors([2,0,2,1,1,0,1,2,0,0,0,0])
