# Author: Allen Anker
# Created by Allen Anker on 10/09/2018
"""
A linked list is given such that each node contains an additional random pointer
which could point to any node in the list or null.

Return a deep copy of the list.
"""
import collections


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    def copy_random_list(self, head):
        """
        Deep copy a linked list with random pointer.
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # My two cents
        '''
        randoms = defaultdict()
        res = RandomListNode(head.label)
        res_copy = res
        dummy = head
        while dummy:
            res.next = RandomListNode(dummy.label)
            if dummy.random:
                randoms[res.next] = dummy.random
            if dummy in randoms.values():
                for key in randoms.keys():
                    if randoms.get(key) == dummy:
                        key.random = res.next
            dummy = dummy.next
            res = res.next
        return res_copy.next
        '''
        # A better way to handle uncreated link nodes
        dic = collections.defaultdict(lambda: RandomListNode(0))
        dic[None] = None
        n = head
        while n:
            dic[n].label = n.label
            dic[n].next = dic[n.next]
            dic[n].random = dic[n.random]
            n = n.next
        return dic[head]
