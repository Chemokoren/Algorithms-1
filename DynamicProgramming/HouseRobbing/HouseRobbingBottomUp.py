'''
O(n^2)
'''

def RobBottomUp(n, nums):
    R =[-1] * (n)
    
    R[0] = nums[0]
    R[1] = max(nums[0], nums[1])
    for i in range(2, n):
        R[i] = R[i - 1]
        for j in range(i - 2, 0, -1):
            R[i] = max(R[i], R[j] + nums[i])
    return R[n -1]




'''
O(n)
'''
def RobBottomUp1(n, nums):
    R =[-1] * (n)
    
    R[0] = nums[0]
    R[1] = max(nums[0], nums[1])
    for i in range(2, n):
        R[i] = R[i - 1]
        R[i] = max(R[i-1], R[i-2] + nums[i])
    return R[n -1]




my_array = [1, 2, 3, 4, 5]
print(RobBottomUp1(5, my_array))