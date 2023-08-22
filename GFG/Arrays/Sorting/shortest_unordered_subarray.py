"""

Shortest Un-ordered Subarray

An array is given of n length, and the problem is that we have to find the length of the 
shortest unordered(neiter increasing nor decreasing) sub array in the given array.

Examples: 

Input : n = 5
        7 9 10 8 11
Output : 3
Explanation : 9 10 8 unordered sub array.

Input : n = 5
       1 2 3 4 5
Output : 0 
Explanation :  Array is in increasing order.

The idea is based on the fact that size of shortest subarray would be either 0 or 3. We have to
check array element is either increasing or decreasing, if all array elements are in increasing
or decreasing, then length of shortest sub array is 0, and if either the array element is not 
following the increasing or decreasing then it's shortest length is 3.


"""
# checks if array eelemts are increasing
def increasing(a):
    n =len(a)

    for i in range(0, n-1):
        if(a[i] >=a[i+1]):
            return False
    return True

# check if array elements are in decreasing
def decreasing(a):
    n =len(a)

    for i in range(0, n-1):
        if a[i] < a[i+1]:
            return False
    return True

def shortestUnsorted(a):
    n =len(a)

    if(increasing(a) == True or decreasing == True):
        return 0
    else:
        return 3


print("Expected: 3, Actual:",shortestUnsorted([7, 9, 10, 8, 11]))



'''
my tests 
'''
def my_tests(arr):

    longest_sbr =-float('inf')
    longest_str = None
    
    if is_sorted(arr):
         return 0
    for i in range(len(arr)-1):
        left =i-1
        right =i+1

        

        if ((arr[left] < arr[i] and arr[right] > arr[i] ) or (arr[right] < arr[i] and arr[left] > arr[i])) :
            left -=1
            right +=1

        if len(arr[left:right+1]) > longest_sbr:
            longest_sbr =len(arr[left:right+1])
            longest_str =arr[left:right+1]

    return longest_str

def is_sorted(arr):
    i =1

    while i < len(arr)-1:
        if arr[i-1] < arr[i] and arr[i+1] >arr[i]:
            i +=1
        else:
            return False
    return True



print("Expected:[9,10,8], Actual:", my_tests([7,9,10,8,11]))
print("Expected:[0], Actual:", my_tests([1,2,3,4,5]))

 
