"""
Find position of rightmost Reset Bit | Find Right Most RESET BIT of a number | Find first Reset Bit
- Find Position of First 0 (Reset Bit) from right side
"""
def firstResetBitFromRightSide(num):
    position = 0
    while(num & 1 == 1):
        num = num >> 1
        position += 1
    return position

print(firstResetBitFromRightSide(175))
print(firstResetBitFromRightSide(12375))
print(firstResetBitFromRightSide(127))


print("################ second approach ################")
# second approach: considers the count of No. of bits to represent num
def firstResetBitFromRightSideTwo(num):
    position = 0
    numberOfBits = countBits(num)
    while(num & 1 == 1):
        num = num >> 1
        position += 1
    if(position == numberOfBits):
        return -1
    return position

def countBits(num):
    count = 0
    while(num > 0):
        num = num >> 1
        count +=1
    return count

print(firstResetBitFromRightSideTwo(175))
print(firstResetBitFromRightSideTwo(12375))
print(firstResetBitFromRightSideTwo(127))

