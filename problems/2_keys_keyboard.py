# Author: Allen Anker
# Created by Allen Anker on 07/06/2018


'''
Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.
'''


# based on the solution
# provided by LeetCode

# key point: Let C denote copying and P denote pasting.
#  Then for example, in the sequence of moves CPPCPPPPCP,
#  the groups would be [CPP][CPPPP][CP].
class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        steps = 0
        d = 2
        while n > 1:
            while n % d == 0:
                steps += d
                n /= d
            d += 1

        return steps
