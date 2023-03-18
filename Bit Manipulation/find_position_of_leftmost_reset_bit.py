"""
Find Position of Leftmost ReSet Bit | Find Left Most RESET BIT of a Number | Find ReSet Bit

- Find position of first 0 (ReSet Bit) From Left Side
"""

def firstResetBitFromLeftSide(num):
    numberOfBits = countBits(num)
    step = numberOfBits - 1
    mask = 1 << step
    while(num & mask > 0):
        step -= 1
        mask = 1 << step
    return step

def countBits(num):
    count =0
    while(num > 0):
        num = num >> 1
        count += 1
    return count

print(firstResetBitFromLeftSide(230))
print(firstResetBitFromLeftSide(23))
print(bin(23))