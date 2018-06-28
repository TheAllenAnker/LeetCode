# Author: Allen Anker
# Created by Allen Anker on 27/06/2018


"""
You are given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
"""
import re


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1, num2 = 0, 0
        while l1:
            num1 = num1 * 10 + l1.val
            l1 = l1.next
        while l2:
            num2 = num2 * 10 + l2.val
            l2 = l2.next
        res_num = num1 + num2
        head = ListNode(None)
        temp = head
        digits = re.findall('\d', str(res_num))
        for i in range(len(digits)):
            temp.val = int(digits[i])
            if i < len(digits) - 1:
                temp.next = ListNode(None)
                temp = temp.next

        return head


solution = Solution()
l1, l2 = ListNode(7), ListNode(5)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l1.next.next.next = ListNode(3)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
head = solution.addTwoNumbers(l1, l2)
while head is not None:
    print(head.val)
    head = head.next

