"""
Subarray Sum

Given an array of integers and an integer target, find a subarray that sums to target and return
the start and end indices of the subarray. It's guaranteed to have a unique solution.

Input:

1 -20 -3 30 5 4

7

Output: 1 4

Explanation: -20 - 3 + 30 = 7. The indices for subarray [-20,-3,30] is 1 and 4 (right exclusive).

Intuition

The brute force way is to find the sum of each subarray and compare it with the target. Let N be
the number of elements in the array. There are N subarrays with size 1, N-1 subarrays with 
size 2 .. and 1 subarray with size N. Time complexity is O(N^2).

A key observation is the the sum of a subarray [i, j] is equal to the sum of [0, j] minus the 
sum of [0, i - 1].


The sum of elements from index 0 to i is called the prefix sum. If we have the subarray sum for 
each index, we can find the sum of any subarray in constant time.

With the knowledge of prefix sum under our belt, the problem boils down to Two Sum. We keep a 
dictionary of prefix_sum: index while going through the array calculating prefix_sum. If at 
any point, prefix_sum - target is in the dictionary we have found our subarray.

Time Complexity: O(n)

"""
from typing import List
def subarray_sum(arr: List[int], target:int)->List[int]:

    # prefix_sum 0 happens when we have an empty array
    prefix_sums ={0: 0}
    cur_sum = 0
    for i in range(len(arr)):
        cur_sum += arr[i]
        complement = cur_sum -target
        if complement in prefix_sums:
            return [prefix_sums[complement], i+ 1]
        prefix_sums[cur_sum] = i + 1

if __name__ =='__main__':
    arr =[int(x) for x in input().split()]
    target = int(input())
    res = subarray_sum(arr, target)
    print(' '.join(map(str, res)))

"""
Note that in the implementation, typically we use prefix_sum[i] to denote the sum of elements in 
0...i - 1 (rightmost element i is not included in the sum). One good thing about this is 
prefix_sum[0] then means sum of array up to but not including the first element, i.e. 
empty array. The definition of empty array sum is useful when there exists a subarray starting 
from 0 that sums up to the target. Without the definition of empty array sum we would miss it 
because its complement 0 does not exist in the dictionary.


Explanation

Since the new problem does not ask for index but total number instead, we can change our hashmap 
to "sum k: number of prefix sums that sums up to k".

"""
from typing import Counter, List

def subarray_sum_total(arr: List[int], target: int)->int:
    prefix_sums = Counter()
    prefix_sums[0] =1 # since empty array's sum is 0
    cur_sum = 0
    count = 0
    for i in range(len(arr)):
        cur_sum += arr[i]
        complement = cur_sum -target
        if complement in prefix_sums:
            count += prefix_sums[complement]
        prefix_sums[cur_sum] += 1
    return count

if __name__=='__main__':
    arr =[int(x) for x in input().split()]
    target = int(input())
    res = subarray_sum_total(arr, target)
    print(res)
