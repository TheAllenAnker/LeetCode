# Author: Allen Anker
# Created by Allen Anker on 23/06/2018


"""
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l)
 there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500.
 All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.
"""
import collections


class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        # A Counter is a dict subclass for counting hashable objects.
        #  It is an unordered collection where elements are stored as dictionary keys
        #  and their counts are stored as dictionary values. (they return a zero count for missing items)
        AB = collections.Counter(a + b for a in A for b in B)
        # the count of (-c-d)
        return sum(AB[-c - d] for c in C for d in D)


solution = Solution()
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
print(solution.fourSumCount(A, B, C, D))