"""
Number of subsets with product less than k

You are given an array of n-elements, you have to find the number of subsets whose 
product of elements is less than or equal to a given integer k.


Examples:

Input : arr[] = {2, 4, 5, 3}, k = 12
Output : 8
Explanation : All possible subsets whose 
products are less than 12 are:
(2), (4), (5), (3), (2, 4), (2, 5), (2, 3), (4, 3)

Input : arr[] = {12, 32, 21 }, k = 1
Output : 0
Explanation : there is not any subset such 
that product of elements is less than 1


If we go through the basic approach to solve this problem, then we have to generate all 
possible 2^n subset and for each of then we have to calculate product of elements of 
subset and compare products value with given then. But the disadvantage of this approach 
is that its time complexity is too high i.e. O(n*2^n). Now, we can see that it is going to
be exponential time complexity which should be avoided in case of competitive codings.

Advance Approach
- We are going to use the concept of meet in the middle. By, using this concept we can 
reduce the complexity of our approach to O(n*2^(n/2)).

How to use MEET IN THE MIDDLE Approach :

- First of all we simply divide the given array into two equal parts and after that we 
generate all possible subsets for both parts of array and store value of elements product 
for each subset separately into two vectors (say subset1 & subset2). 
Now this will cost O(2^(n/2)) time complexity. Now if we sort these two vectors
(subset1 & subset2) having (2^(n/2)) elements each then this will cost 
O(2^(n/2)*log2^(n/2)) ≈ O(n*(2^(n/2)) Time complexity. 
In next step we traverse one vector subset1 with 2^(n/2) elements and find the upper bound
of k/subset1[i] in second vector which will tell us the count of total elements whose 
products will be less than or equal to k. And thus for each element in subset1 we will 
try to perform a binary search in form of upper_bound in subset2 resulting again a Time 
complexity of O(n*(2^(n/2))). So, if we try to compute our overall complexity for this 
approach we will have O(n*(2^(n/2)) + n*(2^(n/2))) + n*(2^(n/2))) ≈ O(n*(2^(n/2))) as our
time complexity which is much efficient than our brute force approach.

Algorithm:
- Divide array into two equal parts.
- Generate all subsets and foe each subset calculate product of elements and push this to
a vector. Try this for both part of array.
- Sort both new vector which contains products of elements for each possible subsets
-Traverse any one vector and find upper-bound of element k/vector[i] to find how many
subsets are there for vector[i] whose product of elements is less than k.

Some key points to improve complexity:
- Ignore elements from array if greater than k.
-Ignore product of elements to push into vector(subset1 or subset2) if greater than k.

"""

# Finding the count of subset having product less than k
import bisect

def findSubset(arr, k):
    n = len(arr) 

    # declare four vector for dividing array into two halves and storing product value
    # of possible subsets for them
    vect1, vect2, subset1, subset2 =[], [], [], []

    # ignore element greater than k and divide array into 2 halves
    for i in range(0, n):

        # ignore element if greater than k
        if arr[i] > k:
            continue
        if i <= n // 2:
            vect1.append(arr[i])
        else:
            vect2.append(arr[i])
        
    # generate all subsets for 1st half(vect1)
    for i in range(0, (1 << len(vect1))):
        value = 1
        for j in range(0, len(vect1)):
            if i & (1 << j):
                value *= vect1[j]
        
        # push only in case subset product is less than equal to k
        if value <= k:
            subset1.append(value)

    # generate all subsets for 2nd half (vect2)
    for i in range(0, (1 << len(vect2))):
        value = 1
        for j in range(0, len(vect2)):
            if i & (1 << j):
                value *=vect2[j]

        # push only in case subset product is less than equal to k
        if value <= k:
            subset2.append(value)

    # sort subset2
    subset2.sort()

    count = 0
    for i in range(0, len(subset1)):
        count += bisect.bisect(subset2, (k // subset1[i]))

    # for null subset decrement the value of count
    count -=1

    return count

print(findSubset([4, 2, 3, 6, 5] , 25)) 