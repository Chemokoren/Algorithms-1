"""
Serialize and Deserialize Binary Tree - Preorder Traversal

Serialization is the process of converting a data structure or object into a sequence
of bits so that it can be stored in a file or memory buffer, or transmitted across a
network connection link to be reconstructed later in the same or another computer
environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction
on how your serialization/deserialization algorithm should work.

You just need to ensure that a binary tree can be serialized to a string and this 
string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary
tree. You do not necessarily need to follow this format, so please be creative and 
come up with different approaches yourself.

Example 1:

                1
               / \
              2   3
                 / \
                4   5

Input: root =[1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
you can use BFS but here we will use DFS - preorder

O(n) time for serializing & deserializing

"""

# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val   = x
        self.left  = None
        self.right = None

    def insert(self, data):
        self.data = self.val
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
               if self.right is None:
                  self.right = TreeNode(data)
               else:
                  self.right.insert(data)
        else:
            self.val = TreeNode(data)

class Codec:

    def serialize(self, root):
        """ 
        Encodes a tree to a single string.

        : type root: TreeNode
        : rtype : str
        
        """
        res =[]

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)

        return ",".join(res)

    def deserialize(self, data):
        """ 
        Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left  =dfs()
            node.right =dfs()
            return node
        return dfs()
    
# def level_order_traversal(root):
#     if root:
#         print(root.val, end="-->")
#         level_order_traversal(root.left)
#         level_order_traversal(root.right)



# print("Deserialized Binary Tree::", cd.deserialize(cd.serialize(tr)))
# level_order_traversal(cd.deserialize(cd.serialize(tr))) 

import unittest

class TestCodec(unittest.TestCase):

    """
    The test cases cover various scenarios, including empty trees, single-node trees, balanced trees, unbalanced trees, and invalid serialized data.
    
    """
    def setUp(self):
        self.codec = Codec()

    def test_sample_tree(self):
        tr =TreeNode(1)
        tr.left = TreeNode(2)
        tr.right = TreeNode(3)
        tr.right.left =TreeNode(4)
        tr.right.right =TreeNode(5)

        serialized = self.codec.serialize(tr)

        self.assertEqual("1,2,N,N,3,4,N,N,5,N,N",serialized, "Should return True")

        # Deserialized Binary Tree Level order Traversal
        # 1-->2-->3-->4-->5-->

        deserialized = self.codec.deserialize(serialized)

        self.assertEqual(deserialized.val, 1)
        self.assertEqual(deserialized.left.val, 2)
        self.assertEqual(deserialized.right.val, 3)
        self.assertIsNone(deserialized.left.left)
        self.assertIsNone(deserialized.right.left.left)
        self.assertIsNone(deserialized.right.left.right)


    def test_empty_tree(self):
        """Tests serialization and deserialization of an empty tree."""
        
        root = None
        serialized = self.codec.serialize(root)
        self.assertEqual(serialized, "N")
        deserialized = self.codec.deserialize(serialized)
        self.assertIsNone(deserialized)

    def test_single_node_tree(self):
        """Tests serialization and deserialization of a single-node tree."""
        root = TreeNode(1)
        serialized = self.codec.serialize(root)
        self.assertEqual(serialized, "1,N,N")
        deserialized = self.codec.deserialize(serialized)

        self.assertEqual(deserialized.val, 1)
        self.assertIsNone(deserialized.left)
        self.assertIsNone(deserialized.right)

    def test_balanced_tree(self):
        """Tests serialization and deserialization of a balanced tree."""

        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(6)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.right = TreeNode(7)

        serialized = self.codec.serialize(root)
        self.assertEqual(serialized, "4,2,1,N,N,3,N,6,N,N,7")
        deserialized = self.codec.deserialize(serialized)

        self.assertEqual(deserialized.val, 4)
        self.assertEqual(deserialized.left.val, 2)
        self.assertEqual(deserialized.right.val, 6)
        self.assertEqual(deserialized.left.left.val, 1)

    def test_unbalanced_tree(self):
        """Tests serialization and deserialization of an unbalanced tree."""
   
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)

        serialized = self.codec.serialize(root)
        self.assertEqual(serialized, "1,2,4,N,N,3,N,N")
        deserialized = self.codec.deserialize(serialized)

        self.assertEqual(deserialized.val, 1)
        self.assertEqual(deserialized.left.val, 2)
        self.assertEqual(deserialized.right.val, 3)
        self.assertEqual(deserialized.left.left.val, 4)
  

    def test_invalid_serialization(self):
        """Tests deserialization of invalid serialized data."""
 
        invalid_data = "1,2,X"  # Invalid value
        with self.assertRaises(ValueError):
            self.codec.deserialize(invalid_data)

        invalid_data = "1,2"  # Incomplete data (missing children)
        with self.assertRaises(ValueError):
            self.codec.deserialize(invalid_data)

if __name__ == '__main__':
    unittest.main()
