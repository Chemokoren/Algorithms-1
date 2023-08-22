import string
import substring as substring

"""
A string S consisting of N characters is called properly nested if:

S is empty;
S has the form "(U)" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, string "(()(())())" is properly nested but string "())" isn't.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.

For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..1,000,000];
string S consists only of the characters "(" and/or ")".
"""

#solution 1
def solution1(S):
    if len(S) % 2 != 0:
        return 0
    str_count1 = S.count('(')
    str_count11 = S.count('((')
    str_count2 = S.count(')')
    str_count22 = S.count('))')
    if str_count1 == str_count2 or str_count11==str_count22:
        return 1
    return 0

#solution 2
def solution2(S):

    matches, stack = dict(['()', '[]', '{}']), []

    for i in S:
        if i in matches.values():
            if stack and matches[stack[-1]] == i:
                stack.pop()
            else:
                return 0
        else:
            stack.append(i)

    return int(not stack)

#solution 3
def solution3(S):
    stack = []
    for bracket in S:
         # open bracket found push in to stack, used array as stack append item at top
        if bracket == "{" or bracket == "[" or bracket == "(":stack.append(bracket)

        # any closing bracket found and stack is not empty remote item from stack top
        elif bracket == "}" and stack:
            pop_item = stack.pop()
        # check  popped item, if it is not similar( ie. opposite or open) as bracket then this S can not be balanced
        if pop_item != "{":
            return 0
        elif bracket == "]" and stack:
            pop_item = stack.pop()
            if pop_item != "[":
                return 0
            elif bracket == ")" and stack:
                pop_item = stack.pop()
        if pop_item != "(":
            return 0
        else:
             # at any point if neither open nor close operation can be performed, stack is not balanced
            return 0

    print(stack)
    # if stack is empty stack, it is balanced ie. all push and pop operation on S is successful¬.
    if not stack:
        return 1
    # S is not balanced
    return 0


# if __name__ == '__main__':
# # result = solution("{[()()]}")
# result = solution("([)()]")
# print("")
# print("Solution " + str(result))


def solution(S):
    if len(S) == 0:
        return 1

    opening = ["(", "{", "["]
    closing = [")", "}", "]"]
    ls_my_o = []
    for s in S:
        if s in opening:
            ls_my_o.append(s)
        elif s in closing:
            if len(ls_my_o) < 1:
                return 0
            ele = ls_my_o.pop()
            if opening.index(ele) != closing.index(s):
                return 0
    if len(ls_my_o) == 0:
        return 1
    return 0

A ='publecatuons'
print(solution(A))

