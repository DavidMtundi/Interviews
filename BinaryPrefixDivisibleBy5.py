# given an array
# take a substring of the array
# reverse it
# make a binary substring till to a given index
# then convert the binary to a decimal
# return the bool of decimal%5 ==0

class Solution(object):
    count = 0

    def reverseArray(arr):
        return arr[::-1]

    def returnDecimalValue(val, index):
        return val * (2 ** index)

    def returnDecimalConverted(arr, index):
        # the first step is to reverse the array
        #print(newarray)

        # loop through the array and get the results
        result = 0
        count = 0
        for element in arr:
            result += Solution.returnDecimalValue(val=element, index=count)
            count += 1
        return result

    def isDivisibleBy5(val):
        if val == 0:
            print(val)
            return True
        return val % 5 == 0

    def mainFunction(arrv):
        count = 0
        boolarra = arrv
        arrv = Solution.reverseArray(arrv)

        for element in arrv:
            if element ==0:
                boolarra[count]=True
            else:
                boolarra[count] = Solution.isDivisibleBy5(
                    val=Solution.returnDecimalConverted(arr=arrv[:count+1], index=count))
            count += 1
        return boolarra[::-1]


arr = [0, 1, 1]
print(Solution.mainFunction(arrv=arr))
