"""
DFS with States

Let's reinforce our understanding of state with one more example.

Ternary Tree Paths
-------------------
Given a ternary tree(each node of the tree has at most three children), find all root-to-leaf
paths.

                     1
                   / | \
                  2  4  6
                 /
                3

[1->2->3, 1->4, 1->6]


"""

from typing import List

class Node:

    def __init__(self, val, children=None):
        if children is None:
            children =[]
        self.val = val
        self.children = children

# we use path to keep track of the nodes we have visited to reach the current node and use it
# to construct our solution when we reach leaf nodes
def ternary_tree_paths(root: Node)->List[str]:
    
    # dfs helper function
    def dfs(root, path, res):
        # exit condition, reached leaf node, append paths to results
        if all(c is None for c in root.children):
            res.append('->'.join(path)+'->'+root.val)
            return

        # dfs on each non-null child
        for child in root.children:
            if child is not None:
                dfs(child, path + [root.val], res)
    res =[]
    if root: dfs(root, [], res)
    return res

    '''
    in the recursive call in the previous solution, we create a new list each time we recurse
    with path + [root.val]. This is not space efficient because creating a new list requires
    allocating new space in memory and copy over each element. A more efficient way is to use 
    a single list and append/pop following the call stack.
    '''
    def ternary_tree_paths_updated(root):
        def dfs(root, path, res):
            if all(c is None for c in root.children):
                res.append('->'.join(path)+'->'+root.val)
                return
            
            for child in root.children:
                if child is not None:
                    dfs(child, path+[root.val],res)
                    path.append(root.val)
                    dfs(child, path, res)
                    path.pop()
        res =[]
        if root: dfs(root, [], res)
        return res

def build_tree(nodes, f):
    val =next(nodes)
    num = int(next(nodes))
    children =[build_tree(nodes, f) for _ in range(num)]
    return Node(f(val), children)

if __name__=='__main__':
    pass