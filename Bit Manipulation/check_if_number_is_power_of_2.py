"""
"""

def check_if_power_of_2(num):
    ans =num & num-1
    return True if ans ==0 else False
print(check_if_power_of_2(9))