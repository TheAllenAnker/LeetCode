# Author: Allen Anker
# Created by Allen Anker on 28/08/2018
"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
"""


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Merge sorted array num2 into sorted array num1
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        """
        curr = m + n - 1
        i, j = m - 1, n - 1
        while curr >= 0:
            if (j < 0 or nums1[i] > nums2[j]) and i >= 0:
                nums1[curr] = nums1[i]
                i -= 1
            else:
                nums1[curr] = nums2[j]
                j -= 1
            curr -= 1


solution = Solution()
num1 = [2, 0]
num2 = [1]
solution.merge(num1, 1, num2, 1)
print(num1)
