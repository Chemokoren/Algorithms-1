"""
Visible Tree Node | Number of Visible Nodes


In a binary tree, we define a node "visible" when no node on the root-to-itself path 
(inclusive) has a greater value. The root is always "visible" since there are no other nodes 
between the root and itself. Given a binary tree, count the number of "visible" nodes.

Input:

                        5
                       / \
                      4   6
                     / \
                    3   8
Output: 3 i.e 5, 8, 6

For example: Node 4 is not visible since 5>4, similarly Node 3 is not visible since both 5>3 
and 4>3. Node 8 is visible since all 5<=8, 4<=8, and 8<=8.


Explanation

We can DFS on the tree and keep track of the max value we have seen as we go.
1. Decide on the return value

The problem asks for the total number of visible nodes, so we return the total number of visible
 nodes for the current subtree after we visit a node.

2. Identify states

The definition for a "visible" node is its value is greater than any other node's value on the 
root-to-itself path. To determine whether the current node is visible or not, we need to know 
the max value from the root to it. We can carry this as a state as we traverse down the tree.

Having decided on the state and return value we can now write the DFS.

Time Complexity: O(n)

There are n nodes and n - 1 edges in a tree so if we traverse each once then the total traversal 
is O(2n - 1) which is O(n).

"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def visible_tree_node(root: Node) -> int:
    def dfs(root, max_sofar):

        if not root:

            return 0

        total = 0
        if root.val >= max_sofar:

            total += 1

        total += dfs(root.left, max(max_sofar, root.val)) # max_sofar for child node is the larger of previous max and current node val
        total += dfs(root.right, max(max_sofar, root.val))

        return total

    # start max_sofar with smallest number possible so any value root has is smaller than it
    return dfs(root, -float('inf'))

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = visible_tree_node(root)
    print(res)