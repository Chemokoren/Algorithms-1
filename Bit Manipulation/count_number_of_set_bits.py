"""
Count Number of Set Bits | Find Number of Set Bits | Set Bits in a Binary of a Number
- It means finding the number of 1's
2 approaches:
- Using the right shift operator
- & Bitwise Operator
"""
import math
# Method 1: using the right shift operator
def countSetBits(num):
    count = 0
    while(num > 0):
        if (num & 1 > 0):
            count +=1
        num = num >> 1
    return count

print(countSetBits(171))
print(countSetBits(14422))   

# gives the total number of bits in the given number
# - it represents the complexity of the number
print(math.ceil(math.log(171,2))) 
print(math.ceil(math.log(14422,2))) 

# Method 2
print("################# Method 2 #################")
# time complexity: number of set bits
def countSetBitsFaster(num):
    count = 0
    while(num > 0):
        mask = num -1
        num = num & mask
        count += 1
    return count

print(countSetBitsFaster(171))
print(countSetBitsFaster(14422))