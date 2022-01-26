"""
Sum Root to Leaf Numbers
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a
number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers
Note: A leaf is a node with no children

Example:
input:[1,2,3]
        1
       / \
      2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12
The root-to-leaf path 1->3 represents the number 13
Therefore, sum =12 + 13 =25

                4
               / \
              9   0
             / \ 
            5   1

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
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
class Solution:
    def sumNumbers(self, root:TreeNode)->int:

        def dfs(cur, num):
            if not cur:
                return 0
            
            num = num * 10 + cur.val
            if not cur.left and not cur.right:
                return num
            leftVal =dfs(cur.left,num)
            rightVal =dfs(cur.right, num)
            return leftVal+rightVal
        return dfs(root,0)



# tree = TreeNode(1) # expected 25
# tree.insert(2)
# tree.insert(3)

tree = TreeNode(1) # expected 1026
tree.insert(4)
tree.insert(9)
tree.insert(0)
tree.insert(5)
tree.insert(1)

sol =Solution()
print(sol.sumNumbers(tree))