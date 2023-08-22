"""

Given an array of non-negative integers nums, you are initially positioned at the first
index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

constraints:
1 <= nums.length <=10^4
0 <= nums[] <=10^5

Example 1:

input: nums =[2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index

Example 2:

input: nums =[3,2,1,0,4]
output: false
Explanation: All jumps will end at index 3 which is a dead end

                [ 3,  2,  1,  0,  4]
                  0   1   2   3   4   -indexes

                  0
           1/    2|     \3
           1      2      3
         /  \     |
        2    3
      /
     3  


If we use brute force as shown above, the time complexity will be n^n
But if we cache some of the values like that of index 2, then we can reduce the time 
complexity to n^2
"""
from typing import List
# Greedy Solution
class Solution:

    def canJump(self, nums:List[int])->bool:
        goal = len(nums) -1

        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >=goal:
                goal = i
        return True if goal == 0 else False
    
sol = Solution()
print("Expected: False, Actual:",sol.canJump([3,2,1,0,4]))
print("Expected: True, Actual:",sol.canJump([2,3,1,1,4]))


def can_jump(nums:List[int])->bool:
    maxjump,N,i =0,len(nums)-1,0
    
    while i<= maxjump and i<N:
        if maxjump >= N:
            break
        maxjump = max(maxjump, i+nums[i])
        i+=1
    return maxjump >=N 

print("Expected: False, Actual:",can_jump([3,2,1,0,4]))
print("Expected: True, Actual:",can_jump([2,3,1,1,4]))


# brute-force approach
def can_jump_brute_force(nums):
	n = len(nums)
	if n < 2: return True
	dp =[False for _ in range(n)]
	dp[0] =True
	
	visited =set()
	
	def rec(pos, dp):
		maxjump = nums[pos]
		for i in range(1,maxjump+1):
			if pos+i > n-1:break
			dp[pos+i] = True
			if pos+i not in visited: rec(pos+i,dp)
		visited.add(pos)
	rec(0,dp)
	return dp[n-1]

print("Brute Force Expected: False, Actual:",can_jump_brute_force([3,2,1,0,4]))
print("Brute Force Expected: True, Actual:",can_jump_brute_force([2,3,1,1,4]))