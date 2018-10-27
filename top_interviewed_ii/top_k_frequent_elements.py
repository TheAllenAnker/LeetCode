# Author: Allen Anker
# Created by Allen Anker on 27/10/2018
"""
Given a non-empty array of integers, return the k most frequent elements.

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums, k):
        """
        Bucket sort works find when n is small, we n gets really great, use heap sort would be better.
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_buckets = []
        for i in range(len(nums) + 1):
            freq_buckets.append(set())
        num_freq_dict = defaultdict(int)
        for num in nums:
            if num_freq_dict[num]:
                num_freq_dict[num] += 1
            else:
                num_freq_dict[num] = 1

        res = []
        for num in nums:
            freq_buckets[num_freq_dict[num]].add(num)

        for i in range(len(freq_buckets) - 1, -1, -1):
            if freq_buckets[i] != 0:
                res += freq_buckets[i]
            if len(res) >= k:
                break

        return res[:k]


solution = Solution()
nums = [3]
k = 1
print(solution.topKFrequent(nums, k))
a = []
for i in range(5):
    a.append(list())
a[0].append(1)
a[0].append(2)
a[0] += [1, 2, 3]
print(a)
