"""
k largest or smallest elements in an array | added Min Heap method

Question:

Write an efficient program for printing k largest elements in an array.
Elements in array can be in any order.
For example, if given array is[1,23,12,9,30,2,50] and you are asked for the largest 3 elements 
 then your program should print 50, 30, and 23.

 Method 1 (Use Bubble k times)

 1) Modify Bubble sort to run the outer loop at most k times.
 2) print the last k elements of the array obtained in step 1.

 Time Complexity: O(n*k)

 Like Bubble sort, other sorting algorithms like Selection Sort can also be modified to get 
 the k largest elements.

 Method 2(use temporary array)

 k largest elements from arr[0..n-1]

 1) Store the first k elements in a temporary array temp[0..k-1].
 2) Find the smallest element in temp[], let the smallest element be min.
 3) a) For each element x in arr[k] to arr[n-1]. O(n-k)

 if x is greater than the min then remove min from temp[] and insert x.

 b) Then, determine the new min from temp[]. O(k)
 4) print final k elements of temp[]

 Time complexity: O((n-k) * k). If we want the output sorted then O((n-k)*k+k*log(k))

Method 3: Use sorting
1) Sort the elements in descending order in O(n*log(n))
2) Print the first k numbers of the sorted array O(k)

Time complexity: O(n*log(n))

"""

''' code for k largest elements in an array '''
def kLargest(arr, k):
    # Sort the given array arr in reverse order
    arr.sort(reverse=True)
    # Print the first kth largest elements
    for i in range(k):
        print(arr[i], end=" ")

arr = [1, 23, 12, 9, 30, 2, 50]
k = 3
kLargest(arr, k)


"""
method 4: use Max Heap
1) Build a Max Heap tree in O(n)
2) Use Extract Max k times to get k maximum elements from Max Heap
O(k * log(n))

Time complexity: O(n+k*log(n))

"""


"""
Method 5: Use order statistics
1) Use order statistic algorithm to find the kth largest element.
2) Use QuickSort Partition algorithm to paratition around the kth largest number O(n)
3) Sorth the k-1 elements (elements greater than the kth largest element)
O(k*log(k)). This step is needed only if sorted output is required.

Time Complexity: O(n) if we don't need the sorted output, otherwise O(n+k*log(k))


"""

print("\n Method 6: Min Heap:  \n")
"""
Method 6: Min Heap

Instead of using temp[] array, use Min Heap.

1) Build a Min Heap MH of the first k elements (arr[0] to arr[k-1]) of the given array. O(log(k))
2) For each element, after the kth element(arr[k] to arr[n-1]), compare it with root of MH.

a) If the element is greater than the root then make it root and call heapify for MH
b) Else ignore it.

# The step  2 is O((n-k)*log(k))

3) Finally, MH has k largest elements and root of MH is the kth largest element.

Time complexity: O(log(k)+(n-k)*log(k)) without sorted output. 
If sorted output is needed then O(log(k) + (n-k) * log(k) + k*log(k))
"""

def FirstKelements(arr, size, k):
    # creating min heap for given array with only k elements

    # create min heap with priority queue
    minHeap =[]
    for i in range(k):
        minHeap.append(arr[i])

    # Loop for each element in array after the kth element
    for i in range(k,size):
        minHeap.sort()

        # If current element is smaller than minimum(top element of the minHeap) element, 
        # do nothing and continue to next element
        if(minHeap[0] > arr[i]):
            continue

        # Otherwise change minimum element (top element of the minHeap) to current element
        # by polling out the top element of the minHeap

        else:
            minHeap.pop(0)
            minHeap.append(arr[i])

    # Now min heap contains k maximum elements, Iterate and print
    for i in minHeap:
        print(i,end=" ")

arr=[11, 3, 2, 1, 15, 5, 4,45, 88, 96, 50, 45]
size = len(arr)
 
# Size of Min Heap
k=3
FirstKelements(arr, size, k)       

print("\n method 6: Using Quick sort partitioning algorithm: \n")
"""
method 6: Using Quick sort partitioning algorithm

choose a pivot number
if K < pivot_index then repeat the step.
if K == pivot_index: print the array (low to pivot to get K-smallest elements and (n-pivot_index)
to n for K-largest elements)
if K > pivot_index: repeat the steps for the right part

We can improve on standard quicksort algorithm by using random() function. Instead of
using pivot element as last element, we can randomly choose the pivot element. The worst 
case time complexity of this version is O(n^2) and average time complexity is O(n).
"""
import random

#picks up last element between start and end
def findPivot(a, start, end):
    
    #Selecting the pivot element
    pivot = a[end]
    
    # Initially partition-index will be at starting
    pIndex = start
    
    for i in range(start,end):
        
        # If an element is lesser than pivot, swap it.
        if (a[i] <= pivot):
            swap(a, a[i], a[pIndex])
            
            # Incrementing pIndex for further swapping.
            pIndex =pIndex+1
            
    # Lastly swapping or the correct position of pivot
    swap(a[pIndex], a[end])
    return pIndex

def swap(list,a,b):
    list[a], list[b] = list[b], list[a]
    return list

# Picks up random pivot element between start and end
def findRandomPivot(arr, start, end):
    n = end - start + 1
    
    #Selecting the random pivot index
    pivotInd = random() % n
    swap(a,arr[end],arr[start+pivotInd])
    pivot = arr[end]
    
    # initialising pivoting point to start index
    pivotInd = start

    for i in range(start,end):
        
        #If an element is lesser than pivot, swap it.
        if (arr[i] <= pivot):
            swap(a,arr[i], arr[pivotInd])
            
            #Incrementing pivotIndex for further swapping.
            pivotInd =pivotInd +1
            
    #Lastly swapping or the correct position of pivot
    swap(arr[pivotInd], arr[end])
    return pivotInd

def SmallestLargest(a, low, high, k, n):
    if (low == high):
        return
    else:
        pivotIndex = findRandomPivot(a, low, high)
        if (k == pivotIndex):
            print(k, " smallest elements are : ")
            for i in range(0, pivotIndex):
                print(a[i], end=" ")
            print() #cout << endl;
            
            print(k," largest elements are : ")
            
            for i in range(n-pivotIndex, n):
                print(a[i], end=" ")
        elif (k < pivotIndex):
            SmallestLargest(a, low, pivotIndex - 1, k, n)
        elif (k > pivotIndex):
            SmallestLargest(a, pivotIndex + 1, high, k, n)

if __name__ =="__name__":
    a = [11, 3, 2, 1, 15, 5, 4, 45, 88, 96, 50, 45]
    n = len(a) / a[0]; # n = len(a) / sizeof(a[0]);
    low = 0
    high = n - 1
    
    # Lets assume k is 3
    k = 4 
    #Function Call
    print(findRandomPivot(a, low, high))
    # SmallestLargest(a, low, high, k, n)
    # return 0
