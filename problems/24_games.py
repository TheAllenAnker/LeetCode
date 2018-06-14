# Author: Allen Anker
# Created by Allen Anker on 09/06/2018


'''
You have 4 cards each containing a number from 1 to 9.
 You need to judge whether they could operated
  through *, /, +, -, (, ) to get the value of 24.

  The game rule (may be useful):
   The rules are simple, you must use all four numbers
    and only those four numbers, and they can only be used once each.
'''


from operator import add, sub, mul, truediv


class Solution:
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if not nums: return False
        if len(nums) == 1: return abs(nums[0] - 24) < 1e-6 # considering the effect of truediv


        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    curr_nums = [nums[k] for k in range(len(nums)) if i != k != j] # the smaller list of number
                                                                                    #  after each operation
                    for op in (add, sub, mul, truediv): # sub and truediv are not commute
                        if (op is add or op is mul) and j > i: continue
                        if op is not truediv or nums[j]:
                            curr_nums.append(op(nums[i], nums[j]))
                            if self.judgePoint24(curr_nums): return True
                            curr_nums.pop()
        return False



solution = Solution()
print(solution.judgePoint24([1, 2, 3, 4]))
