"""
Find distinct elements common to all rows of a matrix

Given a n*n matrix. The problem is to find all distinct elements common to all rows of the 
matrix. The elements can be printed in any order.

Input : mat[][] = {  {2, 1, 4, 3},
                     {1, 2, 3, 2},  
                     {3, 6, 2, 3},  
                     {5, 2, 5, 3}  }
Output : 2 3

Input : mat[][] = {  {12, 1, 14, 3, 16},
                     {14, 2, 1, 3, 35},  
                     {14, 1, 14, 3, 11},  
                     {14, 25, 3, 2, 1},
                     {1, 18, 3, 21, 14}  }
Output : 1 3 14

Method 1:
- Using three nested loops. Check if an element of 1st row is present in all the subsequent 
rows. Time complexity of O(n^3). Extra space could be required to handle the duplicate elements.

Method 2
- Sort all the rows of the matrix individually in increasing order. Then apply a modified 
approach to the problem of finding common elements in 3 sorted arrays.

Time Complexity: O(n2log n), each row of size n requires O(nlogn) for sorting and there are 
total n rows. 
Auxiliary Space: O(n) to store current column indexes for each row.
"""
# implementation to find distinct elements common to all rows of a matrix
MAX = 100

# function to individually sort each row in increasing order
def sort_rows(mat):
    n = len(mat)
    for i in range(0, n):
        mat[i].sort()
    
# function to find all the common elements
def find_and_print_common_elements(mat):
    n = len(mat)
    # sort rows individually
    sort_rows(mat)

    # current column index of each row is stored from where the element is being
    # searched in that row
    curr_index =[0] * n
    for i in range(0, n):
        curr_index[i] = 0

    f = 0

    while(curr_index[0] < n):
        # value present at the current column index of 1st row
        value = mat[0][curr_index[0]]
        present = True

        # 'value' is being searched in all the subsequent rows
        for i in range(1, n):
            # iterate through all the elements of the row from its current column index till an
            # element greater than the 'value' is found or the end of the row is encountered
            while(curr_index[i] < n and mat[i][curr_index[i]] <= value):
                curr_index[i] = curr_index[i] + 1

            # if the element was not present at the column before to the 'curr_index' of 
            # the row
            if(mat[i][curr_index[i]-1] !=value):
                present = False

            # If all elements of the row have been traversed
            if(curr_index[i] == n):
                f = 1
                break
        # if the 'value' is common to all the rows
        if(present):
            print(value, end=" ")
        
        # if any row have been completely traversed, then no more common elements can be found
        if(f == 1):
            break

        curr_index[0] = curr_index[0] + 1

mat = [[12, 1, 14, 3, 16],
       [14, 2, 1, 3, 35],
       [14, 1, 14, 3, 11],
       [14, 25, 3, 2, 1],
       [1, 18, 3, 21, 14]]
 
find_and_print_common_elements(mat)

"""
Method 3: It uses the concept of hashing
- Map the element of the 1st row in a hash table. Let it be hash
- For row = 2 to n
- Map each element of the current row into a temporary hash table. Let it be temp.
- Iterate through the elements of hash and check that the elements in hash are present in temp.
If not present then delete those elements from hash.
- When all the rows are being processed in this manner, then the elements left in hash are 
the required common elements.

Time Complexity: O(n2) 
Space Complexity: O(n), since n extra space has been taken.

"""
# program to find distinct elements common to all rows of a matrix
MAX =100

# function to individually sort each row in increasing order
def find_and_print_common_elements(mat):
    n = len(mat)
    us = dict()

    # map elements of first row into 'us'
    for i in range(n):
        us[mat[0][i]] =1

    
    for i in range(1, n):
        temp = dict()

        # mapping elements of current row in 'temp'
        for j in range(n):
            temp[mat[i][j]] = 1

        # iterate through all the elements of 'us'
        for itr in list(us):
            # if an element of 'us' is not present into 'temp', then erase that element from 'us'
            if itr not in temp:
                del us[itr]

        # if size of 'us' becomes 0, then there are no common elements
        if(len(us) == 0):
            break
    # print common elements
    for itr in list(us)[::-1]:
        print(itr, end=" ")

mat = [[2, 1, 4, 3],
       [1, 2, 3, 2],
       [3, 6, 2, 3],
       [5, 2, 5, 3]]
find_and_print_common_elements(mat)

"""
Method 4: Using Map
1. Insert all the elements of the 1st row in the map
2. Now we check that the elements present in the map are present in each row or not
3. If the element is present in the map and is not duplicated in the current row, then we 
increment the count of the element in the map b 1
4. If we reach the last row while traversing and if the element appears(N-1) times before then 
we print the element.

Time Complexity: O(n2) 

Space Complexity: O(n)
"""
# code to find distinct elements common to all rows of a matrix
def distinct(matrix):
    N = len(matrix)

    # Make an empty map
    ans ={}

    # Insert the elements of the first row in the map and initialize with 1
    for j in range(N):
        ans[matrix[0][j]] =1

    # traverse the matrix from 2nd row
    for i in range(N):
        for j in range(N):

            # if the element is present in the map and is not duplicated in the current row
            if matrix[i][j] in ans and ans[matrix[i][j]] == i:
                # increment count of the element in map by 1
                ans[matrix[i][j]] = i + 1

                # if we have reached the last row
                if(i == N-1):
                    # print the element
                    print(matrix[i][j], end=" ")

matrix = [ [ 2, 1, 4, 3 ],
                  [ 1, 2, 3, 2 ],
                  [ 3, 6, 2, 3 ],
                  [ 5, 2, 5, 3 ] ]
print("\n using hashmap \n")
distinct(matrix)






print("\n my_tests \n")
def my_tests(mat):
    dic ={}
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            dic[mat[i][j]] =dic.get(mat[i][j], 0)+1
        print(dic)

        # print(mat[i])
        return


mat = [  [2, 1, 4, 3],
         [1, 2, 3, 2],  
         [3, 6, 2, 3],  
         [5, 2, 5, 3]  
    ]

my_tests(mat)
