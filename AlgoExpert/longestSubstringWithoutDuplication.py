"""
Conceptual Overview:

The goal of this problem is to find the longest substring in a given string without repeating characters. In other words, we want to identify the maximum length substring where each character appears only once.
Approach to Solving the Problem:

    Sliding Window Technique:
        Use a sliding window approach to keep track of the current substring without duplication.
        Maintain two pointers, startIdx and i, to represent the start and end of the current substring.

    Hash Map (lastSeen):
        Utilize a hash map (lastSeen) to store the index of the last seen occurrence of each character.

    Iterate Through the String:
        Iterate through each character in the string.
        If the character is already in lastSeen, update startIdx to be the maximum of its current value and the next index.
        Check if the length of the current substring is longer than the longest found so far. If yes, update the longest substring.

    Return the Result:
        Return the longest substring found.

        Code Overview:

    lastSeen Dictionary:
        Keeps track of the last seen index of each character to avoid repetition.

    longest List:
        Stores the start and end indices of the longest substring found.

    startIdx Variable:
        Represents the start index of the current substring without repetition.

    Main Loop:
        Iterates through each character in the string.
        Updates startIdx to avoid repetition.
        Checks and updates the longest substring if needed.
        Updates lastSeen with the current index of the character.

    Result:
        Returns the longest substring found in the given string.


        This solution efficiently finds the longest substring without repeating characters using a sliding window approach with constant space complexity. The hash map helps optimize the process of checking for repeated characters
"""

# O(n) time | O(n, a) space -a is length of alphabet represented by the input string
def longest_substring_without_duplication(string):
    """
    Find the longest substring without repeating characters in a given string.
    
    Parameters:
    - string (str): The input string.

    Returns:
    - str: The longest substring without repeating characters.
    
    """
    # Dictionary to store the index of the last seen occurrence of each character
    lastSeen = {}
    # List to store the start and end indices of the longest substring
    longest = [0, 1]
    # Variable to track the start index of the current substring
    startIdx = 0
    
    # Iterate through each character and its index in the string
    for i, char in enumerate(string):
        # Update start index if the character is already seen, ensuring no repetition
        startIdx = max(startIdx, lastSeen.get(char, -1) + 1)
        
        # Check if the current substring is longer than the longest found so far
        if longest[1] - longest[0] < i + 1 - startIdx:
            longest = [startIdx, i + 1]
        
        # Update the last seen index of the current character
        lastSeen[char] = i
    
    # Return the longest substring found
    return string[longest[0]:longest[1]]
    

print(longest_substring_without_duplication("clementisa cap"))
