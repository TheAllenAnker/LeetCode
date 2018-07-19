# Author: Allen Anker
# Created by Allen Anker on 19/07/2018


"""
Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

2 (abc), 3 (def), 4 (ghi), 5 (jkl), 6 (mno), 7 (pqrs), 8 (tuv), 9 (wxyz).
"""


class Solution:
    def letter_combinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
                   '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        result = list(mapping[digits[0]])
        digits = digits[1:]
        for digit in digits:
            # result's elements are getting longer in each iteration
            result = [seq + c for seq in result for c in mapping[digit]]

        return result


solution = Solution()
digits = '23'
print(solution.letter_combinations(digits))
