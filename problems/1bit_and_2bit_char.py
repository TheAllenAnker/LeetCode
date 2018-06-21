# Author: Allen Anker
# Created by Allen Anker on 21/06/2018


"""
We have two special characters. The first character can be represented by one bit 0.
 The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits.
Return whether the last character must be a one-bit character or not.
The given string will always end with a zero.
"""


class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        length = len(bits)
        if length == 1: return True
        i = 0
        while(i < length):
            if bits[i] == 1:
                i+=2
                if i >= length: return False
            else:
                i+=1
                if i == length: return True

        return True


solution = Solution()
bits = [1, 1, 1, 0]
print(solution.isOneBitCharacter(bits))





