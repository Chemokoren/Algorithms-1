"""
Maximum sum such that no two elements are adjacent

Given array arr[] of positive numbers, the task is to find the maximum sum of a 
subsequence with the constraint that no 2 numbers in the sequence should be 
adjacent in the array.


Input: arr[] = {5, 5, 10, 100, 10, 5}
Output: 110
Explanation: Pick the subsequence {5, 100, 5}.
The sum is 110 and no two elements are adjacent. This is the highest possible sum.

Input: arr[] = {3, 2, 7, 10}
Output: 13
Explanation: The subsequence is {3, 10}. This gives sum = 13.
This is the highest possible sum of a subsequence following the given criteria

Input: arr[] = {3, 2, 5, 10, 7}
Output: 15
Explanation: Pick the subsequence {3, 5, 7}. The sum is 15.

Naive Approach
- Each element has two choices: either it can be part of the subsequence with the
the highest sum or it cannot be part of the subsequence. So to solve the problem,
build all the subsequences of the array and find the subsequence with the maximum
sum such that no two adjacent elements are present in the subsequence.

Time Complexity: O(n^N)
Auxiliary space: O(1)

Efficient Approach
------------------
This problem can be solved using Dynamic Programming based on the following idea:

- As seen above, each element has two choices. If one element is picked then its
neighbours cannot be picked. Otherwise, its neighbours may be picked or may not 
be.
- So, the maximum sum till ith index has two possibilities: the subsequence 
includes arr[i] or it does not include arr[i].
- If arr[i] is included then the maximum sum depends on the maximum subsequences 
sum till(i-1)th element excluding arr[i-1].
- Otherwise, the maximum sum is the same as the maximum subsequence sum till(i-1)
where arr[i-1] may be included or excluded.

So, build a 2D dp[N][2] array where dp[i][0] stores maximum subsequence sum till
ith index with arr[i] excluded and dp[i][1] stores the sum when arr[i] 
is included.

The values will be obtained by the following relations :
dp[i][1] = dp[i-1][0] + arr[i] and dp[i][0] = max(dp[i-1][0], dp[i-1][1])

Steps to implement the above idea
-----------------------------------

- If the size of the array is 1, then the answer is arr[0]
- Initialize the values of dp[0][0] = 0 and dp[0][1] = arr[0].
- Iterate from i = 1 to N-1:
    - Fill the dp array as per the relation shown above
- Return the maximum between dp[N-1][1] and dp[N-1][0] as the answer

"""

# function to find the maximum sum
def find_max_sum(arr):
    N = len(arr)

    # array dp declaration
    dp =[[0 for i in range(2)] for j in range(N)]

    if (N ==1):
            return arr[0]

    # Initialize the values in dp array
    dp[0][0] = 0
    dp[0][1] = arr[0]

    # Loop to find the maximum possible sum
    for i in range(1, N):
            dp[i][1] = dp[i-1][0]+arr[i]
            dp[i][0] = max(dp[i-1][1], dp[i-1][0])


    # return the maximum sum 
    return max(dp[N-1][0], dp[N-1][1])

 
# Function call
print(find_max_sum([ 5, 5, 10, 100, 10, 5 ]))

"""
Time Complexity: O(N)
Auxiliary Space: O(N)

Space Optimized Approach: The above approach can be optimized to be done in
constant space based on the following observation:

As seen from the previous dynamic programming approach, the value of current
states (for ith element) depends upon only two states of the previous element.
So, instead of creating a 2D array, we can use only two variables to store the 
two states of the previous element.

- say excl stores the value of the maximum subsequencee sum till i-1 when arr[i-1]
is excluded and
- incl stores the value of the maximum subsequence sum till i-1 when arr[i-1]
is included.
- The value of excl for the current state(say excl_new) will be max(excl, incl).
And the value of incl will be updated to excl + arr[i].

Consider arr[] = {5,  5, 10, 100, 10, 5}

Initially at i = 0:  incl = 5, excl = 0

For i = 1: arr[i] = 5
        => excl_new = 5
        => incl = (excl + arr[i]) = 5
        => excl = excl_new = 5

For i = 2: arr[i] = 10
        => excl_new =  max(excl, incl) = 5
        => incl =  (excl + arr[i]) = 15
        => excl = excl_new = 5

For i = 3: arr[i] = 100
        => excl_new =  max(excl, incl) = 15
        => incl =  (excl + arr[i]) = 105
        => excl = excl_new = 15

For i = 4: arr[i] = 10
        => excl_new =  max(excl, incl) = 105
        => incl =  (excl + arr[i]) = 25
        => excl = excl_new = 105

For i = 5: arr[i] = 5
        => excl_new =  max(excl, incl) = 105
        => incl =  (excl + arr[i]) = 110
        => excl = excl_new = 105

So, answer is max(incl, excl) =  110


Steps to implement the above approach:
- Initialize incl and excl with arr[0] and 0 respectively.
- Iterate from i =1 to N-1
    - Update the values of incl and excl as mentioned above.

Return the maximum of incl and excl after the iteration is over 

"""

def find_max_sum_two(arr):
        incl = 0
        excl = 0

        for i in arr:
            # current max excluding i
            new_excl = max(excl, incl)

            # current max including i
            incl = excl + i
            excl  = new_excl
        # return max of incl and excl
        return max(excl, incl)

print("expected: 110, actual: ", find_max_sum_two([5, 5, 10, 100, 10, 5]))