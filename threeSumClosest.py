"""
Given an array nums of n intergers and an interger target, find three integers in nums
such that the sum is closest to target. return the sum of the three integers. you may
assume that each in put would have exactly one solution
Example
    Given array nums = [-1,2,1,-4] and target = 1
    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)

"""


class Solution:
    def threeSumclosest(self, nums, target):
        if len(nums) < 3 or not nums:
            return 0
        nums.sort()

        upperbound = len(nums) - 1
        threeintegers = []
        closestsum = None
        for i in range(len(nums) - 2):
            lowerbound = i + 1
            while lowerbound < upperbound:
                summation = nums[i] + nums[lowerbound] + nums[upperbound]
                if closestsum is None:
                    closestsum = summation
                    threeintegers = [nums[i], nums[lowerbound], nums[upperbound]]
                if target - summation <= abs(target - closestsum):
                    threeintegers = [nums[i], nums[lowerbound], nums[upperbound]]
                    closestsum = summation
                if summation > target:
                    upperbound -= 1
                elif summation < target:
                    lowerbound += 1
                else:
                    return [threeintegers, closestsum]

        return [threeintegers, closestsum]


sol = Solution()
values = [-1, 2, 1, -4]
print(sol.threeSumclosest(nums=values, target=1))
