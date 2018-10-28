# Author: Allen Anker
# Created by Allen Anker on 28/10/2018
"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
"""


class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return a if b == 0 else self.getSum(a ^ b, (a & b) << 1)


solution = Solution()
print(solution.getSum(12, 3))
