# using 3 loops
print("############################### using 3 loops ######################")
def maxSubarraySumBruteForce1( A , n):
    max_sum = 0
    for i in range(0, n-1):
        for j  in range(i,n-1):
          sum = 0
          for k in range(i,j):
              sum = sum + A[k]
          if(sum > max_sum):
              max_sum = sum
    return max_sum
if __name__ == '__main__':
    A = [3, 4, -7, 1, 3, 3, 1, -4]
    expected_sum = 7
    print(maxSubarraySumBruteForce1(A, expected_sum))

# using 2 loops -optimized brute-force
print("############################### using 2 loops ######################")
def max_Subarray_Sum(A, n):
    max_sum = 0
    for i in range(0, n-1):
       sum=0
       for j in range(i,n-1):
           sum = sum +  A[j]
           if(sum > max_sum):
               max_sum = sum
    return max_sum

if __name__ == '__main__':
    A = [3, 4, -7, 1, 3, 3, 1, -4]
    expected_sum = 7
    print(max_Subarray_Sum(A, expected_sum))


print("############################### second brute-force ######################")

# Function to find subarray with the given the expected sum in a list
def findSubArrayBruteForce(A, expected_sum):
    for i in range(len(A)):

        expected_sum_so_far = 0

        # consider all subarrays starting from `i` and ending at `j`
        for j in range(i, len(A)):

            # expected_sum of elements so far
            expected_sum_so_far += A[j]

            # if the expected_sum so far is equal to the given expected_sum
            if expected_sum_so_far == expected_sum:
                # print subarray `A[i, j]`
                print(A[i:j + 1])


if __name__ == '__main__':
    A = [3, 4, -7, 1, 3, 3, 1, -4]
    expected_sum = 7

    findSubArrayBruteForce(A, expected_sum)

print("############################### end of brute-force ######################")

# Returns true if the there is a subarray
# of arr[] with sum equal to 'expected_sum'
# otherwise returns # false.

def subArraySum(arr, expected_sum):
    # Pick a starting point
    n =len(arr)
    for i in range(n):
        curr_sum = arr[i]

        # try all subarrays starting with 'i'
        j = i + 1
        while j <= n:
            if curr_sum == expected_sum:
                print("subarray sum found between indexes (inclusive): % d and % d" % (i, j - 1))
                return 1

            if curr_sum > expected_sum or j == n:
                break

            curr_sum = curr_sum + arr[j]
            j += 1

    print("No subarray found")
    return 0


# main function to test subArraySum program
if __name__ == "__main__":
    # arr = [15, 2, 4, 8, 9, 5, 10, 23]
    # expected_sum = 23
    arr = [3, 4, -7, 1, 3, 3, 1, -4]
    expected_sum = 7
    n = len(arr)

    subArraySum(arr, expected_sum)



"""
# using sliding window

Time Complexity : O(n). 

Only one traversal of the array is required. So the time complexity is O(n).

Space Complexity: O(1). 

As constant extra space is required.

"""
print("############################### Sliding Window Approach ######################")


# An efficient program to print subarray
# with sum as given sum

# Returns true if there is a subarray
# of arr[] with sum equal to 'sum'
# otherwise returns false & prints
# the result.
def subArraySum(arr_, expected_sum):
    # Initialize curr_sum as value of first element
    # and starting point as 0

    n = len(arr_)
    curr_sum = arr_[0]
    start = 0

    # Add elements one by one to curr_sum and
    # if the curr_sum exceeds the sum, then remove
    # starting element

    i = 1
    while i <= n:

        # If curr_sum exceeds the expected_sum,
        # then remove the starting elements
        while curr_sum > expected_sum and start < i - 1:
            curr_sum = curr_sum - arr_[start]
            start += 1

        # If curr_sum becomes equal to sum,
        # then return true
        if curr_sum == expected_sum:
            print("subarray sum found between indexes (inclusive): % d and % d" % (start, i - 1))
            return 1

        # Add this arr_[i] to curr_sum
        if i < n:
            curr_sum = curr_sum + arr_[i]
        i += 1

    # If at this point there is no subarray
    print("No subarr_ay found")
    return 0


# main function to test subArraySum program
if __name__ =='__main__':
    arr = [15, 2, 4, 8, 9, 5, 10, 23]

    expected_sum = 23

    subArraySum(arr, expected_sum)



print("#################################### using hash maps ##########################")

"""
using hash maps

Complexity Analysis:

Time complexity: O(N).
If hashing is performed with the help of an array then this the time complexity.
In case the elements cannot be hashed in an array a hash map can also be used as shown in the above code.

Auxiliary space: O(n).
As a HashMap is needed, this takes a linear space.

"""


# Python3 program to print subarray with sum as given sum

# Function to print subarray with sum as given sum
def subArraySum(arr, n, Sum):
    # create an empty map
    Map = {}

    # Maintains sum of elements so far
    curr_sum = 0

    for i in range(0, n):

        # add current element to curr_sum
        curr_sum = curr_sum + arr[i]

        # if curr_sum is equal to target sum
        # we found a subarray starting from index 0
        # and ending at index i
        if curr_sum == Sum:
            print("Sum found between indexes 0 to", i)
            return

        # If curr_sum - sum already exists in map
        # we have found a subarray with target sum
        if (curr_sum - Sum) in Map:
            print("Sum found between indexes", \
                  Map[curr_sum - Sum] + 1, "to", i)

            return

        Map[curr_sum] = i

    # If we reach here, then no subarray exists
    print("No subarray with given sum exists")


# Driver program to test above function
if __name__ == "__main__":

    n = len(arr)

    # arr = [10, 2, -2, -20, 10]
    arr = [15, 2, 4, 8, 9, 5, 10, 23]
    # sum_ = -10
    sum_ = 23

    subArraySum(arr, n, sum_)
