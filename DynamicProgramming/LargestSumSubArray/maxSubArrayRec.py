from sys import maxsize
def maxSubArraySum(nums):
    for i in range(len(nums) - 1):
        if i == 1:
            return nums[0]
        if i == 2:
            return max(nums[-1], nums[1])

        max_val = -1
        max_val = max(max_val, maxSubArraySum(nums))
        for j in range(i - 2, 0):
            max_val = max(max_val, maxSubArraySum(nums) + nums[i - 1])
        return max_val


my_array = [1, 2, 3, 4, 5]
# my_array =[1,2,3,4,5,6]
my_array =[-2,1,-3,4,-1,2,1,-5,4]
print("first::", maxSubArraySum(my_array))


"""
kadane's algorithm

# Function to find the maximum contiguous subarray
# Algorithm doesn't work for all negative numbers.
# It returns 0 if all numbers are negative.

Complexity Analysis
Notice that each element has been visited only once.

Time Complexity = O(n)

Space Complexity = O(1)
"""
def maxSubArraySum1(a, size):
    max_so_far = 0
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_ending_here < 0:
            max_ending_here = 0

        # Do not compare for all elements. Compare only
        # when max_ending_here > 0
        elif (max_so_far < max_ending_here):
            max_so_far = max_ending_here

    return max_so_far

"""
Time Complexity: O(n)

Auxiliary Space: O(1)
"""
def maxSubArraySum2(a, size):
    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0

    for i in range(0, size):

        max_ending_here += a[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i

        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1

    print("Maximum contiguous sum is %d" % (max_so_far))
    print("Starting Index %d" % (start))
    print("Ending Index %d" % (end))


# Driver function to check the above function
# a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
# a = [1, 2, 3, 4, 5]
# a = [1,2,3,4,-5,6]
# a = [-2, -3, 4, -1, -2, 1, 5, -3]
a =[-2,1,-3,4,-1,2,1,-5,4]
print("Maximum contiguous sum is", maxSubArraySum1(a, len(a)))
