# Author: Allen Anker
# Created by Allen Anker on 26/06/2018


"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:
The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


class Solution:
    def add_strings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # reverse the num strings
        num1 = num1[::-1]
        num2 = num2[::-1]
        leng1 = len(num1)
        leng2 = len(num2)
        res = ''
        i = 0
        addition = 0
        while i < leng1 or i < leng2:
            sum = (int(num2[i]) if i < leng2 else 0) + (int(num1[i]) if i < leng1 else 0) + addition
            addition = 0
            if sum > 9:
                addition = 1
                sum -= 10
            res += str(sum)
            i += 1

        if addition != 0: res += '1'

        return res[::-1]


solution = Solution()
print(solution.add_strings('1000', '9'))


