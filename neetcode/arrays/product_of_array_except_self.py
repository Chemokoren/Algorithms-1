"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product 
of all the elements of nums except nums[i].

The product of any prefix or suffic of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

input: nums =[1, 2, 3, 4]
output: [24, 12, 8, 6]

Example 2:

Input: nums =[-1, 1, 0,-3,3]
Output: [0, 0, 9, 0, 0]

"""

from typing import List
class Solution:

    def productExceptSelf(self, nums:List[int])->List[int]:
        res =[1] * (len(nums))

        prefix =1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        print("prefix:::", res)
       
        postfix =1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        print("postfix:::", res)
        return res
        
        
sol =Solution()
print("Expected:[24, 12, 8, 6],Actual:",sol.productExceptSelf([1,2,3,4]))


"""
my tests 
"""

def product_arr(arr):
	product_val =1
	
	for i in arr:
		product_val =product_val *i
	return product_val
	
def my_tests(arr):
	
	res_arr =[]
	
	for i in range(len(arr)):
		arr_val=[]
		if i ==0:
			arr_val=arr[1:]
		else:
			start = i -1
			end = i +1
			
			while start > -1:
				arr_val.append(arr[start])
				start -=1
				
			while end <len(arr):
				arr_val.append(arr[end])
				end +=1
				
		res =product_arr(arr_val)
		res_arr.append(res)
		
	return res_arr
	
print("Expected:[24, 12, 8, 6], Actual:", my_tests([1, 2, 3, 4]))


'''
using lambda
'''
from functools import reduce
	
def my_tests_lambda(arr):
	
	res_arr =[]
	
	for i in range(len(arr)):
		
		new_arr =arr.copy()
		new_arr[i]=1
		new_val =reduce((lambda x, y: x*y),new_arr)
		res_arr.append(new_val)
				
		
	return res_arr
	
print("Expected:[24, 12, 8, 6], Actual:", my_tests_lambda([1, 2, 3, 4]))

from functools import reduce 
def my_tests_two():
	nums = [1, 2, 3, 4]

	# calculate prefix values
	prefix =[]
	postfix =[0]*len(nums)
	n = len(nums)-1
	
	for i in range(len(nums)):
		
		val =reduce(lambda x,y: x*y, nums[:i+1])
		prefix.append(val)
	
			
	# calculate postfix values
	for i in range(len(nums)-1, -1, -1):
		postfix[n]= (reduce(lambda x,y: x*y, nums[i:]))
		n -=1
					
			

	new_arr =[]
	for i in range(len(nums)):
		if i == 0:
			prefix_val = 1
		else:
			prefix_val= prefix[i-1]
		
		if i == len(nums)-1:
			postfix_val =1
		else:
			postfix_val =postfix[i+1]
			
		new_arr.append(prefix_val *postfix_val)
	return new_arr
	
print(my_tests_two())
	
	
		
	