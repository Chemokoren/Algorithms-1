"""
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from
the root node down to the farthest leaf node.
Note: A leaf is a node with no children.
Example:
Given binary tree [3, 9, 20, null, null, 15, 7]
                    3
                   /  \
                   9  20
                      / \
                     15  7
return its depth =3  

"""
class Node:

    def __init__(self, root) -> None:
        self.root = root
        self.left = None
        self.right = None

def max_depth(tree):

    def dfs(tree):
        # base case
        if not tree:
            return 0
        left = dfs(tree.left) 
        right = dfs(tree.right)
        max_val = 1 +max(left, right)

        return max_val
        
    return dfs(tree)
    
tree =Node(3)
tree.left=Node(9)
tree.right=Node(20)
tree.right.left=Node(15)
tree.right.right=Node(7)

print("aaa::", max_depth(tree))