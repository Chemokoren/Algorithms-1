"""
K maximum sums of non-overlapping contiguous sub-arrays

Given an Array of Integers and an Integer value k, find out k
non-overlapping sub-arrays which have k maximum sums.

Examples: 

Input : arr1[] = {4, 1, 1, -1, -3, -5, 6, 2, -6, -2}, 
             k = 3.
Output : Maximum non-overlapping sub-array sum1: 8, 
         starting index: 6, ending index: 7.
         
         Maximum non-overlapping sub-array sum2: 6, 
         starting index: 0, ending index: 2.
         
         Maximum non-overlapping sub-array sum3: -1, 
         starting index: 3, ending index: 3.

Input : arr2 = {5, 1, 2, -6, 2, -1, 3, 1}, 
           k = 2.
Output : Maximum non-overlapping sub-array sum1: 8, 
         starting index: 0, ending index: 2.

         Maximum non-overlapping sub-array sum2: 5, 
         starting index: 4, ending index: 7.
Prerequisite: Kadane's algorith

Kadane's algorithm finds out only the maximum subarray sum, but using the same algorithm we
can find out k maximum non-overlapping subarray sums.

approach:
- Find out the maximum subarray in the array using Kadane's algorithm. Also find out its
starting and end indices. Print the sum of this subarray.
- Fill each cell of this subarray by -infinity.
- Repeat process 1 and 2 for k times

Time Complexity: The outer loop runs for k times and kadane’s algorithm in each iteration 
runs in linear time O(n). Hence the overall time complexity is O(k*n).

"""

# program to find out k maximum non-overlapping subarray sums.

# Function to compute k maximum sub-array sums.
def kmax(arr, k, n):
    # in each iteration it will give the ith maximum subarray sum
    for c in range(k):

        # Kadane's algorithm
        max_so_far =-float("inf")
        max_here = 0


        # compute starting and  ending index of each of the subarray
        start = 0
        end = 0
        s = 0

        for i in range(n):
            max_here += arr[i]
            if(max_so_far < max_here):
                max_so_far = max_here
                start =s
                end = i

            if (max_here < 0):
                max_here =0
                s = i + 1

        # print out the result
        print("Maximum non-overlapping sub-array sum", c + 1, ": ", max_so_far,", starting index",
        start, ", ending index: ", end, ".", sep=" ")

        # replace all elements of the maximum subarray by -infinity. Hence these places cannot
        # form maximum sum subarray again.

        for l in range(start, end+1):
            arr[l] = -float("inf")
    print()


arr1 = [4, 1, 1, -1, -3, -5, 6, 2, -6, -2]
k1 = 3
n1 = len(arr1)
 
# Function calling
kmax(arr1, k1, n1)
 
# Test case 2
arr2 = [5, 1, 2, -6, 2, -1, 3, 1]
k2 = 2
n2 = len(arr2)
 
# Function calling
kmax(arr2, k2, n2)
