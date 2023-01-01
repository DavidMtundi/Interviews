"""
Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.



Example 1:

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
"""


class Solution(object):
    def setZeroes(self, matrix):
        ROWS, COLS = len(matrix), len(matrix[0])
        firstZero = False

        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    if row < 1:
                        firstZero = True
                    else:
                        matrix[row][0] = 0

                    matrix[0][col] = 0

        for row in range(1, ROWS):
            for col in range(1, COLS):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
        if matrix[0][0] == 0:
            for row in range(ROWS):
                matrix[row][0] = 0

        if firstZero:
            for col in range(COLS):
                matrix[0][col] = 0
