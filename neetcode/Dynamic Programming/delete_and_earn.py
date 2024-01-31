"""
Delete and Earn

You are given an integer array nums. You want to maximize the number of points you get by
performing the following operation any number of times:

- Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete
every element equal to nums[i] -1 and every element equal to nums[i] + 1

Return the maximum number of points you can earn by applying the above operation some
number of times.


Example 1:

Input: nums =[3, 4, 2]
Output: 6
Explanation: you can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums =[2]
-Delete 2 to earn 2 points. nums =[]
You earn a total of 6 points.

"""
from collections import Counter
from typing import List
import unittest


class Solution:

    def deleteAndEarn(self, nums: List[int])-> int:
        count = Counter(nums)
        nums = sorted(list(set(nums)))

        earn1, earn2 = 0, 0
        for i in range(len(nums)):
            curEarn = nums[i] * count[nums[i]]

            # can't use both curEarn and earn2
            if i > 0 and nums[i] == nums[i-1] + 1:
                temp = earn2
                earn2 = max(curEarn + earn1, earn2)
                earn1 = temp
            else:
                temp = earn2
                earn2 = curEarn + earn2
                earn1 = temp
        return earn2
    

class TestDeleteAndEarn(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol = Solution()

    def test_delete_and_earn(self):
        self.assertEqual(6, self.sol.deleteAndEarn([3, 4, 2]))

if __name__=="__main__":
    unittest.main()
