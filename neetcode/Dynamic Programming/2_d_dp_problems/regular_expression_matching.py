"""
Regular Expression Matching

Given an input string(s) and a pattern (p), implement regular expression matching with
support for '.' and '*' where:

- '.' Matches any single character.
- '*' Matches zero or more of the preceding element.

The matching should cove the entire input string (not partial).

Example 1:
Input: s ="aa", p="a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input: s="aa", p="a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'.
Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input: s ="ab" , p =".*"
Output: True

"""
class Solution:

    def regular_expression_matching(self, s : str, p: str)->bool:

       def dfs(i, j):
           if i >= len(s) and j >= len(p):
               return True
           if j >= len(p):
               return False
           
           match = i < len(s) and (s[i] == p[j] or p[j] ==".")
           if (j + 1) < len(p) and p[j + 1] == "*":
               # choosing to include * or not to include
               return (dfs(i, j+ 2) or (match and dfs(i + 1, j)))
           if match:
               return dfs(i + 1, j + 1)

           return False
       return dfs(0, 0)

sol = Solution()

print("False", sol.regular_expression_matching("ab", ".*c"))
print("False", sol.regular_expression_matching(s ="aa", p="a"))
print("True", sol.regular_expression_matching(s ="aa", p="a*"))
print("True", sol.regular_expression_matching(s ="ab", p=".*"))

print(" ----------- end of iterative approach -----------")

"""



----------------------------------------------------

This code is an implementation of a regular expression matching algorithm using top-down
memoization (dynamic programming). The main goal of this algorithm is to determine if a 
given string s matches a pattern p where the pattern can contain regular expression 
characters like . (matches any single character) and * (matches zero or more occurrences of 
the preceding element).

Here's a walkthrough of the code:
---------------------------------

Step 1: Importing Necessary Modules

The code starts by importing the unittest modules. The unittest module is used for testing 
purposes.

Step 2: Defining the Solution Class

The Solution class is defined to encapsulate the regular_expression_matching function. 
This function takes two input strings: s representing the text string and p representing the
regular expression pattern.

Step 3: Implementing the regular_expression_matching Function

The regular_expression_matching function uses a top-down memoization approach to efficiently 
determine whether the text string s matches the regular expression pattern p.
It utilizes a cache, represented by the cache dictionary, to store the results of previously
computed subproblems, avoiding redundant computations.

Step 4: Defining the dfs Helper Function

The dfs function is a recursive helper function that takes two indices: i representing the 
index in the text string s and j representing the index in the regular expression pattern p.
It determines whether the substring of s starting at i matches the substring of p starting 
at j.

Step 5: Base Cases

The dfs function checks for base cases to determine if the recursion should terminate. 
If both i and j reach the end of their respective strings, it indicates a successful match, 
and True is returned. 
If j reaches the end of the pattern but not the string index (i), it means there's no more 
pattern to match, and False is returned.

Step 6: Matching Characters

The dfs function checks if the character at s[i] matches the character at p[j]. If either 
they match or p[j] is a wildcard (.), the match flag is set to True.

Step 7: Handling Zero or More Repetitions (*)

If the character at p[j + 1] is *, it indicates that the preceding character can be matched
zero or more times. The dfs function recursively calls itself to check two scenarios:

    dfs(i, j + 2): This scenario skips the current character with the * and moves to the 
    next pattern character.
    match and dfs(i + 1, j): This scenario matches the current character with the * and 
    recursively checks for further matches. Move to the next character in the string if 
    there is a match.

The dfs function stores the result of these recursive calls in the cache and returns the 
combined result.

Step 8: Matching Case

If the current characters match  (s[i] == p[j]) or if the pattern has a '.', the dfs function 
recursively calls itself to check the next characters in both strings and returns the result.

Step 9: Handling No Match

If no match is found, the dfs function stores False in the cache and returns False.

"""
import re
import unittest

class Solution1:

    def regular_expression_matching(self, s : str, p: str)->bool:
       # TOP-DOWN Memoization
       cache = {}

       def dfs(i, j):
           if (i, j) in cache:
               return cache[(i, j)]
           if i >= len(s) and j >= len(p):
               return True
           if j >= len(p):
               return False
           
           match = i < len(s) and (s[i] == p[j] or p[j] ==".")
           if (j + 1) < len(p) and p[j + 1] == "*":
               # choosing to include * or not to include
               cache[(i, j)] = (dfs(i, j+ 2) or (match and dfs(i + 1, j)))
               return cache[(i, j)]
           if match:
               cache[(i, j)] = dfs(i + 1, j + 1)
               return cache[(i, j)]
           cache[(i, j)] = False
           return [(i, j)]
       return dfs(0, 0)

"""
The provided test cases are implemented using the unittest module to verify the correctness
of the regular_expression_matching method in the Solution class. 

Let's go through each test case:

Test Case Initialization:

    The TestRegularExpressionMatching class inherits from unittest.TestCase, the base class 
    for all test cases in the unittest module.
    In the __init__ method, the super().__init__(methodName) is called to initialize the
    base class. 
    The self.sol attribute is created to store an instance of the Solution class, which 
    contains the method to be tested.

    Test Method: test_regular_expression_matching:

    The test_regular_expression_matching method is defined to contain the actual test cases.
    For each test case, the assertEqual method is used to check whether the result of 
    self.sol.regular_expression_matching matches the expected value.

    Test Cases:

    Test Case 1: self.sol.regular_expression_matching(s="aa", p="a")
        Description: Checks if the regular expression matching method returns False when the input string s is "aa" and the pattern p is "a".
        Expected Result: False (because the pattern "a" does not match the string "aa" without any repetition).

    Test Case 2: self.sol.regular_expression_matching(s="aa", p="a*")
        Description: Checks if the regular expression matching method returns True when the input string s is "aa" and the pattern p is "a*".
        Expected Result: True (because the pattern "a*" allows zero or more occurrences of "a", and it matches the string "aa").

    Test Case 3: self.sol.regular_expression_matching(s="ab", p=".*")
        Description: Checks if the regular expression matching method returns True when the input string s is "ab" and the pattern p is ".*".
        Expected Result: True (because the pattern ".*" allows any character (.) repeated zero or more times, and it matches the string "ab").

Complexity 
----------
Let's analyze the time and space complexity of the given algorithm for regular expression matching.
Time Complexity:

Time & Space Complexity before memoization
-----------------------------------------
Before applying memoization, the time and space complexity of the regular expression matching algorithm is exponential, particularly in the case of patterns with '' (Kleene star) quantifiers. This is because the algorithm explores all possible combinations of matching or not matching characters when encountering '' in the pattern.
Time Complexity (Without Memoization):

In the worst case, the recursion tree can have an exponential number of nodes, where each node corresponds to a recursive call exploring different possibilities. The time complexity without memoization is O(2^(n+m)), where n is the length of the input string and m is the length of the pattern.
Space Complexity (Without Memoization):

The space complexity without memoization is determined by the maximum depth of the recursion stack. In the worst case, the recursion stack depth can be exponential, leading to a space complexity of O(2^(n+m)).
Summary (Without Memoization):

    Time Complexity: O(2^(n+m))
    Space Complexity: O(2^(n+m))

The use of memoization significantly improves the algorithm's efficiency by avoiding redundant computations and reduces the time and space complexity to O(n * m) with respect to the number of unique subproblems. This makes the algorithm much more practical and efficient for real-world use cases.

Time & Space Complexity after memoization
----------------------------------------

The time complexity of this algorithm depends on the number of subproblems that need to be solved. Let's denote the lengths of the input string s and the pattern p as n and m, respectively.

The algorithm uses memoization to avoid redundant computations. In the worst case, each subproblem (combination of indices i and j) is solved once, and the result is stored in the cache dictionary. Therefore, the time complexity is O(n * m), where n is the length of the input string, and m is the length of the pattern.
Space Complexity:

The space complexity is determined by the space used for memoization (the cache dictionary) and the depth of the recursion stack.

    Memoization (Cache):
        In the worst case, the cache dictionary stores the results of all possible subproblems, leading to a space complexity of O(n * m).

    Recursion Stack:
        The depth of the recursion stack is determined by the length of the pattern p. In the worst case, the recursion depth is O(m), where m is the length of the pattern.

Combining both aspects, the overall space complexity is O(n * m + m) = O(n * m).
Summary:

    Time Complexity: O(n * m)
    Space Complexity: O(n * m)

It's worth noting that the use of memoization significantly improves the algorithm's efficiency by 
avoiding redundant computations. However, the worst-case time and space complexity is still influenced
by the number of subproblems, which is proportional to the product of the lengths of the input string 
and pattern.
        
Running the Tests:
-----------------

The if __name__=='__main__': unittest.main() block at the end runs the tests when the script 
is executed.

To run these tests, execute the script. If the actual results match the expected results 
for all test cases, the tests pass. If any assertion fails, the testing framework will 
raise an exception, indicating a failure in the code being tested.
This approach helps ensure that the regular_expression_matching method behaves as expected
for the given test cases.

Are these tests extensive enough? How would you write better tests?
------------------------------------------------------------------
The provided test cases cover basic scenarios for regular expression matching, but they 
could be enhanced to provide more comprehensive coverage. 
For example, you might want to include additional cases that explore various aspects of the 
regular expression matching algorithm. 
Here are some suggestions for enhancing the test coverage:


    Expand Negative Test Cases: Include more negative test cases to ensure that the function correctly identifies non-matching patterns. For instance, test cases with different patterns that should not match the given text strings.

    Handle Edge Cases: Consider edge cases, such as empty strings, single characters, and patterns with multiple wildcards. Test cases should cover these scenarios to ensure that the function handles them correctly.

    Boundary Values: Include test cases that involve boundary values, such as patterns with the maximum number of repetitions allowed for wildcards. This ensures that the function handles repeated patterns correctly.

    Performance Testing: Consider performance testing to evaluate the function's efficiency for larger input strings and complex patterns. This helps identify potential performance bottlenecks.

    Special Characters: Include test cases with special characters, such as punctuation marks, whitespace, and non-ASCII characters. This ensures that the function correctly matches patterns involving these characters.

    Different Pattern Syntax: Test the function with different regular expression syntax variations, such as POSIX Extended Regular Expressions (PCRE) and Perl Compatible Regular Expressions (PCRE). This ensures compatibility with different regex flavors.

    Randomized Testing: Employ randomized testing to generate a wider range of input strings and patterns, covering a broader spectrum of possible scenarios. This helps identify unexpected behavior or edge cases.

By expanding the test cases and incorporating these suggestions, you can create a more 
comprehensive and robust testing suite that thoroughly assesses the regular expression
 matching function's capabilities.
It's essential to cover a diverse set of cases to account for the various features and
edge conditions that the algorithm might encounter in real-world scenarios.

"""
class TestRegularExpressionMatching(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol = Solution()

    def test_regular_expression_matching(self):
        self.assertEqual(False, self.sol.regular_expression_matching(s ="aa", p="a"))
        self.assertEqual(True, self.sol.regular_expression_matching(s ="aa", p="a*"))
        self.assertEqual(True, self.sol.regular_expression_matching(s ="ab", p=".*"))

        # other additional tests
        self.assertEqual(True, self.sol.regular_expression_matching(s="", p=".*"))
        self.assertEqual(True, self.sol.regular_expression_matching(s="xyz", p="x.."))
        self.assertEqual(True, self.sol.regular_expression_matching(s="abc", p="[a-z]"))
        self.assertEqual(False, self.sol.regular_expression_matching(s="abc", p="[a-z"))
        self.assertEqual(True, self.sol.regular_expression_matching(s="aaa", p="a*"))
        self.assertEqual(True, self.sol.regular_expression_matching(s="abc", p="a|b"))
        self.assertEqual(True, self.sol.regular_expression_matching(s="abc", p="a.*c"))

if __name__=='__main__':
    unittest.main()




class Solution:

    def regular_expression_matching_bottom_up(self, s, p):
        dp = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        dp[len(s)][len(p)] = True
        # for i in range(len(p)):
        #     print(dp[i])
        for i in range(len(s)-1, -1, -1):
            for j in range(len(p)-1, -1, -1):
                # first_match = i < len(s) and (s[i] == p[j] or p[j] == '.')
                # if j < len(p)-1 and p[j+1] == '*':
                #     dp[i][j] = dp[i][j + 2] or (first_match and dp[i + 1][j])
                # else:
                #     dp[i][j] = first_match and dp[i+1][j+1]
                match = i < len(s) and (s[i] == p[j] or p[j] ==".")
                if (j + 1) < len(p) and p[j + 1] == "*":
                    # choosing to include * or not to include
                    dp[i][j] = dp[i][j+ 2] or (match and dp[i + 1][j])
                if match:
                    return dp[i + 1][j + 1]
        return dp[0][0]


# class Solution:

#     def regular_expression_matching_bottom_up(self, s: str, p: str) -> bool:
#         # Initialize a 2D table for memoization
#         dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

#         # Base case: an empty pattern matches an empty string
#         dp[0][0] = True

#         # Handle patterns with '*' at the beginning
#         for j in range(1, len(p) + 1):
#             if p[j - 1] == '*':
#                 dp[0][j] = dp[0][j - 2]

#         # Populate the table
#         for i in range(1, len(s) + 1):
#             for j in range(1, len(p) + 1):
#                 # Check if current characters match or if pattern has a '.'
#                 match = s[i - 1] == p[j - 1] or p[j - 1] == '.'

#                 if p[j - 1] == '*':
#                     # Handle '*' by considering zero or more occurrences
#                     dp[i][j] = dp[i][j - 2] or (match and dp[i - 1][j])
#                 else:
#                     # Regular character matching
#                     dp[i][j] = match and dp[i - 1][j - 1]

#         # The final result is found in the bottom-right corner
#         return dp[len(s)][len(p)]



    
sol = Solution()

# print(sol.regular_expression_matching_bottom_up("ab", ".*c"))
print("False", sol.regular_expression_matching_bottom_up(s ="aa", p="a"))
print("True", sol.regular_expression_matching_bottom_up(s ="aa", p="a*"))
print("True", sol.regular_expression_matching_bottom_up(s ="ab", p=".*"))
