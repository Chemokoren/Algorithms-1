"""
Queries for decimal values of subarrays of a binary array

Given a binary array arr[], we  need to find the number represented by subarrays a[l..r].
There are multiple such queries.

Input :  arr[] = {1, 0, 1, 0, 1, 1};
         l = 2, r = 4
         l = 4, r = 5
Output : 5
         3 
Subarray 2 to 4 is 101 which is 5 in decimal.
Subarray 4 to 5 is 11 which is 3 in decimal.

Input : arr[] = {1, 1, 1}
        l = 0, r = 2
        l = 1, r = 2
Output : 7
         3

A simple solution is to compute decimal value for every given range using simple binary to
decimal conversion. Here, each query takes O(len) time where len is length of range.


An Efficient solution is to do per-computations, so that queries can be answered in O(1)
time.

The number represented by subarray arr[l..r] is 
arr[l]*2^{r-l} + arr[l+1]*2^{r - l - 1} ….. + arr[r]*2^{r-r}
 
Make an array pre[] of same size as of given array where pre[i] stores the sum of 
arr[j]*2^{n - 1 - j} where j includes each value from i to n-1.

The number represented by subarray arr[l..r] will be equal to 
(pre[l] – pre[r+1])/2^{n-1-r} .

pre[l] – pre[r+1] is equal to arr[l]*2^{n - 1 - l} + arr[l+1]*2^{n - 1 - l - 1} 
+……arr[r]*2^{n - 1 - r} . 

So if we divide it by 2^{n - 1 - r} , we get the required answer.

Time complexity: O(n)

Auxiliary Space: O(n)

"""
# implementation of finding number represented by binary subarray
from math import pow

# Fills pre[]
def precompute(arr, pre):
    n = len(arr)
    pre[n-1] = arr[n-1] * pow(2,0)
    i = n-2
    while(i >= 0):
        pre[i] = (pre[i+1] + arr[i] * (1 << (n-1-i)))
        i -=1

# returns the number represented by a binary subarray l to r
def decimalOfSubarr(arr, l, r, pre):
    n = len(arr)

    # if r is equal to n-1, r+1 does not exist
    if(r != n-1):
        return ((pre[l] - pre[r+1]) / (1 << (n - 1 - r)))
    return pre[l] / (1 << (n -1 -r))

if __name__ == '__main__':
    arr =[1,0,1,0,1,1]
    

    pre = [0 for i in range(len(arr))]
    precompute(arr, pre)
    print(int(decimalOfSubarr(arr,2,4,pre)))
    print(int(decimalOfSubarr(arr,4,5,pre)))




print("\n  my tests \n")
'''
my tests

'''
def my_tests(arr,Q):
    l,r =Q
    return convert_binary_to_decimal(arr[l:r+1])

def convert_binary_to_decimal(bin):
    root_val =0
    val =0

    for i in range(len(bin),0,-1):
        val +=(pow(2, root_val) * bin[i-1])
        root_val +=1
    return val

print("expected: 7, actual:", my_tests([1, 1, 1], [0, 2]))
print("expected: 3, actual:", my_tests([1, 1, 1], [1, 2]))