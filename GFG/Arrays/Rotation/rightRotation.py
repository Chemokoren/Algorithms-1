"""
1 2 3 4 5 6 7

5 6 7 1 2 3 4

Len =7 and d =3
"""

def rightRotateArray(arr, n, d):
    # reverse entire array
    reverse(arr,0,n-1)
    reverse(arr,0,d-1)
    reverse(arr,d,n-1)
    return arr

def reverse(arr, start, end):
    while start < end:
        # temp =arr[start]
        # arr[start] =arr[end]
        # arr[end] =temp
        arr[start],arr[end] =arr[end],arr[start]
        start += 1
        end -= 1

arr = [1,2, 3, 4, 5, 6, 7]
n =len(arr)
d =3

print(rightRotateArray(arr,n,d))
