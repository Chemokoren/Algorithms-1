"""
 (OA) - Two Sum - Unique Pairs

Write a function that takes a list of numbers and a target number, and then returns the number of 
unique pairs that add up to the target number.

[X, Y] and [Y, X] are considered the same pair, and not unique.
Examples
Example 1:
Input: [1, 1, 2, 45, 46, 46], target = 47
Output: 2
Explanation:

1 + 46 = 47

2 + 45 = 47
Example 2:
Input: [1, 1], target = 2
Output: 1
Explanation:

1 + 1 = 2
Example 3:
Input: [1, 5, 1, 5], target = 6
Output:
1
Explanation:

[1, 5] and [5, 1] are considered the same, therefore there is only one unique pair that adds up to 6.

Solution

    Prereq: Two sum

Explanation

Implement a regular solution for the two sum problem, but use a set to check for and discard 
duplicates.

Implementation

"""
from typing import List

def two_sum_unique_pairs(nums: List[int], target: int) -> int:
    seen = set()
    complement = set()
    for num in nums:
        if target - num in complement:
            pair =(num, target -num) if num < target - num else(target - num, num)
            seen.add(pair)
        complement.add(num)
    return len(seen)

if __name__ =='__main__':
    nums =[int(x) for x in input().split()]
    target =int(input())
    res = two_sum_unique_pairs(nums, target)
    print(res)
