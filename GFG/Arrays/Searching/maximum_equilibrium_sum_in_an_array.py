"""
Maximum equilibrium sum in an array

Examples : 

Input : arr[] = {-1, 2, 3, 0, 3, 2, -1}
Output : 4
Prefix sum of arr[0..3] = 
            Suffix sum of arr[3..6]

Input : arr[] = {-2, 5, 3, 1, 2, 6, -4, 2}
Output : 7
Prefix sum of arr[0..3] = 
              Suffix sum of arr[3..7]

A simple solution is to one by one check the given condition(prefix sum equal to suffix sum) for
every element and returns the element that satisfies the given condition with maximum value.

Time Complexity: O(n2) 
Auxiliary Space: O(n)

"""
# function for finding maximum equilibrium sum
def find_max_sum(arr):
    n = len(arr)
    res = -float("inf")-1

    for i in range(n):
        prefix_sum =arr[i]
        for j in range(i):
            prefix_sum += arr[j]
        suffix_sum = arr[i]
        j = n-1
        while(j > i):
            suffix_sum += arr[j]
            j -= 1
        if(prefix_sum == suffix_sum):
            res = max(res, prefix_sum)

    return res

print("Expected:, Actual: ", find_max_sum([-2, 5, 3, 1, 2, 6, -4, 2]))

"""
A Better approach is to traverse the array and store prefix sum for each index in array presum[],
in which presum[i] stores sum of subarray arr[0..i]. Do another traversal of the array and store
suffix sum in another array suffsum[], in which suffsum[i] stores sum of subarray arr[i..n-1]. 
After this for each index check if presum[i] is equal to suffsum[i] and if they are equal then 
compare their value with the overall maximum so far.

Time Complexity: O(n) 
Auxiliary Space: O(n)

"""
# function to find max equilibrium sum
def find_max_sum_two(arr):
    n = len(arr)
    # array to store prefix sum
    pre_sum = [0 for i in range(n)]

    # array to store suffix sum
    suff_sum =[0 for i in range(n)]

    # variable to store maximum sum
    ans = -float("inf")

    # calculate prefix sum
    pre_sum[0] = arr[0]

    for i in range(1, n):
        pre_sum[i] = pre_sum[i-1] + arr[i]

    # calculates suffix sum and compare it with prefix sum. Update ans accordingly
    suff_sum[n-1] =arr[n-1]
    if(pre_sum[n-1] ==suff_sum[n-1]):
        ans = max(ans, pre_sum[n-1])

    for i in range(n-2, -1, -1):
        suff_sum[i] = suff_sum[i+1] + arr[i]
        if(suff_sum[i] == pre_sum[i]):
            ans = max(ans, pre_sum[i])

    return ans


print("Expected:, Actual:", find_max_sum_two([-2, 5, 3, 1,2, 6, -4, 2]))


"""
Further optimization

- We can avoid the use of extra space by first computing total sum, then using it to find the 
current prefix and suffix sums.

Time Complexity: O(n) 
Auxiliary Space: O(1)

"""
# function to find maximum equilibrium sum
def find_max_sum_three(arr):
    n = len(arr)

    ss = sum(arr)
    prefix_sum = 0
    res = -float("inf")
    for i in range(n):
        prefix_sum  += arr[i]

        if prefix_sum == ss:
            res = max(res, prefix_sum)
        ss -= arr[i]
    return res

     
print("Expected:, Actual:", find_max_sum_three([ -2, 5, 3, 1, 2, 6, -4, 2 ]))