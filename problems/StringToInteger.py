#Author: Allen Anker
#Created by Fenyr_Allen on 20/05/2018

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        result = ''
        j = 0
        for i in range(0, len(str)):
            if str[i] == ' ':
                continue
            elif str[i].isnumeric():
                result = self.extractNum(i-1, str)

                break
            elif str[i] == '+':
                result = self.extractNum(i, str)

                break
            elif str[i] == '-':
                if len(str)-1 > i and str[i+1].isnumeric():
                    result += '-'
                    result += self.extractNum(i, str)

                break
            else:
                break

        if len(result) == 0:
            result += '0'
        num = int(result)
        num = min(num, 2**31-1)
        num = max(num, -(2**31))

        return num


    def extractNum(self, i, str):
        result = ''
        for j in range(i + 1, len(str)):
            if str[j].isnumeric():
                result += str[j]
            else:
                break

        return result


solution = Solution()
num = solution.myAtoi('-')
print(num)