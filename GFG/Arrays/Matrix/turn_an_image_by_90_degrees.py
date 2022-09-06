"""
Turn an image by 90 degree

given an image, how will you turn it by 90 degrees? An image can be treated as 2D matrix which can
be stored in a buffer. We are provided with matrix dimensions and it's base address. How can we 
turn it? For example see the picture below:


* * * ^ * * *
* * * | * * *
* * * | * * *
* * * | * * *

After rotating right, it appears (observe arrow direction)

* * * *
* * * *
* * * *
— — — >
* * * *
* * * *
* * * *

The idea is simple. Transform each row of source matrix into required column of final image. We
will use an auxiliary buffere to transform the image. From the above picture we can observe that:

first row of source ------> last column of destination
second row of source ------> last but-one column of destination
so ... on
last row of source ------> first column of destination

In pictorial form, we represent the above transformations of an (m*n) matrix into (n*m) matrix.

00  01  02      0n                      m0          10  00
10  11  12      1n                      m1          11  01
20  21  22      2n        --->          m2          12  02


m0  m1  m2      mn                      mn          1n  0n

    m*n                                         n*m


for (r = 0; r < m; r++)
{
   for (c = 0; c < n; c++)
   {
      // Hint: Map each source element indices into
      // indices of destination matrix element.
       dest_buffer [ c ] [ m - r - 1 ] = source_buffer [ r ] [ c ];
   }
}

Note that there are various wasy to implement the algorithm based on traversal of matrix, row major
or column major order. We have two matrices and two ways(row and column major) to traverse each
matrix. Hence, there can atleast be 4 different ways of transformation of source matrix into
final matrix.

Time Complexity: O(N*M), as we are using nested loops for traversing the matrix.

Auxiliary Space: O(N*M), as we are using extra space for matrix.

"""
# program to turn an image by 90 Degree

# void displayMatrix(unsigned int const *p,
# 					unsigned int row,
# 				unsigned int col);
					
# void rotate(unsigned int *pS,
# 			unsigned int *pD,
# 			unsigned int row,
# 			unsigned int col);
			
# def displayMatrix(unsigned int const *p, unsigned int r,unsigned int c):
# 	unsigned int row, col;
# 	print("\n\n")

# 	for (row = 0; row < r; row++):
# 		for (col = 0; col < c; col++)
# 			print( << * (p + row * c + col) << "\t")
# 		print("\n")

# 	print("\n\n")


# void rotate(unsigned int *pS, unsigned int *pD,	unsigned int row, unsigned int col):

# 	unsigned int r, c;
# 	for (r = 0; r < row; r++):
# 		for (c = 0; c < col; c++):
# 			*(pD + c * row + (row - r - 1)) =
# 						*(pS + r * col + c);

# def __name__='__main__':
	
# 	#  declarations
# 	unsigned int image[][4] = {{1, 2, 3, 4},
# 							{5, 6, 7, 8},
# 							{9, 10, 11, 12}};
# 	unsigned int *pSource;
# 	unsigned int *pDestination;
# 	unsigned int m, n;

# 	# setting initial values and memory allocation
# 	m = 3, n = 4, pSource = (unsigned int *)image;
# 	pDestination = (unsigned int *)malloc
# 				(sizeof(int) * m * n);

# 	# process each buffer
# 	displayMatrix(pSource, m, n);

# 	rotate(pSource, pDestination, m, n);

# 	displayMatrix(pDestination, n, m);

# 	free(pDestination);
