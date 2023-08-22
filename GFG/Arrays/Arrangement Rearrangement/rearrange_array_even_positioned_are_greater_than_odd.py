"""
Rearrange array such that even positioned are greater than odd

Given an array A of n elements, sort the array according to the following relations :  

A[i] >= A[i-1], if i is even.

A[i] <= A[i-1], if i is odd. 

Print the resultant array.

Examples:  

Input : A[] = {1, 2, 2, 1}
Output :  1 2 1 2

Explanation : 
For 1st element, 1  1, i = 2 is even.
3rd element, 1  1, i = 4 is even.

Input : A[] = {1, 3, 2}
Output : 1 3 2
Explanation : 
Here, the array is also sorted as per the conditions. 
1  1 and 2 < 3.


Method 1 :

Observe that array consists of [n/2] even positioned elements. If we assign the largest [n/2] elements 
to the even positions and the rest of the elements to the odd positions, our problem is solved.
Because element at the odd position will always be less than the element at the even position as it is 
the maximum element and vice versa. 
Sort the array and assign the first [n/2] elements at even positions.

Time Complexity: O(n * log n)

Auxiliary Space: O(n)

"""
print("Method 1 : 'n")
# code to rearrange the elements in array such that even positioned are greater than 
# odd positioned elements

def assign(a,n):
    # sort the array
    a.sort()

    ans =[0] * n
    p = 0
    q = n -1

    for i in range(n):
        # assign even indexes with maximum elements
        if(i + 1) % 2 == 0:
            ans[i] =a[q]
            q = q - 1

        # assign odd indexes with remaining elements
        else:
            ans[i] = a[p]
            p = p + 1

    # print result
    for i in range(n):
        print(ans[i], end=" ")

A = [ 1, 3, 2, 2, 5 ]
n = len(A)
assign(A, n)


"""
Method 2

One other approach is to traverse the array from the second element and swap the element 
with the previous one if the condition is not satisfied. 
 
Time Complexity: O(n)

Auxiliary Space: O(1)
"""
print("\nMethod 2  \n")
# program to rearrange the elements in the array such that even positioned are greater
# than odd positioned elements
def rearrange(arr, n):
 
    for i in range (1, n):
       
        # if index is even
        if (i % 2 == 0):
            if (arr[i] > arr[i - 1]):
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
         
        # if index is odd
        else:
            if (arr[i] < arr[i - 1]):
                arr[i - 1], arr[i] = arr[i] , arr[i - 1]
 
if __name__ == "__main__":         
    n = 5
    arr = [1, 3, 2, 2, 5]
    rearrange(arr, n);
    for i in range (n):
        print (arr[i], end = " ")
    print ()