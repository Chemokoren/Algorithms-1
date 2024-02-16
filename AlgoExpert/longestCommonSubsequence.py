"""
Problem case

The problem of finding the longest common subsequence (LCS) between two strings. A subsequence is a
sequence that can be derived from another sequence by deleting some elements without changing the 
order of the remaining elements. 
The LCS is the longest sequence that is common to both input strings.

For example, given two strings "ABCDGH" and "AEDFHR", the LCS is "ADH", as it is the longest sequence that is present in both strings.


    Initialization of LCS Matrix:
        We create a matrix lcs initialized with empty lists to store the LCS at each position.

    Dynamic Programming Loop:
        We iterate through each character of both input strings using nested loops.
        At each position (i, j) in the matrix, we consider the LCS between the prefixes of str1 and str2 up to the current indices i and j.
        If the characters at the current positions match, we extend the LCS by one and store it.
        If the characters don't match, we choose the longest LCS from the adjacent cells (lcs[i - 1][j] and lcs[i][j - 1]).

    Return the LCS:
        Finally, we return the LCS found at the bottom-right corner of the matrix, which represents the LCS of the entire input strings.

Time & Space Complexity

    Time Complexity:
        The time complexity is determined by the nested loops used to fill the LCS matrix.
        The outer loop iterates over the characters of str2, and the inner loop iterates over the characters of str1.
        Inside the loop, each cell of the LCS matrix is computed in constant time.
        Therefore, the time complexity is O(m * n), where m is the length of str2 and n is the length of str1.

    Space Complexity:
        The space complexity is primarily determined by the space required to store the LCS matrix.
        We use a 2D matrix lcs to store the LCS at each position.
        The dimensions of the matrix are (len(str2) + 1) * (len(str1) + 1).
        Therefore, the space complexity is O(m * n), where m is the length of str2 and n is the length of str1.

In summary:

    Time complexity: O(m * n)
    Space complexity: O(m * n)

Where:

    m is the length of str2
    n is the length of str1

"""
# O(nm * min(n, m)) | O(nm * min(n,m))
def longest_common_subsequence(str1, str2):
    """
    Finds the longest common subsequence between two strings using dynamic programming.

    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.

    Returns:
        list: The longest common subsequence as a list of characters.
    """

    # Initialize the LCS matrix with empty lists
    lcs = [[[] for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]

    # Iterate through the characters of the input strings
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            # If the characters match, extend the LCS by one and store it
            if str2[i - 1] == str1[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + [str2[i - 1]]
            else:
                # If the characters don't match, choose the longest LCS from the adjacent cells
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1], key=len)

    # Return the LCS found at the bottom-right corner of the matrix
    return lcs[-1][-1]






"""

Here's the thought process behind the dynamic programming solution:

    Understanding Subproblems and Recurrence Relation:
        We observe that finding the LCS of two strings involves solving smaller subproblems.
        Let's consider two substrings of the input strings: str1 and str2.
        The problem of finding the LCS of str1 and str2 can be broken down into finding the LCS of smaller substrings of str1 and str2.

    Dynamic Programming Approach:
        Dynamic programming is a suitable approach when the problem can be divided into overlapping subproblems and has optimal substructure.
        We can use a two-dimensional array (matrix) to store the solutions to subproblems. This matrix will represent the LCS between different prefixes of the input strings.
        We initialize a matrix lcs with dimensions (len(str2) + 1) * (len(str1) + 1), where lcs[i][j] will represent the LCS between the first i characters of str2 and the first j characters of str1.
        We iterate over each character of both strings and fill the lcs matrix based on certain conditions:
            If the characters match, we increment the length of the LCS by one.
            If the characters don't match, we choose the maximum LCS length from the previous characters in the strings.
        By the end of this process, the bottom-right cell of the matrix will contain the length of the LCS of the entire strings.

    Backtracking to Reconstruct the LCS:
        Once we have filled the lcs matrix, we backtrack from the bottom-right corner to reconstruct the LCS itself.
        We start from the bottom-right corner and move towards the top-left corner of the matrix, following certain rules:
            If the characters at the current position match, we include this character in the LCS and move diagonally up.
            If the characters don't match, we move either up or left based on the value stored in the adjacent cells.
        By following this process, we reconstruct the LCS.

    Return the LCS:
        Finally, we return the reconstructed LCS as the result.

This dynamic programming approach efficiently solves the problem by avoiding redundant computations and provides the length of the LCS as well as the LCS itself.

The time and space complexity of this solution can be analyzed as follows:

    Time Complexity:
        Constructing the LCS matrix requires iterating through each cell of the matrix once. The matrix has dimensions (m+1) * (n+1) where m is the length of str2 and n is the length of str1.
        Therefore, the time complexity of constructing the LCS matrix is O(m * n).

    Space Complexity:
        The space complexity is primarily determined by the space required to store the LCS matrix.
        The LCS matrix has dimensions (m+1) * (n+1), where m is the length of str2 and n is the length of str1.
        Therefore, the space complexity is O(m * n) for the LCS matrix.
        Additionally, the space complexity for storing the longest common subsequence itself is O(k), where k is the length of the LCS.
        Overall, the space complexity is O(m * n + k).

In summary:

    Time complexity: O(m * n)
    Space complexity: O(m * n + k)

Where:

    m is the length of str2
    n is the length of str1
    k is the length of the longest common subsequence.

"""
# O(nm) time | o(nm) space
def longest_common_subsequence1(str1, str2):
    """
    Finds the longest common subsequence between two strings using dynamic programming.

    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.

    Returns:
        list: The longest common subsequence as a list of characters.
    """

    # Initialize the LCS matrix with None values and lengths of 0
    lcs = [[[None, 0, None, None] for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]

    # Iterate through the strings to fill the LCS matrix
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            # If characters match, increment the length of LCS
            if str2[i - 1] == str1[j - 1]:
                lcs[i][j] = [str2[i - 1], lcs[i - 1][j - 1][1] + 1, i - 1, j - 1]
            else:
                # If characters don't match, choose the maximum LCS length
                if lcs[i - 1][j][1] > lcs[i][j - 1][1]:
                    lcs[i][j] = [None, lcs[i - 1][j][1], i - 1, j]
                else:
                    lcs[i][j] = [None, lcs[i][j - 1][1], i, j - 1]

    # Construct and return the longest common subsequence
    return build_sequence(lcs)

def build_sequence(lcs):
    """
    Constructs the longest common subsequence from the LCS matrix.

    Args:
        lcs (list): The LCS matrix.

    Returns:
        list: The longest common subsequence as a list of characters.
    """
    sequence = []
    # Start from the bottom-right corner of the matrix
    i = len(lcs) - 1
    j = len(lcs[0]) - 1
    # Traverse the LCS matrix backwards to reconstruct the LCS
    while i != 0 and j != 0:
        currentEntry = lcs[i][j]
        if currentEntry[0] is not None:
            # Add the character to the sequence
            sequence.append(currentEntry[0])
        # Move to the previous position based on the LCS matrix
        i = currentEntry[2]
        j = currentEntry[3]
    # Reverse the sequence to get the correct order
    return list(reversed(sequence))


string_1 ="zxvvyzw"
string_2 ="xkykzpw"
print(longest_common_subsequence(string_1,string_2))


"""
Unit Tests

These tests cover various cases such as:

    Basic case with simple inputs.
    Case with empty strings.
    Case where there's no common subsequence.
    Case where the strings are identical.
    Case where one of the strings is empty.
    Case with longer strings to test efficiency
"""
import unittest

class TestLongestCommonSubsequence(unittest.TestCase):
    
    def test_basic_case(self):
        # Test with simple inputs
        str1 = "ABCDGH"
        str2 = "AEDFHR"
        expected_lcs = ["A", "D", "H"]
        self.assertEqual(longest_common_subsequence(str1, str2), expected_lcs)

    def test_empty_strings(self):
        # Test with empty strings
        str1 = ""
        str2 = ""
        expected_lcs = []
        self.assertEqual(longest_common_subsequence(str1, str2), expected_lcs)

    def test_no_common_subsequence(self):
        # Test with strings having no common subsequence
        str1 = "ABC"
        str2 = "DEF"
        expected_lcs = []
        self.assertEqual(longest_common_subsequence(str1, str2), expected_lcs)

    def test_identical_strings(self):
        # Test with identical strings
        str1 = "ABCD"
        str2 = "ABCD"
        expected_lcs = list(str1)  # The entire string is the LCS
        self.assertEqual(longest_common_subsequence(str1, str2), expected_lcs)

    def test_one_empty_string(self):
        # Test with one empty string
        str1 = "ABC"
        str2 = ""
        expected_lcs = []
        self.assertEqual(longest_common_subsequence(str1, str2), expected_lcs)

    def test_longer_strings(self):
        # Test with longer strings
        str1 = "XMJYAUZ"
        str2 = "MZJAWXU"
        expected_lcs = ["M", "J", "A", "U"]
        self.assertEqual(longest_common_subsequence(str1, str2), expected_lcs)

if __name__ == '__main__':
    unittest.main()
