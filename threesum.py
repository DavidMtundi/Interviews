# given an array nums of n integers,
# are there elements a,b, c in nums such that
# a+b+c =0. find all integer tripletes in the array
# which gives the sum of zero

# given an array of [-1,0,1,2,-1,-4]
# The solution set is:
# [
#   [-1,0,1]
#   [-1,-1.2]
# ]

class Solution:
    def threeSum(self, nums):
        if nums is None:
            return {}
        # sort the array first
        nums.sort()
        # declare the result array
        result = []
        # iterate through each element in the array
        for i, number in enumerate(nums):
            if i > 0 and nums[i - 1] == number:
                continue
            # declare pointers, left and right pointer
            l, r = i + 1, len(nums) - 1
            while l < r:
                summation = number + nums[l] + nums[r]
                if summation > 0:
                    r -= 1
                elif summation < 0:
                    l += 1
                else:
                    result.append([number, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return result


sol = Solution()
print(sol.threeSum(nums=[-1, 0, 1, 2, -1, -4]))
