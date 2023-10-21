"""
Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array(containing at 
least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

"""
from typing import List
class Solution:

	def max_product(self, arr):
		max_so_far=-float("inf")
		dp ={0:arr[0]}
		for i in range(len(arr)):
			max_now = 1
			for j in range(i, -1, -1):
				max_now *=arr[j]
				
			max_so_far =max(arr[i], max_so_far, max_now)
			dp[i] =max_so_far
		return dp[len(arr)-1]
		
	

	def max_product_lin(self, arr):
		start =0

		start_val=1
		min_val=float("inf")
		max_val=-float("inf")

		while start < len(arr):
			if arr[start] == 0:
				arr[start]=1
			start_val *=arr[start]
			min_val =min(min_val, start_val, arr[start])
			max_val =max(max_val, start_val, arr[start])


			start +=1

		return max(max_val, min_val)
	
	# time complexity : O(n) | space complexity : O(1)
	def maxProduct(self, nums: List[int])->int:
		res = max(nums)
		curMin, curMax =1, 1

		for n in nums:
			if n == 0:
				curMin, curMax=1, 1
				continue
			tmp = curMax * n
			curMax = max(n * curMax, n * curMin, n)
			curMin = max(tmp, n * curMin, n)
			res = max(res, curMax)
		return res



sol = Solution()
print(sol.max_product([2,3,-2,4]))
print(sol.max_product([2,-3,-2,4,-1, 96]))
print("----------------------------")
print(sol.max_product_lin([0,2,3,-2,4]))
print(sol.max_product_lin([0, 2,-3,-2,4,-1, 96]))
print(sol.max_product_lin([0, -1, -2, -3]))

print("----------------------------")
print(sol.maxProduct([0,2,3,-2,4]))
print(sol.maxProduct([0, 2,-3,-2,4,-1, 96]))
print(sol.maxProduct([0, -1, -2, -3]))





