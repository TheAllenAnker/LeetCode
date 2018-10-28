# Author: Allen Anker
# Created by Allen Anker on 28/10/2018
"""
Given two arrays, write a function to compute their intersection.

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
"""
from collections import Counter


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # each number's occurrence in two arrays
        c1, c2 = Counter(nums1), Counter(nums2)
        return sum([[num] * min(c1[num], c2[num]) for num in c1 & c2], [])


solution = Solution()
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(solution.intersect(nums1, nums2))
