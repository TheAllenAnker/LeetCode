# Author: Allen Anker
# Created by Allen Anker on 25/10/2018
"""
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.
"""


class Solution:
    def increasing_triplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                # the current number is larger than the first and the second number
                return True

        return False


solution = Solution()
nums = [1, 2, 3, 4, 5]
print(solution.increasing_triplet(nums))
