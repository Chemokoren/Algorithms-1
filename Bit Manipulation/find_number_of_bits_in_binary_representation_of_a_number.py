"""
Find number of bits in binary representation of a Number | 

Required bits to Represent a Number
"""

def count_bits(num):
    ans = 0
    while(num > 0):
        num = num >> 1
        ans += 1
    return ans

print(count_bits(171))
print(count_bits(1701))
print(bin(1701))