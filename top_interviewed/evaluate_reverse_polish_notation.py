# Author: Allen Anker
# Created by Allen Anker on 12/09/2018
"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid.
That means the expression would always evaluate to a result and there won't be any divide by zero operation.
"""


class Solution:
    def eval_RPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operands = []
        for i in range(len(tokens)):
            if tokens[i].isdigit() or tokens[i][1:].isdigit():
                operands.append(int(tokens[i]))
            else:
                a = operands.pop()
                b = operands.pop()
                c = 0
                if tokens[i] == '+':
                    c = a + b
                elif tokens[i] == '-':
                    c = b - a
                elif tokens[i] == '*':
                    c = a * b
                else:
                    c = int(b / a)
                operands.append(c)
        return operands.pop()


solution = Solution()
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(solution.eval_RPN(tokens))
