# Author: Allen Anker
# Created by Allen Anker on 08/09/2018
"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""
from collections import defaultdict


class Solution:
    def longest_consecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest_streak = 0
        # To allow O(1) lookups
        num_set = set(nums)

        for num in num_set:
            # Ensure that the number is not part of a longer streak
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # Build the streak in ascending order
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


solution = Solution()
nums = [100, 4, 200, 1, 3, 2]
print(solution.longest_consecutive(nums))
