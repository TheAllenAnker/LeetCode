# Author: Allen Anker
# Created by Allen Anker on 20/08/2018
"""
Given an array of strings, group anagrams together.
"""
from collections import defaultdict


class Solution:
    def group_anagrams(self, strs):
        """
        If two words have the same numbers of each character, then they are anagrams of each other.
        Iterate through the list, add new list when a new word without anagrams founded is founded
        :param strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return
        sorted_strs = [''] * len(strs)
        for i in range(len(strs)):
            sorted_strs[i] = ''.join(sorted(strs[i]))
        result = [[strs[0]],]
        seen = defaultdict()
        seen[sorted_strs[0]] = 0
        size = 1
        for i in range(1, len(sorted_strs)):
            if sorted_strs[i] not in seen:
                result.append([])
                seen[sorted_strs[i]] = size
                size += 1
            result[seen.get(sorted_strs[i])].append(strs[i])
        return result


solution = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(solution.group_anagrams(strs))
