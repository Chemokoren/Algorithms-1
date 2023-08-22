"""
Subarray/Substring vs Subsequence and Programs to Generate them

A subarray is a contiguous part of array. An array that is inside another array. For example 
consider the array [1,2,3,4], there are 10 non-empty suba-arrays. The subarrays are (1), (2),(3),
(4),(1,2), (2,3),(3,4),(1,2,3),(2,3,4) and (1,2,3,4).
In general, for an array/string of size n, there are n*(n+1)/2 non-empty subarrays/substrings

How to generate all subarrays?
We can run two nested loops, the outer loop picks starting element and inner loop considers all
elements on the right of the picked elements as ending element of subarray.

Time Complexity: 0(n^3)

Space Complexity: 0(1)

"""
# generate all possible subarrays/subarrays: complexity: O(n^3)

# prints all subarrays in arr[0..n-1]
def sub_array(arr):

    n = len(arr)

    # Pick starting point
    for i in range(0, n):

        # Pick ending point
        for j in range(i, n):
            # print subarray between current starting and ending points
            for k in range(i, j+1):
                print(arr[k], end=" ")

            print("\n", end=""),

print ("All Non-empty Subarrays")
  
sub_array([1, 2, 3, 4])

"""
Subsequence

A subsequence is a sequence that can be derived from another sequence by removing zero or more
elements, without changing the order of the remaining elements.
For the same example, there are 15 sub-sequences. They are (1), (2),(3),(4),(1,2),(1,3),(1,4),
(2,3),(2,4),(3,4),(1,2,3),(1,2,4),(1,3,4),(2,3,4),(1,2,3,4). More generally, we can say that for 
a sequence of size n, we can have(2^n-1) non-empty sub-sequences in total.
A string example to differentiate: Consider strings "cooksforcooks" and "cks". "cks" is a 
subsequence of "cooksforcooks" but not a substring. "cooks"is both a subsequence and subarray.
Every subarray is a subsequence. More specifically, Subsequence is a generalizing of substring.

A subarray or substring will always be contiguous, but a subsequence need not be contiguous. That
is, subsequences are not required to occupy consecutive positions within the original sequences.
But we can say that both contiguous subsequence and subarray are the same.

How can we generate all Subsequences?

- We can use algorithm to generate power set for generation of all subsequences.


Time Complexity: 0(n*(2^n))

Space Complexity: 0(1)

"""
# code to generate all possible subsequences. Time complexity: O(n*2^n)
import math

def print_subsequences(arr):
    n = len(arr)

    # Number of subsequences is(2**n-1)
    opsize = math.pow(2, n)

    # Run from counter 000 .. 1 to 111..1
    for counter in range(1, (int)(opsize)):
        for j in range(0, n):

            # check if jth bit in the counter is set, if set then print jth element from arr[]
            if(counter & (1<<j)):
                print(arr[j], end=" ")

        print()


print( "All Non-empty Subsequences")  
print_subsequences([1, 2, 3, 4])
