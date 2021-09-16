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