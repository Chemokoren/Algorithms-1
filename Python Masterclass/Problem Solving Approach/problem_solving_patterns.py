"""
Problem Solving Patterns (They are programming mechanisms - blueprint)
-Frequency Counter
-Multiple Pointers
-Sliding Window
-Divide and Conquer
-Dynamic Programming
-Greedy Algorithms
-Backtracking

Frequency Counters
- This patterns uses objects or sets to collect values/frequencies of values
- This can often avoid the need for nested loops or O(N^2) operations with arrays/strings

Example
Write a function called same, which accepts two arrays. The function should return true if
every value in the array has it's corresponding value squared in the second array. The 
frequency of values must be the same.

same([1,2,3], [4,1,9]) //true
same([1,2,3], [1,9]) // false
same([1,2,1], [4,4,1]) //false (must be same frequency)

O(n^2) time complexity
"""

from jinja2 import Undefined


def same(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    for i in range(0, len(arr1)):
        
        if arr1[i]**2 in arr2:
            correctIndex = arr2.index(arr1[i]**2)
            if (correctIndex):
                del arr2[correctIndex]
        else:
            return False
    return True
    
# print(same([1,2,3], [4,1,9]))
# print(same([1,2,1], [4,4,1]))

'''
Refactored O(n) time complexity
'''

def sameUpdated(arr1, arr2):
    if(len(arr1) != len(arr2)):
        return False
    frequency_counter1 ={}
    frequency_counter2 ={}

    for val in arr1:
        # if (val in frequency_counter1): 
        #     frequency_counter1[val] += 1
        # else: 
        #     frequency_counter1[val] = 1
        frequency_counter1[val] = (frequency_counter1[val] if val in frequency_counter1 else  0)+1
    
    for val in arr2:
        frequency_counter2[val] = (frequency_counter2[val] if val in frequency_counter2   else  0)+1

    for key in frequency_counter1:
        if(not key**2 in frequency_counter2):
            return False
        if(frequency_counter2[key **2] != frequency_counter1[key]):
            return False
    print(frequency_counter1)
    return True

        
print(sameUpdated([1,2,3,2], [4,1,9,4]))
print(sameUpdated([1,2,3,2,5], [4,1,9,4,11]))

'''
ANAGRAMS
-Given two strings, write a function to determine if the second string is an anagram of the first.
An anagram is a word phrase or name formed by rearranging the letters of another, such as cinema, formed
from iceman.

'''

def validAnagram(str1, str2):
    freq_1 ={}
    freq_2 ={}
    if len(str1) == len(str2) ==0:
        return True

    for i in str1:
        freq_1[i] =(freq_1[i] if i in freq_1 else 0)+1

    for i in str2:
        freq_2[i] =(freq_2[i] if i in freq_2 else 0)+1

    for i in freq_1:
        if(i not in freq_2):
           return False
        if(freq_1[i] !=freq_2[i]):
            return False
    return True

print("########################## anagram ##########################")
# print(validAnagram('','')) # true
# print(validAnagram('aaz','zza')) # false
# print(validAnagram('anagram','nagaram')) # true
# print(validAnagram('rat','car')) # false
# print(validAnagram('awesome','awesom')) # false
# print(validAnagram('qwerty','qeywrt')) # true
# print(validAnagram('texttwisttime','timetwisttext')) # true

def validAnagramUpdated(str1, str2):
    if len(str1) != len(str2):
        return False

    lookup ={}

    for i in str1:
        lookup[i] =(lookup[i] if i in lookup else 0)+1

    for i in range(len(str2)):
        letter =  str2[i]
        # can't find letter or letter is zero then it's not an anagram
        if(not letter in lookup):
            return False
        else:
            lookup[letter] -=1
    return True

print("########################## anagram updated ##########################")
print("empty",validAnagramUpdated('','')) # true
print("aaz",validAnagramUpdated('aaz','zza')) # false
print("anagram",validAnagramUpdated('anagram""','nagaram')) # true
print("rat", validAnagramUpdated('rat','car')) # false
print("awesome",validAnagramUpdated('awesome','awesom')) # false
print("qwerty",validAnagramUpdated('qwerty','qeywrt')) # true
print("texttwisttime",validAnagramUpdated('texttwisttime','timetwisttext')) # true


print("############################## MUTLIPLE POINTERS ##############################")
"""
MUTLIPLE POINTERS

-Creating pointers or values that correspond to an index or position and move towards the beginning,
end or middle based on a certain condition

Very efficient for solving problems with minimal space complexity as well

Example:
Write a function called sumZero which accepts a sorted array of integers. The function should find the first
pair where the sum is 0. Return an array that includes both values that sum to zero or undefined if a pair
does not exist.

sumZero([-3,-2,-1,0,1,2,3]) //[-3,3]
sumZero([-2,0,1,3]) // undefined
sumZero([1,2,3]) // undefined
"""

def sumZero(arr):
    start =0
    end = len(arr)-1

    while start < end:
        sum =arr[start]+arr[end]
            
        if sum < 0:
            start = start + 1
            
        elif sum > 0:
            end = end -1
            
        else:
            return [arr[start], arr[end]]
    return Undefined

print(sumZero([-3,-2,-1,0,1,2,3]))
print(sumZero([-2,0,1,3]))
print(sumZero([1,2,3]))
print(sumZero([-4,-3,-2,-1,0,1,2,5]))
print(sumZero([-4,-3,-2,-1,0,1,2,3,10]))
print(sumZero([-4,-3,-2,-1,0,5,10]))
'''
O(N^2) time complexity
'''
def sumZeroNaive(arr):
    for i in range(len(arr)):
        for j in range(i +1,len(arr)):
            sum =arr[i]+arr[j]
            if sum ==0:
                return [arr[i],arr[j]]
    return Undefined

print("Naive sol::::")
print(sumZeroNaive([-3,-2,-1,0,1,2,3]))
print(sumZeroNaive([-2,0,1,3]))
print(sumZeroNaive([1,2,3]))
print(sumZeroNaive([-4,-3,-2,-1,0,1,2,5]))
print(sumZeroNaive([-4,-3,-2,-1,0,1,2,3,10]))
print(sumZeroNaive([-4,-3,-2,-1,0,5,10]))

print("######################## CountUniqueValues ########################")
"""
CountUniqueValues

- Implement a function called countUniqueValues, which accepts a sorted array, and counts the unique values
in the array. There can be negative numbers in the array, but it will always be sorted.

countUniqueValues([1,1,1,1,1,2]) // 2
countUniqueValues([1,2,3,4,4,4,7,7,12,12,13]) //7
countUniqueValues([]) // 0
countUniqueValues([-2,-1,-1,0,1]) // 4

"""

def countUniqueValues(arr):
    if len(arr)==0:
        return 0
    i =0
    j =1
    while j < len(arr):
        if arr[i]== arr[j]:
            j =j+1
        elif(arr[i] != arr[j]):
            i= i+1
            arr[i],arr[j] =arr[j], arr[i]
            j =j+1
    return i +1

print(countUniqueValues([1,1,1,1,1,2]))
print(countUniqueValues([1,2,3,4,4,4,7,7,12,12,13]))
print(countUniqueValues([]))
print(countUniqueValues([-2,-1,-1,0,1]))
print(countUniqueValues([1,1,2,3,3,4,5,6,6,7]))


print("###########  using for loop ########### ")
'''
using for loop
'''
def countUniqueValuesUpdated(arr):
    if len(arr) ==0:
        return 0
    i =0
    for j in range(1,len(arr)):
        if arr[i] != arr[j]:
            i +=1
            arr[i], arr[j] =arr[j], arr[i]
    return i +1

print(countUniqueValuesUpdated([1,1,1,1,1,2]))
print(countUniqueValuesUpdated([1,2,3,4,4,4,7,7,12,12,13]))
print(countUniqueValuesUpdated([]))
print(countUniqueValuesUpdated([-2,-1,-1,0,1]))
print(countUniqueValuesUpdated([1,1,2,3,3,4,5,6,6,7]))

"""
SLIDING WINDOW

This pattern involves creating a window which can either be an array or number from one position to another
Depending on a certain condition, the window either increases or closes(and a new window is created)

Very useful for keeping track of a subset of data in an array/string e.t.c.


Example

Write a function called maxSubarraySum which accepts an array of integers and a number called n. The 
function should calculate the maximum sum of n consecutive elements in the array.

maxSubarraySum([1,2,5,2,8,1,5],2) //10
maxSubarraySum([1,2,5,2,8,1,5],4) //17
maxSubarraySum([4,2,1,6],1) //6
maxSubarraySum([4,2,1,6,2], 4) //13
maxSubarraySum([], 4) //null
"""