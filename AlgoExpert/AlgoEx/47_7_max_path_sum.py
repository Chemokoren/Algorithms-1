"""
Max Path Sum

            1
           / \
          2   3
         / \ / \
        4  5 6  7

Expected: 18  
"""

# O(n) time | O(log(n)) space
def maxPathSum(tree):
    _,maxSum = findMaxSum(tree)
    return maxSum

def findMaxSum(tree):
    if tree is None:
        return (0,0)
    
    leftMaxSumAsBranch, leftMaxPathSum = findMaxSum(tree.left)
    rightMaxSumAsBranch, rightMaxPathSum = findMaxSum(tree.right)
    maxChildSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch)

    value = tree.value
    maxSumAsBranch = max(maxChildSumAsBranch +value, value)
    maxSumAsRootNode = max(leftMaxSumAsBranch +value+rightMaxSumAsBranch,maxSumAsBranch)
    maxPathSum = max(leftMaxPathSum, rightMaxPathSum,maxSumAsRootNode)

    return (maxSumAsBranch, maxPathSum)