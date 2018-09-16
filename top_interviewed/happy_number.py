# Author: Allen Anker
# Created by Allen Anker on 16/09/2018
"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer,
replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.
"""


class Solution:
    def is_happy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # solution 1
        '''
        if n <= 0:
            return False
        seen = [n]
        while True:
            n = sum([int(i) ** 2 for i in str(n)])
            if n == 1:
                return True
            elif n in seen:
                return False
            seen.append(n)
        '''
        # solution 2
        r1 = self.digits_square(n)
        r2 = self.digits_square(r1)
        while r1 != 1:
            if r1 == r2:
                return False
            else:
                r1 = self.digits_square(r1)
                r2 = self.digits_square(self.digits_square(r2))
        return True

    def digits_square(self, n):
        res = 0
        while n:
            res += (n % 10) ** 2
            n //= 10
        return res


solution = Solution()
print(solution.is_happy(19))
