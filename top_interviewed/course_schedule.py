# Author: Allen Anker
# Created by Allen Anker on 17/09/2018
"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def can_finish(self, num_courses, prerequisites):
        """
        Idea 1: Build a linked list, and if there is a loop, return false.
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(num_courses)]
        visit = [0 for _ in range(num_courses)]
        for x, y in prerequisites:
            graph[x].append(y)

        def dfs(i):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            visit[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visit[i] = 1
            return True

        for i in range(num_courses):
            if not dfs(i):
                return False
        return True
