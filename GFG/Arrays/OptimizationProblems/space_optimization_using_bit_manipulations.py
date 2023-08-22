"""
Space optimization using bit manipulations

There are many situtations where we use integer values as index in array to see presence
or absence, we can use bit manipulations to optimze space in such problems.

Example:
Given two numbers say a and b, mark the multiples of 2 and 5 between a and b using less 
than O(|b-1|) space ad output each of the multiples.

Note:
- We have to mark the multiples i.e. save(key, value) pairs in memory such that each key
either have values as 1 or 0 representing as multiple of 2 or 5 or not respectively.

Input : 2 10
Output : 2 4 5 6 8 10

Input: 60 95
Output: 60 62 64 65 66 68 70 72 74 75 76 78 
        80 82 84 85 86 88 90 92 94 95

Simple Approach
- Hash the indices in an array from a to b and mark each of the indices as 1 or 0.
Space complexity: O(max(a,b))

indices from a to b
0   0   1   0   1   1   1   0   1   0   1

0   1   2   3   4   5   6   7   8   9   10

Approach 2: Better than the simple approach
-------------------------------------------

-Save memory, by translating a to 0th index and b to (b-a)th index
Space complexity: O(|b-1|)

Indices from 0 to b-a

1   0   1   0   1   0   1   0   1

0   1   2   3   4   5   6   7   8

# Simply hash |b-1| positions of an array as 0 and 1

"""

# program to mark numbers as multiples of 2 or 5

import math

a =2
b =10
size = abs(b-a)+1
array =[0] * size

# Iterate through a to b, if it is a multiple of 2 or 5 Mark index in array as 1
for i in range(a, b+1):
    if(i % 2 == 0 or i % 5 == 0):
        array[i -a ] = 1

print("MULTIPLES OF 2 and 5:")
for i in range(a,b+1):
    if(array[i-a] == 1):
        print(i, end=" ")




print('\n my tests \n')


def my_tests(a, b, two, five):
    final_arr =[]


    for i in range(a, b+1):
        
        if((i % two == 0) or (i % five == 0) ):
            
            final_arr.append(i)

    return final_arr

print("Expected:[2,4,5,6,8,10], Actual:", my_tests(2, 10, 2, 5))
print("Expected:[60,62,64,65,66,68,70,72,74,75,76,78,80,82,84,85,86,88,90,92,94,95], Actual:", my_tests( 60, 95, 2,5))

"""
Approach 3 (Using Bit Manipulations):
-------------------------------------
Here is a space optimized which uses bit manipulation technique that can be appled to
problems mapping binary values in arrays.

Size of int variable in 64-bit compiler is 4 bytes. 1 byte is represented by 8 bit 
positions in memory. So, an integer in memory is represented by 32 bit positions(4 bytes)
these 32 bit positions can be used instead of just one index to hash binary values.

We can implement the above approach for 32-bit integers by following these steps
1. Find the actual index in int[] that needs to be bit manipulated it will be bitwise 
index/32.
2. Find the index of bit in those 32 bits that needs to be turned on it will be bitwise
index % 32. Let's call it X
3. Turn on the bit by doing | (bitwise OR) with (1 << X) (here we turn on the Xth bit 
by bit manipulation)
4. To get the value of a bit at a bitwise index we calculate the same indices and do a 
bitwise & so that if Xth bit is on it will return an integer not equal to 0 which is true
in C++/
5. Now instead of using arithmetic operations, we can use bitwise operations for 
efficiency


"""

# code for marking multiples
import math

# index >> 5 corresponds to dividing index by 32
# index & 31 corresponds to modulo operation of index by 32

# Function to check value of bit position whether it is zero or one
def checkbit(arr, index):
    return array[index >> 5] & (1 << (index & 31))

#Sets value of bit for corresponding index
def setbit(array, index):
    array[index >> 5] |= (1 << (index & 31))

a =2
b =10
size = abs(b - a)

# size that will be used is actual_size/32
# Ceil is used to initialize the array with positive number
size = math.ceil(size / 32)

# Array is dynamically initialized as we are calculating size at run time
array =[0 for i in range(size)]

# Iterate through every index from a to b and call setbit() if it is a multiple of 2 or 5
for i in range(a, b+1):
    if(i % 2 == 0 or i % 5 == 0):
        setbit(array, i-a)

print("MULTIPLES OF 2 AND 5:")
for i in range(a, b+1):
    if(checkbit(array, i-a)):
        print(i, end=" ")

print("")







'''

my tests

'''
def my_tests_two(a, b, two, five):
    final_arr =[]

    while a <= b:
        if((a % two == 0) or (a % five == 0)):
            final_arr.append(a)
        else:
            pass
        a +=1

    return final_arr

print("Expected:[2,4,5,6,8,10], Actual:", my_tests_two(2, 10, 2, 5))
print("Expected:[60,62,64,65,66,68,70,72,74,75,76,78,80,82,84,85,86,88,90,92,94,95], Actual:", my_tests_two( 60, 95, 2,5))
