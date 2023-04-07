"""
Given an integer 'n'. Print all the possible pairs of 'n' balanced parentheses. 
The ouput strings should be printed in the sorted order considering 
'(' has higher value than ')'.

Input Format:
Single line containing an integral value 'n'

Example 2:
Input: n=1 
Output: ["()"]

- 3 open, 3 close
- only add close parentheses if close < open

                                    /          \
                                [((]            [()]
                               /   \               \
                            [(((]   [(()]            [()(]
                            /      /     \           /    \
                        [((()]  [(()(]    [(())]    [()((] [()()]
                        /         |          |         |      |
                    [((())]      [(()()]   [(())(]  [()(()] [()()(]
                   /              |          |         |       |
                [((()))]         [(()())]  [(())()] [()(())] [()()()]

"""
def genParenthesis(openB, closeB,n, s=[]):

    # base case
    if(closeB == n):
        print(''.join(s))
        return
    else:
        if(openB>closeB):
            # you can definitely put one closing bracket
            s.append(')')
            genParenthesis(openB, closeB+1, n, s)
            s.pop()
        if(openB < n):
            s.append('(')
            genParenthesis(openB+1, closeB, n, s)
            s.pop()
    return 

print(genParenthesis(0,0,3))

print("########################################")

from typing import List
class Solution:
    
    def generateParenthesis(self, n:int)-> List[str]:
        
        # only add open parenthesis if open < n
        # only add a closing paranthesis if closed < open
        # valid IIF open == closed == n
        
        stack = []
        res   = []
        
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
                
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN+1)
                stack.pop()
        backtrack(0, 0)
        return res    
    
    
sol = Solution()
print(sol.generateParenthesis(3))