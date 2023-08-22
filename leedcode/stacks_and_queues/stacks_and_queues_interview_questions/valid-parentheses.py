"""
Valid Parentheses :

Given a string s containing just the characters   '(', ')', '{', '}', '[' and ']',determine 
if the input string is valid.

An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

"""
class Solution:
    def isEqual(self, c1, c2)->bool:
        if(c1 =='(' and c2==')'):
            return True
        if(c1 =='[' and c2==']'):
            return True
        if(c1 =='{' and c2=='}'):
            return True
        return False

    def isValid(self, s:str)->bool:
        st =[]
        for character in s:
            if(len(st) != 0):
                li = st[-1]
                if(self.isEqual(li, character)):
                    st.pop()
                    continue
                st.append(character)
        return len(st) == 0
    
# string ="{[]}" 
string ="([)}"       
sol = Solution()
print(sol.isValid(string))

