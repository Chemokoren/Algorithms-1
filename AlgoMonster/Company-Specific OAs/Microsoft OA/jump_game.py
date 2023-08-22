"""
(OA) - Jump Game

You are given an array of non-negative integers arr and a start index. When you are at an index i, 
you can move left or right by arr[i]. Your task is to figure out if you can reach value 0.

Example 1:
Input: arr = [3, 4, 2, 3, 0, 3, 1, 2, 1], start = 7
Output: true
Explanation:

left -> left -> right
Example 2:
Input: arr = [3, 2, 1, 3, 0, 3, 1, 2, 1], start = 2
Output: false

"""
from collections import deque
from typing import List

def jump_game(arr: List[int], start: int)-> bool:
    seen = set()
    queue = deque([start])
    
    while queue:
        size = len(queue)
        for i in range(size):
            cur = queue.popleft()
            if arr[cur] == 0: return True
            if cur in seen: continue
            seen.add(cur)
            if cur + arr[cur] < len(arr) : queue.append(cur + arr[cur])
            if cur - arr[cur] >= 0: queue.append(cur - arr[cur])
    return False

if __name__=='__main__':
    # arr =[int(x) for x in input().split()]
    # start = int(input())

    arr= [3, 4, 2, 3, 0, 3, 1, 2, 1]
    start = 7
    res = jump_game(arr, start)
    print('true' if res else 'false')
