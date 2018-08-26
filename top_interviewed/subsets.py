# Author: Allen Anker
# Created by Allen Anker on 24/08/2018
"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.
"""


class Solution:
    def subsets(self, nums):
        """
        Find the subsets of a nums list.
        Find the shortest first, then construct the longer ones with the shorter ones.
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[], ]
        if nums:
            for item in result:
                remains = [i for i in nums if i not in item]
                for num in remains:
                    curr = item + [num]
                    curr.sort()
                    if curr not in result:
                        result.append(curr)
            pass
        return result


solution = Solution()
nums = [1, 2, 3]
print(solution.subsets(nums))
