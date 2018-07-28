# Author: Allen Anker
# Created by Allen Anker on 27/07/2018
"""
You are given a string, s, and a list of words, words, that are all of the same length.
Find all starting indices of substring(s) in s that is a concatenation of each word in words
exactly once and without any intervening characters.
"""
class Solution:
    def find_substr(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[str]
        """
        if not s or not words:
            return
        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        n = len(words)
        w_l = len(words[0]) # each word's length
        res = []
        # each substring should have the length of n * w_l (each word has the same length)
        # and the substring may start at any position of the first word in s
        for k in range(w_l):
            left = k
            subd = {}
            count = 0
            for j in range(k, len(s) - w_l + 1, w_l):
                tword = s[j:j + w_l]
                # valid word
                if tword in word_count:
                    if tword in subd:
                        subd[tword] += 1
                    else:
                        subd[tword] = 1
                    count += 1
                    # move the window until the last tword is removed
                    while subd[tword] > word_count[tword]:
                        subd[s[left:left + w_l]] -= 1
                        left += w_l
                        count -= 1
                    if count == len(words):
                        res.append(left)
                # not valid
                else:
                    left = j + w_l
                    subd = {}
                    count = 0
        return res


solution = Solution()
s = 'barfoothefoobarman'
words = ['foo', 'bar']
print(solution.find_substr(s, words))