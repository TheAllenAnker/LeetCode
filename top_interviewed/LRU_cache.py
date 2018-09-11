# Author: Allen Anker
# Created by Allen Anker on 11/09/2018
"""
Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity,
it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?
"""
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.dic = OrderedDict()
        self.remain = capacity

    def get(self, key):
        if key not in self.dic:
            return -1
        v = self.dic.pop(key)
        # set key as the newest one
        self.dic[key] = v
        return v

    def put(self, key, value):
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:  # self.dic is full
                self.dic.popitem(last=False)
        self.dic[key] = value


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
param_1 = obj.get(1)
print([obj.put(1, 1), obj.put(2, 2), obj.get(1), obj.put(3, 3), obj.get(2), obj.put(4, 4), obj.get(1), obj.get(3),
       obj.get(4)])
