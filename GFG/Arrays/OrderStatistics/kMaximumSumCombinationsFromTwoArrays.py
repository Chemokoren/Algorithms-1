"""
K maximum sum combinations from two arrays

Given two equally sized arrays(A,B) and N(size of both arrays). A sum combination is made by
adding one element from array A and another element from array B. Display the maximum K valid
sum combinations from all the possile sum combinations.

Input :  A[] : {3, 2} 
         B[] : {1, 4}
         K : 2 [Number of maximum sum
               combinations to be printed]
Output : 7    // (A : 3) + (B : 4)
         6    // (A : 2) + (B : 4)

Input :  A[] : {4, 2, 5, 1}
         B[] : {8, 0, 3, 5}
         K : 3
Output : 13   // (A : 5) + (B : 8)
         12   // (A : 4) + (B :  8)
         10   // (A : 2) + (B : 8)

Approach 1: Naive algorithm

We can use Brute force through all the possible combinations that can be made by taking one 
element from array A and another from array B and inserting them to a max heap. In max heap 
maximum element is at the root node so whenever we pop from max heap we get the maximum
element present in the heap. After inserting all the sum combinations we take out K elements 
from max heap and display it.

Time Complexity: O(N^2)

"""

# program to find K maximum combinations from two arrays

import math
from queue import PriorityQueue

# Function to display first K maximum sum combinations

def KMaxCombinations(A, B, N, K):
    # Max heap
    pq =PriorityQueue()

    # Insert all the possible combinations in max heap
    for i in range(0, N):
        for j in range(0, N):
            a = A[i] + B[j]
            pq.put((-a, a))

    # Pop first N elements from max heap and display them
    count = 0
    while(count < K):
        print(pq.get()[1])
        count = count + 1

A = [4, 2, 5, 1]
B = [8, 0, 5, 3]
N = len(A)
K = 3
 
# Function call
KMaxCombinations(A, B, N, K)


"""
Approach 2: Sorting, Max heap, Map
Instead of brute-forcing through all possible sum combinations, we should find a way to 
limit our search space to possible candidate sum combinations
1. Sort both arrays array A and array B
2. Create a max heap i.e. to store the sum combinations along with the indices of elements 
from both arrays A and B which make up the sum. Heap is ordered by the sum.
3. Initialize the heap with maximum  possible sum combination i.e. (A[N-1] + B[N -1] where
N is the  size of array) and with the indices of elements from both arrays(N-1, N-1). 
The tuple inside max heap will be(A[N-1] + B[N-1]m N-1, N-1). Heap is ordered by 
first value i.e. sum of both elements.
4. Pop the heap to get the current largest sum and along with the indices of the element 
that make up the sum. Let the tuple be (sum, i, j).
    1) Next insert (A[i-1]+B[j], i-1,j) and (A[i]+B[j-1], i, j-1) into the max heap but make
    sure that the pair of indices i.e (i-1, j) and (i, j-1) are not already present in the 
    max  heap. 
    2) Go back to 4 until K times

Time Complexity : O(N log N) assuming K <= N

"""
from queue import PriorityQueue

# An efficient program to find top K elements from two arrays.
class TestInfo:
    
    def MaxPairSum(self, A,B, N, K):
        #sort both arrays A and B
        A.sort()
        B.sort()

        # Max heap which contains Pair of the format (sum, (i, j)) i and j are the indices 
        # of the elements from array A and array B which make up the sum.
		# PriorityQueue<PairSum> sums = new PriorityQueue<PairSum>();
        sums = PriorityQueue()
		
		# pairs is used to store the indices of the Pair(i, j) we use pairs to make sure
		# the indices doe not repeat inside max heap.
        # HashSet<Pair> pairs = new HashSet<Pair>();

        pairs = {}
		
		#initialize the heap with the maximum sum combination ie (A[N - 1] + B[N - 1])
		# and also push indices (N - 1, N - 1) along with sum.
        l = N - 1
        m = N - 1
        pairs[l]= m
        sums.put(A[l] + B[m], l, m)
		
		# iterate upto K
        for i in range(0, K):
            # Poll the element from the maxheap in theformat (sum, (l,m))
            max = sums.get()
            print(max)  
            #l = max.l - 1
            l = max - 1
            # m = max.m
            m = max
            # insert only if l and m are greater than 0 and the pair (l, m) is  not already present inside set i.e.
            # no repeating pair should be present inside the heap.
            if (l >= 0 and m >= 0 and l not in pairs):
                # insert (A[l]+B[m], (l, m)) in the heap
                sums.put(A[l] + B[m], l, m)
                pairs[l] =m
                
            l = max.l
            m = max.m - 1
            
            # insert only if l and m are greater than 0 and  the pair (l, m) is not
            # # already present inside set i.e. no repeating pair should be present inside the heap.
            
            if (l >= 0 and m >= 0 and l not in pairs):
                # insert (A[i1]+B[i2], (i1, i2)) in the heap
                sums.put((A[l]+ B[m], l, m))
                pairs[l] = m
			


#Driver Code
if __name__=='__main__':
    A= [ 1, 4, 2, 3 ]
    B= [ 2, 5, 1, 6 ]
    N = len(A)
    K = 4
    
    #Function Call
    tt = TestInfo()
    tt.MaxPairSum(A, B, N, K)