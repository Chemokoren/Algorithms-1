"""
Sort a nearly sorted or K sorted array

Given an array of n elements, where each element is at most k away from its target
position, devise an algorithm that sorts in O(n log k ) time. For example let us consider 
k is 2, an element at index 7 in the sorted array, can be at indexes 5,6,7,8,9 in the
given array.

    Input : arr[] = {6, 5, 3, 2, 8, 10, 9}
                k = 3 
    Output : arr[] = {2, 3, 5, 6, 8, 9, 10}

    Input : arr[] = {10, 9, 8, 7, 4, 70, 60, 50}
             k = 4
    Output : arr[] = {4, 7, 8, 9, 10, 50, 60, 70}

Using insertion sort to sort the elements

Time Complexity: O(nk), The inner loop will run at most k times. To move every element to its correct place, at most k elements need to be moved. 
Auxiliary Space: O(1)

"""
def insertionSort(A):
    size =len(A)
    i, key, j = 0, 0, 0
    for i in range(size):
        key = A[i]
        j = i-1
 
        # Move elements of A[0..i-1], that are
        # greater than key, to one position
        # ahead of their current position.
        # This loop will run at most k times
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key
    return A


print(insertionSort([6, 5, 3, 2, 8, 10, 9]))

"""
We can sort such arrays more efficiently with the help of Heap data structure.

Detailed process that uses Heap.

- Create a Min Heap of size+1 with first k+1 elements. This will take O(k) time. We are
creating heap of size k as the element can be at most k distance from its index in a
sorted array.
- One by one remove min element from heap, put it in result array, and add a new element to
heap from remaining elements.
Removing an element and adding a new element to heap will take log k time. So,
overall complexity will be O(k) +O((n-k)) * log(k)).
-

Time Complexity: O(k) + O((m) * log(k)) ,  where m = n – k
Auxiliary Space: O(k)
"""
# program to sort a nearly sorted array
from heapq import heappop, heappush, heapify

# Given an array of size n, where every element is k away from its target position
# sorts the array in O(nLogk) time.
def sort_k(arr: list, k:int):

    """
    :param arr: input array
    :param k: max distance, which every element is away from its target position.
    :return: list
    """

    n = len(arr)

    # List of first k+1 items
    heap =arr[:k+1]

    # using heapify to convert list into heap(or min heap)
    heapify(heap)

    # "rem_elmnts_index" is index for remaining elements in arr and "target_index" is
    # target index of for current minimum element in Min Heap "heap".
    target_index = 0
    for rem_elmnts_index in range(k+1, n):
        arr[target_index] = heappop(heap)
        heappush(heap, arr[rem_elmnts_index])
        target_index += 1

    while heap:
        arr[target_index] = heappop(heap)
        target_index +=1

    return arr


print('Expected:[2,3, 6, 8, 12, 56] , Actual:', sort_k([2, 6, 3, 12, 56, 8], 3))

"""

We can also use a Balanced Binary Search Tree instead of Heap to store k+1 elements. 
The insert and delete operations on Balanced BST also take O(log k) time. 
So Balanced BST 
based method will also take O(n log k) time, but the Heap based method seems to be more 
efficient as the minimum element will always be at root. Also, Heap doesn’t need extra 
space for left and right pointers.

The previous algorithm is good the time and space complexity can be improved with a 
variation of Quick Sort algorithm. 


The algorithm uses quick sort but changes the partition function in 2 ways.

    -Selects pivot element as the middle element instead of the first or last element.
    -Scans the array from max(low, mid – k) to min(mid + k, high) instead of low to high.

The middle element is chosen as pivot for diving the array into almost 2 halves for a 
logarithmic time complexity.

Time Complexity: O(KLogN) 
Auxiliary Space: O(LogN)

"""

def swap(arr, a, b):
        arr[a],arr[b] =arr[b],arr[a]



class nearly_sorted_algorithm:
    
    #ArrayList<Integer> arr
    def sort(arr,l:int, h:int,k:int):
        mid = l + (h-l)/2; #choose middle element as pivot
        i = max(l,mid-k), 
        j=i
        end = min(mid+k,h)#set appropriate ranges
        
        swap(arr,end,mid) #swap middle and last element to avoid extra complications
        while(j<end):
            if(arr.get(j)<arr.get(end)):
                i +=1
                swap(arr,j,i)
                
            j=j+1
            
        swap(arr,end,i)
        return i
    
    # ArrayList<Integer> arr
    def ksorter(self, arr, l: int, h:int, k:int):
        if(l<h):
            q = self.sort(arr,l,h,k)
            self.ksorter(arr,l,q-1,k)
            self.ksorter(arr,q+1,h,k)


    

if __name__=="__main__":
    #     ArrayList<Integer> arr = new ArrayList<>(List.of(3, 3, 2, 1, 6, 4, 4, 5, 9, 7, 8, 11, 12 ));
    arr = [3, 3, 2, 1, 6, 4, 4, 5, 9, 7, 8, 11, 12 ]
    k = 3
    N = len(arr)
    
    print("Array before k sort\n")
    print(arr)
    print("\n")


    cls = nearly_sorted_algorithm()
    
    cls.ksorter(arr, 0, N - 1, k)
    print("Array after k sort\n")
    print(arr)
	

'''
Array before k sort
3 3 2 1 6 4 4 5 9 7 8 11 12 
Array after k sort
1 2 3 3 4 4 5 6 7 8 9 11 12

'''
