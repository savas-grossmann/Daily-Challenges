# Leetcode 1886 - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation
import numpy as np
from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for i in range(4):
            if np.array_equal(np.rot90(mat, i), target):
                return True
        return False


# if __name__ == '__main__':
#    sol = Solution()
#    mat = [[0,1],[1,1]]
#    target = [[1,0],[0,1]]
#    print(sol.findRotation(mat, target)
