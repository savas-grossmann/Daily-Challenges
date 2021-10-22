#  https://leetcode.com/problems/reshape-the-matrix/
#
#   given a matrix and a new form, reshape the matrix to fit the form.
#   return the old matrix if not possible.

from typing import List
import numpy as np


# Numpy has a function which lets you reshape a matrix
def matrixReshape_np(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    try:
        #matrix = np.reshape(mat, (r, c))
        return np.reshape(mat, (r, c)).tolist()
    except:
        return mat


# If the shape of the resizing fits we can try to put in in the correct order.
# We fill out every row and then append it to our result.
def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    if r * c != len(mat) * len(mat[0]):
        return mat
    reshaped = []
    for i in range(r):
        # create empty row
        row = []
        for j in range(c):
            # calculate the correct position of the int we want to append to the row
            # c elements max in a row
            k = i * c + j
            row.append(mat[k // len(mat[0])][k % len(mat[0])])
        reshaped.append(row)
    return reshaped


if __name__ == '__main__':
    print(matrixReshape(0, [[1, 2], [3, 4]], 4, 1))
