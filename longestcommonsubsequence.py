"""Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common
subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted
without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.



Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.


Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
"""


class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        f, l = len(text1), len(text2)
        arrvalue = [[0 for i in range(l + 1)] for j in range(f + 1)]
        print(arrvalue)

        for i in range(f + 1):
            for j in range(l + 1):
                if i == 0 or j == 0:
                    arrvalue[i][j] = 0
                elif text1[i - 1] == text2[j - 1]:
                    arrvalue[i][j] = 1 + arrvalue[i - 1][j - 1]
                else:
                    arrvalue[i][j] = max(arrvalue[i][j - 1], arrvalue[i - 1][j])
        return arrvalue[f][l]


