# Author: Allen Anker
# Created by Allen Anker on 07/07/2018


"""
Given a directed, acyclic graph of N nodes.
Find all possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.
graph[i] is a list of all nodes j for which the edge (i, j) exists.

Note:
The number of nodes in the graph will be in the range [2, 15].
You can print different paths in any order, but you should keep the order of nodes inside one path.
"""


class Solution:
    def all_paths_source_target(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        paths = []

        def dfs(node, path):
            if node == len(graph) - 1:
                paths.append(path)
                return

            for child in graph[node]:
                dfs(child, path + (child,))

        dfs(0, (0,))
        return paths


graph = [[1,2], [3], [3], []]
solution = Solution()
print(solution.all_paths_source_target(graph))