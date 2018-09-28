# Author: Allen Anker
# Created by Allen Anker on 28/09/2018
"""
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.
"""


class Solution:
    def coin_change(self, coins, amount):
        """
        Dynamic programming
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [float('inf')] * amount
        for i in range(1, amount + 1):
            # to get value i, we need dp[i-c] + 1(this one coin's denomination is c) coins at least
            dp[i] = min([dp[i - c] if i >= c else float('inf') for c in coins]) + 1

        return [dp[amount], -1][dp[amount] == float('inf')]


solution = Solution()
coins = [1, 2, 5]
amount = 11
print(solution.coin_change(coins, amount))
