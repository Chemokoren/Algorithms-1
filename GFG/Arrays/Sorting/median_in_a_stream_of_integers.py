"""
Median in a stream of integers (running integers)

Given that integers are read from a data stream. Find the median of elements read so far in an
efficient way. For simplicity assume, there are no duplicates. For example, let us consider the
stream 5, 15, 1, 3 ..

After reading 1st element of stream - 5 -> median - 5
After reading 2nd element of stream - 5, 15 -> median - 10
After reading 3rd element of stream - 5, 15, 1 -> median - 5
After reading 4th element of stream - 5, 15, 1, 3 -> median - 4, so on...

Making it clear, when the input size is odd, we take the middle element of sorted data. If the 
input size is even, we pick the average of the middle two elements in the sorted stream.

Note that output is the effective median of integers read from the stream so far. Such an 
algorithm is called an online algorithm. Any algorithm that can guarantee the output of i-elements
after processing i-th element, is said to be online algorithm. 

Method 1: Insertion Sort
- If we can sort the data as it appears, we can easily locate the median element.
Insertion sort is one such online algorithm that sorts the data appeared so far. At any instance
of sorting, say after sorting i-th element, the first i elements of the array are sorted. The 
insertion sort doesn't depend on future data to sort data input till that point. In other words,
insertion sort considers data sorted so far while inserting the next element. This is the key part
of insertion sort that makes it an online algorithm.

However, insertion sort takes O(n^2) time to sort n elements. Perhaps we can use binary search on 
insertion sort to find the location of the next element in O(log n) time. Yet, we can't do data
movement in O(log n) time. No matter how efficient the implementation is, it takes polynomial time 
in case of insertion sort.

Time Complexity: O(n2)
Space Complexity: O(1)

"""
# Function to find position to insert current element of stream using binary search
def binarySearch(arr, item, low, high):
    if (low >= high):
        return (low + 1) if (item > arr[low]) else low
    mid = (low + high) // 2

    if(item == arr[mid]):
        return mid + 1

    if(item > arr[mid]):
        return binarySearch(arr, item, mid+1,high)

    return binarySearch(arr, item, low, mid -1)

# Function to print median of stream of integers
def printMedian(arr):
    n = len(arr)
    i, j, pos, num = 0, 0, 0, 0
    count = 1
 
    print(f"Median after reading 1 element is {arr[0]}")
 
    for i in range(1, n):
        median = 0
        j = i - 1
        num = arr[i]
 
        # find position to insert current element in sorted
        # part of array
        pos = binarySearch(arr, num, 0, j)
 
        # move elements to right to create space to insert
        # the current element
        while (j >= pos):
            arr[j + 1] = arr[j]
            j -= 1
 
        arr[j + 1] = num
 
        # increment count of sorted elements in array
        count += 1
 
        # if odd number of integers are read from stream
        # then middle element in sorted order is median
        # else average of middle elements is median
        if (count % 2 != 0):
            median = arr[count // 2]
 
        else:
            median = (arr[(count // 2) - 1] + arr[count // 2]) // 2
 
        print(f"Median after reading {i + 1} elements is {median} ")


# printMedian([5, 15, 1, 3, 2, 8, 7, 9, 10, 6, 11, 4])

"""
Method 2

Augmented self-balanced binary search tree(AVL, RB, etc ...)

At every node of BST, maintain a number of elements in the subtree rooted at that node. We can use
a node as the root of a simple binary tree, whole left child is self-balancing BST with elements
less than root and right child is self-balancing BST with elements greater than root. The root
element always holds effective median.

If the left and right subtrees contain the same number of elements, the root node holds the 
average of left and right subtree root data. Otherwise, the root contains the same data as the 
root of subtree which is having more element. After processing an incoming element, the left &
right subtrees(BST) differ at most by 1.

Self-balancing BST is costly in managing the balancing factor of BST. However, they provide 
sorted data which we don't need. We need median only.


Method 3: Heaps

Similar to balancing BST, we can use a max heap on the left side to represent elements that are 
less than the effective median, and a min-heap on the right side to represent elements that are
greater than the effective median.


After processing an incoming element, the number of elements in heaps differs at most by 1 element. 
When both heaps contain the same number of elements, we pick the average of heaps root data as
effective median. Whn heaps are not balanced, we select effective median from the root of the 
heap containing more elements.


Time Complexity: If we omit the way how stream was read, complexity of median finding is 
O(N log N), as we need to read the stream, and due to heap insertions/deletions.

Auxiliary Space: O(N)
"""

from heapq import heappush, heappop, heapify
import math

minHeap =[]
heapify(minHeap)
maxHeap=[]
heapify(maxHeap)

def insertHeaps(num):
    heappush(maxHeap, -num)
    heappush(minHeap, -heappop(maxHeap))

    if len(minHeap) > len(maxHeap):
        heappush(maxHeap, -heappop(minHeap))

def getMedian():
    if len(minHeap) != len(maxHeap):
        return -maxHeap[0]
    else:
        (minHeap[0] -maxHeap[0])/2


A= [5, 15, 1, 3, 2, 8, 7, 9, 10, 6, 11, 4]
n= len(A)

for i in range(n):
    insertHeaps(A[i])
    print("Median is:", getMedian())



print("\n my tests \n")

'''
my tests
'''
import heapq

def my_tests(arr):

    min_heap=[]
    max_heap=[]

    for i in range(len(arr)):
        heapq.heappush(max_heap, -1*(arr[i]))
        heapq.heapify(max_heap)
        if len(max_heap) -len(min_heap) >1:
            heapq.heappush(min_heap,-1*heapq.heappop(max_heap))
    if len(min_heap) > len(max_heap):
        med_val =min_heap[0]
    elif len(max_heap) > len(min_heap):
        med_val =-1*max_heap[0]
    else:
        med_val =(min_heap[0] +(-1*max_heap[0]))/2
    return med_val

        

print(my_tests([5]))
# print(my_tests([5, 15, 1, 3]))