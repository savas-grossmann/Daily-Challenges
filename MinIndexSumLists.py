# leetcode 599 - https://leetcode.com/problems/minimum-index-sum-of-two-lists/
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = []
        for i in list1:
            if i in list2:
                common.append((list1.index(i) + list2.index(i), i))
        common = sorted(common)
        minIndexSum = common[0][0]
        words = []
        for i in common:
            if i[0] == minIndexSum:
                words.append(i[1])
        return words


# if __name__ == '__main__':
#    sol = Solution()
#    list1 = ["Shogun","Piatti","Tapioca Express","Burger King","KFC"]
#    list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
#    print(sol.findRestaurant(list1, list2))
