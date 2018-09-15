# Author: Allen Anker
# Created by Allen Anker on 15/09/2018
"""
Write a function that takes an unsigned integer and
returns the number of '1' bits it has (also known as the Hamming weight).
"""


class Solution:
    def hamming_weight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return str(bin(n))[2:].count('1')

    def hamming_weight2(self, n):
        count = 0
        while n != 0:
            count += 1
            n &= n - 1
        return count


solution = Solution()
print(solution.hamming_weight(7))
print(solution.hamming_weight2(7))
