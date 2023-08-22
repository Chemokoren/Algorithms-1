"""
you are a professional robber planning to rob houses along a street. Each house has a 
certain amount of money stashed, the only constraint stopping you from robbing each of 
them is that adjacent houses have security system connected and it will automatically 
contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.

A[1..5] ={1, 2, 3, 4, 5}

"""

def HouseRobberyRec(i,nums):
    if(i == 0):
        return nums[0]
        
    max_val = -1
    max_val =max(max_val, HouseRobberyRec(i-1, nums))
    
    for j in range(i-2,0,-1):
        max_val =max(max_val, HouseRobberyRec(j, nums)+ nums[i-1])
        
    return max_val
	
nums =[1,2,3,4,5]

print(HouseRobberyRec(5, nums))


    
def dfs(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
    # return max(dfs(nums[:-1]), dfs(nums[:-2]) + nums[-1]) # starting from the end
    return max(dfs(nums[1:]), dfs(nums[2:]) + nums[0]) # starting from the start



nums =[1,2,3,4,5]

print(dfs(nums))