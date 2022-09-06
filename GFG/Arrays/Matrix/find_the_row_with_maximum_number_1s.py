"""
Find the row with maximum number of 1s

Given a boolean 2D array, where each row is sorted. Find the row with the maximum number of 1s.

Input matrix
0 1 1 1
0 0 1 1
1 1 1 1  // this row has maximum 1s
0 0 0 0

Output: 2

A simple method is to do a row-wise traversal of the matrix, count the number of 1s in each row,
and compare the count with max. Finally, return the index of the row with maximum 1s. The time 
complexity of this method is O(m*n) where m is the number of rows and n is the number of columns
in the  matrix.

Index of row with maximum 1s is 2

Time Complexity:  O(m*n)
Space Complexity:  O(1)

"""
R, C = 4, 4

# function to find the index of the first index of 1 in a boolean array arr
def first(arr, low, high):
    if (high >= low):
        # Get the middle index
        mid = low +(high - low) //2

        # check if the element at middle index is first 1
        if((mid == 0 or arr[mid-1] == 0) and arr[mid] == 1):
            return mid
        
        #  if the element is 0, recur for right side
        elif(arr[mid] == 0):
            return first(arr, (mid+1), high)
        
        # if element is not first 1, recur for left side
        else:
            return first(arr, low,(mid-1))
    return -1

# Function that returns index of row with maximum number of 1s
def rowWithMax1s(mat):

    # Initialize max values
    max_row_index, Max = 0, -1

    # Traverse for each row and count of number of 1s by finding the index of first 1
    for i in range(R):

        index = first(mat[i], 0, C-1)
        if(index != -1 and C-index > Max):
            Max = C - index
            max_row_index = i
    return max_row_index


mat = [[0, 0, 0, 1],
       [0, 1, 1, 1],
       [1, 1, 1, 1],
       [0, 0, 0, 0]]
print("Index of row with maximum 1s is " + str(rowWithMax1s(mat)))


"""
We can do better. Since each row is sorted, we can use Binary Search to count of 1s in each row.
We find the index of first instance of 1 in each row. The count of 1s will be equal to total
number of columns minus the index of first 1.

Time Complexity: O(mLogn) where m is number of rows and n is number of columns in matrix.
Auxiliary Space:  O(Log n), as implicit stack is created due to recursion.

"""
# program to find the row with maximum number of 1s

# Function to find the index of first index of 1 in a boolean array arr[]
def first(arr, low, high):
    if high >= low:

        # Get the middle index
        mid = low + (high -low) //2 

        # check if the element at middle index is first 1
        if(mid == 0 or arr[mid -1] == 0) and arr[mid] == 1:
            return mid
        
        # if the element is 0, recur for right side
        elif arr[mid] == 0:
            return first(arr, (mid + 1), high)

        # if element is not first 1, recur for left side
        else:
            return first(arr, low, (mid -1))

    return -1

# Function returning the index of row with maximum number of 1s
def rowWithMax1s(mat):
    
    # Initialze max values
    R = len(mat)
    C = len(mat[0])
    max_row_index = 0

    max = -1

    # Traverse for each row and count number of 1s by finding the index of first 1
    for i in range(0, R):
        index = first(mat[i], 0, C-1)
        if index != -1 and C- index > max:
            max = C - index

            max_row_index = i
    return max_row_index

mat = [[0, 0, 0, 1],
       [0, 1, 1, 1],
       [1, 1, 1, 1],
       [0, 0, 0, 0]]

print ("Index of row with maximum 1s is",rowWithMax1s(mat))

"""

The above solution can be optimized further. Instead of doing binary search in every row, we 
first check whether the row has more 1s than max so far. If the row has more 1s, then only count
1s in the row. also, to cont 1s in a row, we don't do binary search in complete row, we do search
in before the index of last max.

The worst case time complexity of the below optimized version is also O(mLogn), this solution will 
work better on average.

The worst case of the above solution occurs for a matrix like following. 
0 0 0 … 0 1 
0 0 0 ..0 1 1 
0 … 0 1 1 1 
….0 1 1 1 1

"""
# main function returning index of row with maximum number of 1s.
def rowWithMax1s(mat):

    # inititialzie max using values from first row.
    max_row_index =0
    max = first(mat[0], 0, C-1)

    # Traverse for each row and count number of 1s by finding the index of first 1
    for i in range(1, R):

        # count 1s in this row only if this row has more 1s than max so far
        if(max != -1 and mat[i][C -max -1] == 1):
            # Note the optimization here also
            index = first(mat[i], 0, C - max)

            if(index != -1 and C -index > max):
                max = C - index
                max_row_index = i
        else:
            max = first(mat[i], 0, C-1)
    return max_row_index

"""

Method 4: O(m+n) time complexity in worst case

Following method works in O(m+n) time complexity in worst case. 

    Step1: Get the index of first (or leftmost) 1 in the first row.
    Step2: Do following for every row after the first row 
        …IF the element on left of previous leftmost 1 is 0, ignore this row. 
        …ELSE Move left until a 0 is found. Update the leftmost index to this index and 
        max_row_index to be the  current row.
        The time complexity is O(m+n) because we can possibly go as far left as we came ahead in the 
        first step.

Time Complexity: O(m+n) where m is number of rows and n is number of columns in matrix.
Auxiliary Space:  O(1), as implicit stack is created due to recursion.
"""


# Function that returns the index of row with maximum number of 1s.

def rowWithMax1s(mat):

    # Initialize max values
    R = len(mat)
    C = len(mat[0])

    max_row_index = 0
    index = C-1

    # Traverse for each row and count number of 1s by finding the index of first 1
    for i in range(0, R):
        flag = False # to check whether a row has more 1's than previous
        while(index >=0 and mat[i][index]==1):
            flag =True # present row has 1's than previous
            index -= 1
            if(flag): # if the present row has more 1's than previous
                max_row_index = i
        if max_row_index == 0 and mat[0][C-1] ==0:
            return 0
    return max_row_index


mat = [[0, 0, 0, 1],
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 0]]
print ("Index of row with maximum 1s is",rowWithMax1s(mat))
