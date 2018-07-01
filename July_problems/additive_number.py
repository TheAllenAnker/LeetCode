# Author: Allen Anker
# Created by Allen Anker on 01/07/2018


"""
Additive number is a string whose digits can form additive sequence.
A valid additive sequence should contain at least three numbers. (Numbers do not need to be one digit)
Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.
Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.
"""
import itertools


class Solution:
    def is_additive_number(self, num):
        """
        :type num: str
        :rtype: bool
        """
        length = len(num)
        # Return r length subsequences of elements from the input iterable (range(1, length))
        for i, j in itertools.combinations(range(1, length), 2):
            if num[0] == '0': i = 1
            a, b = num[:i], num[i:j]  # two numbers on the front
            if b != str(int(b)):  # check if there are leading zero
                continue
            while j < length:
                c = str(int(a) + int(b))
                if not num.startswith(c, j):  # check if there are corresponding third number
                    break
                j += len(c)  # if there is corresponding third number, move forward and continue
                a, b = b, c  # continue checking the remaining numbers
            if j == length:  # if number sequence is iterated to the end, else, try a different combination
                return True
        return False
