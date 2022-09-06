"""

Check if all rows of a matrix are circular rotations of each other

Given a matrix of n*n size, the task is to find whether all rows are circular rotations of each
other or not.

Examples:

Input: mat[][] =1,  2,  3
                3,  1,  2
                2,  3,  1

Output: Yes
All rows are rotated permutation of each other.

Input: mat[3][3] =1, 2, 3
                  3, 2, 1
                  1, 3, 2

Output: No
Explanation: As 3, 2, 1 is not a rotated or circular permutation of 1, 2, 3

The idea is based on below article.

A program to check if strings are rotations of each other or not

Steps:
1. Create a string of first row elements and concatenate the string with itself so that string
search operations can be efficiently performed. Let this string be str_cat.

2. Traverse all remaining rows. For every row being traversed, create a string str_curr of current
row elements. If str_curr is not a substring of str_cat, return false.
3. Return True.


Time complexity : O(n3) 
Auxiliary Space : O(n), since n extra space has been taken.

"""
# program to check if all rows of a matrix are rotations of each other
MAX =1000

# returns true if all rows of mat[0..n-1][0..n-1] are rotations of each other
def isPermutedMatrix(mat, n):

    # Creating a string that contains elements of first_row.
    str_cat =""
    for i in range(n):
        str_cat = str_cat +"-"+ str(mat[0][i])

    # Concatenating the string with itself so that substring search operations can be performed 
    # on this
    str_cat = str_cat + str_cat

    # Start traversing remaining rows
    for i in range(1, n):

        # Store the matrix into vector in the form of strings
        curr_str =" "
        for j in range(n):
            curr_str = curr_str +"-"+str(mat[i][j])

        # check if the current string is present in the concatenated string or not
        if(str_cat.find(curr_str)):
            return True
    return False

if __name__ =="__main__":
    n = 4
    mat = [[1, 2, 3, 4],
           [4, 1, 2, 3],
           [3, 4, 1, 2],
           [2, 3, 4, 1]]

    if(isPermutedMatrix(mat, n)):
        print("Yes")
    else:
        print("No")

    
