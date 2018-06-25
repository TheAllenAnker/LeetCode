# Author: Allen Anker
# Created by Allen Anker on 24/06/2018


"""
Given a list accounts, each element accounts[i] is a list of strings,
 where the first element accounts[i][0] is a name, and the rest of the elements are emails
  representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person
 if there is some email that is common to both accounts. Note that even if two accounts have the same name,
  they may belong to different people as people could have the same name.
   A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format:
 the first element of each account is the name, and the rest of the elements are emails in sorted order.
  The accounts themselves can be returned in any order.
"""
import collections


class Solution:
    def accounts_merge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """

        """
        Draw an edge between two emails if they occur in the same account.
         The problem comes down to finding connected components of this graph.
        """


        em_to_name = {}
        graph = collections.defaultdict(set)
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                # draw a edge between the first email to all other emails
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
                em_to_name[email] = name

        seen = set()
        ans = []
        # basically, this is a depth first search based on the edges between emails
        for email in graph:
            if email not in seen:
                seen.add(email)
                stack = [email]
                component = []
                while stack:
                    node = stack.pop()
                    component.append(node)
                    # emails that have an edge with node
                    for nei in graph[node]:
                        if nei not in seen:
                            seen.add(nei)
                            # emails that have an edge with every "nei"
                            stack.append(nei)
                ans.append([em_to_name[email]] + sorted(component))
        return ans


solution = Solution()
accounts = [['John', 'johnsmith@mail.com', 'john00@mail.com'],
            ['John', 'johnnybravo@mail.com'],
            ['Allen', 'allenanker@gmail.com'],
            ['John', 'johnsmith@mail.com', 'john_newyork@mail.com'],
            ['Mary', 'mary@mail.com']]
print(solution.accounts_merge(accounts))