
# S = "{[()()]}"
S = "([)()]"
"""
checks whether it contains a properly nested sequence of brackets.

Here's how the function works:

    The function defines a dictionary matches that maps opening brackets to their corresponding closing 
    brackets, and an empty list stack to keep track of the brackets in the input string.
    The function iterates through each character i in the input string S.
    If i is a closing bracket, the function checks if the last opening bracket in the stack matches i. 
    If it does, the opening bracket is removed from the stack. 
    
    If it doesn't match or the stack is empty, the function returns 0 to indicate that the sequence 
    is not properly nested.
    If i is an opening bracket, it is added to the stack.
    After all characters in S have been processed, the function returns 1 if the stack is empty (which 
    means all opening brackets have been matched with their corresponding closing brackets), or 0 if the
     stack is not empty (which means some opening brackets have not been matched).

The function works correctly for the test cases provided in the code (S = "([)()]" and S = "{[()(}]}"),
 returning 0 for both cases to indicate that the sequences are not properly nested.

However, note that the function assumes that the input string only contains brackets and no other 
characters. If the input string contains other characters, the function may not work as intended.
"""
def solution(S):

    matches, stack = dict(['()', '[]', '{}']), []

    for i in S:
        if i in matches.values():
            if stack and matches[stack[-1]] == i:
                stack.pop()
            else:
                return 0 # False
        else:
            stack.append(i)

    return int(not stack)

print(solution(S))

"""
checks if the brackets are balanced
"""
def solution_updated(s):
    start_br = ["(", "[", "{"]
    end_br = [")", "]", "}"]
    map_br = {"}": "{", ")": "(", "]": "["}
    temp = []
    for i in range(len(s)):
        if (s[i] in start_br):
            temp.append(s[i])
        if (s[i] in end_br and map_br[s[i]] in temp):
            temp.remove(map_br[s[i]])
    return True if len(temp) == 0 else False


# S = "([)()]"
S = "{[()(}]}"
print(solution_updated(S))