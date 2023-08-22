"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than [n / 2] times.
You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 10^4
-2^31 <= nums[i] <= 2^31 - 1

Follow-up: Could you solve the problem in linear time and in O(1) space?

#### No need for a base because according to the instructions, an answer will always exist

"""

class Solution:
    def majorityElement(self, nums:int)->int:
        m = {}
        
        max_val =0
        for num in nums:
            m[num] =m.get(num, 0)+1
            if m[num] >max_val:
                max_val=m[num]
        return max_val  # returns index of majority value
    

        # approach 1
        # for num in nums:
        #     if(m[num] > len(nums)//2):
        #         return num
        
        # approach 2
        # max_val =0
        # for num in nums:
        #     if m[num] > max_val:
        #         max_val = m[num]
                
        # for name, age in m.items(): 
        #     if age == max_val:
        #         return name

#nums = [2,2,1,1,1,2,1,2,1]
nums = [9,2,6,1,5,2,7,2,3,4]
sol = Solution()
print(sol.majorityElement(nums))