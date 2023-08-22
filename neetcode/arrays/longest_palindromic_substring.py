"""
Given a string s, find the longest palindromic substring in s. You may assume that the 
maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba is also a valid answer"

Example 2:

Input: "cbbd"
Output: "bb"

Time complexity of this Brute force solution is: O(n^3)
Because it takes n times to check if a string is a palindrome and we are doing this for
all substrings(n^2)

"""

def longestPalindrome(s: str)->str:
    res =" "
    resLen =0

    for i in range(len(s)):

        # odd length
        l, r =i, i
        while l >=0  and r < len(s) and s[l] == s[r]:
            if(r - l +1) > resLen:
                res=s[l:r+1]
                resLen = r-l +1
            l -=1
            r +=1

        # even length
        l, r = i, i +1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res =s[l:r+1]
                resLen = r -1 +1
            l -= 1
            r += 1
    return res

print("Expected:bab, Actual:", longestPalindrome("babad"))		
print("Expected:bb, Actual:", longestPalindrome("cbbd"))				


	
def is_palindrome(string):
	start = 0
	end =len(string)-1
	
	while start <= end:
		if string[start] == string[end]:
			start +=1
			end -=1
		else:
			return False
	return True

	
print("\n my tests \n")
'''
my tests
'''
def longest_palindromic_substring(string):
	max_palindrome = ""

	
	for i in range(len(string)):
		for j in range(1, len(string)):
			if (is_palindrome(string[i:j])):
				if len(string[i:j]) > len(max_palindrome):
					max_palindrome =string[i:j]
	return max_palindrome
	
	

		
print("Expected:bab, Actual:", longest_palindromic_substring("babad"))		
print("Expected:bb, Actual:", longest_palindromic_substring("cbbd"))				


