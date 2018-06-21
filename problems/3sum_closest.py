# Author: Allen Anker
# Created by Allen Anker on 20/06/2018


"""
Given an array nums of n integers and an integer target,
 find three integers in nums such that the sum is closest to target.
  Return the sum of the three integers.
  You may assume that each input would have exactly one solution.
"""


class Solution:
    def three_sum_closest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        closest = []

        for i, num in enumerate(nums[0:-2]):
            l, r = i + 1, length - 1

            # it would only be smaller
            # if it is smaller than the target
            # even added with the largest two
            if num + nums[r] + nums[r - 1] < target:
                closest.append(num + nums[r] + nums[r - 1])
            # similarly, the difference would only be larger if
            # this condition is satisfied
            elif num + nums[l] + nums[l + 1] > target:
                closest.append(num + nums[l] + nums[l + 1])
            else:
                while l < r:
                    closest.append(num + nums[l] + nums[r])
                    # narrows the search range depends on different conditions
                    if num + nums[l] + nums[r] < target:
                        l += 1
                    elif num + nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        return target

        closest.sort(key=lambda x: abs(x - target))
        return closest[0]


solution = Solution()
nums = [-1, 2, 1, -4]
print(solution.three_sum_closest(nums, 1))
print(nums)

