"""
Reorganize String

Given a string s, check if the letters can be rearranged so that two characters that are 
adjacent to each other are not the same.

If possible, output any possible result. If not possible, return the empty string.

Example 1:
Input:s = "aab"
Output: aba
Example 2:
Input:s = "aaab"
Output: ``
Note:

s will consist of lowercase letters and have length in range [1, 500].

"""
from typing import Counter

def reorganize_string(s: str) -> str:
    # WRITE YOUR BRILLIANT CODE HERE
    return ''

if __name__ == '__main__':
    s = input()
    res = reorganize_string(s)
    if not res:
        print("Impossible")
        exit()
    input_counter, output_counter = Counter(s), Counter(res)
    if input_counter != output_counter:
        print("Not rearrangement")
        exit()
    for i in range(len(res) - 1):
        if res[i] == res[i + 1]:
            print(f"Same character at index {i} and {i+1}")
            exit()
    print("Valid")