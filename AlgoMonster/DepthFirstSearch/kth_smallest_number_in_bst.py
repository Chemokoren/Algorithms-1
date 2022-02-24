"""
K-th Smallest Number in BST

Given the root node of a valid BST and a number k, return the kth smallest number in this BST
(1-indexed).

Input:
bst: a binary tree representing the existing BST.
k: an integer

Output
The kth smallest number in bst.

Example

input:
1 bst = <see explanation>
2 k = 4

Output: 6

Explanation:

                        8
                       / \
                      5   10
                     / \    \
                    2   6    14
                     \
                      3

Constrains
1 <= 4 <=n =10^5, where n is the size of bst

"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kth_smallest(bst: Node, k: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    return 0

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    bst = build_tree(iter(input().split()), int)
    k = int(input())
    res = kth_smallest(bst, k)
    print(res)