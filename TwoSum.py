# given an array nums of n intergers, are there elements a,b,c in nums such that a+b+c =0?4
# find all unique triplets in ther array which gives the sum of zero

# NOte
# the solution set must not contain duplicate triplets.

# Example Given an array of nums  = [-1,0,1,2,-1,-4]
# A solution set is:
# [
#       [-1,0,1],
#       [-1,-1,2]
#     ]

class Solution:
    def twoSum(self, array, targetvalue) -> list[list[int]]:
        if targetvalue is None:
            return []
        if array is None:
            return []
        array.sort()
        results = []
        l, r = 0, len(array) - 1
        while l < r:
            while l > 0 and array[l] == array[l - 1]:
                l += 1
            summation = array[l] + array[r]
            if summation < targetvalue:
                l += 1
            elif summation > targetvalue:
                r -= 1
            else:
                results.append([array[l], array[r]])
                l += 1
                while array[l] == array[l - 1] and l < r:
                    l += 1
        return results


arrvalue = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
solution1 = Solution()
print(solution1.twoSum(array=arrvalue, targetvalue=10))
