from typing import List
"""
Maximum Subarray

Given an integer array nums, find the contiquous subarray (containing at least one number)
which has the largest sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum =6 .

"""

'''
that, given an array A consisting of N integers, returns the biggest value X, which occurs 
in A exactly X times. If there is no such value, the function should return 0
'''
class Solution:

    def maxSubArray(self, nums: List[int])->int:
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum +=n
            maxSub =max(maxSub, curSum)
        return maxSub

sol = Solution()
print("Expected:6, Actual:", sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


"""
you are given a String S containing lowercase English letters. Your task is to calculate the
minimum number of letters that need to be removed in order to make it possible to build 
a palindrome from the remaining letters. When building the palindrome, you can rearrange 
the remaining letters in any way

"""
def minDeletions(X, i, j):
    
    # base case
    if i >= j:
        return 0

    # if the last character of the string is the same as the first character
    if X[i] == X[j]:
        return minDeletions(X, i+1, j-1)

    # otherwise, if the last character of the string is different from the first character
    # 1. Remove the last character and recur for the remaining substring
    # 2. Remove the first character and recur for the remaining substring
    # return 1 (for remove operation) + minimum of the two values
    return 1 + min(minDeletions(X, i, j-1), minDeletions(X, i+1, j))


print('Expected:3, Actual:', minDeletions('ACBCDBAA', 0, len('ACBCDBAA') - 1))

"""
The worst-case time complexity of the above solution is exponential (O(2^n)), where n is the 
length of the input string. The worst case happens when there is no repeated character 
present in X, and each recursive call will end up in two recursive calls. It also requires 
additional space for the call stack.


- The problem has an optimal substructure. 
- We have seen that the problem can be broken down into smaller subproblems, which can
further be broken down into yet smaller subproblems etc.
- The problem also exhibits overlapping subproblems, so we will end up solving the same
problem over and over again.

Let's consider the recursion tree for a sequence of length 6 having all distinct characters

say ABCDEF

                                        (0, 5)

                                /                      \
                            (1, 5)                     (0,4)

                        /           \                /                   \
                    (2, 5)        (1,4)            (1,4)                 (0,3)

                /           \    /          \     /    \             /              \  
            (3,5)          (2,4)(2,4)      (1,3)                   (1,3)            (0,2)
        /        \        /    \ /  \      /    \                   /  \         /        \
    (4,5)     (3,4)   (3,4)  (2,3)      (2,3)   (1,2)                           (1,2)     (0,1)

- As we can see, the same subproblems are getting computed repeatedly. 
- We know that problems with optimal substructure and overlapping subproblems can be solved
using dynamic programming, where subproblem solutions are memoized rather than computed
again. 

"""
# Function to find out the minimum number of deletions required to convert a given string 
# `X[i...j]` into a palindrome
def minDeletionsDP(X, i, j, lookup):

    # base condition
    if i >= j:
        return 0
    # construct a unique key from dynamic elements of the input
    key =(i, j)

    # if the subproblem is seen for the first time, solve it and store its result in a
    # dictionary
    if key not in lookup:
        # if the last character of the string is the same as the first character
        if X[i] == X[j]:
            lookup[key] =minDeletionsDP(X,i+1, j-1, lookup)
        else:
            # if the last character of the string is different from the first character

            # 1. Remove the last character and recur for the remaining substring
            # 2. Remove the first character and recur for the remaining substring

            # return 1 (for remove operation) + minimum of the two values
            result = 1 + min(minDeletionsDP(X, i, j-1, lookup), minDeletionsDP(X, i+1, j,lookup))
            lookup[key] = result

    # return the subproblem solution from the dictionary
    return lookup[key]

# create a dictionary to store solutions to subproblems
lookup = {} 
print('Expected:3, Actual:', minDeletionsDP('ACBCDBAA', 0, len('ACBCDBAA') - 1, lookup))

"""
The time complexity of the above solution is O(n^2) and requires O(n^2) extra space, where n
is the length of the input string.

This problem is also a classic variation of the Longest Common Subsequence(LCS) problem. The 
idea is to find the Longest Palindrome subsequence of the given string. The minimum number of
deletions required will be the difference in length of the string and palindromic subsequence.
We can easily find the longest palindromic subsequence by taking the longest common subsequence
of the given string and its reverse, i.e., call LCS(X, reverse(X))

The time complexity of this solution is O(n^2), and the auxiliary space used is O(n^2)
"""
# function to find out the minimum number of deletions required to convert a given string
# `X[0...n-1]` into a palindrome
def minDeletionsTwo(X):
    n =len(X)

    # string 'Y' is a reverse of 'X'
    Y = X[::-1]
    # `lookup[i][j]` stores the length of LCS of substring `X[0...i-1]` and `Y[0...j-1]`
    lookup =[[0 for x in range(n + 1)] for y in range((n+1))]

    # fill the lookup table in a bottom-up manner
    for i in range(1, n+1):
        for j in range(1, n+1):
            # if current character of 'X' and 'Y' matches
            if X[i - 1] == Y[j - 1]:
                lookup[i][j] = lookup[i-1][j-1]+1

            # otherwise, if the current character of 'X' and 'Y' don't match
            else:
                lookup[i][j]=max(lookup[i - 1][j], lookup[i][j - 1])

    # Now, `lookup[n][n]` contains the size of the longest palindromic subsequence.
    # The minimm number of deletions required will be the difference in the size
    # of the string and the size of the palindromic subsequence
    return n - lookup[n][n]

 
print('Expected: 3, Actual:', minDeletionsTwo('ACBCDBAA'))
