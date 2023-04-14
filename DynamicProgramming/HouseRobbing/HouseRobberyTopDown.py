"""

"""
def HouseRobberyTopDown(i,nums):
    sub_solutions =[-1] * (i+1)
    if(i == 0):
        return nums[0]
    
        
    max_val = -1
    max_val =max(max_val, HouseRobberyTopDown(i-1, nums))
    
    for j in range(i-2,0,-1):
        if sub_solutions[j] != -1:
            max_val =sub_solutions[j]
        max_val =max(max_val, HouseRobberyTopDown(j, nums)+ nums[i-1])
        sub_solutions[j] =max_val
        
    return max_val
	
nums =[1,2,3,4,5]

print(HouseRobberyTopDown(5, nums))

def dfs(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
    return max(dfs(nums[1:]), dfs(nums[2:]) + nums[0]) # starting from the start





def dfs1(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])
    
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    
    return dp[-1]


nums =[1,2,3,4,5]

print(dfs1(nums))