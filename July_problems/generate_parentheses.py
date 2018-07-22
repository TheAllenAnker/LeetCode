# Author: Allen Anker
# Created by Allen Anker on 22/07/2018
"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""


class Solution:
    def generate_parenthesis(self, n):
        """
        :param n: pairs of parentheses
        :type n: int
        :rtype: List[str]
        """
        # solution one
        '''
        def generate(s):
            if len(s) == 2 * n:
                if valid(s):
                    res.append(s)
            elif not count_additional(s):
                return
            else:
                s += '('
                generate(s)
                s = s[:-1]
                s += ')'
                generate(s)
                s = s[:-1]

        def valid(s):
            count = 0
            for i in s:
                if i == '(':
                    count += 1
                else:
                    count -= 1
                if count < 0:
                    return False
            return True if count == 0 else False

        def count_additional(s):
            count = 0
            for i in s:
                if i == '(':
                    count += 1
                else:
                    count -= 1
                if count < 0:
                    return False
            return True

        res = []
        generate('')
        return res
        '''
        # solution two (better)
        def dfs(left, right, res, s):
            if right < left:
                return
            if not left and not right:
                res.append(s)
            if left:
                dfs(left - 1, right, res, s + '(')
            if right:
                dfs(left, right - 1, res, s + ')')
            return res

        return dfs(n, n, [], '')


solution = Solution()
pair = 4
print(solution.generate_parenthesis(pair))