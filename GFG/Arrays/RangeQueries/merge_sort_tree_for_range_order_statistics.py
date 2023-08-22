"""
Merge Sort Tree for Range Order Statistics

Given an array of n numbers, the task is to answer the following queries:

kthSmallest(start, end, k): Find the kth smallest number in the range from array
                            index 'start' to 'end'


Examples:

Input : arr[] = {3, 2, 5, 1, 8, 9|
     Query 1: start = 2, end = 5, k = 2
     Query 2: start = 1, end = 6, k = 4
Output : 2
         5
Explanation:
[2, 5, 1, 8] represents the range from 2 to 
5 and 2 is the 2nd smallest number 
in the range[3, 2, 5, 1, 8, 9] represents 
the range from 1 to 6 and 5 is the 4th
smallest number in the range

The key idea is to build a Segment Tree with a vector at every node and the vector contains
all the elements of the sub-range in a sorted order. And if we observe this segment tree 
structure this is somewhat similar to the tree formed during the merge sort 
algorithm(that is why it is called merge sort tree) We use same implementation as discussed
in Merge Sort Tree (Smaller or equal elements in given row range) 

Firstly, we maintain a vector of pairs where each pair {value, index} is such that first 
element of pair represents the element of the input array and the second element of the 
pair represents the index at which it occurs. Now we sort this vector of pairs on the 
basis of the first element of each pair. After this we build a Merge Sort Tree where each 
node has a vector of indices in the sorted range. When we have to answer a query we find 
if the Kth smallest number lies in the left sub-tree or in the right sub-tree.

The idea is to use two binary searches and find the number of elements in the left sub-tree
such  that the indices lie within the given query range. Let the number of such indices be
M. If M>=K, it means we will be able to find the Kth smallest Number in the left sub-tree 
thus we call on the left sub-tree. Else the Kth smallest number lies in the right sub-tree
but this time we don’t have to look for the K th smallest number as we already have first 
M smallest numbers of the range in the left sub-tree thus we should look for the remaining
part ie the (K-M)th number in the right sub-tree. 
This is the Index of Kth smallest number the value at this index is the required number. 

Thus, we can get the Kth smallest number query in range L to R, in O(n(logn)^2) by building 
the merge sort tree on indices.

"""
# program to implement k-th order statistics


MAX = 1000

# Constructs a segment tree and stores tree[]
# vector<pair<int, int> > &a, vector<int> tree[]
def buildTree(treeIndex:int, l:int,r:int,a, tree): 
    ''' l => start of range,
		r => ending of a range
		treeIndex => index in the Segment Tree/Merge
					Sort Tree '''

	# leaf node *
    if (l == r):
        tree[treeIndex].push_back(a[l].second)
        return
        
    mid = (l + r) / 2
    
    #  building left subtree 
    buildTree(2 * treeIndex, l, mid, a, tree)
    
    # building left subtree 
    buildTree(2 * treeIndex + 1, mid + 1, r, a, tree)

	# merging left and right child in sorted order */

    merge(tree[2 * treeIndex].begin(),
		tree[2 * treeIndex].end(),
		tree[2 * treeIndex + 1].begin(),
		tree[2 * treeIndex + 1].end(),
		back_inserter(tree[treeIndex]))

# Returns the Kth smallest number in query range
#  vector<int> tree[])
def queryRec(segmentStart, segmentEnd,queryStart, queryEnd, treeIndex,K, tree):
    
    ''' 
		segmentStart => start of a Segment,
		segmentEnd => ending of a Segment,
		queryStart => start of a query range,
		queryEnd	 => ending of a query range,
		treeIndex => index in the Segment
						Tree/Merge Sort Tree,
		K => kth smallest number to find 
        
    '''
    if (segmentStart == segmentEnd):
        return tree[treeIndex][0]
        
    mid = (segmentStart + segmentEnd) / 2 
    
    # finds the last index in the segment which is <= queryEnd
    last_in_query_range = (upper_bound(tree[2 * treeIndex].begin(),
						tree[2 * treeIndex].end(),
										queryEnd)
					- tree[2 * treeIndex].begin())
                    
    # finds the first index in the segment
	#  which is >= queryStart

    first_in_query_range =(lower_bound(tree[2 * treeIndex].begin(),
							tree[2 * treeIndex].end(),
										queryStart)
						- tree[2 * treeIndex].begin())
                        
    M = last_in_query_range - first_in_query_range
    
    # Kth smallest is in left subtree,
	# so recursively call left subtree for Kth
	# smallest number

    if (M >= K):
        return queryRec(segmentStart, mid, queryStart,
					queryEnd, 2 * treeIndex, K, tree)
    else:
        
        # Kth smallest is in right subtree,
		# so recursively call right subtree for the
		# (K-M)th smallest number

        return queryRec(mid + 1, segmentEnd, queryStart,
			queryEnd, 2 * treeIndex + 1, K - M, tree)

# A wrapper over query()
# vector<pair<int, int> > &a, vector<int> tree[]
# the rest are int
def query(queryStart, queryEnd, K, n,a, tree):
    return queryRec(0, n - 1, queryStart - 1, queryEnd - 1,	1, K, tree)


# Driver code
if __name__=="__main__":
    
    arr =[ 3, 2, 5, 1, 8, 9 ]
    n = len(arr)/(arr[0])

	# vector of pairs of form {element, index}
	# vector<pair<int, int> > v;

    v =[]
    for  i in range(0,n):
        v.push_back(make_pair(arr[i], i))
        
    # sort the vector
    sort(v.begin(), v.end())

	# Construct segment tree in tree[]
	# vector<int> tree[MAX];
    tree[MAX]
    buildTree(1, 0, n - 1, v, tree);

	# Answer queries
    # kSmallestIndex hold the index of the kth smallest number
    # 
    kSmallestIndex = query(2, 5, 2, n, v, tree)
    print(arr[kSmallestIndex])
    
    kSmallestIndex = query(1, 6, 4, n, v, tree)
    print(arr[kSmallestIndex])





'''
my tests

'''
def my_tests(arr,Q):
    l,r,k =Q
    new_arr= arr[l-1:r]
    new_arr.sort()
    return new_arr[k-1]

print("expected: 2, actual: ",my_tests([3, 2, 5, 1, 8, 9],[2,5,2]))
print("expected: 5, actual: ",my_tests([3, 2, 5, 1, 8, 9],[1,6,4]))


