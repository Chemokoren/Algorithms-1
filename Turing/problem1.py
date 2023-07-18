"""
Given a string S, return the "reversed" string where all characters thar are not
a letter stay in the same place, and all letters reverse their positions.

Example 1:
Input: "ab-cd"
Output: "dc-ba"

Example 2:
Input: "a-bC-dEf=ghlj!!"
Output: "j-lh-gfE=dCba!!"
"""
def reversed_string(s):
    new_list =list(s)

    left =0
    right= len(new_list)-1

    while left < right:
        if new_list[left].isalpha() and new_list[right].isalpha():
            new_list[left], new_list[right] =new_list[right], new_list[left]
            left +=1
            right -=1
        elif not new_list[left].isalpha():
            left +=1

        elif not new_list[right].isalpha():
            right -=1

    return ''.join(new_list)

print(reversed_string("ab-cd"))
print(reversed_string("a-bC-dEf=ghlj!!"))