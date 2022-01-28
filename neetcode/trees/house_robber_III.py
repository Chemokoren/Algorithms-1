"""
House Robber III

The thief has found himself a new place for his thievery again. There is only one entrance to
this area, called the "root." Besides the root, each house has one and only one parent house.
After a tour, the smart thief realized that "all houses in this place forms a binary tree." It
will automatically contact the police if two directly-linked houses were broken into on the 
same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
    input: [3, 2, 3, null, 3, null, 1]
                            3
                           / \
                          2   3
                          \    \ 
                           3    1
Output: 7
Explanation: Maximum amount of money the thief can rob = 3+ 3+1 =7

Solution: DFS -O(n)

"""
# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: TreeNode) ->int:

        # return pair: [withRoot, withoutRoot]
        def dfs(root):
            if not root:
                return [0,0]
            leftPair = dfs(root.left)
            rightPair = dfs(root.right)

            withRoot = root.val + leftPair[1] + rightPair[1]
            withoutRoot = max(leftPair) + max(rightPair)

            return [withRoot, withoutRoot]
        return max(dfs(root))

