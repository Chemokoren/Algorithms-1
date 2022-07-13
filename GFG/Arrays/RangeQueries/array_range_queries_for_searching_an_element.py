"""
Array range queries for searching an element

Given an array of N elements and Q queries of the for L R X. For each query, you 
have to output if the element X exists in the array between the indices L and R(included)

Input : N = 5
        arr = [1, 1, 5, 4, 5]
        Q = 3
        1 3 2
        2 5 1
        3 5 5         
Output : No
         Yes
         Yes
Explanation :
For the first query, 2 does not exist between the indices 1 and 3.
For the second query, 1 exists between the indices 2 and 5.
For the third query, 5 exists between the indices 3 and 5.

Naive Approach:
The naive method would be to traverse the elements from L to R for each query, linearly
searching for X. In the worst case, there can be N elements from L to R, hence the worst
case time complexity for each query would be O(N). Therefore, for all the Q queries, the
time complexity would turn out to be O(Q*N).

Using Union-Find Method
-----------------------
This method checks only one element among all the consecutive equal values. If X is not 
equal to these values, then the algorithm skips all the other equal elements and 
contiues traversal with the next different element. This algorithm is evidently useful 
only when there are consecutive equal elements in large amounts.

Algorithm
1. Merge all the consecutive equal elements in one group.
2. While processing a query, start from R. let index = R.
3. Comparre a[index] with X. If they are equal, then print "YES" and break out of
traversing the rest of the range. Else, skip all the consecutive elements belonging to the 
group of a[index]. Index becomes equal to one less than  the index of the root of this 
group.
4.Continue the above step either till X is found or  till index becomes less than L.

5.If index becomes less than L, print "No".

"""
# program to determine ifthe element exists for different range queries

# Structure to represent a query range
class Query:
    def __init__(self, L, R, X):
        self.L = L
        self.R = R
        self.X = X

maxn  =100
root =[0]*maxn

# Find the root of the group containing the element at index x
def find(x):
    if x == root[x]:
        return x
    else:
        root[x] = find(root[x])
        return root[x]

# merge the two groups containing elements at indices x and y into one group
def uni(x, y):
    p = find(x)
    q = find(y)
    if p!= q:
        root[p] = root[q]

def initialize(a, n, q,m):
    # make n subsets with every element as its root
    for i in range(n):
        root[i] = i

    # consecutive elements equal in value are merged into one single group
    for i in range(1, n):
        if a[i]== a[i -1]:
            uni(i, i -1)

if __name__=="__main__":
    a =[1,1,5,4,5]
    n = len(a)

    q =[Query(0,2,2),
        Query(1,4,1),
        Query(2,4,5)
    ]
    m = len(q)
    initialize(a,n,q,m)

    for i in range(m):
        flag = False
        l =q[i].L
        r =q[i].R
        x =q[i].X
        p =r


        while p >= l:
            # check if the current element in consideration is equal to x or not 
            # if it is equal, then x exists in the range
            if a[p]==x:
                flag = True
                break
            p = find(p) - 1

        # print if x exists or not
        if flag:
            print("%d exists between [%d, %d]" % (x, l, r))
        else:
            print("%d does not exist between [%d, %d]" %(x, l, r))

        
"""
Efficient Approach (Using Mo's Algorithm)
Mo's algorithm is one of the finest applications for square root decomposition.
It is based on the basic idea of using the answer to the previous query to compute the 
answer for the current query. This is made possible because the Mo's algorithm is 
constructed in such a way that if F([L,R]) is known, then F([L+1,R]), F([L-1, R]),
F([L, R+1]) and F([L, R-1]) can be computed easily, each in O(F) time.

Answering queries in the order they are asked, then the time complexity is not improved
to what is needed to be. To reduce the time complexity considerably, the queries are 
divided into blocks and then sorted. The exact algorithm to sort the queries is as 
follows:

    Denote BLOCK_SIZE = sqrt(N)
    All the queries with the same L/BLOCK_SIZE are put in the same block
    Within a block, the queries are sorted based on their R values
    The sort function thus compares two queries, Q1 and Q2 as follows: 
    Q1 must come before Q2 if: 
    1. L1/BLOCK_SIZE<L2/BLOCK_SIZE 
    2. L1/BLOCK_SIZE=L2/BLOCK_SIZE and R1<R2

After sorting the queries, the next step is to compute the answer to the first query and
consequently answer the rest of the queries. To determine if a particular elements exists
or not, check the frequency of the element in that range. A non zero frequency confirms
the existence of the element in that range.
To store the frequency of the elements, STL map has been used in the following code. In 
the given example, first query after sorting the array of queries is {0,2,2}. Hash the 
frequencies of the elemets in [0,2] and then check the frequency of the element 2 from the 
map. Since, 2 occurs 0 times, print "No".
While processing the next query, which is {1,4,1} in this case, decrement the frequencies 
of the elements in the range [0,1] and increment the frequencies of the elements in range
[3,4]. This ste gives the frequencies of elements in [1,4] and it can easily be seen from
the map that 1 exists in this range.


Time complexity : 
The pre-processing part, that is sorting the queries takes O(m Log m) time. 
The index variable for R changes at most O(n * sqrt{n}) times throughout the run and 
that for L changes its value at most O(m * sqrt{n}) times. Hence, processing all queries
takes O(n * sqrt{n}) + O(m * sqrt{n}) = O((m+n) * sqrt{n}) time.


"""

#Program to compute sum of ranges for different range queries


#  Class to represent a query range
class Query:
	def __init__(self, L:int, R:int,x:int):
		self.L = L
		self.R = R
		self.x = x
	


class Main{

	// Prints sum of all query ranges. m is number of queries
	// n is size of array a[].
	static void queryResults(int a[], int n, ArrayList<Query> q, int m){
		
		// Find block size
		int block = (int) Math.sqrt(n);
	
		// Sort all queries so that queries of same blocks
		// are arranged together.
		Collections.sort(q, new Comparator<Query>(){
			
			// Function used to sort all queries so that all queries
			// of the same block are arranged together and within a block,
			// queries are sorted in increasing order of R values.
			public int compare(Query x, Query y){

				// Different blocks, sort by block.
				if (x.L/block != y.L/block)
					return (x.L < y.L ? -1 : 1);

				// Same block, sort by R value
				return (x.R < y.R ? -1 : 1);
			}
		});

		// Initialize current L, current R and current sum
		int currL = 0, currR = 0;
		
		Map<Integer,Integer> mp=new HashMap<Integer,Integer>();
		
		// Traverse through all queries
		for (int i=0; i<m; i++)
		{
			// L and R values of current range
			int L = q.get(i).L, R = q.get(i).R, X = q.get(i).x;

			// Remove extra elements of previous range. For
			// example if previous range is [0, 3] and current
			// range is [2, 5], then a[0] and a[1] are subtracted
			while (currL < L)
			{
				if(mp.containsKey(a[currL])){
			mp.put(a[currL],mp.get(a[currL])-1);
				}
				else{
			mp.put(a[currL],1);
				}
				
				//mp.put(a[currL], mp.get(a[currL] - 1));
				currL++;
			}

			// Add Elements of current Range
			while (currL > L)
			{
				if(mp.containsKey(a[currL-1])){
			mp.put(a[currL-1],mp.get(a[currL-1])+1);
				}
				else{
			mp.put(a[currL-1],1);
				}
				//mp.put(a[currL], mp.get(a[currL-1]+1));
				currL--;
			}
			while (currR <= R)
			{
				if(mp.containsKey(a[currR])){
			mp.put(a[currR],mp.get(a[currR])+1);
				}
				else{
			mp.put(a[currR],1);
				}
				//mp.put(a[currR], mp.get(a[currR]+1));
				currR++;
			}

			// Remove elements of previous range. For example
			// when previous range is [0, 10] and current range
			// is [3, 8], then a[9] and a[10] are subtracted
			while (currR > R+1)
			{
				if(mp.containsKey(a[currR-1])){
			mp.put(a[currR-1],mp.get(a[currR-1])-1);
				}
				else{
			mp.put(a[currR-1],1);
				
				//mp[a[currR-1]]--;
				currR--;
			}
			}
			
			if (mp.containsKey(X))
			System.out.println(X + " exists between [" + L +
						", " + R + "] ");
			else
			System.out.println(X + " does not exist between [" + L +
						", " + R + "] ");
				
			// Print sum of current range
			
			
		}
	}
	
	// Driver program
	public static void main(String argv[]){
		ArrayList<Query> q = new ArrayList<Query>();
		q.add(new Query(0,2,2));
		q.add(new Query(1,4,1));
		q.add(new Query(2,4,5));

		int a[] = {1, 1, 5, 4, 5 };
		queryResults(a, a.length, q, q.size());
	}
}




'''
my tests
'''
def my_tests(arr,Q):
    l,r,key =Q
    if key in  (arr[l-1: r]):
        return 'Yes'
    else:
        return 'No'

print("expected: No, actual: ", my_tests([1, 1, 5, 4, 5], [1, 3, 2]))
print("expected: Yes, actual: ", my_tests([1, 1, 5, 4, 5], [2, 5, 1]))
print("expected: Yes, actual: ", my_tests([1, 1, 5, 4, 5], [3, 5, 5]))