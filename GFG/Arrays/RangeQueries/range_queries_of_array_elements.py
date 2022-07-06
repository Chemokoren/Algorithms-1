"""
Range Queries for Frequencies of array elements

Given an array of n non-negative integers. The task is to find frequency of a particular
element in the arbitrary range of array[]. The range is given positions(not 0 based 
indexes) in array. There can be multiple queries of given type.

Examples: 
 

Input  : arr[] = {2, 8, 6, 9, 8, 6, 8, 2, 11};
         left = 2, right = 8, element = 8
         left = 2, right = 5, element = 6

Output : 3
         1

The element 8 appears 3 times in arr[left-1..right-1]
The element 6 appears 1 time in arr[left-1..right-1]

Naive approach: is to traverse from left to right and update count variable whenever we
find the element. 

Time complexity of this approach is O(right – left + 1) or O(n) 
Auxiliary space: O(1)

"""

# program to find total count of an element in a range
# count of an element in a range

#Returns count of element in arr[left-1 .. right-1]

def findFrequency(arr, left, right, element):

    count = 0
    for i in range(left -1, right):
        if(arr[i] == element):
            count +=1
    return count

print("expected: 1, actual:", findFrequency([2, 8, 6, 9, 8, 6, 8, 2, 11], 1, 6, 2))
print("expected: 2, actual:", findFrequency([2, 8, 6, 9, 8, 6, 8, 2, 11], 4, 9, 8))


"""

An Efficient approach is to use hashing. In C++, we can use unordered_map

At first, we will store the position in map[] of every distinct element as a vector 
    like that 

  int arr[] = {2, 8, 6, 9, 8, 6, 8, 2, 11};
  map[2] = {1, 8}
  map[8] = {2, 5, 7}
  map[6] = {3, 6} 
  ans so on...

    As we can see that elements in map[] are already in sorted order (Because we inserted
    elements from left to right), the answer boils down to find the total count in that 
    hash map[] using binary search like method. 
     
    In C++ we can use lower_bound which will returns an iterator pointing to the first 
    element in the range [first, last] which has a value not less than ‘left’. and 
    upper_bound returns an iterator pointing to the first element in the 
    range [first,last) which has a value greater than ‘right’. 
     
    After that we just need to subtract the upper_bound() and lower_bound() result to get
    the final answer. For example, suppose if we want to find the total count of 8 in the 
    range from [1 to 6], then the map[8] of lower_bound() function will return the result
    0 (pointing to 2) and upper_bound() will return 2 (pointing to 7), so we need to 
    subtract the both the result like 2 – 0 = 2 . 

This approach will be beneficial if we have a large number of queries of an arbitrary 
range asking the total frequency of particular element.

Time complexity: O(log N) for single query.

"""
# pgoram to find total count of an element
from collections import defaultdict as dict
from bisect import bisect_left as lower_bound
from bisect import bisect_right as upper_bound

store = dict(list)

# Returns frequency of element in arr[left-1 .. right-1]
def findFrequency(arr, left, right, element):

    # Find the position of first occurrence of element
    a = lower_bound(store[element], left)

    # Find the position of  last occurrence of element
    b = upper_bound(store[element], right)
    return b - a

arr = [2, 8, 6, 9, 8, 6, 8, 2, 11]
 
# Storing the indexes of an element in the map
for i in range(len(arr)):
    store[arr[i]].append(i + 1)

print("Expected 1:, actual:",findFrequency(arr, 1, 6, 2))
print("Expected 2:, actual:",findFrequency(arr, 4, 9, 8))

