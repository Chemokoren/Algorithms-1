"""
Graph Valid Tree

Given  n nodes labeled from 0 to n-1 and a list of undirected edges(each edge is a pair 
of nodes), write a function to check whether these edges makeup a valid tree.

#Note
You can assume that no duplicate edges will appear in edges. Since all edges are undirected,
[0, 1] is the same as [1,0] and thus will not appear to gether in edges.

Example 1:
Input: n =5 edges =[[0,1],[0,2],[0,3],[1,4]]
Output: true.

Checkout : LintCode

####: Trees do not have loops & are connected
-empty graph counts as a tree
Time complexity: O(E+V)

@param edges: a list of undirected edges
@return: true if it's a valid tree, or false
"""

def validTree(self, n, edges):
    if not n:
        return True

    adj ={i: [] for i in range(n)}
    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)

    visit =set()
    def dfs(i, prev): # pass in prev value to avoid false detection of a loop
        if i in visit:
            return False

        visit.add(i)
        for j in adj[i]:
            if j == prev:
                continue
            if not dfs(j, i):
                return False
        return True

    return dfs(0, -1) and n == len(visit)
    

