# Author: Allen Anker
# Created by Allen Anker on 09/09/2018
"""
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Note:

If there exists a solution, it is guaranteed to be unique.
Both input arrays are non-empty and have the same length.
Each element in the input arrays is a non-negative integer.
"""


class Solution:
    def can_complete_circuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # A TLE solution first, I knew it wouldn't be so easy.
        '''
        gas_tank = 0
        for i in range(len(gas)):
            checked = False
            for j in range(len(gas) + 1):
                curr = (i + j) % len(gas)
                if curr == i and checked:
                    return i
                gas_tank += gas[curr]
                gas_tank -= cost[curr]
                checked = True
                if gas_tank < 0:
                    gas_tank = 0
                    break
        return -1
        '''
        diffs = [gas[i] - cost[i] for i in range(len(gas))]
        if sum(diffs) < 0:
            return -1
        i = 0
        while i < len(gas):
            if diffs[i] < 0:
                i += 1
                continue
            checked = False
            extra = diffs[i]
            if extra > 0 and len(gas) == 1:
                return 0
            for j in range(1, len(gas) + 1):
                curr = (i + j) % len(gas)
                if curr == i and checked:
                    return i
                extra += diffs[curr]
                checked = True
                if extra < 0:
                    i = curr
                    break
            i += 1
        return -1


solution = Solution()
gas, cost = [5], [4]
print(solution.can_complete_circuit(gas, cost))
