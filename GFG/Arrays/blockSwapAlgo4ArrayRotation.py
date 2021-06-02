"""
block swap algorithm for array rotation
- write a function rotate(ar[], d,n) that rotates arr[]
 of size n by d elements
consider arryay [1,2,3,4,5,6,7]
rotation of the above array by 2 will make
[3,4,5,6,7,1,2]

Algorithm:
Initialize A = arr[0..d-1] and B = arr[d..n-1]
1) Do following until size of A is equal to size of B

  a)  If A is shorter, divide B into Bl and Br such that Br is of same 
       length as A. Swap A and Br to change ABlBr into BrBlA. Now A
       is at its final place, so recur on pieces of B.  

   b)  If A is longer, divide A into Al and Ar such that Al is of same 
       length as B Swap Al and B to change AlArB into BArAl. Now B
       is at its final place, so recur on pieces of A.

2)  Finally when A and B are of equal size, block swap them.
"""

# wrapper over the recursive function leftRotateRec()
# it left rotates arr by d
def leftRotate(arr, d, n):
    leftRotateRec(arr,0, d,n)

def leftRotateRec(arr,i,d,n):
    '''
    Return if number of elements to be rotated is zero
    or equal to array size
    '''
    if(d == 0 or d == n):
        return
    
    '''
    * If number of elements to be rotated is exactly half
    of the array size
    '''
    if (n-d == d):
        swap(arr,i, n-d+i,d)
        return

    '''If A is shorter '''
    if(d < n-d):
        swap(arr, i,n-d+i,d)
        leftRotateRec(arr, i, d, n-d)
        '''If B is shorter'''
    else:
        swap(arr, i,d, n-d)

        '''This is tricky'''
        leftRotateRec(arr,n-d+i, 2*d-n,d)

"""
Iterative Implementation: 
Here is iterative implementation of the same algorithm. 
"""
def leftRotate1(arr, d, n):
    if(d == 0 or d == n):
        return
    i = d
    j = n - d
    while(i !=j ):
        if(i < j) : # A is shorter
            swap(arr,d-i, d+j-i,i)
            j -= i
        else: # B is shorter
            swap(arr,d -i, d, j)
            i -= j
    swap(arr,d - i, d, i)


def printArray(arr, size):
    for i in range(size):
        print(arr[i], end = " ")
    print()
 
'''
 * This function swaps d elements starting at
 * index fi with d elements starting at index si
 '''
def swap(arr, fi, si, d):
    for i in range(d):
        temp = arr[fi + i]
        arr[fi + i] = arr[si + i]
        arr[si + i] = temp
 
# Driver Code
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    leftRotate(arr, 2, 7)
    printArray(arr, 7)