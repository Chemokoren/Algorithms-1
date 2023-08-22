"""
Size of the Subarray with Maximum Sum

An array is given, find length of the subarray having maximum sum.

Examples : 

Input :  a[] = {1, -2, 1, 1, -2, 1}
Output : Length of the subarray is 2
Explanation: Subarray with consecutive elements 
and maximum sum will be {1, 1}. So length is 2

Input : ar[] = { -2, -3, 4, -1, -2, 1, 5, -3 }
Output : Length of the subarray is 5
Explanation: Subarray with consecutive elements 
and maximum sum will be {4, -1, -2, 1, 5}. 

This problem is mainly a variation of Largest Sum Contiguous Subarray Problem. The idea
is to update starting index whenever sum ending here becomes less than 0

Time Complexity: O(n).

Auxiliary Space: O(1)

"""

# function to find maximum contiguous subarray and print its starting and end index
def max_sub_array_sum(a):

    size = len(a)

    max_so_far=-float('inf')
    max_ending_here =0
    start = 0
    end  =0
    s = 0

    for i in range(0, size):

        max_ending_here += a[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i

        if max_ending_here < 0:
            max_ending_here = 0
            s = i+1

    return (end - start + 1)


print("Expected:2, Actual:",max_sub_array_sum([1, -2, 1, 1, -2, 1]))
print("Expected:5, Actual:",max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3]))



'''
my tests
'''
def my_tests(arr):
    max_sum =-float('inf')
    sum_here=0
    running_sum =0

    for i in range(len(arr)):
        if arr[i] < 0:
            sum_here =0
        else:
            sum_here +=arr[i]
        running_sum +sum_here
        max_sum =max(max_sum,running_sum)
    return max_sum



# print("Expected:2, Actual:",my_tests([1, -2, 1, 1, -2, 1]))


