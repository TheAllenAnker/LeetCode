# Author: Allen Anker
# Created by Allen Anker on 23/09/2018
"""
Given an array nums of n integers where n > 1,
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity?
(The output array does not count as extra space for the purpose of space complexity analysis.)
"""


class Solution:
    def product_except_self(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # with division, pretty easy
        '''
        product_of_all = 1
        for num in nums:
            product_of_all *= num
        return [int(product_of_all / nums[i]) for i in range(len(nums))]
        '''
        # without division and constant space
        res = [1, ]
        for i in range(1, len(nums)):
            res.append(nums[i - 1] * res[i - 1])
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * right
            right *= nums[i]
        return res


solution = Solution()
nums = [1, 2, 3, 4]
print(solution.product_except_self(nums))
