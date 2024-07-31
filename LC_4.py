# Leetcode 4 - https://leetcode.com/problems/median-of-two-sorted-arrays/description/
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        sort = sorted(nums1)
        if len(sort) % 2 != 0:
            return sort[int(len(sort) / 2)]
        else:
            a, b = int(len(sort) / 2) - 1, int(len(sort) / 2)
            return (sort[a] + sort[b]) / 2


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMedianSortedArrays([1,2], [3]))