"""
Find the minimum distance between two numbers

Given an unsorted array arr[] and two numbers x and y, find the minimum distance between
x and y in arr[]. The array might also contain duplicates. You may assume that both
x and y are different and present in arr[].

Input: arr[] = {1, 2}, x = 1, y = 2
Output: Minimum distance between 1 
and 2 is 1.
Explanation: 1 is at index 0 and 2 is at 
index 1, so the distance is 1

Input: arr[] = {3, 4, 5}, x = 3, y = 5
Output: Minimum distance between 3 
and 5 is 2.
Explanation:3 is at index 0 and 5 is at 
index 2, so the distance is 2

Input: 
arr[] = {3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3},  
x = 3, y = 6
Output: Minimum distance between 3 
and 6 is 4.
Explanation:3 is at index 0 and 6 is at 
index 5, so the distance is 4

Input: arr[] = {2, 5, 3, 5, 4, 4, 2, 3}, 
x = 3, y = 2
Output: Minimum distance between 3 
and 2 is 1.
Explanation:3 is at index 7 and 2 is at 
index 6, so the distance is 1

Method 1:

Approach:
- The task is to find the distance between two given numbers, so find the distance 
between any two elements using nested loops. The outer loop for selecting the first 
element(x) and the inner loop for traversing the array in search for the other element(y)
and taking the minimum distance between them.

Algorithm: 

    Create a variable m = INT_MAX
    Run a nested loop, the outer loop runs from start to end (loop counter i), the inner
    loop runs from i+1 to end (loop counter j).
    If the ith element is x and jth element is y or vice versa, update m as m = min(m,j-i)
    Print the value of m as minimum distance


"""

# code to find the minimum distance between two numbers
def minDist(arr, x, y):
    n = len(arr)

    min_dist =float('inf')
    for i in range(n):
        for j in range(i +1, n):
            if (x == arr[i] and y == arr[j] or y == arr[i] and x == arr[j] 
            and min_dist > abs(i-j)):
                min_dist = abs(i - j)
    return min_dist

print("expected:, actual:", minDist([3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3], 3, 6))


"""
Method 2

- So the basic approach is to check only consecutive pairs of x and y. For every element
x or y, check the index of the previous occurrence of x or y, check the index of the 
previous occurrence of x or y and if the previous occuring element is not similar to 
current element update the minimum distance. But a question arises what if an x is 
preceded by another x and that is preceded by a y, then how to get the minimum distance
between pairs. By analyzing closely it can be seen that every x followed by a y or a vice 
versa can only be the closes pair(minimum distance) so ignore all other pairs.

Algorithm
- Create a variable prev -1 and m=INT_MAX
- Traverse through the array from start to end.
- If the current element is x or y, prev is not equal to -1 and array[prev] is not equal
to current element then update m = max(current_index - prev, m), i.e. Find the distance 
between consecutive pairs and pdate m with it.
- print the value of m

Complexity Analysis:
Time Complexity: O(n). 
Only one traversal of the array is needed.
Space Complexity: O(1). 
As no extra space is required.


"""
print("\n Method 2 \n")

import sys

def minDistTwo(arr, x, y):

    n =len(arr)
    #previous index and min distance
    i=0
    p=-1
    min_dist = sys.maxsize;
     
    for i in range(n):
     
        if(arr[i] ==x or arr[i] == y):
         
            #we will check if p is not equal to -1 and
            #If the element at current index matches with
            #the element at index p , If yes then update
            #the minimum distance if needed
            if(p != -1 and arr[i] != arr[p]):
                min_dist = min(min_dist,i-p)
              
            #update the previous index
            p=i
         
     
    #If distance is equal to int max
    if(min_dist == sys.maxsize):
       return -1
    return min_dist


print (" ",minDistTwo([3, 5, 4, 2, 6, 3, 0, 0, 5, 4, 8, 3], 3, 6))



"""
Method 3

- The problems says that we want a minimum distance between x and y. So the approach is
traverse the array and while traversing in array if we got the number as x or y then we
will store the difference between indices of previously found x or y and newly find x or y
and like this for every time we will try to minimize the difference.

1. Create variabels idx1 =-1, idx2 =-1 and min_dist =INT_MAX
2. Traverse the array from i =0 to i=n-1 where n is the size of the array.
3. While traversing if the current element is x then store index of current element in 
idx1  or if the current element is y then store index of current element in idx2.
4. If idx1 and idx2 variable are not equal to -1 then store minimum of min_dist, difference
of idx1 and idx2 into ans.
5. At the end of traversal, if idx1 or idx2 are still -1(x or y not found in array) then
return -1 or else return min_dist.

    Complexity Analysis:
    Time Complexity: O(n). 
    Only one traversal of the array is required.
    Space Complexity: O(1). 
    No extra space is required.

"""
# program to find the minimum distance between two numbers
import sys

def minDistThree(arr, x, y) :

    n = len(arr)
     
    # idx1 and idx2 will store indices of
    # x or y and min_dist will store the minimum difference
    idx1=-1; idx2=-1; min_dist = sys.maxsize
    for i in range(n) :
       # if current element is x then change idx1
       if arr[i]==x :
          idx1=i
           
       # if current element is y then change idx2
       elif arr[i]==y :
          idx2=i
        
       # if x and y both found in array
       # then only find the difference and store it in min_dist
       if idx1!=-1 and idx2!=-1 :
           min_dist=min(min_dist,abs(idx1-idx2))
     
    # if left or right did not found in array
    # then return -1
    if idx1==-1 or idx2==-1 :
        return -1
    # return the minimum distance
    else :
        return min_dist
    
print("", minDistThree([ 3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3],3, 6))



























'''
my tests
'''
def my_tests(arr, x, y):
    min_dist =float('inf')

    i = 0
    

    while i < len(arr):
        j = i
        print("aa:", i)
        if(arr[i] == x):
            while j < len(arr):
                if arr[j] == y:
                    current_val =j -i
                    min_dist =min(min_dist, current_val)
                    i = j+1
                    j = i + 1
                else:
                    j += 1

        else:
            i +=1
    return min_dist
                
# print("expected: 1 , actual:", my_tests([2, 5, 3, 5, 4, 4, 2, 3], 3, 2))
