# Author: Allen Anker
# Created by Allen Anker on 19/07/2018


"""
There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
"""


class Solution:
    def int_to_roman(self, num):
        """
        :type num int
        :rtype: str
        """
        res = ''
        res += 'M' * (num // 1000)
        num %= 1000
        res += 'CM' * (num // 900)
        num %= 900
        res += 'D' * (num // 500)
        num %= 500
        res += 'CD' * (num // 400)
        num %= 400
        res += 'C' * (num // 100)
        num %= 100
        res += 'XC' * (num // 90)
        num %= 90
        res += 'L' * (num // 50)
        num %= 50
        res += 'XL' * (num // 40)
        num %= 40
        res += 'X' * (num // 10)
        num %= 10
        res += 'IX' * (num // 9)
        num %= 9
        res += 'V' * (num // 5)
        num %= 5
        res += 'IV' * (num // 4)
        num %= 4
        res += 'I' * (num // 1)
        num %= 1
        return res


solution = Solution()
num = 58
print(solution.int_to_roman(num))
