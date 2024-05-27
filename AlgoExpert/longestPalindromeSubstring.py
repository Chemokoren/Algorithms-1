"""
The problem

The problem being solved is finding the longest palindrome substring within a given string. 
A palindrome is a sequence of characters that reads the same forwards and backwards. The task is to 
find the longest such substring within the given string.

For example, in the string "babad", the longest palindrome substring is "bab" or "aba". In "cbbd", 
the longest palindrome substring is "bb".

The solution provided iterates through the string and, for each character, expands around it to find 
the longest palindrome substring centered at that character. It then updates the longest palindrome 
substring found so far and returns it at the end.


The Thought Process

The solution employs an iterative expansion approach to find the longest palindrome substring within the given string. Here's the thought process behind the 
solution:

    Iterative Expansion Approach:
        The algorithm iterates through each character of the string. For each character, it tries to 
        expand around it to find the longest palindrome substring centered at that character.
        This expansion process considers both odd-length and even-length palindromes.
    Finding Palindromes:
        For each character, the algorithm expands outward to the left and right, comparing characters
        at each step. If the characters are equal, it means they contribute to forming a palindrome.
        The expansion continues until the characters are no longer equal, marking the end of the 
        palindrome.
    Updating Longest Palindrome Substring:
        During the expansion process, the algorithm keeps track of the longest palindrome substring 
        found so far. 
        It compares the length of the current palindrome substring with the length of the longest one
        found previously, updating it if necessary.
    Returning the Result:
        After iterating through all characters, the algorithm returns the longest palindrome substring
        found.

This approach ensures that every possible palindrome substring centered at each character is 
considered, allowing the algorithm to find the longest palindrome substring efficiently. 
By expanding around each character, it avoids the need to check all possible substrings separately, 
leading to a more optimal solution.

Complexity Analysis

Let's analyze the time and space complexity of the provided solution:
Time Complexity Analysis:

    Iterative Expansion:
        For each character in the string, the algorithm expands outward to the left and right to find 
        palindrome substrings. In the worst case, the expansion for each character may take O(n) time,
        where nn is the length of the string.
        Since there are n characters in the string, the overall time complexity for finding 
        palindromes is O(n^2).

        Considering other operations such as comparisons, updating the longest palindrome substring, 
        and building the final result, they all take constant time or linear time relative to the 
        input size.
        Therefore, the overall time complexity of the solution is O(n^2).

Space Complexity Analysis:

    Memory for Storing Indices:
        The algorithm uses a constant amount of extra memory to store indices and other variables such 
        as currentLongest.
        The space required for these variables is independent of the input size and can be considered 
        O(1).

"""


# O(n^2) time | O(1) space
def longest_palindrome_substring(string):
    """
    Finds the longest palindrome substring in the given string.

    Args:
    string (str): The input string.

    Returns:
    str: The longest palindrome substring found in the input string.
    """
    # Initialize the current longest palindrome substring as the first character.
    currentLongest = [0, 1]

    # Iterate through the string to find the longest palindrome substring.
    for i in range(1, len(string)):
        # Get the longest palindrome substring considering the current character as the center
        # for both odd and even length palindromes.
        odd = get_longest_palindrome_from(string, i - 1, i + 1)
        even = get_longest_palindrome_from(string, i - 1, i)
        
        # Choose the longest palindrome substring among the odd and even length palindromes.
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        
        # Update the current longest palindrome substring.
        currentLongest = max(longest, currentLongest, key=lambda x: x[1] - x[0])
    
    # Return the longest palindrome substring found.
    return string[currentLongest[0]:currentLongest[1]]

def get_longest_palindrome_from(string, leftIdx, rightIdx):
    """
    Finds the longest palindrome substring starting from the given left and right indices.

    Args:
        string (str): The input string.
        leftIdx (int): The left index to start expanding the palindrome substring.
        rightIdx (int): The right index to start expanding the palindrome substring.

    Returns:
        list: A list containing the start and end indices of the longest palindrome substring found.
    """
    # Expand the palindrome substring as long as characters at leftIdx and rightIdx are equal.
    while leftIdx >= 0 and rightIdx < len(string):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1
        rightIdx += 1
    
    # Return the indices of the longest palindrome substring found.
    return [leftIdx + 1, rightIdx]







my_string ="abaxyzzyxf"
print(longest_palindrome_substring(my_string))


"""
Unit Tests

These tests cover various scenarios including:

    Strings with odd and even length palindromes.
    Single character strings.
    Empty strings.
    Strings with no palindromes.
    Strings with all characters the same.
    Strings with multiple palindromes.
    Edge cases like "racecar" and "abacdfgdcaba".

These tests help ensure that the algorithm behaves correctly under different conditions and provides robustness to the solution.

"""
import unittest

class TestLongestPalindromeSubstring(unittest.TestCase):
    
    def test_longest_palindrome_substring(self):
        # Test cases with various inputs
        self.assertIn(longest_palindrome_substring("babad"), ["bab", "aba"])
        self.assertEqual(longest_palindrome_substring("cbbd"), "bb")
        self.assertEqual(longest_palindrome_substring("a"), "a")
        self.assertIn(longest_palindrome_substring("ac"), ["a", "c"])
        self.assertEqual(longest_palindrome_substring("racecar"), "racecar")
        self.assertIn(longest_palindrome_substring("abcde"), ["a","b","c","d","e"])
        self.assertEqual(longest_palindrome_substring(""), "")
        self.assertEqual(longest_palindrome_substring("abb"), "bb")
        self.assertEqual(longest_palindrome_substring("aaaa"), "aaaa")
        self.assertEqual(longest_palindrome_substring("abcda"), "a")
        self.assertEqual(longest_palindrome_substring("abacdfgdcaba"), "aba")
        
if __name__ == '__main__':
    unittest.main()

 
