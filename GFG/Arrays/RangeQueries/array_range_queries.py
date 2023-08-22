"""
Array range queries over range queries

Given an array of size n and a given set of commands of size m. The commands are enumerated
from 1 to m. These commands can be of the following two types of commands:
1. Type 1 [lr (1<=l<=r<=n)]: Increase all elements of the array by one, whose indices 
belongs to the range[l,r]. In these queries of the index is inclusive in the range.

2. Type 2[lr (1<=l<=r<=m)]: Execute all the commands whose indices are in the range[l,r]. 
In  these queries of the index is inclusive in the range. It's guaranteed that r is strictly
less than the enumeration/number of the current command.

Note: The array indexing is from 1 as per the problem statement.

Example 1 

Input : 5 5
        1 1 2
        1 4 5
        2 1 2
        2 1 3
        2 3 4
Output : 7 7 0 7 7

Explanation of Example 1 : 

Our array initially is of size 5 whose each element has been initialized to 0. 
So now the question states that we have 5 queries for the above example. 

    Query 1 is of type 1 
    -------------------- 
    As stated above we will simply increment the array indices by 1 the given indices are 
    1 and 2 so after the execution of the first our array turns down to be 1 1 0 0 0 .
   
    Query 2 is of type 1 
    --------------------
    As stated above we will simply increment the array indices by 1 
    the given indices are 4 and 5 so after the execution of the first our array turns down
    to be 1 1 0 1 1 .

    Query 3 is of type 2
    --------------------
    
    As stated in the definition of this type of query we will execute the queries stated 
    in the range i.e. we will operate the queries instead of the array. The range given
    is 1 and 2 so we will execute queries 1 and 2 again i.e. we will use repetitive
    approach for the type 2 queries so we will execute query 1 again and our array will 
    be 2 2 0 1 1. Now when we execute the query we will execute query 2 and our resultant
    array will be 2 2 0 2 2 .

    Query 4 is of type 2
    --------------------
    
    As stated in the definition of this type of query we will execute the queries stated 
    in the range i.e. we will operate the queries instead of the array.
    The range given is 1 and 3 so we will execute queries 1, 2 and 3 again i.e. using 
    repetitive approach queries 1, 2 and 3 will be executed. After the execution of the 
    query 1 again the array will be 3 3 0 2 2 . After the execution of the query 2 again 
    the array will be 3 3 0 3 3 . Now due to query 3 inclusive in the range we will 
    execute query 3 the resultant array will be 4 4 0 4 4 . As explained above.

    Query 5 is of type 2
    --------------------
    
    The last query will execute the 3rd and 4th query which has been explained above. 
    After the execution of the 3rd query our array will be 5 5 0 5 5 . And after the 
    execution of the 4th query i.e. execution of query 1, 2 and 3 our array will 
    be 7 7 0 7 7 The above is the desired result.

Example 2 

Input : 1 2
        1 1 1
        1 1 1
Output : 2

Explanation of the example 2: 
Our array initially is of size 1 whose each element has been initialized to 0. 
So now the question states that we have 2 queries for the above example.  

    Query 1 is of type 1 
    --------------------
    
    As stated above we will simply increment the array indices by 1 the given indices 
    are 1 and 1 so after the execution of the first our array turns down to be 1 .

    Query 2 is of type 1
    --------------------
    
    As stated above we will simply increment the array indices by 1 the given indices are 
    1 and 1 so after the execution of the first our array turns down to be 2 . 
    This gives us the desired result

Method 1 : 

This method is the brute force method where by simple recursion is applied on the type 2
queries and for type 1 queries simple increment in the array index is performed. 

The Time complexity of the above code is O(2 ^ m)

"""
# program to perform range queries over range queries.

# Function to create the record array
def record_sum(record, l, r, n, adder):
	
	for i in range(l, r + 1):
		record[i] += adder

# Driver Code
n = 5
m = 5
arr = [0]*n

# Build query matrix
query = [[1, 1, 2 ],[ 1, 4, 5 ],[2, 1, 2 ],
		[ 2, 1, 3 ],[ 2, 3, 4]]
record = [0]*m

for i in range(m - 1, -1, -1):
	
	# If query is of type 2 then function
	# call to record_sum
	if (query[i][0] == 2):
		record_sum(record, query[i][1] - 1,
				query[i][2] - 1, m, record[i] + 1)
		
	# If query is of type 1 then simply add
	# 1 to the record array
	else:
		record_sum(record, i, i, m, 1)
		
# for type 1 queries adding the contains of
# record array to the main array record array
for i in range(m):
	if (query[i][0] == 1):
		record_sum(arr, query[i][1] - 1,
			query[i][2] - 1, n, record[i])

# printing the array
for i in range(n):
	print(arr[i], end=' ')


"""
Method 2 : 

In this method we use an extra array for creating the record array to find the number of 
time a particular query is being executed and after creating the record array we simply
execute the queries of type 1 and the contains of the record array is simply added to
the main array the and this would give us the resultant array.

The Time complexity of the above code is O(n^2) 


"""
print("\n Method 2 \n")
# program to perform range queries over range queries
#  
# Function to create the record array
def record_sum(record, l,r,n,adder):
    for i in range(l, r+1):
        record[i] += adder

# Driver code
n =5
m =5
arr =[0] * n

# Build query matrix
query = [[1, 1, 2 ],[ 1, 4, 5 ],[2, 1, 2 ],
        [ 2, 1, 3 ],[ 2, 3, 4]]

record = [0] * m

for i in range(m -1, -1, -1):

    # if query is of type 2 then function call to record_sum
    if(query[i][0] == 2):
        record_sum(record, query[i][1] -1, query[i][2] -1, m, record[i]+1)

    # if query is of type 1 then simply add 1 to the record array
    else:
        record_sum(record, i, i, m, 1)

# for type 1 queries adding the contains of record array to the main array record array
for i in range(m):
    if(query[i][0] == 1):
        record_sum(arr, query[i][1]-1, query[i][2]-1, n, record[i])

# printing the array
for i in range(n):
    print(arr[i], end=' ')


"""
Method 3

This method has been made more efficient by applying square root decomposition to the 
record array. 

The Time complexity  is O(log n).


"""
print("\n Method 3 \n")
# program to perform range queries over range queries.
import math

max = 10000

# For prefix sum array
def update(arr, l):
	
	arr[l] += arr[l - 1]

# This function is used to apply square root
# decomposition in the record array
def record_func(block_size, block,
				record, l, r, value):

	# Traversing first block in range
	while (l < r and
		l % block_size != 0 and
		l != 0):
		record[l] += value
		l += 1

	# Traversing completely overlapped
	# blocks in range
	while (l + block_size <= r + 1):
		block[l // block_size] += value
		l += block_size

	# Traversing last block in range
	while (l <= r):
		record[l] += value
		l += 1

# Function to print the resultant array
def print_array(arr, n):
	
	for i in range(n):
		print(arr[i], end = " ")

# Driver code
if __name__ == "__main__":

	n = 5
	m = 5
	arr = [0] * n
	record = [0] * m
	
	block_size = (int)(math.sqrt(m))
	block = [0] * max
	
	command = [ [ 1, 1, 2 ],
				[ 1, 4, 5 ],
				[ 2, 1, 2 ],
				[ 2, 1, 3 ],
				[ 2, 3, 4 ] ]

	for i in range(m - 1, -1, -1):

		# If query is of type 2 then function
		# call to record_func
		if (command[i][0] == 2):
			x = i // (block_size)
			
			record_func(block_size, block,
						record, command[i][1] - 1,
								command[i][2] - 1,
						(block[x] + record[i] + 1))

		# If query is of type 1 then simply add
		# 1 to the record array
		else:
			record[i] += 1

	# Merging the value of the block
	# in the record array
	for i in range(m):
		check = (i // block_size)
		record[i] += block[check]

	for i in range(m):
		
		# If query is of type 1 then the array
		# elements are over-written by the record
		# array
		if (command[i][0] == 1):
			arr[command[i][1] - 1] += record[i]
			
			if ((command[i][2] - 1) < n - 1):
				arr[(command[i][2])] -= record[i]

	# The prefix sum of the array
	for i in range(1, n):
		update(arr, i)

	# Printing the resultant array
	print_array(arr, n)

"""
Method 4 : 
This method has been made more efficient by applying Binary Indexed Tree or Fenwick Tree 
by creating two binary indexed tree for query 1 and query 2 respectively. 

The Time complexity  is O(log n).

"""

<script>
// Javascript program to perform range queries over range
// queries.

// Updates a node in Binary Index Tree (BITree) at given index
// in BITree. The given value 'val' is added to BITree[i] and
// all of its ancestors in tree.
function updateBIT(BITree, n, index, val)
{

	// index in BITree[] is 1 more than the index in arr[]
	index = index + 1;

	// Traverse all ancestors and add 'val'
	while (index <= n)
	{

	// Add 'val' to current node of BI Tree
	BITree[index] = (val + BITree[index]);

	// Update index to that of parent in update View
	index = (index + (index & (-index)));
	}
	return;
}

// Constructs and returns a Binary Indexed Tree for given
// array of size n.
function constructBITree(n)
{

	// Create and initialize BITree[] as 0
	let BITree = new Array(n + 1);
	for (let i = 1; i <= n; i++)
	BITree[i] = 0;

	return BITree;
}

// Returns sum of arr[0..index]. This function assumes
// that the array is preprocessed and partial sums of
// array elements are stored in BITree[]
function getSum(BITree, index)
{
	let sum = 0;

	// index in BITree[] is 1 more than the index in arr[]
	index = index + 1;

	// Traverse ancestors of BITree[index]
	while (index > 0)
	{

	// Add element of BITree to sum
	sum = (sum + BITree[index]);

	// Move index to parent node in getSum View
	index -= index & (-index);
	}
	return sum;
}

// Function to update the BITree
function update(BITree, l, r, n, val)
{
	updateBIT(BITree, n, l, val);
	updateBIT(BITree, n, r + 1, -val);
	return;
}

// Driver code
	let n = 5, m = 5;
	let temp = [ 1, 1, 2, 1, 4, 5, 2, 1, 2, 2, 1, 3, 2, 3, 4 ];
	let q = new Array(6).fill(0).map(() => new Array(3))
	let j = 0;
	for (let i = 1; i <= m; i++) {
	q[i][0] = temp[j++];
	q[i][1] = temp[j++];
	q[i][2] = temp[j++];
	}

	// BITree for query of type 2
	let BITree = constructBITree(m);

	// BITree for query of type 1
	let BITree2 = constructBITree(n);

	// Input the queries in a 2D matrix
	/*Scanner sc=new Scanner(System.in);
		for (int i = 1; i <= m; i++)
		{
			q[i][0]=sc.nextInt();
			q[i][1]=sc.nextInt();
			q[i][2]=sc.nextInt();
		}*/

	// If query is of type 2 then function call
	// to update with BITree
	for (let i = m; i >= 1; i--)		
	if (q[i][0] == 2)
		update(BITree, q[i][1] - 1, q[i][2] - 1, m, 1);

	for (let i = m; i >= 1; i--) {
	if (q[i][0] == 2) {
		let val = getSum(BITree, i - 1);
		update(BITree, q[i][1] - 1, q[i][2] - 1, m, val);
	}
	}

	// If query is of type 1 then function call
	// to update with BITree2
	for (let i = m; i >= 1; i--) {		
	if (q[i][0] == 1) {
		let val = getSum(BITree, i - 1);
		update(BITree2, q[i][1] - 1, q[i][2] - 1,
			n, (val + 1));
	}
	}

	for (let i = 1; i <= n; i++)
	document.write(getSum(BITree2, i - 1)+" ");

// This code is contributed by gfgking.
</script>
