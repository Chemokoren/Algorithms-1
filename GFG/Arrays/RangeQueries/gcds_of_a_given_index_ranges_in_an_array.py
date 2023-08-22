"""
GCDs of given index ranges in an array

Given an array a[0...n-1]. We should be able to efficiently find the GCD from index 
qs(query start) to qe(query end) where 0 <=qs<qe<=n-1. Example:

Input : a[] = {2, 3, 60, 90, 50};
        Index Ranges : {1, 3}, {2, 4}, {0, 2}
Output: GCDs of given ranges are 3, 10, 1

Method 1
- A simple solution is to run a loop from qs to qe and find GCD in a given range. This 
solution takes O(n) time in worst case.

Method 2 (2D Array)

Another solution is to create a 2D array where an entry[i,j] stores the GCD in range
arr[i..j]. GCD of a given range can now be calculated in O(1) time, but preprocessing 
takes  O(n^2) time. Also, this approach needs O(n^2) extra space which may become huge
for large input arrays.

Method 3(Segment Tree)

Segment tree can be used to do preprocessing and query in moderate time. With segment 
tree, preprocessing time is O(n) and time to for GCD query is O(Logn). 
The extra space required is O(n) to store the segment tree.

Representation of Segment trees

    Leaf Nodes are the elements of the input array.
    Each internal node represents GCD of all leaves under it.

Array representation of tree is used to represent Segment Trees i.e., for each node at
index i,

    Left child is at index 2*i+1
    Right child at 2*i+2 and the parent is at floor((i-1)/2).

Construction of Segment Tree from given array

    Begin with a segment arr[0 . . . n-1] and keep dividing into two halves. Every time 
    we divide the current segment into two halves (if it has not yet become a segment of
    length 1), then call the same procedure on both halves, and for each such segment,
    we store the GCD value in a segment tree node.

    All levels of the constructed segment tree will be completely filled except the last 
    level. Also, the tree will be a Full Binary Tree (every node has 0 or two children) 
    because we always divide segments in two halves at every level.

    Since the constructed tree is always full binary tree with n leaves, there will be n-1 
    internal nodes. So total number of nodes will be 2*n – 1.
    Height of the segment tree will be &lceillog2n&rceil. 
    Since the tree is represented using array and relation between parent and child
    indexes must be maintained, size of memory allocated for segment tree will be 
    2*2⌈log2n⌉ – 1

Query for GCD of given range

/ qs --> query start index, qe --> query end index
int GCD(node, qs, qe)
{
   if range of node is within qs and qe
      return value in node
   else if range of node is completely 
      outside qs and qe
      return INFINITE
   else
      return GCD( GCD(node's left child, qs, qe), 
                  GCD(node's right child, qs, qe) )
}

Time Complexity: Time Complexity for tree construction is O(n * log(min(a, b))), 
where n is the number of modes and a and b are nodes whose GCD is calculated during
merge operation. There are total 2n-1 nodes, and value of every node is calculated only
once in tree construction. Time complexity to query is O(Log n * Log n).

"""
import math

# program to find GCD of a nmber in a given Range sing segment Trees
st =[] # Array to store segment tree

'''
Function to construct segment tree from given array. This function allocates memory
for segment tree and calls constructSTUtil() to fill the allocated memory
'''
def constructSegmentTree(arr):
    height =math.floor(math.ceil(math.log(len(arr)) /math.log(2)))
    size  = 2 * math.pow(2, height) -1
    st = [0] * int(size)
    constructST(arr, 0, len(arr) -1, 0)
    return st

'''
A recursive function that constructs segment Tree for array[ss..se]. si is index of 
current node in segment tree st

'''
def constructST(arr, ss, se, si):
    if(ss == se):
        st[si] =arr[ss]
        return st[si]
    mid = math.floor(ss + (se - ss) / 2)
    st[si] = gcd(constructST(arr, ss, mid, si * 2 + 1)),constructST(arr, mid+1, se, si * 2 + 2)
    return st[si]

# function to find gcd of 2 numbers.
def gcd(a,b):
    if(a < b):
        # if b is greater than a, swap and b
        temp = b
        b = a
        a = temp
    if(b == 0):
        return a
    return gcd(b, a%b)

# finding the gcd of given range
def findRangeGCD(ss, se, arr):
    n = len(arr)
    if (ss < 0 or se > n-1 or ss > se):
        print("Invalid arguments")
    return findGcd(0, n-1, ss, se, 0)

'''
A recrsive function to get gcd of given range of array indexes. The following are 
parameters for this function

st --> Pointer to segment tree
si --> Index of current node in the segment tree. Initially 0 is passed as root is always
at index 0
ss & se --> starting and ending indexes of the segment represented by current node, i.e.,
st[si]
qs & qe --> starting and ending indexes of query range

'''
def findGcd(ss, se, qs, qe, si):
    if(ss > qe or se < qs):
        return 0

    if(qs <= ss and qe >= se):
        return st[si]
    
    mid = math.floor(se + (se -ss) / 2)

    return gcd(findGcd(ss, mid, qs, qe, si *2+1), findGcd(mid +1, se, qs, qe, si*2 +2))

a = [2, 3, 6, 9, 5]
 
constructSegmentTree(a)
 
l = 1; # Starting index of range.
r = 3; # Last index of range.
print("GCD of the given range is: ")
print(findRangeGCD(l, r, a))




'''
my tests
'''

# def my_tests(arr, Q):
#     l, r =Q
#     arr =arr[l:r+1]
#     greatest = max(arr[l:r+1])
#     ans =greatest
#     for i in arr:
#         if i % greatest ==0:
#             ans =i
#         greatest -=1
#     return ans

# print("expected: 3, actual:", my_tests([2, 3, 60, 90, 50], [1,3]))


