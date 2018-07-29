# Author: Allen Anker
# Created by Allen Anker on 28/07/2018
"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


class Solution:
    def next_permutation(self, nums):
        """
        :type nums: List[int]
        :rtype None, the list nums is changed in-place to form the next permutation
        """
        if len(nums) > 1:
            l, r = len(nums) - 2, len(nums) - 1
            while l != -1 and nums[l] >= nums[l + 1]:
                l -= 1
            if l != -1:
                while nums[r] <= nums[l] and r > l:
                    r -= 1
                nums[l], nums[r] = nums[r], nums[l]
                self.reverse(nums, l + 1)
            else:
                self.reverse(nums, 0)

    def reverse(self, nums, start):
        l, r = start, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


solution = Solution()
nums = [3, 2, 1]
solution.next_permutation(nums)
print(nums)