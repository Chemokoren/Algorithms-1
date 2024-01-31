"""
the stack frame will appear as follows
   e # return true & pop this off
  cec
 aceca
racecar # evaluates to true & we pop it off

"""
def is_palindrome(s):
    start =0
    end =len(s)-1
    if len(s) ==0 or len(s) == 1:
        return True
    elif s[start] == s[end]:
        return is_palindrome(s[start +1:(end-1)+1])
    else:
        return False
print("aaa::", is_palindrome("racecar"))
print("aaa::", is_palindrome("aba"))
print("aaa::", is_palindrome("aa"))