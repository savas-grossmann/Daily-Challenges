
# https://leetcode.com/problems/intersection-of-two-arrays-ii/
#
# Given two Arrays, find the intersection
# With collections.counter we can count the appearances of each number in nums1.
# Then we can go trough nums2 and check if we have the number in our count.
# If the number is there, we put it into our result list and reduce the count of that number by one.
# if its zero we wont add that number to our array. For numbers that are not in nums1
# row 18 is always false
from typing import List
import collections


def intersection_counter(self, nums1: List[int], nums2: List[int]) -> List[int]:
    result = []
    count = collections.Counter(nums1)
    for i in nums2:
        if count[i] > 0:
            result.append(i)
            count[i] -= 1
    return result


if __name__ == '__main__':
    print(intersection_counter(0, [1, 2, 2, 1, 3, 2, 4], [2, 2, 2, 2, 3, 3, 1]))
