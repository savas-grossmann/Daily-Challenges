# Leetcode 2053 - https://leetcode.com/problems/kth-distinct-string-in-an-array/description/
from collections import Counter
from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counted = Counter(arr)
        distinct = [i for i in counted if counted[i] == 1]
        if len(distinct) < k:
            return ""
        else:
            return distinct[k - 1]


# if __name__ == '__main__':
#    test = ["d", "b", "c", "b", "c", "a"]
#    k = 2
#    sol = Solution()
#    print(sol.kthDistinct(arr=test, k=k))
