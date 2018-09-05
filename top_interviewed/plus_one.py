# Author: Allen Anker
# Created by Allen Anker on 05/09/2018
"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list,
and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
"""


class Solution:
    def plus_one(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        increment = 1
        for i in range(len(digits) - 1, -1, -1):
            curr = digits[i]
            if curr + increment == 10:
                digits[i] = 0
                increment = 1
                if i == 0:
                    digits = [1] + digits
            else:
                digits[i] = curr + increment
                increment = 0
        return digits

        #
        # # a faster solution?
        # if len(digits) == 0:
        #    digits = [1]
        #
        # elif digits[-1] == 9:
        #         digits = self.plusOne(digits[:-1])
        #         digits.extend([0])
        #
        # else:
        #      digits[-1] += 1
        #
        # return digits
        #


solution = Solution()
digits = [0]
print(solution.plus_one(digits))
