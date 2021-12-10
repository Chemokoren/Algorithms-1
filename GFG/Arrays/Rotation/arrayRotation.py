"""
program to rotate an array by d elements


Time complexity : O(n * d) 
Auxiliary Space : O(1)

"""
def leftRotate(arr, d, n):
    for i in range(d):
        leftRotatebyOne(arr,n)

def leftRotatebyOne(arr, n):
    temp =arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] =temp

# utility function to print an array */
def printArray(arr, size):
    for i in range(size):
        print ("% d"% arr[i], end =" ")
 
  
# Driver program to test above functions */
arr = [1, 2, 3, 4, 5, 6, 7]
leftRotate(arr, 2, 7)
printArray(arr, 7)
print("")


print("######################### Method 3 ######################### ")
"""
METHOD 3 (A Juggling Algorithm) 
This is an extension of method 2. Instead of moving one by one, divide the array in 
different sets.
where number of sets is equal to GCD of n and d and move the elements within sets. 

If GCD is 1 as is for the above example array (n = 7 and d =2), then elements will be moved 
within one set only, we just start with temp = arr[0] and keep moving arr[I+d] to arr[I] and 
finally store temp at the right place.

Here is an example for n =12 and d = 3. GCD is 3 and 

Let arr[] be {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

a) Elements are first moved in first set 
arr[] after this step --> {4 2 3 7 5 6 10 8 9 1 11 12}

b)    Then in second set.
          arr[] after this step --> {4 5 3 7 8 6 10 11 9 1 2 12}

c)    Finally in third set.
          arr[] after this step --> {4 5 6 7 8 9 10 11 12 1 2 3}

Time complexity : O(n) 
Auxiliary Space : O(1)

"""

# program to rotate an array by d elements
# Function to left rotate arr[] of size n by d
def leftRotate(arr, d, n):
    d = d % n
    g_c_d = gcd(d,n)

    for i in range(g_c_d):
        # move i-th values of blocks
        temp = arr[i]
        j = i
        while 1:
            k =j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] =arr[k]
            j = k
        arr[j] = temp

# function to print an array

def printArray(arr, size):
    for i in range(size):
        print("% d" %arr[i], end=" ")

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
d = 2
print("before rotation \n")
printArray(arr, n)

leftRotate(arr, d, n)

print("after rotation \n")
printArray(arr, n)


print("\n################################## Method 4 ##################################")

"""
Method 4 (The Reversal Algorithm) :
rotate(arr[], d, n)
  reverse(arr[], 1, d) ;
  reverse(arr[], d + 1, n);
  reverse(arr[], 1, n);

Let AB be the two parts of the input array where A = arr[0..d-1] and B = arr[d..n-1]. The idea of the algorithm is : 
 

Reverse A to get ArB, where Ar is reverse of A.
Reverse B to get ArBr, where Br is reverse of B.
Reverse all to get (ArBr) r = BA.
Example : 
Let the array be arr[] = [1, 2, 3, 4, 5, 6, 7], d =2 and n = 7 
A = [1, 2] and B = [3, 4, 5, 6, 7] 


Reverse A, we get ArB = [2, 1, 3, 4, 5, 6, 7]
Reverse B, we get ArBr = [2, 1, 7, 6, 5, 4, 3]
Reverse all, we get (ArBr)r = [3, 4, 5, 6, 7, 1, 2]

Time Complexity : O(n)

"""

# program for reversal algorithm of array rotation
# function to reverse arr[] from index start to end

def reverseArray(arr, start, end):
    while(start < end):
        temp =arr[start]
        arr[start] = arr[end]
        arr[end] =temp
        start += 1
        end =end - 1

# Function to left rotate arr[] of size n by d
def leftRotate(arr, d):
    if d == 0:
        return
    n = len(arr)
    # in case the rotating factor is greater than array length
    d = d % n
    reverseArray(arr, 0, d-1)
    reverseArray(arr, d, n-1)
    reverseArray(arr, 0, n-1)

# Function to print an array
def printArray4(arr):
    for i in range(0,len(arr)):
        print(arr[i],end=" ")

# test above functions
arr =[1,2,3,4,5,6,7]
n = len(arr)
d = 2

leftRotate(arr,d) # Rotate array by 2
printArray4(arr)
