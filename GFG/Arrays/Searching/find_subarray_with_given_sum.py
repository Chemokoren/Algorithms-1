"""
Find subarray with given sum | Set 1 (Non-negative Numbers)

Given an array arr[] of non-negative integers and an integer sum, find a continuous subarray that
adds to a given sum.

- There may be more than one subarrays with sum as the given sum, print first such subarray.

Examples: 

    Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
    Output: Sum found between indexes 2 and 4
    Explanation: Sum of elements between indices 2 and 4 is 20 + 3 + 10 = 33

    Input: arr[] = {1, 4, 0, 0, 3, 10, 5}, sum = 7
    Output: Sum found between indexes 1 and 4
    Explanation: Sum of elements between indices 1 and 4 is 4 + 0 + 0 + 3 = 7

    Input: arr[] = {1, 4}, sum = 0
    Output: No subarray found
    Explanation: There is no subarray with 0 sum

Find subarray with given sum using Nested loop

    The idea is to consider all subarrays one by one and check the sum of every subarray. Following program implements the given idea. 
    Run two loops: the outer loop picks a starting point i and the inner loop tries all subarrays starting from i.

Follow the steps given below to implement the approach:

    Traverse the array from start to end.
    From every index start another loop from i to the end of the array to get all subarrays starting from i, and keep a variable currentSum to calculate the sum of every subarray.
    For every index in inner loop update currentSum = currentSum + arr[j]
    If the currentSum is equal to the given sum then print the subarray.

Time Complexity: O(N2), Trying all subarrays from every index, used nested loop for the same
Auxiliary Space: O(1). 

"""
def sub_array_sum(arr, key):
    n = len(arr)

    # pick a starting point
    for i in range(n):
        currentSum  =arr[i]

        # try all subarrays starting with 'i'
        j = i + 1
        while j <= n:
            if currentSum ==key:
                return (i, j-1)

            if currentSum > key or j == n:
                break
            currentSum += arr[j]
            j +=1
    return -1

print("SS Expected:(2,4),Actual:", sub_array_sum([1, 4, 20, 3, 10, 5],33))
print("SS Expected:(1,4),Actual:", sub_array_sum([1, 4, 0, 0, 3, 10, 5],7))
print("SS Expected:-1,Actual:", sub_array_sum([1, 4],0))
print("SS Expected:-1,Actual:", sub_array_sum([15, 2, 4, 8, 9, 5, 10, 23],23))

"""

Find subarray with given sum using Sliding Window

    The idea is simple as we know that all the elements in subarray are positive so, If a subarray
     has sum greater than the given sum then there is no possibility that adding elements to the 
     current subarray will be equal to the given sum. So the Idea is to use a similar approach 
     to a sliding window. 

        Start with an empty subarray 
        add elements to the subarray until the sum is less than x( given sum ). 
        If the sum is greater than x, remove elements from the start of the current subarray.

Follow the steps given below to implement the approach:

    Create two variables, start=0, currentSum = arr[0]
    Traverse the array from index 1 to end.
    Update the variable currentSum by adding current element, currentSum = currentSum + arr[i]
    If the currentSum is greater than the given sum, update the variable currentSum as currentSum = currentSum – arr[start],
    and update start as, start++.
    If the currentSum is equal to given sum, print the subarray and break the loop.

"""

# Time Complexity: O(N) | Auxiliary Space: O(1) 
def sub_array_sum_two_1(arr, key):
    n = len(arr)

    current_sum  =arr[0]
    start = 0

    i = 1
    while i <= n:

        while current_sum > key and start < i-1:
            current_sum = current_sum -arr[start]
            start +=1
        if current_sum == key:
            return (start, i-1)

        if i < n:
            current_sum += arr[i]
        i +=1
    return -1

print("KK Expected:(2,4),Actual:", sub_array_sum_two_1([1, 4, 20, 3, 10, 5],33))
print("KK Expected:(1,4),Actual:", sub_array_sum_two_1([1, 4, 0, 0, 3, 10, 5],7))
print("KK Expected:-1,Actual:", sub_array_sum_two_1([1, 4],0))
print("KK Expected:-1,Actual:", sub_array_sum_two_1([15, 2, 4, 8, 9, 5, 10, 23],23))



'''
my tests
'''
# Time complexity : O(n) | Space complexity: O(1)
def my_tests(arr,key):

    start = 0
    end = 0

    while start <= end and end <= len(arr)-1:
        if sum(arr[start:end+1]) == key:
            return (start, end)
        elif sum(arr[start:end+1]) < key:
            end +=1
        else:
            start +=1
    return -1

print("Expected:(2,4),Actual:", my_tests([1, 4, 20, 3, 10, 5],33))
print("Expected:(1,4),Actual:", my_tests([1, 4, 0, 0, 3, 10, 5],7))
print("Expected:-1,Actual:", my_tests([1, 4],0))

# Time complexity: O(n^2) | Space complexity : O(1)
def my_tests_two(arr, key):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if sum(arr[i:j+1]) == key:
                return (i, j)
    return -1

print("Expected:(2,4),Actual:", my_tests_two([1, 4, 20, 3, 10, 5],33))
print("Expected:(1,4),Actual:", my_tests_two([1, 4, 0, 0, 3, 10, 5],7))
print("Expected:-1,Actual:", my_tests_two([1, 4],0))

# incomplete
def sub_array_sum_two(arr, key):
    start = 0
    current_sum =arr[0]

    i =1
    while i <= len(arr)-1:
        if current_sum == key:
            return (start, i-1)
        elif current_sum > key:
            current_sum =current_sum- arr[start]
            start +=1
        else:
            current_sum += arr[i]
            i +=1
    return -1


print("TT Expected:(2,4),Actual:", sub_array_sum_two([1, 4, 20, 3, 10, 5],33))
print("TT Expected:(1,4),Actual:", sub_array_sum_two([1, 4, 0, 0, 3, 10, 5],7))
print("TT Expected:-1,Actual:", sub_array_sum_two([1, 4],0))
print("TT Expected:-1,Actual:", sub_array_sum_two([15, 2, 4, 8, 9, 5, 10, 23],23))