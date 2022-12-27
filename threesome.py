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

def solution1(arr):
    resultarray = []
    arr = arr.sort()

    # -4,-1,-1,0,1,2
    for i, a in enumerate(arr):
        if i > 0 and a == arr[i - 1]:
            continue
        l, r = i + 1, len(arr) - 1
        while l < r:
            threesum = a + arr[l] + arr[r]
            if threesum > 0:
                r -= 0
            elif threesum < 0:
                l += 1
            else:
                resultarray.append([a, arr[l], arr[r]])
    return resultarray


print(solution1([-1, 0, 1, 2, -1, -4]))
