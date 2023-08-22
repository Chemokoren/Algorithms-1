"""
Write an efficient program to find the sum of the contiguous subarray within a 
one-dimensional array of numbers that has the largest sum.

Given array, [-2,-3,4,-1,-2,1,5,-3], the answer is 7

4 +(-1)+(-2)+1+5 = 7

Kadane's algorithm

Initalize:
max_so_far = INT_MIN
max_ending_here =0

Loop for each element of the array
a) max_ending_here = max_ending_here + a[i]
b) if(max_so_far < max_ending_here)
    max_so_far = max_ending_here
c) if(max_ending_here < 0)
    max_ending_here =0
return max_so_far


Explanation

The simple idea of Kadane's algorithm is to look for all positive contiguous segments
of the array(max_ending_here is used for this). And keep track of the maximum sum 
contiguous segment among all positive segments(max_so_far is used for this). Each time we
get a positive-sum compare it with max_so_far and update max_so_far if it is greater than
max_so_far

    max_so_far = INT_MIN
    max_ending_here = 0

    for i=0,  a[0] =  -2
    max_ending_here = max_ending_here + (-2)
    Set max_ending_here = 0 because max_ending_here < 0
    and set max_so_far = -2

    for i=1,  a[1] =  -3
    max_ending_here = max_ending_here + (-3)
    Since max_ending_here = -3 and max_so_far = -2, max_so_far will remain -2
    Set max_ending_here = 0 because max_ending_here < 0
      
    
    for i=2,  a[2] =  4
    max_ending_here = max_ending_here + (4)
    max_ending_here = 4
    max_so_far is updated to 4 because max_ending_here greater 
    than max_so_far which was -2 till now

    for i=3,  a[3] =  -1
    max_ending_here = max_ending_here + (-1)
    max_ending_here = 3

    for i=4,  a[4] =  -2
    max_ending_here = max_ending_here + (-2)
    max_ending_here = 1

    for i=5,  a[5] =  1
    max_ending_here = max_ending_here + (1)
    max_ending_here = 2

    for i=6,  a[6] =  5
    max_ending_here = max_ending_here + (5)
    max_ending_here = 7
    max_so_far is updated to 7 because max_ending_here is 
    greater than max_so_far

    for i=7,  a[7] =  -3
    max_ending_here = max_ending_here + (-3)
    max_ending_here = 4

Note: The above algorithm only works if and only if at least one positive number should 
be present otherwise it does not work i.e if an Array contains all negative numbers it 
doesn’t work.

"""
# program to find maximum contiguous subarray

# Function to find the maximum contiguous subarray
# Time Complexity: O(n) | Auxiliary Space: O(1)
def maxSubArraySum(a):
    size =len(a)

    max_so_far = -float("inf")
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here =max_ending_here +a[i]
        if(max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


  
print("Maximum contiguous sum is", maxSubArraySum([-2, -3, 4, -1, -2, 1, 5, -3]))


'''
approach 2

'''
def maxSubArraySumTwo(a):
    size = len(a)

    max_so_far=a[0]
    max_ending_here =0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_ending_here < 0:
            max_ending_here = 0

        # Do not compare for all elements. Compare only when max_ending_here > 0
        elif (max_so_far < max_ending_here):
            max_so_far = max_ending_here
    return max_so_far

print("Maximum contiguous sum is", maxSubArraySumTwo([-2, -3, 4, -1, -2, 1, 5, -3]))


"""
Algorithm Paradigm: Dynamic Programming

- Handles the case when all numbers in the array are negative

Time complexity: O(n), where n is the size of the array.
Auxiliary Space: O(1)

"""
# program to find maximum contiguous subarray
def maxSubArraySumThree(a):
    size =len(a)
    max_so_far = a[0]
    curr_max =a[0]

    for i in range(1, size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far, curr_max)

    return max_so_far

print("Maximum contiguous sum is" , maxSubArraySum([-2, -3, 4, -1, -2, 1, 5, -3]))

"""
To print the subarray with the maximum sum, we maintain indices whenever we get the 
maximum sum.



"""

# program to print largest contiguous array sum
from sys import maxsize

# function to find the maximum contigous subarray and print its starting and end index
def maxSubArraySumFour(a):

    size = len(a)

    max_so_far =-maxsize -1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0

    for i in range(0, size):
        max_ending_here +=a[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i

        if max_ending_here < 0:
            max_ending_here = 0
            s = i+1

    print ("Maximum contiguous sum is %d"%(max_so_far))
    print ("Starting Index %d"%(start))
    print ("Ending Index %d"%(end))

 
maxSubArraySumFour([-2, -3, 4, -1, -2, 1, 5, -3])

"""
Kadane’s Algorithm can be viewed both as greedy and DP. As we can see that we are keeping 
a running sum of integers and when it becomes less than 0, we reset it to 0 (Greedy Part).
This is because continuing with a negative sum is way worse than restarting with a new 
range. Now it can also be viewed as a DP, at each stage we have 2 choices: Either take the
current element and continue with the previous sum OR restart a new range.
Both choices are being taken care of in the implementation.

Time Complexity: O(n)
Auxiliary Space: O(1)

Quiz
----
Given an array of integers (possibly some elements negative), write a C program to find 
out the *maximum product* possible by multiplying ‘n’ consecutive integers in the array
where n ≤ ARRAY_SIZE. Also, print the starting point of the maximum product subarray.

"""