"""
cyclically rotate the array clockwise by one. 

Examples:  

Input:  arr[] = {1, 2, 3, 4, 5}
Output: arr[] = {5, 1, 2, 3, 4}

steps:
1) Store last element in a variable say x. 
2) Shift all elements one position ahead. 
3) Replace first element of array with x.
"""
def rotate(arr,n):
    x = arr[n-1]

    for i in range(n-1,0,-1):
        arr[i] =arr[i-1]
    arr[0] =x

"""
We can use two pointers, say i and j which point to first and last element of array 
respectively. As we know in cyclic rotation we will bring last element to first and 
shift rest in forward direction, 
so start swaping arr[i] and arr[j] and keep j fixed and i moving towards j.  
Repeat till i is not equal to j.
"""
def rotate2(arr, n):
    i = 0
    j = n-1
    while i != j:
        arr[i], arr[j] = arr[j],arr[i]
        i =i+1
    pass


arr= [1, 2, 3, 4, 5]
n = len(arr)
print ("Given array is :")
for i in range(0, n):
    print (arr[i], end = ' ')
 
rotate2(arr, n)
 
print ("\nRotated array is: ")
for i in range(0, n):
    print(arr[i], end = ' ')





