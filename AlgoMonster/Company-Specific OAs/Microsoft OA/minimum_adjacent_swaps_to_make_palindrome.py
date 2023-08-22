"""
(OA) - Minimum Adjacent Swaps to Make Palindrome

Given a string, what is the minimum number of adjacent swaps required to convert a string into a palindrome. If not possible, return -1.
Example 1:
Input: mamad
Output: 3
Explanation:

swap m with a => maamd

swap m with d => maadm

swap a with d => madam
Example 2:
Input: asflkj
Output: -1
Example 3:
Input: mideld
Output: 3
Explanation:

swap e with l => midled

swap e with d => midlde

swap l with d => middle

"""
from typing import Counter

def is_valid(s: str)->bool:
    count = Counter(s)
    return len([char for char, freq in count.items() if freq % 2]) <=1

def min_swaps(inp: str) -> int:
    if not is_valid(inp):
        return -1
    s = list(inp)
    n = len(inp)

    count = 0
    i = 0
    while i < n // 2:
        left = i
        right = n - left - 1

        while left < right:
            if s[left] == s[right]:
                break
            else:
                right -= 1

        if left == right:
            # s[left] is the character in the middle of the palindrome
            (s[left], s[left + 1]) = (s[left + 1, s[left]])
            count += 1
        else:
            for j in range(right, n - left -1):
                (s[j], s[j + 1]) =(s[j + 1], s[j])
                count += 1
            i += 1
    return count

if __name__ =='__main__':
    inp = input()
    res = min_swaps(inp)
    print(res)

