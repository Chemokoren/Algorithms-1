"""
Given a binary search tree(BST), find the lowest common ancestor(LCA) of two given
nodes in the BST.

According to the definition of LCA on Wikipedia: "The lowest common ancestor is 
defined between two nodes p and q as the lowest node in T that has both p and q 
as descendants (where we allow a node to be a descendant of itself)."

Example 1:
                   6
                  /  \
                 2     8
               /  \   /  \
              0    4 7    9
                  / \
                 3   5
Input: root =[6,2,8,0,4,7,9,null,null,3,5], p=2, q =8
Output: 6
Explanation : The LCS of nodes 2 and 8 is 6.
O(log(n)) time | O(1) space 
"""

# Definition for a binary tree node .
class TreeNode:
    def __init__(self,x) -> None:
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',q: 'TreeNode')->'TreeNode':
        cur = root

        while cur:
            if p.val >cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else: return cur.val # cur if cur is one of the nodes or the diversion point


tr = TreeNode(6)
tr.left = TreeNode(2)
tr.right = TreeNode(8)
tr.left.left = TreeNode(0)
tr.left.right = TreeNode(4)
tr.right.left = TreeNode(7)
tr.right.right = TreeNode(9)
tr.left.right.left = TreeNode(3)
tr.left.right.right = TreeNode(5)

sol = Solution()
p = TreeNode(2)
q = TreeNode(8)

p1 = TreeNode(7)
q1 = TreeNode(6)

p2 = TreeNode(7)
q2 = TreeNode(9)



print("sol::", sol.lowestCommonAncestor(tr, p, q))
print("Example 2 sol::", sol.lowestCommonAncestor(tr, p1, q1))
print("Example 3 sol::", sol.lowestCommonAncestor(tr, p2, q2))