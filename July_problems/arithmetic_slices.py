# Author: Allen Anker
# Created by Allen Anker on 09/07/2018


"""
A sequence of number is called arithmetic if it consists of at least three elements
and if the difference between any two consecutive elements is the same.

A zero-indexed array A consisting of N numbers is given.
A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.
So each slice has at least 3 numbers.

The function should return the number of arithmetic slices in the array A.
"""


class Solution:
    def number_of_arithmetic_slices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # # the length of list A must be 3 or bigger
        # if len(A) < 3: return 0
        # # find the longest slices first
        # arithmetic_seqs = []
        # start, end, diff = 0, 1, abs(A[1] - A[0])
        # while end < len(A):
        #     if end < len(A) - 1 and abs(A[end + 1] - A[end]) == diff:
        #         end += 1
        #     else:
        #         if end - start > 1:
        #             arithmetic_seqs.append((start, end))
        #
        #         start, end = end, end + 1
        #         if end < len(A): diff = A[end] - A[start]
        #
        # # find shorter slices inside those longest slices
        # actual_sequences = []
        # for start, end in arithmetic_seqs:
        #     if end - start > 2:
        #         for i in range(end - start - 1):
        #             for j in range(i + 2, end - start + 1):
        #                 actual_sequences.append((i, j))
        #     else:
        #         actual_sequences.append((start, end))
        #
        # return len(actual_sequences)

        if len(A) < 3:
            return 0
        # an infinity tail to list for breaking arithmetic sequence for checking until last element
        A.append(float("inf"))
        d, l, n, res = A[1] - A[0], 0, len(A), 0
        for i in range(2, n):
            if d != A[i] - A[i - 1]:
                diff = i - l - 2
                # the length of the slices is bigger than 3, diff = length - 3
                if diff > 0:
                    # the number of arithmetic slices possible in the current sequence
                    # The new arithmetic slices will be a total of (x+1), where x is the the number of arithmetic
                    # slices before adding the new number (added the new number constitutes a arithmetic slice as well)
                    # so the number of slices in a sequence with the length of n will be 1 + 2 + 3 + 4+...+(len(seq)-2)
                    res += diff * (diff + 1) // 2
                d, l = A[i] - A[i - 1], i - 1
        return res


solution = Solution()
A = [1, 2, 3, 4]
print(solution.number_of_arithmetic_slices(A))
