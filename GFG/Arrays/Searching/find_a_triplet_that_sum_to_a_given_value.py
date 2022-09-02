"""
Find a triplet that sum to a given value

given an array and a value, find if there is a triplet in array whose sum is equal to the given 
value. If there is such a triplet present in array, then print the triplet and return true. Else
return false.

Input: array = {12, 3, 4, 1, 6, 9}, sum = 24; 
Output: 12, 3, 9 
Explanation: There is a triplet (12, 3 and 9) present 
in the array whose sum is 24. 
Input: array = {1, 2, 3, 4, 5}, sum = 9 
Output: 5, 3, 1 
Explanation: There is a triplet (5, 3 and 1) present 
in the array whose sum is 9.

Method 1: This is the naive approach towards solving the above problem.  

 

    Approach: A simple method is to generate all possible triplets and compare the sum of every 
    triplet with the given value. The following code implements this simple method using three 
    nested loops.
    Algorithm: 
        Given an array of length n and a sum s
        Create three nested loop first loop runs from start to end (loop counter i), second loop
        runs from i+1 to end (loop counter j) and third loop runs from j+1 to end (loop counter k)
        The counter of these loops represents the index of 3 elements of the triplets.
        Find the sum of ith, jth and kth element. If the sum is equal to given sum. Print the 
        triplet and break.
        If there is no triplet, then print that no triplet exist.


Method 2: This method uses sorting to increase the efficiency of the code. 

    Approach: By Sorting the array the efficiency of the algorithm can be improved. This efficient 
    approach uses the two-pointer technique. Traverse the array and fix the first element of the 
    triplet. Now use the Two Pointers algorithm to find if there is a pair whose sum is equal to
     x – array[i]. Two pointers algorithm take linear time so it is better than a nested loop.

    Algorithm : 
        Sort the given array.
        Loop over the array and fix the first element of the possible triplet, arr[i].
        Then fix two pointers, one at i + 1 and the other at n – 1. And look at the sum, 
            If the sum is smaller than the required sum, increment the first pointer.
            Else, If the sum is bigger, Decrease the end pointer to reduce the sum.
            Else, if the sum of elements at two-pointer is equal to given sum then print the 
            triplet and break.

    Time complexity: O(N^2). 
    There are only two nested loops traversing the array, so time complexity is O(n^2). 
    Two pointers algorithm takes O(n) time and the first element can be fixed using another nested 
    traversal.
    Space Complexity: O(1). 
    As no extra space is required.

"""

def find_3_numbers(arr, key):
    arr_size =len(arr)

    arr.sort()

    # fix the first element one by one and find the other two elements
    for i in range(0, arr_size-2):

        # to find the other two elements, start two index variables from two corners of the 
        # array and move them toward each other

        # index of the first element in the remaining elements
        l = i +1
        r = arr_size-1

        while (l < r):
            if(arr[i] + arr[l] +arr[r] == key):
                return [arr[i] , arr[l] , arr[r]], True
            elif (arr[i] + arr[l] +arr[r] < key):
                l += 1
            else:
                r -=1
    return False


print("3 Expected:[12,3,9], Actual:", find_3_numbers([12, 3, 4, 1, 6, 9], 24))
print("3 Expected:[5, 3, 1], Actual:", find_3_numbers([1, 2, 3, 4, 5], 9))


"""

Method 3: This is a Hashing-based solution. 

    Approach: This approach uses extra space but is simpler than the two-pointers approach. 
    Run two loops outer loop from start to end and inner loop from i+1 to end. Create a hashmap or
    set to store the elements in between i+1 to j-1. So if the given sum is x, check if there is 
    a number in the set which is equal to x – arr[i] – arr[j]. If yes print the triplet. 
     
    Algorithm: 
        Traverse the array from start to end. (loop counter i)
        Create a HashMap or set to store unique pairs.
        Run another loop from i+1 to end of the array. (loop counter j)
        If there is an element in the set which is equal to x- arr[i] – arr[j], then print the 
        triplet (arr[i], arr[j], x-arr[i]-arr[j]) and break
        Insert the jth element in the set.

Time complexity: O(N^2) 
Auxiliary Space: O(N), since n extra space has been taken.

"""
def find_3_Numbers_two(A,  sum):
    arr_size = len(A)
    for i in range(0, arr_size-1):
        # Find pair in subarray A[i + 1..n-1]
        # with sum equal to sum - A[i]
        s = set()
        curr_sum = sum - A[i]
        for j in range(i + 1, arr_size):
            if (curr_sum - A[j]) in s:
                print("Triplet is", A[i],
                        ", ", A[j], ", ", curr_sum-A[j])
                return True
            s.add(A[j])
     
    return False

print("33 Expected:[12,3,9], Actual:", find_3_Numbers_two([12, 3, 4, 1, 6, 9], 24))
print("33 Expected:[5, 3, 1], Actual:", find_3_Numbers_two([1, 2, 3, 4, 5], 9))










print("\n my tests \n")
'''
my tests
'''

# Time complexity: O(n^3) | Space complexity : O(1)
def my_tests(arr, key):
    for i in range(len(arr)-2):
        for j in range(i+1, len(arr)-1):
            for k in range(j+1, len(arr)):
                if (arr[i] + arr[j] + arr[k]) == key:
                    return [arr[i], arr[j], arr[k]], True
    return False

print("Expected:[12,3,9], Actual:", my_tests([12, 3, 4, 1, 6, 9], 24))
print("Expected:[5, 3, 1], Actual:", my_tests([1, 2, 3, 4, 5], 9))

# Time complexity : O(n^2) | Space complexity : O(n)
def my_tests_two(arr, key):
    for i in range(len(arr)):
        new_val =key-arr[i]
        new_arr = arr.copy()
        new_arr.remove(new_arr[i])
        new_arr.sort()

        start =0
        end = len(new_arr) -1

        while start <=end:
            if new_arr[start] + new_arr[end] == new_val:
                return [arr[i], new_arr[start], new_arr[end]], True
            elif new_arr[start] + new_arr[end] < new_val:
                start +=1
            else:
                end -=1
    return False

print("2 Expected:[12,3,9], Actual:", my_tests_two([12, 3, 4, 1, 6, 9], 24))
print("2 Expected:[5, 3, 1], Actual:", my_tests_two([1, 2, 3, 4, 5], 9))

def triplet_sum(arr, key):
    arr.sort()

    
    start = 0
    end =len(arr)-1

    l =start +1
    while l <=end:
        
        if(arr[start] +arr[end] +arr[l]) == key:
            return [arr[l], arr[start], arr[end]], True
        elif (arr[start] +arr[end] + arr[l]) < key:
            l +=1
        else:
            end -=1
        start +=1
    return False

print("Expected:[12,3,9], Actual:", triplet_sum([12, 3, 4, 1, 6, 9], 24))
print("Expected:[5, 3, 1], Actual:", triplet_sum([1, 2, 3, 4, 5], 9))