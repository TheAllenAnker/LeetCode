# Author: Allen Anker
# Created by Allen Anker on 16/09/2018
"""
Count the number of prime numbers less than a non-negative number, n.
"""


class Solution:
    def count_primes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        # the marking process actually goes until i * i
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                # with increment i, mark each number met in the process
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        # the numbers of number remain unmarked
        return sum(primes)


a = [1, 2, 3, 4, 5]
a[::2] = [1, 1, 1]
print(a)
