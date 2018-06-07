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
        if length < 3:
            return False
        min_left = [0] * length
        # find the smallest number on the left side of nums[i]
        for i in range(1, length):
            min_left[i] = min(min_left[i-1], nums[i])
        k = length
        for j in range(length - 1, -1, -1):
            if nums[j] > min_left[j]:
                while k < length and nums[k] <= min_left[j]: # the iteration
                    k += 1
                if k < length and nums[k] < nums[j]:
                    return True
                # the num visited before is not potential anymore?
                # num[j] must be larger than min_left[i], so the iteration will stop when reaching old k next time?
                k -= 1
                nums[k] = nums[j]

        return False


solution = Solution()
nums = [1, 3, 2]
print(solution.find132pattern(nums))