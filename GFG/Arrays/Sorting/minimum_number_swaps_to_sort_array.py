"""
Minimum number of swaps required to sort an array

Given an array of n distinct elements, find the minimum number of swaps required to sort the
array

Input: {4, 3, 2, 1}
Output: 2
Explanation: Swap index 0 with 3 and 1 with 2 to 
              form the sorted array {1, 2, 3, 4}.

Input: {1, 5, 4, 3, 2}
Output: 2

This can be easily done by visualizing the problem as a graph. We will have n nodes and an edge
directed from node i to node j if the element at i'th index must be present at j'th index in
the sorted array.

The graph will now contain many non-intersecting cycles. Now a cycle with 2 nodes will only
require 1 swap to reach the correct ordering, similarly, a cycle with 3 nodes will only require
2 swaps to do so.

Hence,

    ans = Σi = 1^k(cycle_size – 1)

where, k is the number of cycles

Time Complexity: O(n Log n) 
Auxiliary Space: O(n)
"""
# returns minimu no of swaps needed to sort the array
def minSwaps(arr):
    n = len(arr)

    #create two arrays and use as pairs where first aray is element and second array is 
    # position of first element
    arrpos =[*enumerate(arr)]

    # sort the array by array element values to get right position of every element as the 
    # element of second array
    arrpos.sort(key =lambda it:it[1])

    # To keep track of visited elements, initialize all elements as not visited or false
    vis ={k: False for k in range(n)}

    # Initialize result
    ans = 0
    for i in range(n):

        # already swapped or already present at correct position
        if vis[i] or arrpos[i][0] ==i:
            continue
        # find number of nodes in this cycle and add it to ans
        cycle_size = 0
        j = i

        while not vis[j]:

            # mark node as visited
            vis[j] = True

            # move to next node
            j = arrpos[j][0]
            cycle_size +=1

        # update answer by adding current cycle
        if cycle_size > 0:
            ans += (cycle_size - 1)
    return ans


print("Expected:2, Actual:", minSwaps([1, 5, 4, 3, 2]))


"""
Method 2: 

Time Complexity: O(n Log n) 
Auxiliary Space: O(n)

"""

# function retursn the min no. of swaps to sort the array
from functools import cmp_to_key
from operator import indexOf

def cmp(a, b):
    return a -b

def min_swaps_two(nums):

    Len = len(nums)
    map ={}
    for i in range(Len):
        map[nums[i]] =i

    nums = sorted(nums, key = cmp_to_key(cmp))

    # To keep track of visited elements. Initialize all elements as not visited or false.
    visited = [False for col in range(Len)]

    # Initialize result
    ans = 0
    for i in range(Len):

        # already swapped and corrected or already present at correct pos
        if(visited[i] or map[nums[i]]==i):
            continue
        j, cycle_size =i, 0
        while(visited[j] == False):
            visited[j] =True

            # move to next node
            j =map[nums[j]]
            cycle_size +=1
        
        # update answer by adding current cycle.
        if(cycle_size > 0):
            ans += (cycle_size -1)

    return ans


print("Expected:2, Actual:", min_swaps_two([ 1, 5, 4, 3, 2 ]))


"""
Straight forward solution : Greedy solution

While iterating over the array, check the current element, and if not in the correct place, 
replace that element with the index of the element which should have come in this place greedily
which will give the optimal answer

Time Complexity: O(n*n) 
Auxiliary Space: O(n)

We can still improve the complexity by using a hashmap. The main operation here is the indexOf 
method inside the loop, which costs us n*n. We can improve this section to O(n), by using a
hashmap to store the indexes. Still, we use the sort method, so the complexity cannot improve
beyond O(n Log(n))

"""

def min_swaps_three(arr):

    N = len(arr)

    ans = 0
    temp = arr.copy()
    temp.sort()
    for i in range(N):

        # checking whether the current element is at the right place or not
        if(arr[i] != temp[i]):
            ans +=1

            # Swap the current element with the right index so that arr[0] to arr[i] is sorted
            swap(arr, i, indexOf(arr,temp[i]))
    return ans

def swap(arr, i, j):
    temp =arr[i]
    arr[i] =arr[j]
    arr[j] =temp

def indexOf(arr, ele):
    for i in range(len(arr)):
        if(arr[i] == ele):
            return i
    return -1


print("Expected: 5, Actual: ", min_swaps_three([101, 758, 315, 730, 472, 619, 460, 479]))


"""

Using HashMap

- Make a new array(temp), which is sorted form of the input array. We know that we need to 
transform the input array to the new array(temp) in the minimum number of swaps. Make a map that
stores the elements and their corresponding index, of the input array.

so, at each i starting from 0 to N in the given array, where N is the size of the array:
 - if i is not in its correct position according to the sorted array, the
 - we will fill this position with the correct element from the hashmap we built earlier. 
 We know the correct element which should come here is temp[i], so we look up the index of this
 element from the hashmap.
 - after swapping the required elements, we update the content of the hashmap accordingly, as 
 temp[i] to the ith position, and arr[i] to where temp[i] was earlier.

Complexity: O(n Log n) 
Auxiliary Space: O(n)

"""
def min_swap_four(arr):
    n = len(arr)

    ans = 0
    temp = arr.copy()

    # dictionary stores the indexes of the input array
    h ={}
    temp.sort()
    for i in range(n):

        h[arr[i]] = i

    init = 0

    for i in range(n):

        # checks whether the current element is at the right place or not
        if(arr[i] != temp[i]):
            ans += 1
            init = arr[i]

            # if not, swap this element with the index of the element which should come here
            arr[i], arr[h[temp[i]]] = arr[h[temp[i]]], arr[i]

            # update the indexes in the hashmap accordingly
            h[init] = h[temp[i]]
            h[temp[i]] = i

    return ans


print("Four Expected: 5, Actual:", min_swap_four([ 101, 758, 315, 730,472, 619, 460, 479 ]))
 




'''
my tests 
'''
def my_tests(arr):
    start =0
    end =len(arr)-1
    count =0

    while start <= end:
        if arr[start] > arr[end]:
            arr[start], arr[end] =arr[end], arr[start]
            start += 1
            end -=1
            count +=1
        else:
            start +=1
    return count

print("Expected:2, Actual:", my_tests([4, 3, 2, 1]))
print("Expected:2, Actual:", my_tests([1, 5, 4, 3, 2]))
