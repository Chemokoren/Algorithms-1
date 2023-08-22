"""
Unique Number (2*N + 1) - All occurs twice except one number
This is the best use of XOR Bitwise Operator(^)

Quiz: Find the element that appears once, every other element appears twice.
"""

def uniqueNumber(x):
    ans = 0
    for num in x:
        # print("aa:",ans,":",num,"=",ans ^ num)
        ans = ans ^ num
    return ans

duplicate_list_1=[-1,0,1,9,-2,11,0,1,-2,9,11]
duplicate_list_2=[-1,0,1,9,-2,11,-1,1,-2,9,11]
duplicate_list_3=[-1,0,1,9,-2,11,0,-1,-2,1,11]

print("list 1:",uniqueNumber(duplicate_list_1))
print("list 2:",uniqueNumber(duplicate_list_2))
print("list 3:",uniqueNumber(duplicate_list_3))