"""
Range max

For this question we will give you an array and a series of queries and updates. Each update can 
change 1 particular value in the array and each query will give you an interval where you have to
 return the maximum value on the interval. Each query or update will be a list of 3 elements. 
 The first element is a number denoting a query or update operation, 1 will denote a query and 2 an 
 update operation. If the number is a 1 the next 2 numbers will denote the interval that is to be 
 queried in the 0-indexed array. If the number is a 2 the next 2 numbers will denote the index i and
  value v in that order which means that index i in the array should be updated to v.

Input

    arr: original array of numbers
    operations: list of queries and updates on the array

Output

list containing the answer to all the queries

Examples
Example 1:

Input:

arr = [1,2,3,4,5]

operations = [[1,0,4], [2,4,7], [1,1,4]]

Output: [5,7]

Explanation:

We are given a 1 query operation which means we first query from interval 0 - 4 the largest number 
which is 5. We then are given a 2 update operation which means we update the array at index 4 to the 
value of 7. Therefore, our new array is [1,2,3,4,7]. Lastly, we query one more time between 1 and 4 
where we get a largest value of 7.

Constraints

    1 <= arr.length <= 10000
    1 <= operations.length <= 10000
    Each value of arr will be in the range [1, 30000]


"""
from typing import List

def range_max(arr: List[int], operations: List[List[int]]) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    return []

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    operations = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = range_max(arr, operations)
    print(' '.join(map(str, res)))
