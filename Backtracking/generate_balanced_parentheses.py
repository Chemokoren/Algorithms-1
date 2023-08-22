"""
Generate parentheses
- Given an integer 'n'. Print all the possible pairs of 'n' balanced
parentheses.
The output strings should be printed in the sorted order considering
'(' has higher value than ')'
"""
def genParanthesis(openB, closeB, n, s=[]):
    # Base Case
    if(closeB==n):
        #print(s) # returns a list
        print(''.join(s))
        return
    else:
        if(openB > closeB):
            # you can put one closing bracket
            s.append(')')
            genParanthesis(openB, closeB+1,n,s)
            s.pop() # backtracking
        if(openB < n):
            s.append('(')
            genParanthesis(openB+1,closeB,n, s)
            s.pop() # backtracking
    return

genParanthesis(0,0,3)