"""
Given a matrix of order M*N and a value of K, the task is to rotate each ring of the matrix
anticlockwise by K elements. If in any ring elements are less than and equal K then don't rotate it.

Input : k = 3
        mat[4][4] = {{1, 2, 3, 4},
                    {5, 6, 7, 8},
                    {9, 10, 11, 12},
                    {13, 14, 15, 16}}
Output: 4 8  12 16
        3 10  6 15
        2 11  7 14
        1  5  9 13

Input : k = 2
        mat[3][4] = {{1, 2, 3, 4},
                    {10, 11, 12, 5},
                    {9, 8, 7, 6}}
Output: 3 4  5  6
        2 11 12 7
        1 10  9 8

The idea is to traverse matrix in spiral form.

Algorithm:
- Make an auxiliary array temp[] of size M*N
- Start traversing matrix in spiral form and store elements of current ring in temp[] array. While
storing the elements in temp, keep track of strting and ending positions of current ring.
- For every ring that is being stored in temp[], rotate that subarray temp[]
- Repeat this process for each ring of matrix. 
- In last traverse matrix again spirally and copy elements of the temp[] array to matrix.

Time Complexity : O(M*N)  as we are using nested loops to traverse the matrix.
Auxiliary space : O(M*N)  as we are using extra space for matrix.



"""
# program to rotate individual rings by k in spiral order traversal.

# Fills temp array into mat[][] using spiral order traversal.
def fillSpiral(mat[][MAX], m, n,temp[]): 
	i, k, l = None,0,0

    '''
    k - starting row index
	m - ending row index
	l - starting column index
	n - ending column index
	int tIdx = 0; // Index in temp array
    '''


	while (k < m and l < n):

		# first row from the remaining rows 
        #  (int i = l; i < n; ++i)
		for i in range(l,n):
			mat[k][i] = temp[tIdx++];
		k +=1

		# last column from the remaining columns 
		# for (int i = k; i < m; ++i)
        for i in range(k,m):
			mat[i][n-1] = temp[tIdx+1]
		n -=1;

		#  last row from the remaining rows 
		if (k < m):
            # for (int i = n-1; i >= l; --i)
			for i in range(n-1, i >= l, -i):
				mat[m-1][i] = temp[tIdx+1]
			m-=1

		#  first column from the remaining columns
		if (l < n):
			# for (int i = m-1; i >= k; --i)
            for i in range(m-1, i >= k, -i)
				mat[i][l] = temp[tIdx+1];
			l +=1

''' Function to spirally traverse matrix and
rotate each ring of matrix by K elements
mat[][] --> matrix of elements
M	 --> number of rows
N --> number of columns
'''
# def spiralRotate(int mat[][MAX], int M, int N, int k)

def spiralRotate(mat[][MAX], M, N, k):
	# Create a temporary array to store the result
	temp[M*N]

	'''	 s - starting row index
			m - ending row index
			l - starting column index
			n - ending column index; '''
	m = M
    n = N
    s = 0 
    l = 0

	start = temp # int *start = temp; // Start position of current ring
	tIdx = 0; # Index in temp
	while (s < m and l < n):
		# Initialize end position of current ring
		end = start # int *end = start;

		# copy the first row from the remaining rows
		for i in range(l,n):
			temp[tIdx+1] = mat[s][i]
			end = end +1
		
		s =s+1

		# copy the last column from the remaining columns
		for i in range(s,i < m):
            temp[tIdx+1] = mat[i][n-1]; # tIdx+1
			end =end+1
		
		n =n-1

		# copy the last row from the remaining rows
		if(s < m):
			for i in range(n-1, i >= l, -i):
				temp[tIdx+1] = mat[m-1][i]
				end = end+1
			m = m-1
		

		# copy the first column from the remaining columns 
		if (l < n):
			for i in range(m-1, i >= s,-i):
				temp[tIdx+1] = mat[i][l]
				end = end+1
			l = l+1


		# if elements in current ring greater than k then rotate elements of current ring
		if (end-start > k):
			#  Rotate current ring using reversal algorithm for rotation
			reverse(start, start+k)
			reverse(start+k, end)
			reverse(start, end)

			# Reset start for next ring
			start = end

	# Fill temp array in original matrix.
	fillSpiral(mat, M, N, temp)

#  Driver program to run the case
if '__name__' ==_main__:
    M = 4
    N = 4
    k = 3

	mat[MAX]= {{1, 2, 3, 4},
					{5, 6, 7, 8},
					{9, 10, 11, 12},
					{13, 14, 15, 16} 
                    }

	spiralRotate(mat, M, N, k)

	# print modified matrix
	for (int i=0; i<M; i++):
		for (int j=0; j<N; j++):
            print(mat[i][j])