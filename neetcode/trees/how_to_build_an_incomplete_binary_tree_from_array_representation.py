"""
if the input is an array, where null means no node.

input:
[1,2,3,null,5,null,7]

Please assume that I have already checked the input.

For each array[i], its parents array[i/2] cannot be null(recursively,so root cannot be null).

How to build a tree with such logic relation

Example 1: [1,2,3,null,5,null,7]

                1
               / \
              2   3
              \     \
               5     7

Example 2: [5,4,8,11,null,17,4,7,null,null,null,5]

                        5
                       / \
                      4   8
                     /   / \  
                    11  17  4
                   /        /
                  7        5

each node should be represented by a TreeNode object.
"""
from typing import Optional, List
class TreeNode:
    """Definition for a binary tree node"""
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def createTree(array):
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

# inorder traversal
def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.val,end='--')
        inorderTraversal(root.right)

# preorder traversal
def preorderTraversal(root):
    if root:
        print(root.val, end='--')
        preorderTraversal(root.left)
        preorderTraversal(root.right)

# postorder traversal
def postorderTraversal(root):
    if root:
        postorderTraversal(root.left)
        postorderTraversal(root.right)
        print(root.val, end='--')



test_data =[5,4,8,11,None,17,4,7,None,None,None,5]

test_data=[-64,12,18,-4,-53,None,76,None,-51,None,None,-93,3,None,-31,47,None,
3,53,-81,33,4,None,-51,-44,-60,11,None,None,None,None,78,None,-35,-64,26,-81,
-31,27,60,74,None,None,8,-38,47,12,-24,None,-59,-49,-11,-51,67,None,None,None,
None,None,None,None,-67,None,-37,-19,10,-55,72,None,None,None,-70,17,-4,None,
None,None,None,None,None,None,3,80,44,-88,-91,None,48,-90,-30,None,None,90,-34,
37,None,None,73,-38,-31,-85,-31,-96,None,None,-18,67,34,72,None,-17,-77,None,56,
-65,-88,-53,None,None,None,-33,86,None,81,-42,None,None,98,-40,70,-26,24,None,None,
None,None,92,72,-27,None,None,None,None,None,None,-67,None,None,None,None,None,None,
None,-54,-66,-36,None,-72,None,None,43,None,None,None,-92,-1,-98,None,None,None,None,
None,None,None,39,-84,None,None,None,None,None,None,None,None,None,None,None,None,
None,-93,None,None,None,98]

print("inorder traversal: ",inorderTraversal(createTree(test_data)))
print("preorder traversal: ",preorderTraversal(createTree(test_data)))
print("postorder traversal: ",postorderTraversal(createTree(test_data)))

print(f"-------------------implementation 2-------------------")
def array_to_tree(arr: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Convert an array representation of a binary tree to an actual binary tree.

    :param arr: List of integers where None represents a missing node.
    :return: The root of the binary tree.
    """
    if not arr:
        return None

    # Create a list of TreeNode objects for non-null values in the array
    nodes = [TreeNode(val) if val is not None else None for val in arr]

    # The root is the first element
    root = nodes[0]

    # Fill in the left and right children
    for i in range(len(nodes)):
        if nodes[i] is not None:
            left_index = 2 * i + 1
            right_index = 2 * i + 2
            if left_index < len(nodes):
                nodes[i].left = nodes[left_index]
            if right_index < len(nodes):
                nodes[i].right = nodes[right_index]

    return root


# Helper function to print the tree (for debugging purposes)
def print_tree(root: Optional[TreeNode], depth=0, label="Root"):
    if root is not None:
        print(" " * (depth * 4) + f"{label}: {root.val}")
        print_tree(root.left, depth + 1, "L")
        print_tree(root.right, depth + 1, "R")


tree1 = array_to_tree([1, 2, 3, None, 5, None, 7])
tree2 = array_to_tree([5, 4, 8, 11, None, 17, 4, 7, None, None, None, 5])
tree3 = array_to_tree([1,2,3,None,5,None,7])

print("Example 1 Tree:")
print_tree(tree1)

print("\nExample 2 Tree:")
print_tree(tree2)

print(f" --------------------- preorder tree 1 ---------------------")
preorderTraversal(tree1)
print(f" --------------------- preorder tree 2 ---------------------")
preorderTraversal(tree2)
print(f" --------------------- preorder tree 3 ---------------------")
preorderTraversal(tree3)

import unittest
class TestArrayToTree(unittest.TestCase):
    """
    Unit tests for the array_to_tree function

    Empty Tree: Tests the case where the input array is empty.
    Single Node: Tests the case where the input array has only one element.
    Two Levels: Tests a simple tree with two levels.
    Tree with Nulls: Tests a tree with some None values to represent missing nodes.
    Complex Tree: Tests a more complex tree structure with multiple levels and missing nodes.
    All Nulls: Tests the case where the input array contains only None values.
    Mixed Nulls: Tests a tree with a mix of non-null and None values in the array.

    """

    def setUp(self):
        self.solution = array_to_tree

    def assertTreeEqual(self, t1: Optional[TreeNode], t2: Optional[TreeNode]):
        """
        Helper function to assert that two binary trees are equal.
        """
        if t1 is None and t2 is None:
            return True
        if t1 is not None and t2 is not None:
            return (t1.val == t2.val and
                    self.assertTreeEqual(t1.left, t2.left) and
                    self.assertTreeEqual(t1.right, t2.right))
        return False

    def test_empty_tree(self):
        self.assertIsNone(self.solution([]))

    def test_single_node(self):
        root = TreeNode(1)
        result = self.solution([1])
        self.assertTrue(self.assertTreeEqual(result, root))

    def test_two_levels(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        result = self.solution([1, 2, 3])
        self.assertTrue(self.assertTreeEqual(result, root))

    def test_tree_with_nulls(self):
        root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(7)))
        result = self.solution([1, 2, 3, None, 5, None, 7])
        self.assertTrue(self.assertTreeEqual(result, root))

    def test_complex_tree(self):
        root = TreeNode(5,
                        TreeNode(4, TreeNode(11, TreeNode(7)), None),
                        TreeNode(8, TreeNode(17, TreeNode(5)), TreeNode(4)))
        result = self.solution([5, 4, 8, 11, None, 17, 4, 7, None, None, None, 5])
        self.assertTrue(self.assertTreeEqual(result, root))

    def test_all_nulls(self):
        self.assertIsNone(self.solution([None, None, None, None]))

    def test_mixed_nulls(self):
        root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
        result = self.solution([1, None, 2, 3])
        self.assertFalse(self.assertTreeEqual(result, root))

if __name__ == '__main__':
    unittest.main()