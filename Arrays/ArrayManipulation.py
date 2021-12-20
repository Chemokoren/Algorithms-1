"""
starting with a 1-indexed array of zeros and a list of operations, 
for each operation add a value to each array element between two given indices, inclusive. 
Once all operations have been performed, return the maximum value in the array.

Example
n =10
queries =[[1,5,3],[4,8,7],[6,9,1]]

queries are interpreted as follows

a b k
1 5 3
4 8 7
6 9 1

add the values of k between the indices a and b inclusive:

index ->    1  2  3  4  5  6  7  8  9  10
          [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
          [ 3, 3, 3, 3, 3, 0, 0, 0, 0, 0 ]
          [ 3, 3, 3,10,10, 8, 8, 8, 1, 0 ]

The largest value is 10 after all operations are performed.

Function Description

Complete the function arrayManipulation in the editor below.

arrayManipulation has the following parameters:
- int n - the number of elements in the array
- int queries[q][3] - a two dimensional array of queries where each queries[i] contains 
    three integers, a,b, and k.

Returns
- int -the maximum value in the resultatnt array

Input Format
The first line contains two space-sperated integers n and m, the size of the array and
the number of operations.
Each of the next m lines contains three space-seperated integers a,b and k, the left index,
right index and summand.

constraints
- 3<=n<=10^7
- 1<=m<=2*10^5
- 1<=a<=b<=n
- 0<=k<=10^9

Sample Input
5   3
1   2   100
2   5   100
3   4   100


Sample Output

200

Explanation
After the first update the list is 100  100 0   0   0.
After the second update list is 100 200 100 100 100.
After the third update list is 100 200 200 200 100.

The maximum value is 200

"""
# input the size of the array and the number of manipulations as n and t
def Array_Manipulation(n, t):

    # allocate the memory to the array dynamically as n can be of order 10^7 and use 
    # long s values after summing may exceed range of int
    
    
    # initial value of elements of array is 0 by default.
    while(t>0):
        # input indices and value to be added
        a = input()
        b = input()
        k = input()
        arr[a] += k # Add the value to the left index
        arr[b + 1] -= k # subtract the value from the element at b+1 index

    # res will store the answer to the problem, i.e. maximum value present in
    # the array after all the manipulations
    res = 0  
    
    # This is the implementation of prefix sum array (or cumulative array)
    # iterating through all the elements, we'll keep adding the elements left to right
    for i in range(1, n):
        arr[i] +=arr[i-1]
        res =max(arr[i], res) # simultaneously update res if current element is greater than res
    return res

# keep the size n+2 as we'll be using 1-indexed array and we're also accessing
# (b+1)th element
arr =[]
n =len(arr)
arr = len(arr) + 2
t =3

print(Array_Manipulation(n,t))
