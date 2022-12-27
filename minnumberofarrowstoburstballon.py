# There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

"""
Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.



Example 1:

Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
"""


class Solution(object):
    def findMinArrowShots(self, points):
        length = len(points)
        if points == None:
            return 0
        if length < 2:
            return length
        points.sort(key=lambda x: x[0])
        print(points)
        prev_end = float('-inf')
        minimum_arrows = 0
        for start, end in points:
            if start > prev_end:
                print(start, end)
                minimum_arrows += 1
                prev_end = end
        return minimum_arrows

    def numberofarrowstoburst(self, points):
        # points refer to the list of points
        size = len(points)
        if size < 2:
            return size
        # sort the points first by the last value
        points = sorted(points, key=lambda x: x[0], reverse=True)
        print(points)
        previouscomparison = points[0]
        arrowscount = 1
        print(previouscomparison)
        for el in points:
            if previouscomparison[-1] >= el[-1] >= previouscomparison[0]:
                continue
            else:
                arrowscount += 1
                print(el, previouscomparison)
                previouscomparison = el

        return arrowscount


sol = Solution()
pointsg=[[10,16],[2,8],[1,6],[7,12]]
print(sol.numberofarrowstoburst(pointsg))
print(sol.findMinArrowShots(pointsg))