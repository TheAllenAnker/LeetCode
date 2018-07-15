# Author: Allen Anker
# Created by Allen Anker on 15/07/2018


"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Follow up:
Could you solve it without converting the integer to a string?
"""


class Solution:
    def is_palindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        res, p = 0, x
        while p:
            res = res * 10 + p % 10
            p //= 10

        return True if res == x else False


solution = Solution()
x = 1221
print(solution.is_palindrome(x))
