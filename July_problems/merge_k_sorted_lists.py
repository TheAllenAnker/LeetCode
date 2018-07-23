# Author: Allen Anker
# Created by Allen Anker on 22/07/2018
"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""
from queue import PriorityQueue


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __lt__(self, other):
        return self.val < other.val


class Solution:
    def merge_k_lists(self, lists):
        """
        :param lists: list or linked list
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # solution 1
        '''
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        head = head_copy = ListNode(0)
        l1 = lists[0]
        for i in range(1, len(lists)):
            l2 = lists[i]
            while l1 and l2:
                if l1.val < l2.val:
                    head_copy.next = l1
                    l1 = l1.next
                else:
                    head_copy.next = l2
                    l2 = l2.next
                head_copy = head_copy.next
            head_copy.next = l1 or l2
            l1, head_copy = head.next, head
        return head.next
        '''
        #solution 2
        head = head_copy = ListNode(0)
        q = PriorityQueue()
        for list in lists:
            if list:
                q.put((list.val, list))
        while not q.empty():
            val, node = q.get()
            head_copy.next = ListNode(val)
            head_copy = head_copy.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next



solution = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
l3 = ListNode(1)
l3.next = ListNode(2)
l3.next.next = ListNode(4)
lists = [l1, l2, l3]
new_head = solution.merge_k_lists(lists)
while new_head:
    print(new_head.val, end='->')
    new_head = new_head.next
