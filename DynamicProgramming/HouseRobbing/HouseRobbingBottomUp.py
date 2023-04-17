'''
O(n^2)
'''

def RobBottomUp(n, nums):
    sub_solution =[-1] * (n)
    
    sub_solution[0] = nums[0]
    sub_solution[1] = max(nums[0], nums[1])
    for i in range(2, n):
        sub_solution[i] = sub_solution[i - 1]
        for j in range(i - 2, 0, -1):
            sub_solution[i] = max(sub_solution[i], sub_solution[j] + nums[i])
    return sub_solution[n -1]




'''
O(n)
'''
def RobBottomUp1(n, nums):
    sub_solution =[-1] * (n)
    
    sub_solution[0] = nums[0]
    sub_solution[1] = max(nums[0], nums[1])
    for i in range(2, n):
        sub_solution[i] = sub_solution[i - 1]
        sub_solution[i] = max(sub_solution[i-1], sub_solution[i-2] + nums[i])
    return sub_solution[n -1]




my_array = [1, 2, 3, 4, 5]
print(RobBottomUp1(5, my_array))