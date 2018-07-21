# Author: Allen Anker
# Created by Allen Anker on 21/07/2018
"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.
"""


class Solution:
    def valid_parentheses(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s:
            p_list = []
            for i in range(len(s)):
                if s[i] == ')':
                    if not p_list or p_list.pop() != '(':
                        return False
                elif s[i] == '}':
                    if not p_list or p_list.pop() != '{':
                        return False
                elif s[i] == ']':
                    if not p_list or p_list.pop() != '[':
                        return False
                else:
                    p_list.append(s[i])
            return True if not p_list else False
        return True


s = '([)]'
solution = Solution()
print(solution.valid_parentheses(s))