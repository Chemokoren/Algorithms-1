
# S = "{[()()]}"
S = "([)()]"
def solution(S):

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

print(solution(S))
