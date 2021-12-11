def swap(arr, aIndex, bIndex, k):

    for i in range(0, k):
        temp = arr[aIndex +i]
        arr[aIndex + i] = arr[bIndex+i]
        arr[bIndex+i] = temp

def printArray(msg, arr):
    print(msg)
    for i in range(len(arr)):
        print(""+ str(arr[i]), end=" ")
    print(" ")

def rotateLeft(arr, r):
    n =len(arr)

    r %= n
    if r == 0 or r ==n:
        return arr

    A = int(r)
    B = int(n-r)

    while(A!=B):
        if(A < B):
            swap(arr, r-A, r-A+B, A)
            B = B-A
        else:
            swap(arr, r-A, r, B)
            A= A-B

    swap(arr, r-A, r, A)

    return arr

# driver code
arr =[1,2,3,4,5]
r =2
n =len(arr)

arrLeft=rotateLeft(arr,r)

printArray("Left Rotation:", arrLeft)