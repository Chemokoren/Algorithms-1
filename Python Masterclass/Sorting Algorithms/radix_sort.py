"""
Radix Sort

- Radix sort is a special sorting algorithm that works on lists of numbers
- It never makes comparisons between elements
- It exploits the fact that information about the size of a number is encoded in the number of digits
- More digits means a bigger number

Radix Sort Helpers

- In order to implement radix sort, it's helpful to build a few helper functions first:
- getDigit(num, place) - Returns the digit in num at the given place value

getDigit(12345, 0) # 5
getDigit(12345, 1) # 4
getDigit(12345, 2) # 3
getDigit(12345, 3) # 2
getDigit(12345, 4) # 1
getDigit(12345, 5) # 0

- digitCount(num) - returns the number of digits in num

- mostDigits(nums) - Given an array of numbers, returns the number of digits in the largest numbers in the
list


"""
import math

def getDigit(num, i):
    return math.floor(abs(num) / pow(10,i)) % 10

print(getDigit(12345,0))
print(getDigit(12345, 1)) # 4
print(getDigit(12345, 2)) # 3
print(getDigit(12345, 3)) # 2
print(getDigit(12345, 4)) # 1
print(getDigit(12345, 5)) # 0


def digitCount(num):
    if(num == 0): return 1
    return math.floor(math.log10(abs(num)))+1

print("expected: 1, actual:", digitCount(1))  # 1
print("expected: 2, actual:",digitCount(25)) # 2
print("expected: 3, actual:",digitCount(314))  # 3


def mostDigits(nums):
    maxDigits = 0
    for i in range(0, len(nums)):
        maxDigits = max(maxDigits, digitCount(nums[i]))
    return maxDigits

print("most digits")
print("expected: 4, actual:",mostDigits([1234, 56, 7])) # 4
print("expected: 5, actual:", mostDigits([1,1,11111, 1])) # 5
print("expected: 2, actual:",mostDigits([12, 34,56,78])) # 2

"""
RADIX SORT PSEUDOCODE
- Define a function that accepts list of numbers
- Figure out how many digits the largest number has
- Loop from k=0 up to this largest number of digits
- For each iteration of the loop:
    - create buckets for each digit(0 to 9)
    - Place each number in the corresponding bucket based on its kth digit
- Replace our existing array with values in our buckets, starting with 0 and going up to 9
- Return list at the end!

Radix Sort Big O
Time complexity : O(nk) for Best, Average, & Worst
Space complexity: O(n + k)

 n - length of array
 k - number of digits(average)

 Recap
 - Merge sort and quick sort are standard effcient sorting algorithms
 - Quick sort can be slow in the worst case, but is comparable to merge sort on average
 - Merge sort takes up more memory because it creates a new array(in-place merge sort exists, but
 they are really complex)
 - Radix sort is a fast sorting algorithms for numbers
 - Radix sort exploits place value to sort numbers in linear time(for a fixed number of digits)
"""
import numpy as np

def radixSort(nums):
    maxDigitCount = mostDigits(nums)

    for k in range(0,maxDigitCount):
        digitBuckets =[[] for i in range(10)]
        for i in range(len(nums)):
            print("vvvvvvv:",nums[i], type(nums[i]),"aaa:", getDigit(nums[i],k))
            digit = getDigit(nums[i],k)
            digitBuckets[digit].append(nums[i])
    
    for i in digitBuckets:
        # for j in i:
        print("kkk",type(i), type([]), type(nums))
        nums =np.concatenate([],i)

    print("aaa:", nums)
    

        # nums =[] +(digitBuckets)
        # print("ddd:", nums)
    # return nums
    

print(radixSort([23,345,5467,12,2345,9852]))

# expected results [12, 23,345,2345,5467,9852]