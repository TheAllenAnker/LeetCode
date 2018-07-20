# Author: Allen Anker
# Created by Allen Anker on 20/07/2018


"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""


class Solution:
    def longest_common_prefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) <= 1:
            return strs[0] if len(strs) == 1 else ''
        s1, s2 = strs[0], strs[1]
        longest = self.__longest_prefix(s1, s2)
        i = 2
        while i < len(strs):
            if strs[i].startswith(longest):
                i += 1
                continue
            else:
                longest = longest[:len(longest) - 1]

        return longest

    def __longest_prefix(self, s1, s2):
        """
        :param s1: string 1
        :param s2: string 2
        :rtype: str
        """
        i = 0
        res = ''
        while i < len(s1) and i < len(s2):
            if s1[i] == s2[i]:
                res += s1[i]
                i += 1
            else:
                break
        return res


solution = Solution()
strs = ["dog","racecar","car"]
print(solution.longest_common_prefix(strs))
