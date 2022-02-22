
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def tree_max_depth(root: Node) -> int: 
    def dfs(node, depth) -> int: 
        if not node: 
            return depth 
        return max(dfs(node.left, depth+1), dfs(node.right, depth+1))
    return dfs(root, 0)