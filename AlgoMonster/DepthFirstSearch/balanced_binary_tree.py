"""
Balanced Binary Tree

A balanced binary tree is defined as a tree such that either it is an empty tree, or both its
subtree are balanced and has a height difference of at most 1.

In that case, given a binary tree, determine if it's balanced.

Parameter
- tree: A binary tree.

Result
A boolean representing whether the tree given is balanced

Example 1:

input
                        1
                       / \
                      2   3
                     / \   \
                    4   5   6 
                    \
                    7

Output: true

Example 2

Input:  
                1
               / \
              2   3
             / \   \
            4   5   6
             \      /
             7     8

Output: 6

Explanation: The subtrees of the node labelled 3 has a height difference of 2, so it is not
balanced.



"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(tree: Node) -> bool:
    # WRITE YOUR BRILLIANT CODE HERE
    return False

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    tree = build_tree(iter(input().split()), int)
    res = is_balanced(tree)
    print('true' if res else 'false')
