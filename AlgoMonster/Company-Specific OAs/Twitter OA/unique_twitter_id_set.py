"""
(OA) - Unique Twitter User ID Set

Given an array of integers l with size n, write a function that determines the minimum sum of another
array l_unique with size n such that:

    l[i] <= l_unique[i] for all 0 <= i < n;
    l_unique[i] != l_unique[j] for all 0 <= i != j < n.

Example 1:

Input: l = [3, 2, 1, 2, 7]

Output: 17

Explanation: In this case, one l_unique could be [3, 2, 1, 4, 7], and the sum of this array is equal 
to 3 + 2 + 1 + 4 + 7 = 17.

Constraints:

    1 <= n <= 2000
    1 <= l[i] <= 3000 for all 0 <= i < n

"""

from typing import List

def get_sum(l: List[int]) -> int:
    return 0

if __name__ == '__main__':
    l = [int(x) for x in input().split()]
    res = get_sum(l)
    print(res)