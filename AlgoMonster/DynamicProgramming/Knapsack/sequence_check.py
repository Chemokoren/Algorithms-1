"""
Sequence Check

    Prereq: Knapsack Intro

Given 2 strings determine how many distinct subsequences of s equal t. A subsequence of
s is a the original sequence s with some characters deleted. The answer is guaranteed to
be less than 2^31-1.

Constraints

1 <= s.length, t.length <= 100001

The strings s and t will only contain lowercase english letters
Examples
Example 1
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:

You can remove any of the 3 middle b values from s to make the t value

"""