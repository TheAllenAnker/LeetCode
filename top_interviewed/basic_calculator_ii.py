# Author: Allen Anker
# Created by Allen Anker on 20/09/2018
"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces.
The integer division should truncate toward zero.
"""
import re


class Solution:
    def calculate(self, s):
        """
        Note that the number might be two-digit number
        :type s: str
        :rtype: int
        """
        # this does not work
        '''
        operands = []
        operators = []
        priorities = {'+': 0, '-': 0, '*': 1, '/': 1}
        i = 0
        pre_operator = ''
        while i < len(s):
            if s[i].isdigit():
                start = i
                if i < len(s) - 1 and s[i + 1].isdigit():
                    while i < len(s) and s[i].isdigit():
                        i += 1
                    operands.append(s[start:i])
                    continue
                else:
                    operands.append(s[i])

            elif s[i] != ' ':
                if operators:
                    if priorities[operators[-1]] > priorities[s[i]]:
                        a, b = int(operands.pop()), int(operands.pop())
                        op = operators.pop()
                        if op == '+' and operators[-1] == '-':
                            a = -a
                        operands.append(self.arith_res(b, a, op))

                operators.append(s[i])
            i += 1
        while operators:
            a, b = int(operands.pop()), int(operands.pop())
            op = operators.pop()
            if op == '+' and operators and operators[-1] == '-':
                a = -a
            operands.append(self.arith_res(b, a, op))
        return operands[-1]

    # calculate the result of (a op b)
    def arith_res(self, a, b, op):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        else:
            return a // b
    '''
        if not s:
            return '0'
        stack, num, sign = [], 0, '+'
        for i in range(len(s)):
            if s[i].isdigit():
                # number that is more than one digit
                num = num * 10 + ord(s[i]) - ord('0')
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s) - 1:
                if sign == '-':
                    stack.append(-num)
                elif sign == '+':
                    stack.append(num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    tmp = stack.pop()
                    if tmp // num < 0 and tmp % num != 0:
                        stack.append(tmp // num + 1)
                    else:
                        stack.append(tmp // num)
                sign = s[i]
                num = 0
        return sum(stack)


solution = Solution()
s = '3+2*2'
print(solution.calculate('1*2-3/4+5*6-7*8+9/10'))
