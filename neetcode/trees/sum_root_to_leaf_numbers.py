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
        self.val    = val
        self.left   = left
        self.right  = right

    def insert(self,data):
        new_node =TreeNode(data)
        if self.val:
            if data < self.val:
                if self.left is None:
                    self.left = new_node
                else:
                    self.left.insert(data)
            if data > self.val:
                if self.right is None:
                    self.right = new_node
                else:
                    self.right.insert(data)
        else:
            self.val = new_node
            
    def traverse(self,root):
        cur = root
        if cur.val >=0:
            print(cur.val, end="-->")
            if cur.left:
                self.traverse(cur.left)
            elif cur.right:
                self.traverse(cur.right)

class Solution:
    def sumNumbers(self, root:TreeNode)->int:

        def dfs(cur, num):
            if not cur:
                return 0
            
            num = num * 10 + cur.val
            if not cur.left and not cur.right:
                return num
            print("aaa:", num)
            return dfs(cur.left,num)+dfs(cur.right, num)
        return dfs(root,0)



tree = TreeNode(1) # expected 25
tree.left=TreeNode(2)
tree.right=TreeNode(3)
# tree.insert(2)
# tree.insert(3)

#       1
#     /    \
#   2        3

# 0 * 10 + 1 = 1
# 1 * 10 + 2 = 12
# 1 * 10 + 3 = 13

tree = TreeNode(4) # expected 1026
# # # tree.insert(4)
# tree.insert(9)
# tree.insert(0)
# tree.insert(5)
# tree.insert(1)
tree.left=TreeNode(9)
tree.right=TreeNode(0)
tree.left.left=TreeNode(5)
tree.left.right=TreeNode(1)



sol =Solution()
print(sol.sumNumbers(tree))
# tree.traverse(tree)


"""
my tests 
"""
def sum_numbers(root:TreeNode):
    
    temp = 0
    res  = 0
    def recursion(N:TreeNode):
        
        temp = temp * 10 + N.val
        if(N.left == None and N.right == None):
            res += temp
            
        else:
            if N.left != None:
                recursion(N.left)
            if N.right != None:
                recursion(N.right)
        temp /=10
    recursion(root)
    return res
# print("recu::",sum_numbers(tree))