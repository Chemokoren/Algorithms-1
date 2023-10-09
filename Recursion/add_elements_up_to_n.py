"""
Add the Elements Up to N

Review of how sum_up(4) works
sum_up(4) = 4 + sum_up(3)
sum_up(4) = 4 + 3 + sum_up(2)
sum_up(4) = 4 + 3 + 2 + sum_up(1)
sum_up(4) = 4 + 3 + 2 + 1 + sum_up(0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
sum_up(4) = 4 + 3 + 2 + 1 + 0 # base case is 0
sum_up(4) = 4 + 3 + 2 + 1
sum_up(4) = 4 + 3 + 3
sum_up(4) = 4 + 6
sum_up(4) = 10
"""

def sum_up(n:int) -> int:
    if n <= 0:
        return n
    return n + sum_up(n-1)


print(sum_up(4))

print(" ############################### tail recursive ###############################")

"""
how the execution will look like

sum_up_tail(4) = sum_up_tail(4, 0)
                    = sum_up_tail(3, 4)
                        = sum_up_tail(2, 7)
                            = sum_up_tail(1, 9)
                                = sum_up_tail(0, 10) # 0 is our base case
               = 10



"""

def sum_up_tail_rec(n: int, x: int)->int:
    if n <= 0:
        return x
    else:
        return sum_up_tail_rec(n-1, x +  n)
    
def sum_up_tail(n: int)->int:
    return sum_up_tail_rec(n, 0)

print(sum_up_tail(4))