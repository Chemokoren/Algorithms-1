"""
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string

Example 1:

Input: s="abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c"

Example 2:

Input: s ="aaa"
Output: six palindromic strings: "a", "a", "a", "aa", "aa", "aaa"
"""
import unittest

class Solution:

    def is_palindrome(self, s: str)->bool:
        start =0
        end =len(s)-1

        while start < end:
            if s[start] == s[end]:
                start +=1
                end -=1
            else:
                return False
        return True

    def palindromic_substrings(self, s: str)->int:

        count =0
        

        for i in range(len(s)):
            
            end =i
            start =0
            if self.is_palindrome(s[i]):
                count +=1
            
            while start < end:
                if self.is_palindrome(s[start: end+1]):
                    count +=1
                start +=1

        return count
    
    def countSubstrings(self, s: str)-> int:

        res =0

        for i in range(len(s)):
            
            # odd palindromes
            l = r = i
            while l >=0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -=1 # expand leftwards
                r +=1 # expand rightwards

            l =i
            r = i + 1

            while l >=0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -=1 # expand leftwards
                r +=1 # expand rightwards
        return res
    
    def count_substrings_optimized(self, s: str)-> int:

        def is_pali(s, l, r):
            count = 0

            while l >=0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -=1 # expand leftwards
                r +=1 # expand rightwards
            return count
        
        res =0

        for i in range(len(s)):
            
            # odd palindromes
            l = r = i
            res += is_pali(s, i, i)
            # even palindromes
            res += is_pali(s, i, i + 1)

            
        return res

        





class TestPalindromicSubstrings(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol = Solution()

    def test_palindromic_substrings(self):
        self.assertEqual(6, self.sol.palindromic_substrings("aaa"))
        self.assertEqual(3, self.sol.palindromic_substrings("abc"))
        self.assertEqual(4, self.sol.palindromic_substrings("aba"))
        self.assertEqual(7, self.sol.palindromic_substrings("aaab"))

    def test_countSubstrings(self):
        self.assertEqual(6, self.sol.countSubstrings("aaa"))
        self.assertEqual(3, self.sol.countSubstrings("abc"))
        self.assertEqual(4, self.sol.countSubstrings("aba"))
        self.assertEqual(7, self.sol.countSubstrings("aaab"))

    def test_count_substrings_optimized(self):
        self.assertEqual(6, self.sol.count_substrings_optimized("aaa"))
        self.assertEqual(3, self.sol.count_substrings_optimized("abc"))
        self.assertEqual(4, self.sol.count_substrings_optimized("aba"))
        self.assertEqual(7, self.sol.count_substrings_optimized("aaab"))

if __name__=="__main__":
    unittest.main()