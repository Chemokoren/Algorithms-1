"""
K'th Smallest / Largest Element in Unsorted Array

Given an array and a number k where k is smaller than the size of the array,
we need to find the k'th smallest element in the given array. It is given that 
all array elements are distinct.

Examples:

Input: arr[] = {7, 10, 4, 3, 20, 15} 
k = 3 
Output: 7

Input: arr[] = {7, 10, 4, 3, 20, 15} 
k = 4 
Output: 10 

Method 1 (Simple Solution)

A simple solution is to sort the given array using a O(NlogN) sorting algorithm like Merge Sort,
Heap Sort and return the element at index k-1 in the sorted array.

Time complexity of this solution is O(N Log N)



"""

# Function to return k'th smallest element in a given array

def kthSmallest(arr, n, k):
    # sort the given array
    arr.sort()

    # return k'th element in the sorted array
    return arr[k-1]

if __name__=='__main__':
    arr = [12, 3, 5, 7, 19]
    n = len(arr)
    k = 4
    print("K'th smallest element is: ",  kthSmallest(arr, n, k))

print("\n Method 2: Using Min Heap - HeapSelect: \n")

"""
Method 2: Using Min Heap - HeapSelect

We can find k'th smallest element in time complexity better than O(N Log N). A simple
optimization is to create a Min Heap of the given n elements and call extractMin() k times.


Time complexity of this solution is O(n + kLogn).

"""

#  A Java program to find k'th smallest element using min heap

# A class for Max Heap
import sys

class MinHeap:
    harr =None  # pointer to array of elements in heap
    capacity=sys.maxsize # maximum possible size of min heap
    heap_size =0 # Current number of elements in min heap
    
    
    def parent(self,i):
        return (i - 1) / 2
    
    def left(self,i):
        return ((2 * i )+ 1)
        
    def right(self, i):
        return ((2 * i) + 2)
        
    def getMin(self):
        return self.harr[0] # Returns minimum
        
     # to replace root with new node x and heapify() new root
    def replaceMax(self,x):
        self.harr[0] = x
        self.minHeapify(0)
    
    def getMinHeap(self,a, size):
        self.heap_size = size
        harr = a; # store address of array
        i = (self.heap_size - 1) / 2
        while (i >= 0):
            self.minHeapify(i)
            i =i -1
            
    # Method to remove maximum element (or root) from min heap
    def extractMin(self):
        if(self.heap_size == 0):
            return sys.maxsize

        # Store the maximum value.
        root = self.harr[0]

        # If there are more than 1 items, move the last item to root
        # and call heapify.
        if (self.heap_size > 1):
            self.harr[0] = self.harr[self.heap_size - 1]
            self.minHeapify(0)
	
        heap_size = self.heap_size -1
        return root
        
    # A recursive method to heapify a subtree with root at given index
	# This method assumes that the subtrees are already heapified
    def minHeapify(self, i):
        l = self.left(i)
        r = self.right(i)
        smallest = i
        if (l < self.heap_size and self.harr[l] < self.harr[i]):
            smallest = l
        if (r < self.heap_size and self.harr[r] < self.harr[smallest]):
            smallest = r
        if (smallest != i):
            t = self.harr[i]
            self.harr[i] = self.harr[smallest]
            self.harr[smallest] = t
            self.minHeapify(smallest)

# Function to return k'th largest element in a given array
def kthSmallest(arr, n, k):
    # Build a heap of first k elements: O(k) time
    mh = MinHeap()
    # mh = MinHeap(arr, n)
    # getMinHeap
    
    # Process remaining n-k elements. If current element is
	# smaller than root, replace root with current element
    
    for i in range(0, k-1):
        mh.extractMin()

	# Return root
    return mh.getMin()

# Driver program to test above methods
if __name__=="__main__":
    arr = [12, 3, 5, 7, 19 ]
    n = len(arr)
    k = 2
    print("K'th smallest element is: ",	kthSmallest(arr, n, k))


print("\n Method 3: Using Max-Heap: \n")
"""
Method 3: Using Max-Heap

We can also use Max Heap for finding the k'th smallest element. Following is an algorithm.

1) Build a Max-Heap MH of the first k elements (arr[0] to arr[k-1]) of the given array. O(k)
2) For each element, after the k'th element(arr[k] to arr[n-1]), compare it with root of MH
---a) If the element is less than the root then make it root and call heapify for MH
---b) Else ignore it
# The step 2 is O((n-k)*logk)
3) Finally, the root of the MH is the kth smallest element
Time complexity of this solution is O(k+(n-k)*Logk)

"""

# A  program to find k'th smallest element using max heap
class MaxHeap:
    
    harr=None # pointer to array of elements in heap
    capacity= sys.maxsize # maximum possible size of max heap
    heap_size =0 # Current number of elements in max heap
    
    def parent(self,i):
        return (i - 1) / 2
        
    def left(self,i):
        return (2 * i + 1)
        
    def right(self,i):
        return (2 * i + 2)
    
    def getMax(self):
        return self.harr[0] # Returns maximum
        
    # to replace root with new node x and heapify() new root
    
    def replaceMax(self,x):
        self.harr[0] = x
        self.maxHeapify(0)
        
    def MaxHeap(self,a, size):
        self.heap_size = size
        harr = a; #store address of array
        i = (self.heap_size - 1) / 2
        while (i >= 0):
            self.maxHeapify(i)
            i= i - 1

	# Method to remove maximum element (or root) from max heap
    def extractMax(self):
        if(self.heap_size == 0):
            return sys.maxsize

        # Store the maximum value.
        root = self.harr[0]
        
        # If there are more than 1 items, move the last item to root and call heapify.
        if (self.heap_size > 1):
            self.harr[0] = self.harr[self.heap_size - 1]
            self.maxHeapify(0)
    
        heap_size =self.heap_size -1
        return root
        
    # A recursive method to heapify a subtree with root at given index
    # This method assumes that the subtrees are already heapified
    
    def maxHeapify(self,i):
        l = self.left(i)
        r = self.right(i)
        largest = i

        if (l < self.heap_size and self.harr[l] > self.harr[i]):
            largest = l
        
        if (r < self.heap_size and self.harr[r] > self.harr[largest]):
            largest = r
    
        if (largest != i):
            t = self.harr[i] 
            self.harr[i] = self.harr[largest]
            self.harr[largest] = t
            self.maxHeapify(largest)
	

# Function to return k'th largest element in a given array
def kthSmallest(arr, n, k):
    
    # Build a heap of first k elements: O(k) time
    
    mh = MaxHeap(arr, k)
    
    # Process remaining n-k elements. If current element is
    # smaller than root, replace root with current element
    
    for i in range(k,n):
        if (arr[i] < mh.getMax()):
            mh.replaceMax(arr[i])
            
    return mh.getMax()

if __name__=="__main__":
    arr = { 12, 3, 5, 7, 19 }
    n = arr.length, k = 4
    print("K'th smallest element is: ", kthSmallest(arr, n, k))


print("\n Method 4 : QuickSelect \n")

"""
Method 4 : QuickSelect

This is an optimization over method 1 if QuickSort is used as a sorting algorithm in first
step. In QuickSort, we pick a pivot element, then move the pivot element to its correct position
and partition the surrounding array. The idea is, not to do complete quicksort, but stop at the
point where pivot itself is k'th smallest element. Also, not to recur for both left and 
right sides of pivot, but recur for one of them according the  position of pivot. 
The worst case time complexity of this method is O(n^2) but it works in O(n) on average.
"""

# This function returns k'th smallest element in arr[l..r] using QuickSort based method.
# Assumption: All elements in arr[] are distinct

import sys

def kthSmallest(arr, l, r, k):
    # if k is smaller than number of elements in array
    if(k > 0 and k <= r -l + 1):

        # partition the array aroind last element and get  position of pivot element in sorted array
        pos = partition(arr, l, r)

        # if position is same as k
        if(pos -l == k - 1):
            return arr[pos]

        if(pos -l > k -l): # If position is more, recur for left subarray
            return kthSmallest(arr, l, pos -1, k)

        # Else recur for right subarray
        return kthSmallest(arr, pos + 1, r, k -pos + l - 1)

    # If k is more than number of elements in array
    return sys.maxsize

# Standard partition process of QuickSort(). It considers the last element as pivot and 
# moves all smaller element to left of it and greater elements to right
def partition(arr, l, r):
    x =  arr[r]
    i =  l
    for j in range(l, r):
        if(arr[j] <= x):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i

if __name__=="__main__":
    arr = [12, 3, 5, 7, 4, 19, 26]
    n = len(arr)
    k = 3
    print("K'th smallest element is: ",  kthSmallest(arr, 0, n - 1, k))


"""
Method 5 :  Map STL

A map based STL approach is although very much similar to the quickselect and counting sort
algorithm but much easier to implement. We can use an ordered map and map each element
with it's frequency. And as we know that an ordered map would store the data in a sorted manner,
we keep on adding the frequency of each element till it does not become greater than or equal
to k so that we reach the k'th element from the start i.e. the k'th smallest element.
"""


"""

Method 6:

K'th Smallest /  Largest Element in Unsorted Array | Set 2 (Expected Linear Time)

Given an array and a number k where k is smaller than size of array, we need to 
find the k'th largest element in the given array. It is given that all array elements 
are distinct.

Input: arr[] ={7, 10, 4, 3, 20, 15}
k = 3
output = 7

Input: arr[] = {7, 10, 4, 3, 20, 15}
k = 4
Output: 10

"""

# This function returns k'th smallest element in arr[l..r] using QuickSort based method.
# ASSUMPTION: Allelements in arr[] are distinct

from random import randint

def randomPartition(arr, l, r):
    n = r - l + 1
    pivot = randint(1, 100) % n
    arr[l + pivot], arr[r] = arr[l + pivot], arr[r]
    return partition(arr, l, r)

def kthSmallest(arr, l, r, k):
    # If k is smaller than number of elements in array
    if(k > 0 and k <= r - l + 1):
        # partition the array around last element and get position of pivot element 
        # in sorted array
        pos = randomPartition(arr, l, r)

        # If position is same as k
        if(pos -l == k -1):
            return arr[pos]

        # If position is more, recur for left subarray
        if(pos -l > k -1):
            return kthSmallest(arr, l, pos -1, k)

        # Else recur for right subarray
        return kthSmallest(arr, pos + 1, r, k- pos + l-1)
    # if k is more than number of elements in array
    return 10**9

# standard partition process of QuickSOrt(). It considers the last element as pivot and moves
# all smaller element to left of it and greater elements to right
def partition(arr, l, r):
    x =arr[r]
    i = l
    for j in range(l,  r):
        if(arr[j] <= x):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[r] = arr[r], arr[i]
    return i

arr = [12, 3, 5, 7, 4, 19, 26]
n = len(arr)
k = 3
print("K'th smallest element is", kthSmallest(arr, 0, n - 1, k))



"""
Given an array and a number k where  k is smaller than the size of the array, we need
to find the k'th smallest element in the given array. It is is given that all array elements
are distinct.

Examples: 
 

Input: arr[] = {7, 10, 4, 3, 20, 15}
       k = 3
Output: 7

Input: arr[] = {7, 10, 4, 3, 20, 15}
       k = 4
Output: 10

The idea in this new method is similar to quickSelect(), we get worst-case linear time by 
selecting a pivot that divides array in a balanced way (there are not very few elements on
one side and many on another side). After the array is divided in a balanced way, 
we apply the same steps  as used in quickSelect() to decide whether to go left or
right of pivot.

Complete algorithm:
1) Divide arr[] into [n/5] groups where size of each group is 5 except possibly the last
group which may have less than 5 elements.
2) Sort the above created [n/5] groups and find median of all groups. Create an auxiliary 
array 'median[]' and store medians of all [n/5] groups in this median array.
// Recursively call this method to find median of median [0..[n/5]-1]
3) medOfMed =kthSmallest(median[0..[n/5]-1, [n/10]])
4) partition arr[] around medOfMed and obtain its position.
pos = partition(arr, n, medOfMed)
5) if pos == k return medOfMed
6) if pos > k return kthSmallest(arr[l..pos-1], k)
7) if pos < k return kthSmallest(arr[pos+1..r],k-pos+l-1)

The first four steps are used to obtain a good point for partitioning the array(to make sure
that there are not too many elements either side of pivot).

Time complexity:
- The worst case time complexity of this algorithm is O(n).
Analysis:
The steps 1) and 2) take O(n) time as finding median of an array of size 5 takes O(1) time 
and  there are n/5 arrays of size 5.

The step 3) takes T(n/5) time. 
The  step 4 is standard partition takes O(n) time.
At most one of either steps 6) or step 7 is executed. These are recursive steps. What is the 
worst case size of these recursive calls. The answer is  maximum number of elements greater
than medOfMed(obtained in step 3) or maximum number of elements smaller than medOfMed.

How many elements are greater than medOfMed and how many are smaller?

 At least half of the medians found in step 2 are greater than or equal to medOfMed. Thus,
 at least  half of the n/5 groups contribute 3 elements that are greater than medOfMed, 
 except for the one group that has fewer than 5 elements. Therefore, the number 
 of elements greater than medOfMed is at least.

---

 Similarly, the number of elements that are less then medOfMed is at least 3n/10-6. 
 In the worst case, the function recurs for at most n - (3n/10 -6) which is 7n/10 +  6 
 elements.

 Note that 7n/10+62020 and that any input of 80 or fewer elements requires O(1)  time. We
 can therefore obtain the recurrence

 We show that the running time is linear by substitution. Assume that T(n) cn for some 
 constant c and all n>80. Substituting this inductive hypothesis into right-hand side
 of the recurrence yields

 T(n)  <= cn/5 + c(7n/10 + 6) + O(n)
     <= cn/5 + c + 7cn/10 + 6c + O(n)
    <= 9cn/10 + 7c + O(n)
    <= cn, 

since we can pick c large enough so that c(n/10 – 7) is larger than the function 
described by the O(n) term for all n > 80. The worst-case running time of is therefore 
linear

Note that the above algorithm is linear in worst case, but the constants are very high 
for this algorithm. Therefore, this algorithm doesn’t work well in practical situations, 
randomized quickSelect works much better and preferred..


"""
# Returns k'th smallest element in arr[l..r] in worst case linear time.
# Assumption: All elements in arr[] are distinct
def kthSmallest(arr, l, r, k):
     
    # If k is smaller than number of
    # elements in array
    if (k > 0 and k <= r - l + 1):
         
        # Number of elements in arr[l..r]
        n = r - l + 1
 
        # Divide arr[] in groups of size 5,
        # calculate median of every group
        # and store it in median[] array.
        median = []
 
        i = 0
        while (i < n // 5):
            median.append(findMedian(arr, l + i * 5, 5))
            i += 1
 
        # For last group with less than 5 elements
        if (i * 5 < n):
            median.append(findMedian(arr, l + i * 5,
                                              n % 5))
            i += 1
 
        # Find median of all medians using recursive call.
        # If median[] has only one element, then no need
        # of recursive call
        if i == 1:
            medOfMed = median[i - 1]
        else:
            medOfMed = kthSmallest(median, 0,
                                   i - 1, i // 2)
 
        # Partition the array around a medOfMed
        # element and get position of pivot
        # element in sorted array
        pos = partition(arr, l, r, medOfMed)
 
        # If position is same as k
        if (pos - l == k - 1):
            return arr[pos]
        if (pos - l > k - 1): # If position is more,
                              # recur for left subarray
            return kthSmallest(arr, l, pos - 1, k)
 
        # Else recur for right subarray
        return kthSmallest(arr, pos + 1, r,
                           k - pos + l - 1)
 
    # If k is more than the number of
    # elements in the array
    return 999999999999


def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

# It searches for x in arr[l..r], and partitions the array around x
def partition(arr, l, r, x):
    for i in range(l, r):
        if arr[i] == x:
            swap(arr, r, i)
            break
    
    x = arr[r]
    i = l
    for j in range(l, r):
        if(arr[j] <= x):
            swap(arr, i, j)
            i += 1
    swap(arr, i, r)

    return i

# A simple function to find median of arr[] from index l to l+n
def findMedian(arr, l, n):
    lis =[]
    for i in range(l, l + n):
        lis.append(arr[i])

    # sort the array
    lis.sort()

    return lis[n // 2]

if __name__ == '__main__':
 
    arr = [12, 3, 5, 7, 4, 19, 26]
    n = len(arr)
    k = 3
    print("K'th smallest element is",kthSmallest(arr, 0, n - 1, k))



    
"""
Approach 8: 
-----------

We can find the kth smallest element in time complexity better than O(N log N)
We are using the set because it is mentioned in the question that all the elements in an array are 
distinct.

"""
print("#################### return_kth_element #################### ")
def return_kth_element(arr,k):
	set_i = set((arr))
	myit = iter(set_i )
	for i in range(k):
		val = myit.__next__()
	return val

print("expected:7, actual:", return_kth_element([7, 10, 4, 3, 20, 15],3))
print("expected:10, actual:", return_kth_element([7, 10, 4, 3, 20, 15],4))
print("expected:12, actual:", return_kth_element([12, 3, 5, 7, 19],4))

'''
Set 2 (Expected Linear Time)

'''

# This function returns k'th smallest element in arr[l..r] using QuickSort based method.
# ASSUMPTION:  All elements in arr[] are distinct
from random import randint

def randomPartition(arr, l, r):
    n = r - l + 1
    pivot =randint(1,100) % n
    arr[l + pivot],arr[r] = arr[l + pivot],arr[r]
    return partition(arr, l, r)

def kth_smallest_set_two(arr, l, r, k):

        # if k is smaller than number of elements in array
        if(k > 0 and k <= r -l +1):

            # Parititon the array around last element and get position of pivot element in sorted array
            pos = randomPartition(arr, l, r)

            # if position is same as k
            if(pos -l == k-1):
                return arr[pos]

            # if position is more, recur for left subarray
            if(pos -l > k -1):
                return kth_smallest_set_two(arr, l, pos -1, k)
            
            # Else recur for right subarry
            return kth_smallest_set_two(arr, pos +1, r, k-pos +l -1)
        
        # if k is more than number of elements in array
        return 10**9


# Standard partition process of QuickSort().
# It considers the last element as pivot and moves all smaller element to left of it and greater elements
# to right
def partition(arr, l, r):
        x =arr[r]
        i = l
        for j in range(l,r):
            if(arr[j] <= x):
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i], arr[r] = arr[r], arr[i]
        return i

arr = [12, 3, 5, 7, 4, 19, 26]
n = len(arr)
k = 3
print("K'th smallest element(set 2) is",kth_smallest_set_two(arr, 0, n - 1, k))


'''
Set 3 (Worst Case Linear Time)

The idea is similar to quickSelect(), we get worst-case linear time by selecting a pivot that divides array 
in a balanced way (there are not very few elements on one side and many on another side). After the array is 
divided in a balanced way, we apply the same steps as used in quickSelect() to decide whether to go left or 
right of the pivot.

kthSmallest(arr[0..n-1], k)
1) Divide arr[] into [n/5] groups where size of each group is 5 except possibly the last group which may have 
less than 5 elements.
2) Sort the above created[n/5] groups and find median of all groups. Create an auxiiliary array 'median[]' 
and store medians of all[n/5] groups in this median array.

# Recursively call this method to find median of median[0..[n/5]-1]
3) medOfMed = kthSmallest(median[0..[n/5]-1],[n/10])
4)Partition arr[] around medOfMed and obtain its position.
pos = partition(arr, n, medOfMed)
5) if pos == k return medOfMed
6) if pos > k return kthSmallest(arr[l..pos-1],k)
7) if pos < k return kthSmallest(arr[pos+1..r], k-pos+l-1)

The last 3 steps are same as in set 2 above. The first four steps are used to obtain a good 
 point for partitioning the array(to make sure that there are not too many elements either side of pivot).

'''

# implementation of worst case linear time algorithm to find k'th smallest element
# Returns k'th smallest element in arr[l..r] in worst case linear time
# ASSUMPTION: ALL ELEMENTS IN ARR[] ARE DISTINCT
def kth_smallest_set_3(arr, l, r, k):

    # if k is smaller than number of elements in array
    if( k > 0 and k <= r -l +1):

        # Number of elements in arr[l..r]
        n = r - l + 1

        # Divide arr[] in groups of size 5, calculate the median of each group & store it in median array
        median =[]

        i = 0
        while(i < n // 5):
            median.append(findMedian(arr, l + i * 5, 5))
            i += 1

        # For last group with less than 5 elements
        if(i * 5 < n):
            median.append(findMedian(arr, l +i * 5, n % 5))
            i +=1

        # Find median of all medians using recursive call.
        # If median[] has only one element, then no need of recursive call
        if i == 1:
            medOfMed = median[i -1]
        else:
            medOfMed = kth_smallest_set_3(median, 0, i-1, i//2)

        # Partition the array around a medOfMed element and get position of pivot element in sorted array
        pos = partition(arr, l, r, medOfMed)

        # If position is same as k
        if(pos -l == k-1):
            return arr[pos]
        if(pos -l > k -1): # if position is more, recur for left subarray
            return kth_smallest_set_3(arr, l, pos -1, k)
        return kth_smallest_set_3(arr, pos +1,r, k-pos +l -1)

    # if k is more than the number of elements in the array
    return 999999999999

def swap(arr, a, b):
    temp = arr[a]
    arr[a] =arr[b]
    arr[b] = temp

# it searches for x in arr[l ..r], and partitions the array around x.
def partition(arr, l, r,x):
    for i in range(l, r):
        if arr[i] == x:
            swap(arr, r, i)
            break
    x = arr[r]
    i = l
    for j in range(l, r):
        if(arr[j] <= x):
            swap(arr, i, j)
            i += 1
    swap(arr, i, r)
    return i

# A simple functon to find median of arr[] from index l to l+n
def findMedian(arr, l, n):
    lis =[]
    for i in range(l, l+n):
        lis.append(arr[i])
    
    # sort the array
    lis.sort()

    #return the middle element
    return lis[n // 2]

if __name__ == '__main__':
 
    arr = [12, 3, 5, 7, 4, 19, 26]
    n = len(arr)
    k = 3
    print("K'th smallest element is",kth_smallest_set_3(arr, 0, n - 1, k))

'''
Time Complexity: 
The worst case time complexity of the above algorithm is O(n). Let us analyze all steps. 

The steps 1) and 2) take O(n) time as finding median of an array of size 5 takes O(1) time and 
there are n/5 arrays of size 5. 
The step 3) takes T(n/5) time. The step 4 is standard partition and takes O(n) time.

The interesting steps are 6) and 7). At most, one of them is executed. These are recursive steps.
What is the worst case size of these recursive calls. The answer is maximum number of elements 
greater than medOfMed (obtained in step 3) or maximum number of elements smaller than medOfMed.

How many elements are greater than medOfMed and how many are smaller?

At least half of the medians found in step 2 are greater than or equal to medOfMed. Thus, at least 
half of the n/5 groups contribute 3 elements that are greater than medOfMed, except for the one group 
that has fewer than 5 elements. Therefore, the number of elements greater than medOfMed is at least. 

[Formula]

Similarly, the number of elements that are less than medOfMed is at least 3n/10 – 6. 

In the worst case, the function recurs for at most n – (3n/10 – 6) which is 7n/10 + 6 elements.

Note that 7n/10 + 6 20 20 and that any input of 80 or fewer elements requires O(1) time. We can 
therefore obtain the recurrence 

[Formula]

We show that the running time is linear by substitution.

Assume that T(n) cn for some constant c and all n > 80. Substituting this inductive hypothesis into
the right-hand side of the recurrence yields 

T(n)  <= cn/5 + c(7n/10 + 6) + O(n)
     <= cn/5 + c + 7cn/10 + 6c + O(n)
    <= 9cn/10 + 7c + O(n)
    <= cn, 
since we can pick c large enough so that c(n/10 – 7) is larger than the function described by 
the O(n) term for all n > 80. 
The worst-case running time of is therefore
linear (Source: http://staff.ustc.edu.cn/~csli/graduate/algorithms/book6/chap10.htm ).
Note that the above algorithm is linear in worst case, but the constants are very high for this 
algorithm. Therefore, this algorithm doesn’t work well in practical situations, 
randomized quickSelect works much better and preferred.

# http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-introduction-to-algorithms-sma-5503-fall-2005/video-lectures/lecture-6-order-statistics-median/
# http://www.flipkart.com/introduction-algorithms-8120340078/p/itmczynzhyhxv2gs?pid=9788120340077&affid=sandeepgfg
# http://staff.ustc.edu.cn/~csli/graduate/algorithms/book6/chap10.htm





Time complexity of the solution below is O(n Log n). Note that set in STL uses a self-balancing BST
internally and therefore time complexity of search and insert operations is O(log n).
'''
print("Using an Iterator - STL")

def kth_smallest(arr,k):
	n = len(arr)
	set_arr =set((arr))
	my_iter =iter(set_arr)
	for i in range(k):
		val = my_iter.__next__()
	return val

print("expected is 5, actual:", kth_smallest([12, 3, 5, 7, 3, 19],2))