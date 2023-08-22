"""
Count the number of possible triangles

Given an unsorted array of positive integers, find the number of triangles that can be formed
with three different array elements as three sides of triangles. For a triangle to be possible 
from 3 values,  the sum of any of two values (or sides) must be greater than the third value
(or third side).

Examples:

Examples: 

Input: arr= {4, 6, 3, 7}
Output: 3
Explanation: There are three triangles 
possible {3, 4, 6}, {4, 6, 7} and {3, 6, 7}. 
Note that {3, 4, 7} is not a possible triangle.  

Input: arr= {10, 21, 22, 100, 101, 200, 300}.
Output: 6

Explanation: There can be 6 possible triangles:
{10, 21, 22}, {21, 100, 101}, {22, 100, 101}, 
{10, 100, 101}, {100, 101, 200} and {101, 200, 300}

Method 1: Brute Force

The brute force method is to run three loops and keep track of the number of triangles possible
so far. The three loops select three different values from an array. The innermost loop checks for
the triangle property which specifies the sum of any two sides must be greater than the value of
the third side.

Algorithm:
- Run three nested loops each loop starting from the index of the previous loop to end of array
i.e run first loop from 0 to n, loop j from i to n and k from j to n.
- Check if array[i] + array[j] > array[k], i.e. sum of two sides is greater than the third
- Check condition (2) for all combinations of sides by interchanging i, j, k
- if all three conditions match, increase the count
- print the count

    Time Complexity: O(N^3) where N is the size of input array.
    Space Complexity: O(1)
"""

def find_number_of_triangles(arr):
    n = len(arr)

    count = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            # innermost loop checks for the triangle property
            for k in range(j + 1, n):
                # sum of two sides is greater than the third
                if(arr[i] + arr[j] > arr[k] and 
                arr[i] + arr[k] > arr[j] and 
                arr[k] + arr[j] > arr[i]):
                    count +=1
    return count

print("Expected:3, Actual: ", find_number_of_triangles([4, 6, 3, 7]))
print("Expected:6, Actual: ", find_number_of_triangles([10, 21, 22, 100, 101, 200, 300]))

"""

Method 2
- Time complexity is: O(N^2) where two sides of the triangles are fixed and the count can be found
using those two sides.

Approach
- First sort the array in ascending order. Then use two loops. The outer loop to fix the first
side and inner loop to fix the second side and then find the farthest index of the third side(
    greater than indices of both sides) whose length is less than sum of the other two sides.
So a range of values third sides can be found, where it is guaranteed that its length if greater 
than the other two  individual sides but less than the sum of both sides.


Algorithm
- Let a, b and c be three sides. The below condition must hold for a triangle(sum of two sides
is greater than the third side)
1. a+b >c
2. b+c >a
3. a+c >b

The following are the steps to count triangle:

1. sort the array in ascending order.
2. Now run a nested loop. The outer loop runs from start to end and the inner loop runs from 
index + 1 of the first loop to the end. Take the loop counter of first loop as i and second
loop as j. Take another k = i + 2
3. Now there is two pointers i and j, where array[i] and array[j] represents two sides of the 
triangles. For a fixed i and j, find the count of third sides which will satisfy the conditions
of a triangle. i.e find the largest value of array[k] such that array[i] + array[j]>array[k]
4. So, when we get the largest value, then the count of third side is k -j, add it to the total
count.
5. Now sum up for all valid pairs of i and j where i < j

    Time Complexity: O(n^2). 
    The time complexity looks more because of 3 nested loops. It can be observed that k is
    initialized only once in the outermost loop. The innermost loop executes at most O(n) time for
    every iteration of the outermost loop, because k starts from i+2 and goes up to n for all 
    values of j. Therefore, the time complexity is O(n^2).
    Space Complexity: O(1). 
    No extra space is required. So space complexity is constant
"""

def find_number_of_triangles(arr):

    n = len(arr)
    arr.sort()

    count = 0

    # fix the first element. We need to run till n-3 as the
    # other two elements are selected from arr[i+1 ..n-1]
    for i in range(0, n-2):

        # Initialize index of the rightmost 3rd element
        k =i +2

        # fix the second element
        for j in range(i +1, n):

            # Find the rightmost element which is smaller
            # than the sum of two fixed elements
            # The important thing to note here is, we use
            # the previous value of k. If value of arr[i] +
            # arr[j-1] was greater than arr[k], then arr[i] +
            # arr[j] must be greater than k, because the array
            # is sorted.
            while(k < n and arr[i] + arr[j] > arr[k]):
                k += 1
            
            # Total number of possible triangles that can be
            # formed with the two fixed elements is k - j - 1.
            # The two fixed elements are arr[i] and arr[j]. All
            # elements between arr[j + 1] to arr[k-1] can form a
            # triangle with arr[i] and arr[j]. One is subtracted
            # from k because k is incremented one extra in above
            # while loop. k will always be greater than j. If j
            # becomes equal to k, then above loop will increment k,
            # because arr[k] + arr[i] is always greater than arr[k]

            if (k > j):
                count += k-j-1

    return count


print ("Expected Number of Triangles:6, Actual:", find_number_of_triangles([10, 21, 22, 100, 101, 200, 300]))

print("\n my tests \n")


"""
Method 3
- The time complexity can be greatly reduced using Two Pointer methods in just two nested loops.

- First sort the array, and run a nested loop, fix an index and then try to fix an upper and 
lower index within which we can use all the lengths to form a triangle with that fixed index.

Algorithm:
1. Sort the array and then take three variables l, r and i, pointing to start, end-1 and array
element starting from end of the array.
2. Traverse the array from end(n-1 to 1), and for each iteration keep the value of l=0 and r=i-1
3. Now if a triangle can be formed using arr[l] and arr[r] then triangles can obviously be formed.

from a[l+1], a[l+2] ..a[r-1] and a[i], because the array is sorted, which can be directly 
calculated using(r-l) and then decrement the value of r and continue the loop till l is less than
r
4. If a triangle cannot be formed using arr[l] and arr[r] then increment the value of l and 
continue the loop till l is less than r
5. So the overall complexity of iterating through all array elements reduces.

    Time complexity: O(n^2). 
    As two nested loops are used, but overall iterations in comparison to the above method reduces greatly.
    Space Complexity: O(1). 
    As no extra space is required, so space complexity is constant
"""

def count_triangles(A):

    n = len(A)
    A.sort()

    count = 0

    for i in range(n-1, 0, -1):
        l = 0
        r = i-1
        while(l < r):
            if(A[l] +A[r] > A[i]):

                # if it is possible with a[l], a[r]
                # and a[i] then it is also possible
                # with a[l + 1] ..a[r-1], a[r] and a[i]
                count += r -l

                # checking for more possible solutions
                r -= 1
            else:
                # if not possible check for higher values of arr[l]
                l += 1
    return count 

print("CC Expected:6, Actual: ", count_triangles([10, 21, 22, 100, 101, 200, 300]))
print("CC Expected:9, Actual: ", count_triangles([ 4, 3, 5, 7, 6 ]))


'''
my tests
'''

def my_tests(arr):
    count = 0
    for i in range(len(arr)-2):
        if (arr[i] +arr[i+1] > arr[i+2]) and (arr[i] +arr[i+2] > arr[i+1])and (arr[i+1] +arr[i+2] > arr[i]):
            count +=1
    return count


print("Tests Expected:3, Actual: ", my_tests([4, 6, 3, 7]))
print("Tests Expected:6, Actual: ", my_tests([10, 21, 22, 100, 101, 200, 300]))
