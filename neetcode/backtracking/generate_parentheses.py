"""
Given an integer 'n'. Print all the possible pairs of 'n' balanced parentheses. The ouput 
strings should be printed in the sorted order considering '(' has higher value than ')'.

Input Format:
Single line containing an integral value 'n'

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