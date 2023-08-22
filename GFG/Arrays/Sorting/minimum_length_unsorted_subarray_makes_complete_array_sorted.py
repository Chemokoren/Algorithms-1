"""
Find the Minimum length Unsorted Subarray, sorting which makes the complete array sorted

Given an unsorted array arr[0..n-1] of size n, find the minimum length subarray arr[s..e] such
that sorting this subarray makes the whole array sorted.

Examples:

Examples: 

    If the input array is [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60], your program should be
    able to find that the subarray lies between the indexes 3 and 8.
    If the input array is [0, 1, 15, 25, 6, 7, 30, 40, 50], your program should be able to find 
    that the subarray lies between the indexes 2 and 5.

Find the candidate unsorted subarray
- Scan from left to right and find the first element which is greater than the next element. Let s
be the index of such an element. In the above example 1, s is 3 (index of 30)
- Scan from right to left and find the first element(first in right to left order) which is smaller 
than the next element(next in right to left order). Let e be the index of such an element.
In the above example 1, e is 7 

Check whether sorting the candidate unsorted subarray makes the complete array sorted or not. 
If not, then include more elements in the subarray.
1. Find the minimum and maximum values in arr[s..e]. Let minimum and maximum values be min and
max. min and max for [30,25,40,32,31] are 25 and 40 respectively.
2. Find the first element(if there is any) in arr[0..s-1] which is greater  than min, change s to
index of this element. There is no such element in above example 1.
3. Find the last element(if there is any) in arr[e+1..n-1] which is smaller than max, change e to
index of this element. In the above example 1, e is changed to 8(index of 35)

print s and e

Time Complexity : O(n) 
Auxiliary Space : O(1)
 

"""
# find the min length of unsorted subarray, sorting which makes the complete array sorted
def printUnsorted(arr):
    n = len(arr)
    e = n-1
    # step 1(a) of above algo
    for s in range(0, n-1):
        if arr[s]>arr[s+1]:
            break
    if s == n-1:
        print("The complete array is sorted")
        exit()
    #step 1(b)of above algo
    e = n-1
    while e > 0:
        if arr[e] < arr[e-1]:
            break
        e -=1
    
    # step 2(a) of above algo
    max = arr[s]
    min = arr[s]
    for i in range(s+1, e+1):
        if arr[i] > max:
            max =arr[i]
        if arr[i] < min:
            min = arr[i]

    # step 2(b) of above algo
    for i in range(s):
        if arr[i] > min:
            s = i
            break
    # step 2(c) of above algo
    i = n-1
    while i >= e+1:
        if arr[i]< max:
            e = i
            break
        i -= 1
    
    # step 3 of above algo
    print ("The unsorted subarray which makes the given array")
    print ("sorted lies between the indexes %d and %d"%( s, e))
printUnsorted([10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60])




def my_tests(arr):
    start= 0
    i = 0
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            start =i
            break
    
    for i in range(len(arr)-1, 0, -1):
        if arr[i] < arr[i-1]:
            end =i
            break
    # for i in range(start, end+1):
    #     if arr[i] > arr[i+1]:
    #         arr[i], arr[i+1] =arr[i+1],arr[i]
    vals =arr[start:end+2]
    vals.sort()
    k =0
    while k < len(vals):
        arr[start] =vals[k]
        k +=1
        start +=1
        
    return arr
# print(my_tests([0, 1, 15, 25, 6, 7, 30, 40, 50]))
print(my_tests([10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]))