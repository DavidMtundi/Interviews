# Maximum Sub Array
# finding a sub array in an array that has the maximum sum
arr1 = [-2, 1, 3, 4, -1, 2, 1, -5, 4]


class Solution(object):
    def findMaxSubArray(array):
        count = 0
        startindex = 0
        maxsum = 0
        lastindex = 0
        sum = 0
        for val in array:
            sum += val
            if maxsum < sum:

                if array[startindex] < 0:
                    sum += -array[startindex]
                    startindex = startindex + 1
                lastindex = count
                maxsum = sum
                count += 1

            else:
                count += 1
        print(maxsum)

        return array[startindex:lastindex+1]
    # return resultfound


print(Solution.findMaxSubArray(arr1))
