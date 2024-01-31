"""
Distinct Subsequences

Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some
(can be none) of the characters without disturbing the remaining character's relative
positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

It is guaranteed the answer fits on a 32-bit signed integer.

Example 1:

Input: s ="rabbbit", t ="rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
rabbbit
    _
rabbbit
   _
rabbbit
  _ 
"""
class Solution:

    """
    This code is an implementation of a function to find the number of distinct subsequences of string t in string s. The function uses a recursive depth-first search (DFS) approach to explore all possible subsequences. Here's a breakdown of what's happening in the code:

    The distinct_subsequences method is defined within a class called Solution. It takes two string arguments, s and t, representing the input strings.

    The core logic for finding distinct subsequences is implemented within the nested dfs function. The purpose of this function is to recursively explore and count the distinct subsequences of t within the substring of s starting from index i and j, respectively. The word variable keeps track of the current subsequence being built, and count is used to store the count of valid subsequences.

    The base cases for the recursion are as follows:

        If the word is equal to t, it means a valid subsequence of t has been found in s. In this case, count is incremented by 1, and the function returns count.

        If i has exceeded the length of s or j has exceeded the length of t, it means we have reached the end of either string. In this case, the function returns the current value of count.

    If the characters at indices i and j in s and t, respectively, match (i.e., s[i] == t[j]), we have two options:

        We can include the matching character in the subsequence by recursively calling dfs(i + 1, j + 1, word + s[i], count). In this case, both i and j are incremented by 1, and the current character is added to word.

        We can skip the matching character in s and continue to look for subsequences by calling dfs(i + 1, j, word, count).

    The function returns the sum of the results from these two recursive calls. This is because we are exploring both possibilities: including the matching character and skipping it.

    The main distinct_subsequences function is invoked with an initial state of i = 0, j = 0, an empty word, and count = 0. It returns the result of the dfs function, which recursively explores all possible subsequences and counts the valid ones.

In summary, this code uses a depth-first search (DFS) approach to explore and count the distinct subsequences of string t in string s. It uses recursion to consider both including and skipping matching characters while building valid subsequences.

Time complexity:
----------------

    The time complexity of this solution is exponential, specifically O(2^N), where N is the length of the string s.

The reason for this exponential time complexity is that the dfs function explores all possible combinations of subsequences of s by making recursive calls. At each character position in s, it has two choices: include the character in the subsequence or skip it. This binary choice results in an exponential number of recursive calls and, as a result, an exponential time complexity.

In the worst case, the function will explore all possible combinations of subsequences of s, resulting in a time complexity of O(2^N), where N is the length of s. This makes the solution inefficient for large input strings.

Memory Complexity:
-----------------
The memory complexity of this solution is determined by the maximum depth of the recursive call stack, and it depends on the input strings and their lengths.

In the worst case, where all possible subsequences are explored, the depth of the recursive call stack can reach the length of string s. This is because at each position in s, the dfs function makes recursive calls, potentially branching for each character. Therefore, the memory complexity is O(N), where N is the length of string s.

Keep in mind that this solution also uses a moderate amount of memory to store intermediate results in the word and count variables for each call on the stack. However, this memory usage is proportional to the depth of the recursive call stack and does not contribute significantly to the overall memory complexity.

    """
    def distinct_subsequences(self, s, t):
        
        
        def dfs(i, j, word, count):
            
            if (word == t):
                count += 1
                return count
            if i >= len(s) or j >= len(t):
                return count
            if s[i] == t[j]:
                count = dfs(i + 1, j + 1, word + s[i], count)
            count = dfs(i + 1, j, word, count)
            return count
        
        return dfs(0, 0, word="", count=0)
    
    """
    Code Walk-through
    -----------------
    Here's a step-by-step explanation of how the code works:

    The num_distinct function takes two strings, s and t, as input.

    It initializes a cache dictionary to store computed results. This is used for memoization to avoid redundant calculations.

    The core logic is implemented in the dfs (depth-first search) function, which takes two parameters: i and j. These parameters represent the current indices in s and t, respectively.

    The function begins with two base cases:
        If j has reached the end of t, it means we have found a valid subsequence, so it returns 1.
        If i has reached the end of s, it means we've exhausted s without finding a valid subsequence, so it returns 0.

    The function checks the cache to see if it has already computed a result for the given indices (i, j). If it has, it returns the cached result to avoid recomputation.

    If the characters at s[i] and t[j] match, there are two choices:
        Include the current character from s in the subsequence and make a recursive call by advancing both i and j.
        Skip the current character from s and make a recursive call by advancing only i.

    The function sums the results of both choices and caches the result.

    If the characters at s[i] and t[j] don't match, we can only skip the current character from s and make a recursive call by advancing i. The result is cached.

    Finally, the dfs function returns the cached result for the current indices (i, j).

    The main function starts the recursion by calling dfs(0, 0) to explore all possible subsequences starting from the beginning of s and t.

    The dfs function returns the number of distinct subsequences, and this value is returned as the final result by the num_distinct function.

The code uses memoization to optimize the computation of the number of distinct subsequences, reducing the time complexity from exponential to polynomial.

    """
    def num_distinct(self, s: str, t: str) -> int:
        cache = {}  # Initialize a cache to store computed results

        def dfs(i, j):
            # Base cases:
            if j == len(t):
                return 1  # If we have matched all characters in t, we've found a valid subsequence
            if i == len(s):
                return 0  # If we've exhausted all characters in s and haven't matched t, it's not possible

            if (i, j) in cache:
                return cache[(i, j)]  # Check if we've already computed the result for these indices

            if s[i] == t[j]:
                # If the characters match, we have two choices:
                # 1. Include the current character from s in the subsequence.
                # 2. Skip the current character from s.
                # We recursively call dfs for both choices and sum the results.
                cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                # If the characters don't match, we can only skip the current character from s.
                # We make a recursive call for that.
                cache[(i, j)] = dfs(i + 1, j)

            return cache[(i, j)]  # Return the result for the current indices

        # Start the recursion from the beginning of s (i=0) and t (j=0)
        return dfs(0, 0)

            
sol = Solution()
print(sol.distinct_subsequences(s ="rabbbit", t ="rabbit"))

# Test Case 1: No matching subsequences
print("Expected output: 0", sol.distinct_subsequences(s="abcde", t="fghij"))  # Expected output: 0

# Test Case 2: Only one possible subsequence "abcde"
print("Expected output: 1", sol.distinct_subsequences(s="abcde", t="abcde"))  # Expected output: 1

# Test Case 3: Multiple distinct subsequences
print(" Expected output: 3", sol.distinct_subsequences(s="abab", t="ab"))  # Expected output: 3 (abab, abab, abab)

# Test Case 4: Longer input strings
print("Expected output: 5", sol.distinct_subsequences(s="hellothere", t="he"))  # Expected output: 168

# Test Case 5: Empty input strings, one is a subsequence of the other
print("Expected output: 0", sol.distinct_subsequences(s="", t="abcde"))  # Expected output: 0


print("------")

print("Expected output: 3, Actual ::",sol.num_distinct(s ="rabbbit", t ="rabbit"))
print("Expected output: 0, Actual ::", sol.num_distinct(s="abcde", t="fghij"))  # Expected output: 0
print("Expected output: 1, Actual ::", sol.num_distinct(s="abcde", t="abcde"))  # Expected output: 1
print(" Expected output:3, Actual ::", sol.num_distinct(s="abab", t="ab"))  # Expected output: 3 (abab, abab, abab)
print("Expected output: 5, Actual ::", sol.num_distinct(s="hellothere", t="he"))  # Expected output: 168
print("Expected output: 0, Actual ::", sol.num_distinct(s="", t="abcde"))  # Expected output: 0