# Author: Allen Anker
# Created by Allen Anker on 11/07/2018


"""
A zero-indexed array A of length N contains all integers from 0 to N-1. (all elements are distinct)
Find and return the longest length of set S, where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below.

Suppose the first element in S starts with the selection of element A[i] of index = i,
the next element in S should be A[A[i]], and then A[A[A[i]]]…
By that analogy, we stop adding right before a duplicate element occurs in S.
"""


class Solution:
    def array_nesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # all numbers are not visited at the beginning
        visited = [0] * len(nums)
        result = 0
        for i in range(len(nums)):
            start, count = nums[i], 0
            while visited[i] == 0:
                visited[start] = 1
                count += 1
                if start >= len(nums) or (start == nums[i] and count != 1): break
                else: start = nums[start]
            visited[i] = 1
            result = max(result, count)

        return result


solution = Solution()
nums = [5,4,0,3,1,6,2]
print(solution.array_nesting(nums))