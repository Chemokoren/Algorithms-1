"""
Rose Garden

You are planting onions to make salads. Given an array of positive integers that indicates the day 
that each of your onion is ready for harvest, the minimum number of adjacent mature onions required 
for a salad, and the number of salads you want to make, return the earliest day that you can finish 
making all salads. If it is impossible to make the required number of salads, return -1.

Input

    onions: an array of positive integers. Onion i will be ready for harvest on day onions[i].
    k: the minimum number of adjacent onions required to make a salad.
    n: the number of salads you want to make.

Output

Return the earliest day that you can finish making n salads, or -1 if the task is impossible.

Examples
Example 1:

Input:

onions = [1, 2, 6, 10, 3, 4, 1]

k = 2

n = 2

Output: 4

Explanation:

Day 1: [h, o, o, o, o, o, h]

The first and last onions are ready for harvest.

Day 2: [h, h, o, o, o, o, h]

The second onion matures, and the first 2 mature onions can be used to make a salad.

Day 3: [h, h, o, o, h, o, h]

Day 4: [h, h, o, o, h, h, h]

The last 3 onions make a salad, meeting the required n = 2 salads. So day 4 is the earliest day to 
finish making the required number of salads.

Constraints

    1 <= onions.length == 10^5
    1 <= onions[i] <= 10^9
    1 <= n <= 10^6
    1 <= k <= onions.length

"""

from typing import List

def min_days_salads(onions: List[int], k: int, n: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    return 0

if __name__ == '__main__':
    onions = [int(x) for x in input().split()]
    k = int(input())
    n = int(input())
    res = min_days_salads(onions, k, n)
    print(res)