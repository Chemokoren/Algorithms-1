"""

Print All Distinct Elements of a given integer array

Given an integer array, print all distinct elements in array. The given array may 
contain duplicates and the output should print every element only once. The given array is not 
sorted.

Input: arr[] = {12, 10, 9, 45, 2, 10, 10, 45}
Output: 12, 10, 9, 45, 2

Input: arr[] = {1, 2, 3, 4, 5}
Output: 1, 2, 3, 4, 5

Input: arr[] = {1, 1, 1, 1, 1}
Output: 1


Simple Solution - use two nested loops
The outer loop picks an element one by one starting from the leftmost element. the inner 
loop checks if element is present on the left side of it. If present, then ignores the element,
else prints the element,

"""
# Time Complexity: O(n2) | Auxiliary Space: O(1)
def print_distinct(arr):
    n = len(arr)

    # pick all elements one by one
    for i in range(0,n):
        # check if the picked element is already printed
        d = 0
        for j in range(0, i):
            if(arr[i] == arr[j]):
                d = 1
                break
        # if not printed earlier, then print it
        if(d == 0):
            print(arr[i])

print_distinct([6, 10, 5, 4, 9, 120, 4, 6, 10])

"""
We can Use Sorting to solve the problem in O(nLogn) time. The idea is simple, first sort 
the array so that all occurrences of every element becomes consecutive. Once the occurrences 
become consecutive, we can traverse the sorted array and print distinct elements in O(n) time.


"""
# Time Complexity: O(n log n). | Auxiliary Space: O(1)
def printDistinct(arr):
    n = len(arr)
    arr.sort()

    for i in range(n):
        # move the index ahead while there are duplicates
        if(i < n-1 and arr[i] == arr[i+1]):
            while (i < n-1 and (arr[i] == arr[i+1])):
                i +=1

        else:
            print(arr[i], end=" ")

"""
We can use Hashing to solve this in O(n) time on average. The idea is to traverse the given array
from left to right and keep track of visited elements in a hash table

One more advantage of hashing over sorting is, the elements are printed in same order as they
are in the input array

"""
# Time Complexity: O(n). | Auxiliary Space: O(n)
def print_distinct_three(arr):
    n = len(arr)

    dic = dict()

    for i in range(n):

        # if not present, then put it in hashtable and print it
        if(arr[i] not in dic.keys()):
            dic[arr[i]] =arr[i]
            print(arr[i], end=" ")

print_distinct_three([10, 5, 3, 4, 3, 5, 6])
print("|||||||||||")
print_distinct_three([12, 10, 9, 45, 2, 10, 10, 45])

"""
Put all input integers to hashmap’s key 
Print keySet outside the loop

Time Complexity: O(n*logn)
Auxiliary Space: O(n)

"""

ar = [ 10, 5, 3, 4, 3, 5, 6 ];
dic = {}
for i in range(len(ar)):
    dic[ar[i]] = i
 
# Using dic.keySet() to print output
# reduces time complexity. - Lokesh
print(dic.keys())
 






print("\n my tests \n")
'''
my tests
'''
# Time complexity: O(n) | Space complexity: O(n)
def my_tests(arr):
    dic ={}
    for i in arr:
        dic[i] =dic.get(i, 0) +1

    for i in dic:
        print(i, end=',')


print(my_tests([12, 10, 9, 45, 2, 10, 10, 45]))
print(my_tests([1, 2, 3, 4, 5]))
print(my_tests([1, 1, 1, 1, 1]))


def print_distinct_two(arr):
    arr.sort()

    i =0
    while i < len(arr)-1:
        
        if arr[i] ==arr[i+1]:
            i +=1
        else:
            print(arr[i], end=',')
            i +=1
            
            
    

print("testing tiings", print_distinct_two([12, 10, 9, 45, 2, 10, 10, 45]))

