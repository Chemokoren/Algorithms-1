"""
Two Pointers Technique

Two pointers is really an easy and effective technique that is typically used for searching
 pairs in a sorted array.
Given a sorted array A (sorted in ascending order), having N integers, find if there exists any
 pair of elements (A[i], A[j]) such that their sum is equal to X.


 A[] = {10, 20, 35, 50, 75, 80}
X = =70
i = 0
j = 5

A[i] + A[j] = 10 + 80 = 90
Since A[i] + A[j] > X, j--
i = 0
j = 4

A[i] + A[j] = 10 + 75 = 85
Since A[i] + A[j] > X, j--
i = 0
j = 3

A[i] + A[j] = 10 + 50 = 60
Since A[i] + A[j] < X, i++
i = 1
j = 3
m
A[i] + A[j] = 20 + 50 = 70


The working of two pointer algorithm in brief is as follows. The algorithm basically uses the fact
 that the input array is sorted. We start the sum of extreme values (smallest and largest) and 
 conditionally move both pointers. We move left pointer ‘i’ when the sum of A[i] and A[j] is less 
 than X. We do not miss any pair because the sum is already smaller than X. Same logic applies for
 right pointer j.


Method 2: Two Pointers Technique

Now let’s see how the two-pointer technique works. We take two pointers, one representing the
 first element and other representing the last element of the array, and then we add the values
  kept at both the pointers. If their sum is smaller than X then we shift the left pointer to 
  right or if their sum is greater than X then we shift the right pointer to left, in order to 
  get closer to the sum. We keep moving the pointers until we get the sum as X. 

"""

# Time Complexity:  O(n log n) (As sort function is used) | Auxiliary Space: O(1)
def my_tests(arr,x):
    start = 0
    end = len(arr)-1
    while start < end:
        if(arr[start] + arr[end]) == x:
            return (start, end)
        elif (arr[start] + arr[end]) < x:
            start +=1
        else:
            end -=1



print("Expected: (), Actual:", my_tests([10, 20, 35, 50, 75, 80], 70))


"""

Naive approach

"""
# Time Complexity:  O(n2) | Auxiliary Space: O(1)
def my_tests_naive(arr, x):

    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                continue
            if arr[i] +arr[j] == x:
                return (i, j)

print("Naive Expected: (), Actual:", my_tests_naive([10, 20, 35, 50, 75, 80], 70))

