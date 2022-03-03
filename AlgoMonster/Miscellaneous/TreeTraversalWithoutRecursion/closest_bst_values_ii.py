"""
Closest BST Values II

Given a BST, output k closest values in this BST to x. Sort the output by value.

The output set is guaranteed to be unique.

Do not convert the BST to a list.

Input

    bst: a valid BST of size n.
    x: an integer representing the number to find the k closest numbers to.
    k: an integer.

Output

A list of integers containing the k closest numbers to x.

Examples

Example 1:

Input:

bst = <See explanation>

x = 7

k = 4

Output: [5, 6, 8, 10]

Explanation:

                8
               / \
              5   10
             / \    \
            2   6    14
             \
              3
All four numbers in the output are within 3 away from 7.
Constraints

    1 <= k <= n <= 10^5
"""
from typing import List

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def closest_values(bst: Node, x: int, k: int) -> List[int]:
    return []

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    bst = build_tree(iter(input().split()), int)
    x = int(input())
    k = int(input())
    res = closest_values(bst, x, k)
    print(' '.join(map(str, res)))
