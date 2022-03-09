"""
(OA) - Min Steps to Make Piles Equal Height

Given N piles of equal or unequal heights. In one step, You can remove any number of boxes from the 
pile which has the maximum height and try to make it equal to the one which is just lower than the 
maximum height of the stack. Determine the minimum number of steps required to make all of the piles
equal in height.

Example 1

Input: [5, 2, 1]

Output: 3

Explanation:

Step 1: reducing 5 -> 2 = [2, 2, 1] Step 2: reducing 2 -> 1 = [2, 1, 1] Step 3: reducing 2 -> 1 = [1, 1, 1]


"""
from typing import Counter, List

def min_steps(nums: List[int])->int:
    cnt = Counter(nums)
    nums = sorted(cnt.keys(), reverse=True)
    k, ans = 0, 0
    for x in nums[:-1]:
        k+= cnt[x]
        ans += k
    return ans

if __name__ == '__main__':
    nums =[int(x) for x in input().split()]
    res = min_steps(nums)
    print(res)

# input: [5 5 2 2 1 1], output =6
# input: [5 5 1], expected output =2
# input: [5 5 5 5 1], expected output = 4
# input: [3 2 2], exptected output = 1

