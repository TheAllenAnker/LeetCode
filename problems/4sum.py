# Author: Allen Anker
# Created by Allen Anker on 21/06/2018


"""
Given an array nums of n integers and an integer target,
 are there elements a, b, c, and d in nums such that a + b + c + d = target?
  Find all unique quadruplets in the array which gives the sum of target.

Note:
The solution set must not contain duplicate quadruplets.
"""


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def nSum(nums, target, n, result, results):
            # list nums has been sorted
            if len(nums) < n or n < 2 or n * nums[0] > target or n * nums[-1] < target:
                return []
            if n == 2:
                begin, end = 0, len(nums) - 1
                while begin < end:
                    sums = nums[begin] + nums[end]
                    if sums < target:
                        begin += 1
                    elif sums > target:
                        end -= 1
                    else:
                        plet = [nums[begin], nums[end]]
                        results.append(result + plet)
                        # remove duplicates by removing the duplicated numbers in both sides
                        while begin < end and nums[begin] == plet[0]: begin += 1
                        while begin < end and nums[end] == plet[1]: end -= 1
            else:
                # there is (n-1) numbers left to search to finally get the target
                # so the search range of the current number is limited to (0, len(nums)-(n-1))
                for i in range(len(nums) - n + 1):
                    # if the current number is too small or equivalent to the last one, continue
                    if (i > 0 and nums[i] == nums[i - 1]) or (nums[i] + (n - 1) * nums[len(nums) - 1] < target):
                        continue
                    # if the sum of smallest ones are larger, no need to continue
                    # because n * nums[i] is the smallest sum
                    if n * nums[i] > target:
                        break
                    # if the following n numbers sum is equal to the target
                    # if this condition holds, the sum of with the numbers later
                    #  in the list will be larger than the target
                    if n * nums[i] == target and i + n - 1 < len(nums) and nums[i + n - 1] == nums[i]:
                        plet = [nums[i]] * n
                        results.append(result + plet)
                        break
                    # subtract a number in each recursion (problem nSum turns to problem (n-1)Sum)
                    # produce a new target (target-nums[i])
                    # building the n-plets (result+[nums[i]]) in each recursion
                    nSum(nums[i + 1:], target - nums[i], n - 1, result + [nums[i]], results)

        results = []
        nums.sort()
        nSum(nums, target, 4, [], results)
        return results


solution = Solution()
nums = [1, 0, -1, 0, -2, 2]
target = 0
print(solution.fourSum(nums, target))