"""
Prefix Count

For this question, we ask you to compute the number of strings that conform to a given 
prefix. That is you will first be given a dictionary of words. Then you will be given a 
series of prefixes of words and you will be given a series of queries to return the number
of words in the dictionary that contains that prefix. Each query will simply be a string 
which is asking for the number of words that contain the string.

Only lower-case English letters will be used.

Constraints

1 <= words.length <= 100001

1 <= words[i] <= 10
Examples
Example 1:
Input: word = ["forgot", "for", "algomonster", "while"], prefix = ["fo", "forg", "algo"]
Output: ans = [2, 1, 1]
Explanation:

"forgot" and "for" have the prefix "fo", only "forgot" has "forg" and lastly only 
"algomonster" has the prefix "algo".

"""

from typing import List

def prefix_count(words: List[str], prefixes: List[str]) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    return []

if __name__ == '__main__':
    words = input().split()
    prefixes = input().split()
    res = prefix_count(words, prefixes)
    print(' '.join(map(str, res)))

