"""
Implement atoi which converts a string to an integer
the function first discards as many whitespace characters as necessary
until the first non-whitespace character is found.
then starting fom this character, takes an optional initial plus or minus sign
followed by as many numerical digits as possible and interprets them as a numerical value
the string can contain additional characters after those that form the integral number
which are ignored and have no efefect on the behaviour of this function
if the first sequence of non-whitespace chareactesr sin str is not a valid integral
number, or if no such sequence exists becasue either str is empty or it contains only whitespace
characters, no conversion is performed
if no valid conversion could be performed, a zero value is returned

note:
    only the space character ' ' is considered as whitespace character
    assume we are dealing with an environment which could only store integers within the bit signed integer range
    if the numerical value is out of the range of representable values,
    INT_MAX(2^31-1) or INT_MIN(-2^31) is returned

for example:
    "42" -> returns a digit 42
    " -42" -> returns a digit -42
    "4193 with words" -> returns a digit 4193
    "words and 987" -> returns 0
"""

class Solution:
    def stringToInteger(self,stringvalue):

        return stringvalue

