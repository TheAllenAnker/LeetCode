# Author: Allen Anker
# Created by Allen Anker on 08/07/2018


"""
We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)".
Then, we removed all commas, decimal points, and spaces, and ended up with the string S.
Return a list of strings representing all possibilities for what our original coordinates could have been.

Our original representation never had extraneous zeroes,
so we never started with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01",
or any other number that can be represented with less digits.
Also, a decimal point within a number never occurs without at least one digit occurring before it,
so we never started with numbers like ".1".

The final answer list can be returned in any order.
Also note that all coordinates in the final answer have exactly one space between them (occurring after the comma.)

Note:
4 <= S.length <= 12.
S[0] = "(", S[S.length - 1] = ")", and the other elements in S are digits.
"""


import itertools


class Solution:
    def ambiguous_coordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        # my idea: find all combinations of the character sequence (adds comma)
        # then insert decimal into those combinations
        res = []
        S = S[1:len(S) - 1]
        for i in range(1, len(S)):
            coor1, coor2 = int(S[:i]), int(S[i:])
            current = [str((coor1, coor2))]
            for j in range(0, len(str(coor1))):
                new_coor1 = str(coor1)[:j+1] + '.' + str(coor1)[j+1:]
                if (len(str(float(new_coor1))) == len(new_coor1) or new_coor1[-1] == '.') \
                        or (int(str(new_coor1)[:j+1]) != float(new_coor1) and new_coor1[-1] == '0'):
                    new_coor1 = int(float(new_coor1)) if new_coor1[-1] == '.' else float(new_coor1)
                    for k in range(0, len(str(coor2))):
                        new_coor2 = str(coor2)[:k+1] + '.' + str(coor2)[k+1:]
                        if (len(str(float(new_coor2))) == len(new_coor2) or new_coor2[-1] == '.') \
                                or (int(str(new_coor2)[:k + 1]) != float(new_coor2) and new_coor2[-1] == '0'):
                            new_coor2 = int(float(new_coor2)) if new_coor2[-1] == '.' else float(new_coor2)
                            current.append((new_coor1, new_coor2))

            for item in current:
                if item not in res:
                    res.append(str(item))

        return res


solution = Solution()
print(solution.ambiguous_coordinates('(123)'))