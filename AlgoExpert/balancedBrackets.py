# O(1) time | O(n) space
def balancedBracket(string):
    startingBrackets =["[","(","{"]
    closingBrackets =["]",")","}"]
    comparisonBrackets={"]":"[",")":"(","}":"{"}
    stack =[]

    for char in string:
        if char in startingBrackets:
            stack.append(char)
        elif char in closingBrackets:
            if len(stack) == 0:
                return False
            if comparisonBrackets.get(char) ==stack[-1]: # comparisonBrackets.get(char)
                stack.pop()
            else:
                return False
    return len(stack) ==0




my_string ="(([]()()){})"
print(balancedBracket(my_string))
