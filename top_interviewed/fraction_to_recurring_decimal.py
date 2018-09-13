# Author: Allen Anker
# Created by Allen Anker on 13/09/2018
"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.
"""
from collections import defaultdict


class Solution:
    def fraction_to_decimal(self, numerator, denominator):
        """
        The remainder is the point, once you get the same remainder as before, then the repeating part emerges.
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        quotient, remainder = divmod(abs(numerator), abs(denominator))
        # the sign needs to be handled only once
        sign = '-' if numerator * denominator < 0 else ''
        decimal = [sign + str(quotient)]
        if remainder == 0:
            return ''.join(decimal)

        remainder_dict = defaultdict()
        decimal.append('.')
        while remainder != 0:
            if remainder in remainder_dict:
                # insert '(' before index dict[remainder]
                # where the repeating part starts
                decimal.insert(remainder_dict[remainder], '(')
                decimal.append(')')
                return ''.join(decimal)
            remainder_dict[remainder] = len(decimal)
            quotient, remainder = divmod(remainder * 10, abs(denominator))
            decimal.append(str(quotient))
        return ''.join(decimal)


solution = Solution()
numerator = 1
denominator = 2
print(solution.fraction_to_decimal(numerator, denominator))
