"""
Longest Palindromic Substring
"""

def longestPalindromicSubstring(string):
    starting_idx = 0
    end_idx = 1
    longest_palindrome =0
    while starting_idx < end_idx:
        new_string =string[starting_idx:end_idx+1]
        if isPalindrome(new_string):
            if len(new_string) >longest_palindrome:
                longest_palindrome=len(new_string)
                end_idx +=1

        else:
            end_idx +=1
    return string[starting_idx:end_idx+1]


def isPalindrome(string):
    starting_idx = 0
    ending_idx =len(string)-1

    while starting_idx <= ending_idx:
        if string[starting_idx] == string[ending_idx]:
            starting_idx +=1
            ending_idx -=1
        else:
            return False
    return True

input_string="abaxyzzyxf"


# O(n^2) time | O(1) space
def longestPalindromicSubstring(string):
    currentLongest =[0,1]
    for i in range(1, len(string)):
        odd = getLongestPalindromeFrom(string, i-1,i+1)
        even = getLongestPalindromeFrom(string, i-1, i)
        longest = max(odd, even, key =lambda x: x[1] - x[0])
        currentLongest =max(longest, currentLongest, key =lambda x: x[1] - x[0])
    return string[currentLongest[0]:currentLongest[1]]

def getLongestPalindromeFrom(string, leftIdx, rightIdx):
    while leftIdx >= 0 and rightIdx < len(string):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -=1
        rightIdx +=1
    return [leftIdx + 1, rightIdx]

print(longestPalindromicSubstring(input_string))