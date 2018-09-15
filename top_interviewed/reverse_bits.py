# Author: Allen Anker
# Created by Allen Anker on 15/09/2018
"""
Reverse bits of a given 32 bits unsigned integer.

Follow up:
If this function is called many times, how would you optimize it?
"""


class Solution:
    def reverse_bits(self, n):
        """
        :type n: int
        :rtype: int
        """
        bin_res = str(bin(n))[2:][::-1]
        trailing_zeroes = '0' * (32 - len(bin_res))
        return int(bin_res + trailing_zeroes, 2)


solution = Solution()
n = 43261596
print(solution.reverse_bits(n))
