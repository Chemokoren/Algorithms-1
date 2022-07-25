"""
Array with Elements Not Equal to Average of Neighbors

You are given a 0-indexed array nums of distinct integers. You want to rearrange the 
elements in the array such that every element in the rearranged array is not equal to 
the average of its neighbors.

More formally, the rearranged array should have the property such that for every i in the
range 1<= i < nums.length -1, (nums[i-1]+ nums[i+1]) /2 is not equal to nums[i].

Return any rearrangement of nums that meets the requirements.

Example 1:
Input: nums =[1,2,3,4,5]
Output: [1,2,4,5,3]
Explanation:
when i=1, nums[i] = 2, and the average of its neighbors is(1+4) /2 =2.5
when i=2, nums[i] = 4, jand the average of its neighbors is (2+5) /2 =3.5
when i=3, nums[i] =5, and the average of its neighbors is (4+3) / 2 =3.5

Example 2:
Input: nums =[6,2,0,9,7]
Output: [9,7,6,2,0]

Explanation:
When i=1, nums[i] =7, and the average of its neighbors is (9+6) / 2 =7.5
When i=2, nums[i] =6, and the average of its neighbors is (7+2) / 2 =4.5
When i=3, nums[i] =2, and the average of its neighbors is (6+0) / 2 =3

is there a way to guarantee that the neighbours of a given number are larger than the
number? i.e 4, 2, 5
Alternatively, what if the neighbours of a given number are smaller than the number?
i.e 2, 5, 3

Conclusively, we want to guarantee that the neighbours are either smaller or larger than
the given number.
-Put the numbers in a new list while skipping a single number each time
e.g.
1 _ 2 _ 3 
1 4 2 5 3
"""

# time complexity: O(nlog(n))
from typing import List
class Solution:

    def rearrangeArray(self, nums: List[int])->List[int]:

        nums.sort()
        res =[]

        l, r =0, len(nums) -1
        while len(res) != len(nums):
            res.append(nums[l])
            l +=1

             # handles cases where we have odd total numbers 
             # so if we increment left pointer & it becomes greater than r pointer then,
             # we do not want to add an element multiple times
            if l <= r:
                res.append(nums[r])
                r -= 1
        return res

sol = Solution()
print("Expected: [1,2,4,5,3], Actual:",sol.rearrangeArray([1,2,3,4,5]))
print("Expected: [9,7,6,2,0], Actual:",sol.rearrangeArray([6,2,0,9,7]))

