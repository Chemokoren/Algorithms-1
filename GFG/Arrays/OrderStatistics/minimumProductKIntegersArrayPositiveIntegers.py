"""
Minimum product of k integers in an array of positive integers

Given an array of n positive integers. We are required to write a program to print the minimum
product of k integers of the given array.

Input : 198 76 544 123 154 675
         k = 2
Output : 9348
We get minimum product after multiplying
76 and 123.

Input : 11 8 5 7 5 100
        k = 4
Output : 1400

The idea is simple, we find the smallest k elements and print multiplication of them. We have
used simple Heap based approach where we insert array elements into a min heap and then find
product of top k elements.

Time Complexity : O(n * log n) 

"""
# program to find minimum product of k elements in an array

import math
import heapq

def minProduct(arr, n, k):
    heapq.heapify(arr)
    count =0
    ans = 1


    print("my count is: ", arr)
    # one by one extract items from min heap
    while(arr) and count < k:
        x = heapq.heappop(arr)
        ans =ans * x
        count = count + 1
        

    
    return ans

arr = [198, 76, 544, 123, 154, 675]
k = 2
n = len(arr)
print ("Minimum product is", minProduct(arr, n, k))


