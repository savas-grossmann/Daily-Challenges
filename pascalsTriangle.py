# given a number, return the Pascal Triangle with rows according to the number

def pascalsTriangle(numRows: int):
    # create a 2D array filled with 0s
    triangle = [[0]*(x + 1) for x in range(numRows)]
    # we go trough the number of rows
    for row in range(0, numRows):
        # every row has len(row) numbers in it. f.e 2nd row -> 2 numbers
        for j in range(0, row + 1):
            # check if its the first or last element which is always 1
            if j == 0 or j == row:
                triangle[row][j] = 1
            else:
                # get the two numbers which are above the one we search and add them together
                triangle[row][j] = triangle[row - 1][j - 1] + triangle[row - 1][j]
    return triangle


if __name__ == '__main__':
    print(pascalsTriangle(5))
