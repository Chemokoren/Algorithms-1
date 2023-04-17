# Algorithm Paradigm: Dynamic Programming
def maxSubArraySumBottomUp(a, size):
    max_so_far = a[0]
    curr_max = a[0]

    for i in range(1, size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far, curr_max)

    return max_so_far

a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
# a = [1, 2, 3, 4, 5]
# a = [1,2,3,4,-5,6]
# a = [-2, -3, 4, -1, -2, 1, 5, -3]
# a =[-2,1,-3,4,-1,2,1,-5,4]
print("Maximum contiguous sum is", maxSubArraySumBottomUp(a, len(a)))