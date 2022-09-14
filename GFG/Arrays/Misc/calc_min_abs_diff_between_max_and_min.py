"""
Minimize(max(A[i], B[j], C[k]) - min(A[i], B[j], C[k])) of three different sorted arrays

Given three sorted arrays A, B, and C of not necessarily same sizes. Calculate the minimum absolute 
difference between the maximum and minimum number of any triplet A[i], B[j], C[k] such that they belong 
to arrays A, B and C respectively, i.e., minimize (max(A[i], B[j], C[k]) - min(A[i], B[j], C[k]))

Examples:

Input : A : [ 1, 4, 5, 8, 10 ]
        B : [ 6, 9, 15 ]
        C : [ 2, 3, 6, 6 ]

Output : 1

Explanation: When we select A[i] = 5
B[j] = 6, C[k] = 6, we get the minimum difference 
as max(A[i], B[j], C[k]) - min(A[i], B[j], C[k]))
= |6-5| = 1 

Input : A = [ 5, 8, 10, 15 ]
        B = [ 6, 9, 15, 78, 89 ]
        C = [ 2, 3, 6, 6, 8, 8, 10 ]
Output : 1
Explanation: When we select A[i] = 10
b[j] = 9, C[k] = 10.

Start with the largest elements in each of the arrays A, B & C. Maintain a variable to update the
answer during each of the steps to be followed.
In every step, the only possible way to decrease the difference is to decrease the maximum element out
of the three elements.
So traverse to the next largest element in the array containing the maximum element for this step and
update the answer variable.

Time Complexity : O(n), where n is the combined sizes of all input arrays.
Auxiliary Space: O(1), since no extra space has been taken

"""
def solve(A, B, C):

    # assigning the length -1 value to each of three variables
    i = len(A) -1
    j = len(B) -1
    k = len(C) -1

    # calculating min difference from last index of lists
    min_diff = abs(max(A[i], B[j], C[k]) - min(A[i], B[j], C[k]))

    while i != -1 and j !=-1 and k !=-1:
        current_diff = abs(max(A[i], B[j], C[k] - min(A[i], B[j], C[k])))

        # checking condition
        if current_diff < min_diff:
            min_diff = current_diff

        # calculating max term from list
        max_term = max(A[i], B[j], C[k])

        # Moving to smaller value in the array with maximum out of three
        if A[i] == max_term:
            i -= 1
        elif B[j] == max_term:
            j -= 1
        else:
            k -= 1
    return min_diff


A = [ 5, 8, 10, 15 ]
B = [ 6, 9, 15, 78, 89 ]
C = [ 2, 3, 6, 6, 8, 8, 10 ]
print(solve(A, B, C))