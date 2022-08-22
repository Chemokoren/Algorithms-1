"""
Count all distinct pairs with difference equal to k

Given an integer array and a positive integer k, count all distinct pairs with differences 
equal to k.


Examples: 

Input: arr[] = {1, 5, 3, 4, 2}, k = 3
Output: 2
There are 2 pairs with difference 3, the pairs are {1, 4} and {5, 2} 

Input: arr[] = {8, 12, 16, 4, 0, 20}, k = 4
Output: 5
There are 5 pairs with difference 4, the pairs are {0, 4}, {4, 8}, 
{8, 12}, {12, 16} and {16, 20} 


Use sorting

- We can find the  count in O(nLogn) time using a O(nLogn) sorting algorithm like Merge Sort,
Heap sort etc. The following are the detailed steps

1) Initialize count as 0
2) Sort all numbers in increasing order.
3) Remove duplicates from array.
4) Do the following for each element arr[i]
    a) Binary search for arr[i] + k in subarray from  i+1 to n-1
    b) If arr[i] + k found, increment count.
5) Return count

The first step (sorting) takes O(nLogn) time. The second step runs binary search n times, 
so the time complexity of second step is also O(nLogn). Therefore, overall time complexity 
is O(nLogn). The second step can be optimized to O(n).

Time Complexity: O(nlogn)
Auxiliary Space: O(logn)

"""

# Standard binary search function
def binarySearch(arr, low, high, x):
    if(high >= low):

        mid = low + (high -low) //2
        if x == arr[mid]:
            return (mid)
        elif (x > arr[mid]):
            return binarySearch(arr, (mid+1), high, x)
        else:
            return binarySearch(arr, low, (mid-1), x)
    return -1

# returns count of pairs with difference k in arr[] of size n
def countPairsWithDiff(arr, k):
    n = len(arr)
    count = 0
    arr.sort() # sort array elements

    # code to remove duplicates from arr[]

    # Pick a first element point
    for i in range(0, n-2):
        if(binarySearch(arr, i + 1, n-1,arr[i]+ k)  !=-1):
            count +=1

    return count

print ("Count of pairs with given diff is ",countPairsWithDiff([1, 5, 3, 4, 2], 3))


"""
Use self-balancing BST

We can also use a self-balancing BST like AVL tree or Red Blck tree to solve this problem.

1) Initialize count as 0
2) Insert all elements of arr[] in an AVL tree. While inserting, ignore an element if already
present in AVL tree.
3) Do the following for each element arr[i]
    a) Search for arr[i] + k in AVL tree, if found then increment  count.
    b) Search for arr[i] - k in AVL tree, if found then increment count.
    c) Remove arr[i] from AVL tree.

Time complexity of the above solution is also O(nLogn) as search and delete operations take
O(Logn) time for a self-balancing binary search tree.


Use Hashing

- use hashing to achieve the average time complexity as O(n) for many cases
1) Initialize count as 0
2) Insert all distinct elements of arr[] in a hash map. While inserting,ignore an 
element if already present in the hash map.
3) Do the following for each element arr[i]
    a) Look for arr[i] + k in the hash map, if found then increment count
    b) Look for arr[i] - k in the hash map, if found then increment count
    c) Remove arr[i] from hash table.

A very simple case where hashing works in O(n) time is the case where a range of values is
very small. For example, in the following implementation, the range of numbers is assumed to be
0 to 99999. A simple hahsing technique to use values as an index can be used.



"""
'''
An efficient program to count pairs with difference k when the range numbers is small
Time Complexity: O(n)
Auxiliary Space: O(n)
'''
MAX = 100000

def countPairsWithDiffK(arr, k):
    n = len(arr)
    count = 0 # Initialize count

    # Initialize empty hashmap
    hashmap =[False for i in range(MAX)]

    # Insert array elements to hashmap
    for i in range(n):
        hashmap[arr[i]] = True

    for i in range(n):
        x = arr[i]
        if(x -k >= 0 and hashmap[x -k]):
             count +=1
        if(x + k < MAX and hashmap[x + k]):
            count +=1
        hashmap[x] =False

    return count

print("Hashmap Expected: , Actual:", countPairsWithDiffK([1, 5, 3, 4, 2], 3))


"""
Use Sorting :

    Sort the array arr
    Take two pointers, l, and r, both pointing to 1st element
    Take the difference arr[r] – arr[l]
        If value diff is K, increment count and move both pointers to next element
        if value diff > k, move l to next element
        if value diff < k, move r to next element
    return count


"""
# Time Complexity: O(nlogn) | Auxiliary Space: O(1)
def count_pairs_with_diff_k(arr,k):

    n = len(arr)

    count = 0

    arr.sort()

    l = 0
    r = 0
    res =[]

    while r < n:
        if arr[r] -arr[l] ==k:
            res.append((arr[r], arr[l]))
            count += 1
            l +=1
            r +=1
            

        elif arr[r]-arr[l] > k:
            l +=1
        else:
            r +=1
    return count, res


print("Two pointers Expected: , Actual:", count_pairs_with_diff_k([1, 5, 3, 4, 2], 3))


"""

Using Binary Search: Works with duplicates in the array
1) Initialize count as 0
2) Sort all numbers in increasing order.
4) Do the following for each element arr[i]
    a) Binary Search for the first occurrence of arr[i] + k in the sub array arr[i+1, N-1], let 
    this index be 'X'
    b) if arr[i]+k is not found, return the index of the first occurrence of the value greater 
    than arr[i] + k
    c) Repeat steps a and b to search for the first occurrence of arr[i] + k + 1, let this be 'Y'
    d) Increment count with 'Y - X'
    e) Return count

Time Complexity: O(nlogn)
Auxiliary Space: O(1)

"""

def BS(arr, X, low):
    high = len(arr)-1
    ans =len(arr)

    while(low <= high):
        mid = low + (high -low) //2
        if(arr[mid] >= X):
            ans = mid
            high = mid -1
        else:
            low = mid + 1
    return ans

def count_pairs_with_diff_k_two(arr, k):
    N = len(arr)
    count = 0
    arr.sort()
    for i in range(N):
        X = BS(arr, arr[i]+k, i + 1)
        if (X != N):
            Y = BS(arr, arr[i]+k+1, i+1)
            count += Y - X
    return count


print("CCCCC Expected " , count_pairs_with_diff_k_two([ 1, 3, 5, 8, 6, 4, 6 ], 2));






'''

my tests

'''
def my_tests(arr, k):
    arr.sort()
    i =0
    j =len(arr)-1
    res =[]

    while i < j:
        if (arr[j] -arr[i]) ==k:
            res.append((arr[j], arr[i]))
            i +=1
        else:
            if (arr[j] -arr[i]) > k:
                i +=1
            else:
                j -=1
            
            
    return res

# O(n^2)
# This solution doesn’t work if there are duplicates in array as the requirement is to 
# count only distinct pairs.
def my_tests_two(arr, k):
    res =[]
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if abs(arr[i]-arr[j]) ==k:
                res.append((arr[j], arr[i]))
    return res

# Time complexity: O(n) | Space complexity: O(n)
def my_tests_three(arr, k):
    dic ={}
    res=[]
    for i in arr:
        dic[i]=i
    for i in range(len(arr)):
        if (arr[i] +k) in dic:
            new_val =arr[i] +k
            res.append((dic.get(new_val), arr[i]))
    return res

print("Expected: , Actual:", my_tests_three([1, 5, 3, 4, 2], 3))

