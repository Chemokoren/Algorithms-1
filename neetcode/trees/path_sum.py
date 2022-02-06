from typing import Optional
"""
Given the root of a binary tree and an integer targetSum return true if the tree has a 
root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Example 1:

                    5
                   / \
                  4   8
                 /   / \
                11  13  4   
               / \       \
              7   2       1
Input: root =[5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum =22
Output: True
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val  =val
        self.left =left
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
            self.val = data

    def createTree(self,array):
        if (array == None or len(array)==0):
            return None

        treeNodeQueue = []
        integerQueue  = []

        for i in range(1,len(array)):
            integerQueue.append(array[i])
        

        treeNode = TreeNode(array[0])
        treeNodeQueue.append(treeNode)

        while (len(integerQueue)> 0):

            leftVal  = None if len(integerQueue)== 0 else integerQueue.pop(0)
            rightVal = None if len(integerQueue)== 0 else integerQueue.pop(0)

            current = treeNodeQueue.pop(0)

            if (leftVal !=None):
                    left = TreeNode(leftVal)
                    current.left = left
                    treeNodeQueue.append(left)
            
            if (rightVal !=None):
                    right = TreeNode(rightVal)
                    current.right = right
                    treeNodeQueue.append(right)
            
        
        return treeNode

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int)->bool:

        # O(n) time where n is number of nodes | O(n) time in the worst case & O(log(n)) if
        # it is a balanced binary tree
        def dfs(node, curSum):
            if not node:
                return False
            curSum += node.val
            if not node.left and not node.right:
                return curSum == targetSum
            
            return (dfs(node.left, curSum) or 
                    dfs(node.right, curSum))
        return dfs(root, 0)

tree_vals =[5,4,8,11,None,13,4,7,2,None,None,None,1]
t =TreeNode()
tree_root =t.createTree(tree_vals)
sol =Solution()
print(sol.hasPathSum(tree_root, 22))
