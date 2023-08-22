"""
K largest(or smallest ) elements in an array

Question

Write an efficient program for printing k largest elements in an array.
Elements in an array can be in any order.
For example, if the given array is[1,23,12,9,30,2,50] and you are asked for the largest 3 elements i.e., k=3 
then your program should print 50, 30, and 23.

Method 1 (Bubble k times)
-------------------------

1) Modify bubble sort to run the outer loop at most k times
2) Print the last k elements of the array obtained in step 1.

Time complexity: O(n*k)

Like Bubble sort, other sorting algorithms like selection sort can also be modified to get the k largest 
elements.

Method 2(Use temporary array)
-----------------------------

K largest elements from arr[0..n-1]
-----------------------------------
1) Store the first k elements in a temporary array temp[0...k-1]
2) Find the smallest element in temp[], let the smallest element be min.
3-a) For each element x in arr[k] to arr[n-1]. O(n-k)
if x is greater than the min then remove min from temp[] and insert x.
3-b) Then, determine the new min from temp[]. O(k)
4) Print final k elements of temp[]

Time complexity: O((n-k)*k). If we want the output sorted then O((n-k)*k+k*log(k))

Method 3(Use Sorting)
1) Sort the elements in descending order in O(n*log(n))
2) Print the first k numbers of the sorted array O(k)

Time complexity: O(n*log(n))

"""
def k_largest(arr, k):
    # sort the given array arr in reverse order
    arr.sort(reverse=True)
    # print the first kth largest elements
    for i in range(k):
        print(arr[i], end=" ")

k_largest([1, 23, 12, 9, 30, 2, 50], 3)

"""
Method 5 (Use Order Statistics )
1) Use an order statistic algorithm to find the kth largest element
2) Use QuickSort Partition algorithm to partition around the kth largest number O(n).
3) Sort the k-1 elements (elements greater than the kth largest element)
O(k*log(k)). This step is needed only if the sorted output is required.

Time complexity: O(n) if we don't need the sorted output, otherwise O(n + k*log(k))

Method 6(Use Min Heap)
----------------------
This method is mainly an optimization of method 1 which uses a temp[] array.
 Instead of using temp[] array, use Min Heap.

1) Build a Min Heap MH of the first k elements(arr[0] to arr[k-1]) of the given array.
O(k * log(k))
2) For each element, after the kth element(arr[k] to arr[n-1]), compare it with root of MH

    a) if the element is greater than the root then make it root and call heapify for MH
    b) Else ignore it.
# The step 2 is O((n-k)*log(k))
3) Finally, MH has k largest elements, and the root of the MH is the kth largest element.

Time Complexity: O(k*log(k) + (n-k)*log(k)) without sorted output. If sorted output is needed then 
O(k*log(k) + (n-k)*log(k)+k*log(k)) so overall it is O(k*log(k)+(n-k)*log(k))
All of the above methods can also be used to find the kth largest(or smallest) element.


"""

def first_k_elements(arr, k):
    size = len(arr)
    # Creating Min Heap for given array with only k elements
    # Create min heap with priority queue

    minHeap =[]
    for i in range(k):
        minHeap.append(arr[i])

    # Loop for each element in array after the kth element
    for i in range(k, size):
        minHeap.sort()

        # if current element is smaller than minimum ((top element of the minHeap) element, do nothing
        # and continue to next element)
        if(minHeap[0] > arr[i]):
            continue

        # Otherwise Change minimum element (top element of the minHeap) to
        # current element by polling out 
        # the top element of the minHeap
        else:
            minHeap.pop(0)
            minHeap.append(arr[i])
        
    # Now min heap contains k maximum elements, Iterate and print
    # for i in minHeap:
    #     print(i, end=" ")
    return minHeap

print(" ################################### using min heap ###################################")
print("expected is: actual:",first_k_elements([1, 23, 12, 9, 30, 2, 50], 3))
print("expected is: actual:",first_k_elements([11, 3, 2, 1, 15, 5, 4,45, 88, 96, 50, 45], 3))


"""
Method 7: Using Quick Sort partitioning algorithm
1) Choose a pivot number
2) If K is lesser than pivot_index then repeat the step.
3) if K == pivot_index: Print the array (low to pivot to get K-smallest elements and (n-pivot_index) to n
for  K-largest elements)
4) if K > pivot_index: Repeat the steps for right part.

We can improve on the standard quicksort algorithm by using the random() function. Instead of using the pivot
element as the last element, we can randomly choose the pivot element. The worst-case time complexity of this
version is O(n^2) and the average complexity is O(n).

"""

print("####################### Method 7: Using Quick Sort partitioning algorithm ####################### \n")

import random

def findPivot(a, start, end):

    # selecting the pivot element
    pivot =a[end]

    # Initially partition-index will be at starting
    pIndex = start

    for i in range(start, end):
        
        # If an element is lesser than pivot, swap it
        if(a[i] <= pivot):
            a[i],a[pIndex] = a[pIndex],a[i]
        
            # Incrementing pIndex for further swapping
            pIndex +=1

    # Lastly swapping or the correct position of pivot
    a[end],a[pIndex]= a[pIndex],a[end]
    return pIndex

# picks up random pivot element between start and end
def findRandomPivot(arr, start, end):

    n = end -start + 1
    # selecting the random pivot index
    pivotInd =(int((random.random()* 1000000))%n)
    arr[end], arr[start+pivotInd] = arr[start+pivotInd], arr[end]
    pivot = arr[end]

    # initialising pivoting poto start index
    pivotInd = start
    for i in range(start, end):

        # if an element is lesser than pivot, swap it
        if(arr[i] <= pivot):
            arr[i], arr[pivotInd] =arr[pivotInd], arr[i]

            # Incrementing pivotIndex for further swapping.
            pivotInd +=1
    
    # Lastly swapping or the correct position of pivot
    arr[pivotInd], arr[end] = arr[end], arr[pivotInd]
    return pivotInd

def SmallestLargest(a, low, high, k, n):
    if(low == high):
        return
    else:
        pivotIndex = findRandomPivot(a, low, high)

        if(k == pivotIndex):
            print(str(k)+ " smallest elements are:", end="")
            for i in range(pivotIndex):
                print(a[i], end=" ")
        
            print()

            print(str(k)+ " largest elements are: ", end ="")
            for i in range(n -pivotIndex, n):
                print(a[i], end=" ")

        elif (k < pivotIndex):
            SmallestLargest(a, low, pivotIndex-1, k, n)
        elif (k > pivotIndex):
            SmallestLargest(a, pivotIndex +1, high, k, n)

a = [ 11, 3, 2, 1, 15, 5, 4, 45, 88, 96, 50, 45 ]
n = len(a)
  
low = 0
high = n - 1
  
k = 3
  
SmallestLargest(a, low, high, k, n)



