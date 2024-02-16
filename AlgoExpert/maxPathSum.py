"""
Problem:

The problem this solution is trying to solve is to find the maximum path sum in a binary tree. The path can start and end at any node in the tree, but it must follow parent-child connections and go downward.
Thought Process:

    Understanding the Problem:
        We need to find the maximum sum of a path in a binary tree. The path can start and end at any node.
        This problem can be efficiently solved using recursion by traversing the binary tree.

    Identifying Key Components:
        We need to traverse the binary tree and calculate the maximum path sum for each node.
        At each node, we need to consider three possibilities:
            The maximum sum ending at the current node.
            The maximum path sum in the left subtree.
            The maximum path sum in the right subtree.
        We also need to consider the possibility of an empty tree.

    Developing the Solution:
        We can use a recursive approach to traverse the binary tree and calculate the maximum path sum for each node.
        For each node, we compute the maximum sum of a branch ending at the current node and the maximum path sum in the subtree rooted at the current node.
        We update the maximum path sum encountered so far.
        We continue this process recursively for the left and right subtrees until we reach the leaf nodes.

    Handling Edge Cases:
        We need to handle the case of an empty tree by returning 0 as the maximum path sum.

    Testing:
        We can test the solution with various test cases, including both balanced and unbalanced trees, to ensure it works correctly.


The time and space complexity of the provided solution can be analyzed as follows:
Time Complexity:

    Traversal: The algorithm traverses each node of the binary tree exactly once. Since there are N nodes in the binary tree (where N is the number of nodes), the time complexity of the traversal is O(N).
    Recursion: At each node, the algorithm performs constant-time operations to compute the maximum sum. Since the recursion traverses each node once, the time complexity of the recursion is also O(N).
    Therefore, the overall time complexity of the solution is O(N).

Space Complexity:

    Recursion: The space complexity of the recursion depends on the maximum depth of the recursion stack. In the worst case, the binary tree is skewed, leading to a recursion depth of N (the number of nodes). Therefore, the space complexity of the recursion is O(N).
    Auxiliary Space: Apart from the recursion stack, the algorithm uses a constant amount of auxiliary space for variables such as leftMaxSumAsBranch, rightMaxSumAsBranch, etc. Therefore, the auxiliary space complexity is O(1).
    Therefore, the overall space complexity of the solution is O(N) due to the recursion stack.

"""
# O(n) time | O(log(n)) space
class TreeNode:
    def __init__(self, value):
        """
        Initialize a TreeNode with a given value.

        Parameters:
        - value: The value of the TreeNode.
        """
        self.value = value
        self.left = None
        self.right = None

def maxPathSum(tree):
    """
    Finds the maximum path sum in a binary tree.

    Parameters:
    - tree: The root node of the binary tree.

    Returns:
    - The maximum path sum in the binary tree.
    """

    _, maxSum = findMaxSum(tree)
    return maxSum

def findMaxSum(tree):
    """
    Recursively finds the maximum path sum in a binary tree rooted at 'tree'.

    Parameters:
    - tree: The root node of the binary tree.

    Returns:
    - A tuple containing two elements:
      - The maximum sum of a branch ending at the current node.
      - The maximum path sum found in the subtree rooted at the current node.
    """
    if tree is None:
        # Base case: If the tree is empty, return (0, 0) indicating no sum.
        return (0, 0)

    # Recursively find the maximum sum in the left subtree.
    leftMaxSumAsBranch, leftMaxPathSum = findMaxSum(tree.left)
    
    # Recursively find the maximum sum in the right subtree.
    rightMaxSumAsBranch, rightMaxPathSum = findMaxSum(tree.right)
    
    # Determine the maximum sum of a branch considering the current node.
    maxChildSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch)
    value = tree.value
    maxSumAsBranch = max(maxChildSumAsBranch + value, value)
    
    # Determine the maximum path sum considering the current node as the root.
    maxSumAsRootNode = max(leftMaxSumAsBranch + value + rightMaxSumAsBranch, maxSumAsBranch)
    
    # Determine the maximum path sum considering the current node.
    maxPathSum = max(leftMaxPathSum, rightMaxPathSum, maxSumAsRootNode)

    # Return the maximum sum of a branch and the maximum path sum.
    return (maxSumAsBranch, maxPathSum)


# Create a binary tree from the given list [1, 2, 3, 4, 5, 6, 7]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Call maxPathSum function with the root of the tree
print(maxPathSum(root))


"""
Here are some unit tests for the provided solution using the unittest module:

In these tests:

    We define a TreeNode class within the setUp method to avoid repetition.
    We have test cases for an empty tree, a tree with a single node, a balanced tree, and an unbalanced tree to cover various scenarios.
    We use assertEqual to verify that the output of maxPathSum matches the expected maximum path sum for each tree.

"""
import unittest

class TestMaxPathSum(unittest.TestCase):
    def setUp(self):
        # Define the TreeNode class
        class TreeNode:
            def __init__(self, value):
                self.value = value
                self.left = None
                self.right = None

        self.TreeNode = TreeNode

    def test_maxPathSum_emptyTree(self):
        root = None
        self.assertEqual(maxPathSum(root), 0)

    def test_maxPathSum_singleNode(self):
        root = self.TreeNode(5)
        self.assertEqual(maxPathSum(root), 5)

    def test_maxPathSum_balancedTree(self):
        # Construct a balanced binary tree
        root = self.TreeNode(1)
        root.left = self.TreeNode(2)
        root.right = self.TreeNode(3)
        root.left.left = self.TreeNode(4)
        root.left.right = self.TreeNode(5)
        root.right.left = self.TreeNode(6)
        root.right.right = self.TreeNode(7)
        self.assertEqual(maxPathSum(root), 18)  # Path: 5 -> 2 -> 1 -> 3 -> 7

    def test_maxPathSum_unbalancedTree(self):
        # Construct an unbalanced binary tree
        root = self.TreeNode(10)
        root.left = self.TreeNode(2)
        root.left.left = self.TreeNode(20)
        root.left.right = self.TreeNode(1)
        root.right = self.TreeNode(10)
        root.right.right = self.TreeNode(-25)
        root.right.right.left = self.TreeNode(3)
        root.right.right.right = self.TreeNode(4)
        self.assertEqual(maxPathSum(root), 42)  # Path: 20 -> 2 -> 10 -> 10 -> 3 -> 4

if __name__ == "__main__":
    unittest.main()

