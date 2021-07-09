"""
find k pairs with smallest sums in two arrays

Given two integer arrays arr1[] and arr2[] sorted in ascending order and an integer k. Find k
pairs with smallest sums such that one element of a pair belongs to arr1[] and other elements
belong to arr2[]

Examples: 

Input :  arr1[] = {1, 7, 11}
         arr2[] = {2, 4, 6}
         k = 3
Output : [1, 2],
         [1, 4],
         [1, 6]
Explanation: The first 3 pairs are returned 
from the sequence [1, 2], [1, 4], [1, 6], 
[7, 2], [7, 4], [11, 2], [7, 6], [11, 4], 
[11, 6]

method 1: simple
1) Find all pairs and store their sums. Time complexity of this step is O(n1 * n2) where n1
and n2 are sizes of input arrays.
2) Then sort pairs according to sum. Time complexity of this step is O(n1*n2 * log(n1*n2))

Overall Time Complexity: O(n1*n2*log(n1*n2))

Method 2: Efficient

One by one find k smallest sum pairs, starting from least sum pair. The idea is to keep track
of all elements of arr2[] which have been already considered for every element arr[i] so 
that in an iteration we only consider next element. For this purpose, we use an index 
array index2[] to track the indexes of next elements in the other array. It simply means 
that which element of second array to be added with the element of first array in each and 
every iteration. We increment value in index array for the element that forms next minimum
value pair.

Time Complexity : O(k*n1)

"""

# program to print first k pairs with least sum from two arrays
import sys

# Function to find k pairs with least sum such that one element of a pair is from arr1[] and
# other element is from arr2[]
def kSmallestPair(arr1, n1, arr2, n2, k):
    if (k > n1*n2):
        print("k pairs don't exist")
        return
 
    # Stores current index in arr2[] for
    # every element of arr1[]. Initially
    # all values are considered 0.
    # Here current index is the index before
    # which all elements are considered as
    # part of output.
    index2 = [0 for i in range(n1)]
 
    while (k > 0):
        # Initialize current pair sum as infinite
        min_sum = sys.maxsize
        min_index = 0
 
        # To pick next pair, traverse for all elements
        # of arr1[], for every element, find corresponding
        # current element in arr2[] and pick minimum of
        # all formed pairs.
        for i1 in range(0,n1,1):
            # Check if current element of arr1[] plus
            # element of array2 to be used gives minimum
            # sum
            if (index2[i1] < n2 and arr1[i1] + arr2[index2[i1]] < min_sum):
                # Update index that gives minimum
                min_index = i1
 
                # update minimum sum
                min_sum = arr1[i1] + arr2[index2[i1]]
         
        print("(",arr1[min_index],",",arr2[index2[min_index]],")",end = " ")
 
        index2[min_index] += 1
 
        k -= 1


if __name__ == '__main__':

    arr1 = [1, 3, 11]
    n1 = len(arr1)
 
    arr2 = [2, 4, 8]
    n2 = len(arr2)
 
    k = 4
    kSmallestPair( arr1, n1, arr2, n2, k)

"""
Method 3: Using Sorting, Min heap, Map

Instead of brute forcing through all the possible sum combinations we should find a way 
to limit our search space to possible candidate sum combinations.



Sort both arrays array A and array B.

Create a min heap i.e priority_queue to store the sum combinations along with the indices 
of elements from both arrays A and B which make up the sum. Heap is ordered by the sum.

Initialize the heap with the minimum possible sum combination i.e (A[0] + B[0]) and with the
indices of elements from both arrays (0, 0). The tuple inside min heap will 
be (A[0] + B[0], 0, 0). Heap is ordered by first value i.e sum of both elements.

Pop the heap to get the current smallest sum and along with the indices of the element that
make up the sum. Let the tuple be (sum, i, j). 

Next insert (A[i + 1] + B[j], i + 1, j) and (A[i] + B[j + 1], i, j + 1) into the min heap but make sure that the pair of indices i.e (i + 1, j) and (i, j + 1) are not already present in the min heap.To check this we can use set in C++.
Go back to 4 until K times.

Time Complexity : O(n*logn) assuming k<=n

"""