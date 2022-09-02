"""
Find all triplets with zero sum

Given an array of distinct elements. The task is to find triplets in the array whose sum is zero

Input : arr[] = {0, -1, 2, -3, 1}
Output : (0 -1 1), (2 -3 1)

Explanation : The triplets with zero sum are
0 + -1 + 1 = 0 and 2 + -3 + 1 = 0  

Input : arr[] = {1, -2, 1, 0, 5}
Output : 1 -2  1
Explanation : The triplets with zero sum is
1 + -2 + 1 = 0   

Method 1: This is a simple method that takes O(n3) time to arrive at the result.

Approach: 

- The naive approach runs three loops and check one by one that sum of three elements is zero or 
not. If the sum of three elements is zero then print elements otherwise print not found.

Algorithm: 
- Run three nested loops with loop counter i, j, k
- The first loops will run from 0 to n-3 and second loop from i+1 to n-2 and the third loop 
from j+1 to n-1. The loop counter represents the three elements of the triplet.
- Check if the sum of elements at i’th, j’th, k’th is equal to zero or not. If yes print the sum 
else continue.

    Time Complexity: O(n3). 
    As three nested loops are required, so the time complexity is O(n3).
    Auxiliary Space: O(1). 
    Since no extra space is required, so the space complexity is constant.


Method 2
--------

The second method uses the process of Hashing to arrive at the result and is solved at
a lesser time of O(n^2). 

Approach: This involves traversing through the array. For every element arr[i], find a pair with sum “-arr[i]”. This problem reduces to pair sum and can be solved in O(n) time using hashing.

Algorithm: 

    Create a hashmap to store a key-value pair.
    Run a nested loop with two loops, the outer loop from 0 to n-2 and the inner loop from i+1
    to n-1
    Check if the sum of ith and jth element multiplied with -1 is present in the hashmap or not
    If the element is present in the hashmap, print the triplet else insert the j’th element in 
    the hashmap.


    Time Complexity: O(n2). 
    Since two nested loops are required, so the time complexity is O(n2).
    Auxiliary Space: O(n). 
    Since a hashmap is required, so the space complexity is linear.

"""
def find_triplets(arr):
    n = len(arr)
    found = False
    res =[]

    for i in range(n-1):

        # Find all pairs with sum equals to "-arr[i]"
        s = set()
        for j in range(i+1, n):
            x =-(arr[i] + arr[j])
            if x in s:
                res.append([x, arr[i], arr[j]])
                found = True
            else:
                s.add(arr[j])
    if found == False:
        return "No Triplet Found"
    else:
        return res


print(" Trip Expected:[[2, -1, -1], [2, -3, 1]] , Actual: ",find_triplets([0, -1, 2, -3, 1]))
print(" Trip Expected:[1 -2  1], Actual: ",find_triplets([1, -2, 1, 0, 5]))


"""

Method 3: This method uses Sorting to arrive at the correct result and is solved in O(n2) time. 
 

Approach: The above method requires extra space. The idea is based on method 2 of this post. For every element check that there is a pair whose sum is equal to the negative value of that element.

Algorithm: 

    - Sort the array in ascending order.
    - Traverse the array from start to end.
    - For every index i, create two variables l = i + 1 and r = n – 1
    - Run a loop until l is less than r if the sum of array[i], array[l] and array[r] is equal to 
    zero then print the triplet and break the loop
    - If the sum is less than zero then increment the value of l, by increasing the value of l 
    the sum will increase as the array is sorted, so array[l+1] > array [l]
    - If the sum is greater than zero then decrement the value of r, by decreasing the value of r 
    the sum will decrease as the array is sorted, so array[r-1] < array [r].

    Time Complexity : O(n2). 
    Only two nested loops are required, so the time complexity is O(n2).
    Auxiliary Space : O(1), no extra space is required, so the time complexity is constant.
    
"""





'''
my tests
'''
def my_tests(arr):
    res =[]
    for i in range(len(arr)-2):
        for j in range(i+1, len(arr)-1):
            for k in range(j+1, len(arr)):
                if arr[i] +arr[j] + arr[k] ==0:
                    res.append([arr[i],arr[j], arr[k]])

    return res

print(" 1 Expected:[[2, -1, -1], [2, -3, 1]] , Actual: ",my_tests([0, -1, 2, -3, 1]))
print(" 2 Expected:[1 -2  1], Actual: ",my_tests([1, -2, 1, 0, 5]))




# Time complexity : O(n^2) | Space complexity: O(1)
def my_tests_two(arr):
    arr.sort()
    res =[]

    for i in range(len(arr)):


        start = i+1
        end =len(arr)-1

        while start <=end:
            if arr[start] + arr[end] +arr[i] ==0:
                res.append([arr[i], arr[start], arr[end]])
                start +=1
                end -=1
            elif arr[start] + arr[end] + arr[i] < 0:
                 start +=1
            else:
                end -=1
    return res

print("Expected:[[2, -1, -1], [2, -3, 1]] , Actual: ",my_tests_two([0, -1, 2, -3, 1]))
print("Expected:[1 -2  1], Actual: ",my_tests_two([1, -2, 1, 0, 5]))