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

from cmath import inf
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
    
print(same([1,2,3], [4,1,9]))
print(same([1,2,1], [4,4,1]))

# Refactored O(n) time complexity
def same_opt(arr1, arr2):
	if len(arr1) != len(arr2):
		return False
	for i in range(len(arr1)):
		if (arr1[i] **2) in arr2:
			curr =arr2.index((arr1[i] **2))
			del arr2[curr]
		else:
			return False
	return True

print("::",same_opt([1,2,3], [4,1,9]))
print(":::",same_opt([1,2,3], [1,9])) 
print("Expected: False, Actual:", same_opt([1,2,1], [4,4,1]))

'''
Refactored O(n) time complexity
'''

def same_updated(arr1, arr2):
    if(len(arr1) != len(arr2)):
        return False
    map_1 ={}
    map_2 ={}

    for val in arr1:
        map_1[val] = (map_1[val] if val in map_1 else  0)+1
    
    for val in arr2:
        map_2[val] = (map_2[val] if val in map_2   else  0)+1

    for key in map_1:
    	# checks if the square item is not available in map_2
        if(not key**2 in map_2):
            return False
        # checks if count of items in map_1 is equivalent to corresponding squared item in map_2
        if(map_2[key **2] != map_1[key]):
            return False
    return True

print("Expected: True, Actual:",same_updated([1,2,3], [4,1,9]))
print("Expected: False, Actual:",same_updated([1,2,3], [1,9])) 
print("Expected: False, Actual:", same_updated([1,2,1], [4,4,1]))       
print("Expected: , Actual:",same_updated([1,2,3,2], [4,1,9,4]))
print("Expected: , Actual:",same_updated([1,2,3,2,5], [4,1,9,4,11]))

'''
ANAGRAMS
-Given two strings, write a function to determine if the second string is an anagram of 
the first.
An anagram is a word phrase or name formed by rearranging the letters of another, 
such as cinema, formed from iceman.

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

def anagram(str1, str2):
	list2 =list(str2)
	
	for i in range(len(str1)):
		if str1[i] in list2:
			index =list2.index(str1[i])
			del list2[index]
		else:
			return False
	return True if len(list2)==0 else False

print("Expected::True, Actual::", anagram("cinema", "iceman"))
print("Expected::True, Actual::",anagram('','')) # true
print("Expected::False, Actual::",anagram('aaz','zza')) # false
print("Expected::True, Actual::",anagram('anagram','nagaram')) # true
print("Expected::False, Actual::",anagram('rat','car')) # false
print("Expected::False, Actual::",anagram('awesome','awesom')) # false
print("Expected::True, Actual::",anagram('qwerty','qeywrt')) # true
print("Expected::True, Actual::",anagram('texttwisttime','timetwisttext')) # true


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
-----------------

-Creating pointers or values that correspond to an index or position and move towards 
the beginning, end or middle based on a certain condition

Very efficient for solving problems with minimal space complexity as well

Example:
-------
Write a function called sumZero which accepts a sorted array of integers. The function 
should find the first pair where the sum is 0. 
Return an array that includes both values that sum to zero or undefined if a pair
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
-----------------

- Implement a function called countUniqueValues, which accepts a sorted array, 
and counts the unique values in the array. 
There can be negative numbers in the array, but it will always be sorted.

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

the function uses a two-pointer approach to move all the unique elements of the given
list to the beginning and count their occurrence.

The value of i is incremented by 1 before it is returned because i represents the index 
of the last unique element in the list. Since i is initialized as 0 at the beginning 
of the function, the count of unique values in the list is equal to the
value of i plus 1.

For example, if there are 2 unique elements in the list, i would be equal to 1 after
the swapping process. Therefore, the value of i needs to be incremented by 1 to get 
the count of unique elements in the list, which is equal to 2 in this case.

Hence, adding 1 to the value of i before returning it gives the correct count of 
unique elements in the list.
'''
def countUniqueValuesUpdated(arr):
    if len(arr) ==0:
        return 0
    i =0
    for j in range(1,len(arr)):
        if arr[i] != arr[j]:
            i +=1
            # The swapping process is done to move all the unique values to the beginning 
            # of the list and all the duplicate values to the end of the list
            arr[i], arr[j] =arr[j], arr[i]
    return i +1

print(countUniqueValuesUpdated([1,1,1,1,1,2]))
print(countUniqueValuesUpdated([1,2,3,4,4,4,7,7,12,12,13]))
print(countUniqueValuesUpdated([]))
print(countUniqueValuesUpdated([-2,-1,-1,0,1]))
print(countUniqueValuesUpdated([1,1,2,3,3,4,5,6,6,7]))


def count_unique_values_maps(arr):

	map ={}
	
	for i in range(len(arr)):
		map[arr[i]] =map.get(arr[i], 0)+1
	return len(map)

print("Expected:2, Actual:",count_unique_values_maps([1,1,1,1,1,2])) # 2
print("Expected:7, Actual:",count_unique_values_maps([1,2,3,4,4,4,7,7,12,12,13])) #7
print("Expected:0, Actual:",count_unique_values_maps([])) # 0
print("Expected:4, Actual:",count_unique_values_maps([-2,-1,-1,0,1])) # 4


def count_unique_values_maps_2(arr):
	unique_values = set(arr)
	return len(unique_values)

print("Expected:2, Actual:",count_unique_values_maps_2([1,1,1,1,1,2])) # 2
print("Expected:7, Actual:",count_unique_values_maps_2([1,2,3,4,4,4,7,7,12,12,13])) #7
print("Expected:0, Actual:",count_unique_values_maps_2([])) # 0
print("Expected:4, Actual:",count_unique_values_maps_2([-2,-1,-1,0,1])) # 4
"""
SLIDING WINDOW
--------------

This pattern involves creating a window which can either be an array or number from one 
position to another.
Depending on a certain condition, the window either increases or closes(and a new
window is created)

Very useful for keeping track of a subset of data in an array/string e.t.c.


Example

Write a function called maxSubarraySum which accepts an array of integers and a number
called n. 
The function should calculate the maximum sum of n consecutive elements in the array.

maxSubarraySum([1,2,5,2,8,1,5],2) //10
maxSubarraySum([1,2,5,2,8,1,5],4) //17
maxSubarraySum([4,2,1,6],1) //6
maxSubarraySum([4,2,1,6,2], 4) //13
maxSubarraySum([], 4) //null
"""

def maxSubarraySum(arr,num):
    if(num > len(arr)):
        return None
    max_val =0
    start =0
    end =0
    while end <=len(arr):
        end = start + num
        new_sum =sum(arr[start:end])
        if new_sum > max_val:
            max_val=new_sum
        start +=1
    return max_val
         

print("############### maxSubarraySum ###############")

print("expected: 10 ~ actutal:",maxSubarraySum([1,2,5,2,8,1,5],2)) # 10
print("expected: 17 ~ actutal:",maxSubarraySum([1,2,5,2,8,1,5],4)) # 17
print("expected: 6 ~ actutal:", maxSubarraySum([4,2,1,6],1)) #6
print("expected: 13 ~ actutal:", maxSubarraySum([4,2,1,6,2], 4)) #13
print("expected: None ~ actutal:",maxSubarraySum([], 4)) #null

def maxSubarraySumNaive(arr,num):
    if(num > len(arr)):
        return None

    max_val =0

    for i in range(len(arr)):
        sum_vals =sum(arr[i:i+num])
        if sum_vals > max_val:
            max_val =sum_vals
            
    return max_val

print("############### maxSubarraySum -for loop ###############")

print("expected: 10 ~ actutal:",maxSubarraySumNaive([1,2,5,2,8,1,5],2)) # 10
print("expected: 17 ~ actutal:",maxSubarraySumNaive([1,2,5,2,8,1,5],4)) # 17
print("expected: 6 ~ actutal:", maxSubarraySumNaive([4,2,1,6],1)) #6
print("expected: 13 ~ actutal:", maxSubarraySumNaive([4,2,1,6,2], 4)) #13
print("expected: None ~ actutal:",maxSubarraySumNaive([], 4)) #null

def maxSubArraySum(arr, num):
    if num > len(arr):
        return None
    max =-float('inf')
    for i in range(len(arr)-num +1):
        temp =0
        for j in range(0,num):
            temp += arr[i + j]
        if temp > max:
            max = temp
    return max


print("############### maxSubarraySum Naive solution ###############")

print("expected: 10 ~ actutal:",maxSubArraySum([1,2,5,2,8,1,5],2)) # 10
print("expected: 17 ~ actutal:",maxSubArraySum([1,2,5,2,8,1,5],4)) # 17
print("expected: 6 ~ actutal:", maxSubArraySum([4,2,1,6],1)) #6
print("expected: 13 ~ actutal:", maxSubArraySum([4,2,1,6,2], 4)) #13
print("expected: None ~ actutal:",maxSubArraySum([], 4)) #null


def maxSubarraySum(arr, n):
	start =0
	end   =start+n-1
	max_val =-1
	if len(arr) < n:
		return "range is greater than the array given"
	while end < len(arr):
		new_sum =sum(arr[start:end+1])
		if new_sum >max_val:
			max_val =new_sum
		start +=1
		end +=1
	return max_val if max_val >0 else None
	

print("Expected::10, Actual::", maxSubarraySum([1,2,5,2,8,1,5],2)) #10
print("Expected::17, Actual::", maxSubarraySum([1,2,5,2,8,1,5],4)) #17
print("Expected::6, Actual::", maxSubarraySum([4,2,1,6],1)) #6
print("Expected::13, Actual::", maxSubarraySum([4,2,1,6,2], 4)) #13
print("Expected::None, Actual::", maxSubarraySum([1,3,5], 4)) #null

'''
sliding window

O(N) time complexity

'''
def maxSubarraySumF(arr,num):

    if(len(arr) < num): return None
    maxSum =sum(arr[0:num])

    tempSum = maxSum
    for i in range(num,len(arr)):
        tempSum = tempSum -arr[i-num] +arr[i]
        maxSum =max(maxSum,tempSum)
    return maxSum

print("############### Sliding Window solution ###############")

print("expected: 10 ~ actutal:",maxSubarraySumF([1,2,5,2,8,1,5],2)) # 10
print("expected: 17 ~ actutal:",maxSubarraySumF([1,2,5,2,8,1,5],4)) # 17
print("expected: 6 ~ actutal:", maxSubarraySumF([4,2,1,6],1)) #6
print("expected: 13 ~ actutal:", maxSubarraySumF([4,2,1,6,2], 4)) #13
print("expected: None ~ actutal:",maxSubarraySumF([], 4)) #null


"""
Divide and Conquer

This pattern involves dividing a data set into smaller chunks and then repeating a 
process with a subset of data.
This pattern can tremendously decrease time complexity

Example:

Given a sorted array of integers, write a function called search, that accepts a value 
and returns the index where the value passed to the function is located.
If the value is not found, return -1

search([1,2,3,4,5,6], 4) //3
search([1,2,3,4,5,6], 6) //5
search([1,2,3,4,5,6], 11) //-1

"""

# Linear search

def search(arr, num):
    for i in range(len(arr)):
        if arr[i] ==num:
            return i
    return -1


print("expected value is 3:  actual value is",search([1,2,3,4,5,6], 4))
print("expected value is 5:  actual value is",search([1,2,3,4,5,6], 6))
print("expected value is -1:  actual value is",search([1,2,3,4,5,6], 11))


'''
Binary Search

Log(N) time complexity
'''

def binarySearch(arr, num):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = (start + end) // 2

        if num < arr[mid]:
            end = mid-1
        elif num > arr[mid]:
            start =mid +1
        else:
            return mid
    return -1
    
print("############## binary search ##############")

print("expected value is 3:  actual value is",binarySearch([1,2,3,4,5,6], 4))
print("expected value is 5:  actual value is",binarySearch([1,2,3,4,5,6], 6))
print("expected value is -1:  actual value is",binarySearch([1,2,3,4,5,6], 11))