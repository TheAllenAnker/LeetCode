# Author: Allen Anker
# Created by Fenyr_Allen on 20/05/2018


class Solution(object):
    def my_atoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str.strip()) == 0:
            return 0
        ls = list(str.strip())

        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-', '+']:
            del ls[0]
        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit():
            ret = ret * 10 + ord(ls[i]) - ord('0')
            i += 1

        return max(-2 ** 31, min(sign * ret, 2 ** 31 - 1))


solution = Solution()
num = solution.my_atoi('42')
print(num)
