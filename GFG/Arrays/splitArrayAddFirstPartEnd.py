"""
Split the arra and add the first part to the end

- given a certain array, split it from a  specified position,
 and move the first part of the array and add to the end


 Input : arr[] = {12, 10, 5, 6, 52, 36}
            k = 2
Output : arr[] = {5, 6, 52, 36, 12, 10}
Explanation : Split from index 2 and first 
part {12, 10} add to the end .

Input : arr[] = {3, 1, 2}
           k = 1
Output : arr[] = {1, 2, 3}
Explanation : Split from index 1 and first
part add to the end.

Simple Solution:
- We one by one rotate array. 

Time complexity of the above solution is O(nk). 
"""

# program to split array and move first part to end

def splitArr(arr, n, k):
    for i in range(0, k):
        x = arr[0]
        for j in range(0, n-1):
            arr[j] = arr[j + 1]

        arr[n -1] = x

arr = [12, 10, 5, 6, 52, 36]
n = len(arr)
position = 2
 
splitArr(arr, n, position)
 
for i in range(0, n):
    print(arr[i], end = ' ')

print("approach 2 :\n")
"""
A different approach is to make a temporary array with double the size and copy 
our array element into a new array twice. and then copy the element from the new array
to our array by taking the rotation as starting index up to the length of our array.
"""

# program to split array and move first part to end

def SplitAndAdd(A, length, rotation):
    # make a temporary array with double the size and each index is initialized to 0
    tmp =[0 for i in range(length * 2)]

    # copy array element in to a new array twice
    for i in range(length):
        tmp[i] =A[i]
        tmp[i + length] = A[i]

    for i in range(rotation, rotation + length, 1):
        A[i - rotation] =tmp[i]

arr = [12, 10, 5, 6, 52, 36]
n = len(arr)
position = 2
SplitAndAdd(arr, n, position);
for i in range(n):
    print(arr[i], end = " ")
print()