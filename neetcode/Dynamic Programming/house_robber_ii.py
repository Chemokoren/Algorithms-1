"""
House Robber II

You are a professional robber planning to rob houses along a street. Each house has a 
certain amount of money stashed. All houses at his place are arranged in a circle.
That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have
a security system connected, and it will automatically contact the police if two adjcent
houses were broken into on the same night.

Given a list of non-negative integers nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: nums =[2, 3, 2]
Output: 3
Explanation: You cannot rob house 1 (money =2) and then rob house 3 (money =2), because
they are adjacent houses.

"""
import unittest

class Solution:

    def house_robber_ii(self, nums):
        return max(nums[0], self.helper_rec(nums[1:]), self.helper_rec(nums[:-1]))
        # return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))


    def helper(self, nums):

        rob1, rob2 =0, 0

        for n in nums:
            temp =max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
    
    def helper_rec(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        return max(self.helper_rec(nums[1:]), self.helper_rec(nums[2:]) + nums[0])

    
class TestHouseRobberII(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()        

    def test_house_robber_ii(self):
        self.assertEqual(3, self.solution.house_robber_ii([2, 3, 2]))


if __name__=="__main__":
    unittest.main()