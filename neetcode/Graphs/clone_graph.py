"""
Clone Graph

Given a reference of a node in a connected undirected graph.

Return a deep copy(clone) of the graph.

Each node in the graph contains a val(int) and a list(List[Node]) of its neighbors.

class Node{

    public int val;
    public List<Node> neighbors;
}
Time : O(n) =E+V
"""

# Definition for a Node.
class Node:
    def __init__(self, val =0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node')->'Node':
        oldToNew ={}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None