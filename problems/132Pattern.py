# Author: Allen Anker
# Created by Allen Anker on 31/05/2018


'''
Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak
 such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input
  and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.
'''


class Solution:
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        for i in range(0, length):
            for j in range(length-1, i, -1):
                if nums[j] > nums[i]:
                    for k in range(i+1, j):
                        if nums[k] > nums[j]:
                            return True

        return False


solution = Solution()
nums = [-1, 3, 2, 0]
print(solution.find132pattern(nums))