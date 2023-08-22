"""
Given a sorted and rotated array find if there is a pair with a given sum

Given an array that is sorted and then rotated around an unknown point. Find if the array has a pair with 
a given sum 'x'. It may be assumed that all elements in the array are distinct.

Exampes:

Input: arr[] ={11, 15, 6, 8, 9, 10}, x =16
Output: True
There is a pair(6,10) with sum 16

Input: arr[] ={11,15,26,38,9,10}, x=35
Output: True
There is a pair (26, 9) with sum 35

Input: arr[] ={11,15,26,38,9,10}, x=45
Output: False
There is no pair with sum 45.

Time complexity: O(n)
The step to fid the pivot can be optimized to O(Log(n)) using  https://www.geeksforgeeks.org/find-minimum-element-in-a-sorted-and-rotated-array/
"""
# Program to find a pair with a given sum in a sorted and rotated array


# This function returns True if arr[0..n-1] has a pair with sum equals to x.
def pairInSortedRotated(arr, n, x):

    # find the pivot element
    for i in range(0, n-1):
        if(arr[i]> arr[i+1]):
            break
    # l is now index of smallest element
    l =(i+1) % n

    # r is now index of largest element
    r = i
    print("pivot point is: ", i+1, r)

    # keep moving either l or r till they meet
    while (l!=r):
        # if we find a pair with sum x, we return True
        if(arr[l] + arr[r] == x):
            return True
        
        # if current pair sum is less, move to the higher sum
        if(arr[l] + arr[r] < x):
            l =(l + 1) % n
        else:
            # Move to the lower sum side
            r = (n + r -1) % n

    return False

arr = [11, 15, 6, 8, 9, 10]
sum = 29
n = len(arr)

if (pairInSortedRotated(arr, n, sum)):
    print ("Array has two elements with sum 29")
else:
    print ("Array doesn't have two elements with sum 29 ")
        
        

"""
How to count all pairs having sum x?

steps:
- Find the pivot element of the sorted and the rotated array. The pivot element is the largest element in
the array. The smallest element will be adjacent to it.
- Use two pointers(say left and right) with the left pointer pointing to the smallest element and the right
pointer pointing to largest element.
- Find the sum of the elements pointed by both the pointers
- If the sum is equal to x, then increment the count. If the sum is less than x, then to increase sum move 
the left pointer to next position by incrementing it in a rational manner. If the sum is greater than x, then
to decrease sum, move the right pointer to next position by decrementing it in rational manner.
-Repeat step 3 and 4 until the left pointer is not equal to the right pointer or until the left pointer is 
not equal to right pointer -1
print final count
"""

# returns count of number of pairs with sum equals to x.
def pairsInSortedRotated(arr, n, x):

    # Find the pivot element - largest element of array
    for i in range(n):
        if arr[i] > arr[i+1]:
            break
    # l - index of smallest element
    l =(i + 1) % n

    # r is index of largest element
    r = i
    cnt = 0

    while(l != r):
        # if we find a pair with sum x, then increment cnt, move l and r to next element.
        if(arr[l]) + arr[r] ==x:
            cnt +=1

            # l and r will cross each other and loop will never terminate if this condition is not checked
            if(l == (r -1 +n) %n):
                return cnt

            l =(l+1) % n
            r =(r-1+n)% n

        # if current pair sum is less, move to the higher sum side
        elif arr[l] + arr[r] < x:
            l = (l +1) % n

        # if current pair sum is greater, move to the lower side
        else:
            r =(n+r-1) % n

    return cnt

arr = [11, 15, 6, 7, 9, 10]
s = 16

print("maneno:", pairsInSortedRotated(arr, 6, s))



''' Test '''

def pairInSortedRotatedUpdated(arr, n, x):

    count = 0

    # find the pivot element
    for i in range(0, n-1):
        if(arr[i]> arr[i+1]):
            break
    # l is now index of smallest element
    l =(i+1) % n

    # r is now index of largest element
    r = i
    print("pivot point is: ", i+1, r)

    # keep moving either l or r till they meet
    while (l!=r):
        # if we find a pair with sum x, we return True
        if(arr[l] + arr[r] == x):
            count +=1        
        # if current pair sum is less, move to the higher sum
        if(arr[l] + arr[r] < x):
            l =(l + 1) % n
        else:
            # Move to the lower sum side
            r = (n + r -1) % n

    return count

arr = [11, 15, 6, 7, 9, 10]
sum = 16
n = len(arr)

print("final count:",pairInSortedRotatedUpdated(arr, n, sum))