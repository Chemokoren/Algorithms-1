"""
Insert Into BST

Given the root node of a valid BST and a value to insert into the tree, return a new root node
representing the valid BST with the addition of the new item. If the new item already exists
in the binary search tree, do not insert anything.

You must expand on the original BST by adding a leaf node. Do not change the structure of
the original BST.

Input

bst: a binary tree representing the existing BST.
val: an integer representing the value to be  inserted.

Output

A valid BST with the inserted number, or the same BST if the number already exists.

Example 1:

input:
1 tree = <see explanation>
2 val = 7

Explanation:

Before insertion

                    8
                   / \
                  5   10
                 / \    \
                2   6    14
                 \
                  3

After insertion

                    8
                   / \
                  5   10
                 / \    \
                2   6    14
                 \   \
                  3   7

"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert_bst(bst: Node, val: int) -> Node:
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
    bst = build_tree(iter(input().split()), int)
    val = int(input())
    res = insert_bst(bst, val)
    print(' '.join(format_tree(res)))