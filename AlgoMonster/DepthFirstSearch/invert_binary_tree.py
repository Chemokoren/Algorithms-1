"""
Invert Binary Tree

Given a binary tree, invert it and return the new value. You may invert it in-place.

To "invert" a binary tree, switch the left subtree and the right subtree, and invert them both
Inverting an empty tree does nothing.

Input

tree: a binary tree that needs to be inverted

Output

The inverted binary tree.

Example 

input

1 tree =<see explanation>

Output: <see explanation>

Explanation:

original tree:

                            1                           1
                           / \                         / \ 
                          2   3                       3   2
                         / \   \                     /   / \
                        4  5    6                   6   5   4
                         \                                  /
                         7                                 7


"""
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_binary_tree(tree: Node) -> Node:
    # WRITE YOUR BRILLIANT CODE HERE
    return None

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

def format_tree(node):
    if node is None:
        yield 'x'
        return
    yield str(node.val)
    yield from format_tree(node.left)
    yield from format_tree(node.right)

if __name__ == '__main__':
    tree = build_tree(iter(input().split()), int)
    res = invert_binary_tree(tree)
    print(' '.join(format_tree(res)))