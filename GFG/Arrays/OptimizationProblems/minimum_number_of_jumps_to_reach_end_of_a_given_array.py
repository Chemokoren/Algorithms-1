"""
Given an array of integers where each element represents the max numbers of steps that 
can be made forward from that element. Write a function to return the minimum number of 
jummps to reach the end of the array(starting from the first element). If an element
is 0, they cannot move through that element. If the end isn't reachable, return -1.

Examples: 

Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
Output: 3 (1-> 3 -> 9 -> 9)
Explanation: Jump from 1st element 
to 2nd element as there is only 1 step, 
now there are three options 5, 8 or 9. 
If 8 or 9 is chosen then the end node 9 
can be reached. So 3 jumps are made.

Input:  arr[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
Output: 10
Explanation: In every step a jump 
is needed so the count of jumps is 10.

Method 1: Naive Recursive Approach
- A naive approach is to start from the first element and recursively call for all the
elements reachable from first element. The minimum number of jumps to reach end from 
first can be calculated using minimum number of jumps needed to reach end from the 
elements reachable from first.

minJumps(start, end) =Min(minJumps(k,end)) for all k reachable from start

Complexity Analysis: 

    Time complexity: O(n^n). 
    There are maximum n possible ways to move from a element. So maximum number of steps can be N^N so the upperbound of time complexity is O(n^n)
    Auxiliary Space: O(1). 
    There is no space required (if recursive stack space is ignored).

Note: If the execution is traced for this method, it can be seen that there will be 
overlapping subproblems. For example, minJumps(3, 9) will be called two times as arr[3]
is reachable from arr[1] and arr[2]. So this problem has both properties 
(optimal substructure and overlapping subproblems) of Dynamic Programming.

"""

# program to find Minumum number of jumps to reach end
# Returns minimum number of jumps to reach arr[h] from arr[l]

def minJumps(arr, l, h):

    # Base case: when source and destination are same
    if(h == l):
        return 0
    
    # when nothing is reachable from the given source
    if(arr[l] == 0):
        return float('inf')

    # Traverse through all the points reachable from arr[l]. Recursively get the 
    # minimum number of  jumps needed to reach arr[h] from these reachable points.

    min = float('inf')
    for i in range(l+1, h+1):
        if(i < l + arr[l] + 1):
            jumps = minJumps(arr, i, h)
            if(jumps != float('inf') and jumps +1 < min):
                min = jumps + 1

    return min

arr =[1, 3, 6, 3, 2, 3, 6, 8, 9, 5]
print("Expected: 4, actual:", minJumps(arr, 0, len(arr)-1))

"""
Method 2: Dynamic Programming
- In this way, make a jumps[] array from left to right such that jumps[i] indicate the
minimum number of jumps needed to reach arr[i] from arr[0].
- To fill the jumps array, run a nested loop inner loop counter is j and outer loop count
is i.
- Outer loop from 1 to n-1 and inner loop from 0 to i
- If i is less than j+arr[j] then set jumps[i] to minimum of jumps[i] and jumps[j] + 1.
initially set jump[i] to INT MAX
- Finally, return jumps[n-1]

"""
print("\n Dynamic Programming \n")

# program to find Minimum number of jumps to reach end
# Returns minimum number of jumps to reach arr[n-1] from arr[0]
def minJumps(arr, n):
    jumps = [0 for i in range(n)]
 
    if (n == 0) or (arr[0] == 0):
        return float('inf')
 
    jumps[0] = 0
 
    # Find the minimum number of
    # jumps to reach arr[i] from
    # arr[0] and assign this
    # value to jumps[i]
    for i in range(1, n):
        jumps[i] = float('inf')
        for j in range(i):
            if (i <= j + arr[j]) and (jumps[j] != float('inf')):
                jumps[i] = min(jumps[i], jumps[j] + 1)
                break
    return jumps[n-1]

arr = [1, 3, 6, 1, 0, 9]
print('expected:3, actual:', minJumps(arr, len(arr)))

"""
Time Complexity: O(n^2) 

Auxiliary Space: O(n)

Method 3: Dynamic Programming. 

In this method, we build jumps[] array from right to left such that jumps[i] indicates the
minimum number of jumps needed to reach arr[n-1] from arr[i].

Finally, we return jumps[0]. 

Complexity Analysis: 

    Time complexity:O(n^2). 
    Nested traversal of the array is needed.
    Auxiliary Space:O(n). 
    To store the DP array linear space is needed.
    

"""

# program to find Minimum number of jumps to reach end
# Returns Minimum number of jumps to reach end

def minJumpsThree(arr):
    n = len(arr)-1

    # jumps[0] will hold the result
    jumps =[0 for i in range(n)]

    # Minimum number of jumps needed to reach last element from the last elements
    # itself is always 0. jumps[n-1] is also initialized to 0

    # Start from the second element, move from right to left and construct the jumps[]
    # array where jumps[i] represents minimum number of jumps needed to reach arr[m-1]
    # from arr[i]

    for i in range(n-2, -1, -1):
        # if arr[i] is 0 then arr[n-1] can't be reached from here
        if(arr[i] == 0):
            jumps[i] = float('inf')

        # If we can directly reach to the end point from here then jumps[i] is 1
        elif(arr[i] >=n -1 -1):
            jumps[i] =1

        # otherwise, to find out the minimum number of jumps needed to reach arr[n-1],
        # check all the points reachable from here and jumps[] value for those points
        else:
            # initialize min value
            min = float('inf')

            # following loop checks with all reachable points and takes the minimum
            for j in range(i + 1, n):
                if(j <= arr[i] + i):
                    if(min > jumps[j]):
                        min = jumps[j]

            # Handle overflow
            if(min != float('inf')):
                jumps[i] = min + 1
            else:
                # or INT_MAX
                jumps[i] = min

    return jumps[0]

print("expected:3, actual",minJumpsThree([1, 3, 6, 3, 2, 3, 6, 8, 9, 5]))