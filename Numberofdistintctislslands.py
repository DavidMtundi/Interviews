"""
Given a non-empty 2D array grid of 0's and 1's. an island is a group of 1's[representing land]
connected 4-directionally (horizontal or vertical). you may assume all four eges of the grid are sorrounded by water

count the number of distinct islands. an island is considered to be the same as another if and only if one island can be
translated(and not rotated or reflected) to equal the other

Example 1:
    11000
    11000
    00011
    00011

Given the above grid map, return 1

Example 2:
    11011
    10000
    00001
    11011

Given the above grid map, return 3
"""


def getDistinctisland(arr, i, j, rows, columns, param):
    if i < 0 or j < 0 or i >= rows or j >= columns or arr[i][j] == 0:
        return "O"
    arr[i][j] = 0
    left = getDistinctisland(arr, i, j - 1, rows, columns, "L")
    right = getDistinctisland(arr, i, j + 1, rows, columns, "R")
    top = getDistinctisland(arr, i - 1, j, rows, columns, "N")
    bottom = getDistinctisland(arr, i + 1, j, rows, columns, "S")

    return param + left + right + top + bottom


class Solution:
    def numberOfDistinctIslands(self, arr):
        # X -- represents the start
        # R -- represents the Right
        # L -- represents the left
        # N -- represents the north
        # S -- represents the south
        # 0 -- represents the zero OR water
        if len(arr) == 0 or arr is None:
            return 0
        rows = len(arr)
        columns = len(arr[0])
        map = {}
        for i in range(rows):
            for j in range(columns):
                if arr[i][j] == 1:
                    data = getDistinctisland(arr, i, j, rows, columns, "X")
                    map[data] = 1
        return len(map)


sol = Solution()
valuearray = [

    [1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1]
]
print(sol.numberOfDistinctIslands(arr=valuearray))
