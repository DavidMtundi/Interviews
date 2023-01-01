"""
Write a function islandcount, that takes in a grid containing Ws and LS.
w represents water and L represents land. the function should
return the number of islands on the grid. an island is a vertically
or horizontally connected region of land

Example
    grid =[
    ['w','l','w','w','w'],
    ['w','l','w','l','w'],
    ['w','w','w','l','w'],
    ['w','w','l','l','w'],
    ['l','w','w','l','l'],
    ['l','l','w','w','w'],
    ];
"""

class Solution:
    def islandCount(self,grid):

        for row in range(0,len(grid)):
            for col in range(0,len(grid[row])):
                