from typing import List
"""
Given an integer array nums, find the contiguous subarray with an array(containing at least 
one number) which has the largest product.

Input: [2,3,-2,4]
Output: 6

Explanation: [2,3] has the largest product 6.

"""

# using Dynamic Programming
class Solution:

    def maxProduct(self, nums: List[int])-> int:
        res = max(nums)
        curMin, curMax = 1,1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            tmp = curMax *n
            curMax = max(n*curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        return res

sol =Solution()

print("DP Expected:6",sol.maxProduct([0,2,3,-2,4]))
print("DP Expected:4",sol.maxProduct([2,0,3,-2,4]))

"""

my tests

"""

def my_tests(arr):
    start = 0
    end = len(arr)
    i=0
    running_product = arr[i]
    
    while start <= end-1:

        if(arr[i] ==0 or arr[i] < 0):
            i +=1
            start =i
            
        if(arr[i] > 0 and arr[i] <=end-2):
            i +=1
        product_now =find_product(arr[start:i+1])
        running_product= max(arr[i],running_product,product_now)
        
        i +=1
        start =i
    return running_product
		
		
def find_product(arr):
    if len(arr) ==1:
        return arr[0]
    else:
        product_val =1
        for i in arr:
            product_val =product_val*i
        return product_val
	
print("Expected:6, Actual:", my_tests([2,3,-2,4]))
print("Expected:6, Actual:", my_tests([0,2,3,-2,4]))
print("Expected:4, Actual:", my_tests([2,0,3,-2,4]))


def maxProduct(nums):
    max_val=nums[0]
    curProd=1
    for i in nums:
        if i ==0:
            i =1
        curProd =i * curProd
        max_val=max(max_val, curProd, i)
    return max_val


# print("Product Expected:6, Actual:",maxProduct([0,2,3,-2,4]))
# print("Product Expected:4, Actual:",maxProduct([2,0,3,-2,4]))