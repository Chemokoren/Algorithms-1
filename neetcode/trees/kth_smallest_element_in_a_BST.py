"""
Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k, return the kth(1-indexed) smallest
element in the tree.

                    3
                   /  \
                  1    4
                   \
                    2
Input: root =[3,1,4,null,2], k=1
Output: 1
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self,data):
        if self.val:
            if data < self.val:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            if data > self.val:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.val = TreeNode(data)

    def traverse(self,troot):
        if troot:
            print(troot.val,end="--")
            self.traverse(troot.left)
            self.traverse(troot.right)

class Solution:
    def kthSmallest(self,root: TreeNode,k:int)->int:
        n = 0
        stack =[]
        cur = root

        while cur and stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right

k=3
tree = TreeNode(20) 
tree.insert(8)
tree.insert(22)
tree.insert(4)
tree.insert(12)
tree.insert(10)
tree.insert(14)
#keys = [ 20, 8, 22, 4, 12, 10, 14 ]
# keys = [ 8, 22, 4, 12, 10, 14 ]
 
# for x in keys:
#     tree.insert(x)

tree.traverse(tree.val)
# sol = Solution()
# print(sol.kthSmallest(tree, k))