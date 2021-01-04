def RobBottomUp(n, nums):
    R[n] =[]
    R[0] = nums[0]
    R[1] = max(nums[0], nums[1])
    for i in range(2, n):
        R[i] = R[i - 1]
        for j in range(i - 2, 0):
            R[i] = max(R[i], R[j + nums[i]])
    return R[n - 1]




my_array = [1, 2, 3, 4, 5]
# my_array =[1,2,3,4,5,6]
print(RobBottomUp(5, my_array))