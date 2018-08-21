# Author: Allen Anker
# Created by Allen Anker on 21/08/2018
"""
Implement pow(x, n), which calculates x raised to the power n (xn).
"""


class Solution:
    def my_pow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        '''
        if x == 0:
            return 0.0
        result = 1.0
        x = 1 / x if n < 0 else x
        n = -n if n < 0 else n
        for i in range(n):
            result *= x
        return result
        '''

        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow


solution = Solution()
x = 2
n = -2
print(solution.my_pow(x, n))
