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
    temp = arr[n-1]

    for i in range(n-1,0,-1):
        arr[i] =arr[i-1]
    arr[0] =temp

arr=[1, 2, 3, 4, 5]
print("ttttttttttttttttttttttt")
print(rotate(arr,5))
print("nini:",arr)

"""

We can use two pointers, say i and j which point to first and last element of array 
respectively. As we know in cyclic rotation we will bring last element to first and 
shift the rest in a forward direction, so start swaping arr[i] and arr[j] and keep j fixed and i moving towards j.  
Repeat till i is not equal to j.

"""
def rotate2(arr, n):
    start = 0
    end = n-1

    while start != end:
        arr[start], arr[end] = arr[end],arr[start]
        start =start+1
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


"""
Using Slicing
-We can also solve this problem using slicing in Python

"""
def rotateArray(array):
    '''
    array[-1:] - taking the last element
    array[:-1] - taking elements from start to last second element
    array[:] - changing array from starting to end
    '''

    array[:] =array[-1:] + array[:-1]
    print("ataaa: ",array)

print("\nUsing slicing")

array = [1, 2, 3, 4, 5]

# send array to rotateArray function
rotateArray(array)
 
print(*array)



