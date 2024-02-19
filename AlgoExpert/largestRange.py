"""
Largest Range
Find the largest range of numbers contained in this array wherethe range of numbers is a set of 
numbers that come after one another in the set of real integers for instance the range from
2-5 consists of numbers 2,3,4,5

A range does not necessarily need to have all the numbers next to each other in the array. It's
just that the numbers need to be contained somewhere in the array.

Given the array, [1,11,3,0,15,5,2,4,10,7,12,6], here are the sample ranges we can create.
1) [0,1,2,3,4,5,6,7]
2) [10,11,12]
3) [5]

The thought process
- Iterate through the array once and put everything in the has table with each value initialized to True.
- Go through all the numbers a second time and expanded outwards where necessary and marked them as False.
- We store the range using pointers to the first and last value and the length of the range in a variable
leading to constant space utilization

Time Complexity
- O(N) Because we loop through the array twice in two seperate iterations. In the first iteration,
we map the values as True while adding them to a hashtable.
- In the second iteration, we expanded outwards of the given number while doing constant operations and
marking the value as False.

Space Complexity
- O(N) because we created a hashtable to store every single element in the array.
- We also store the start and end values of the array in constant time and the longest length of
range encountered in constant time.

"""

# O(n) time | O(n) space
def largestRange(array):
    bestRange =[]
    longestLength =0
    nums ={}
    for num in array:
        nums[num] =True
    for num in array:
        if not nums[num]:
            continue
        nums[num] =False
        currentLength =1
        left =num -1
        right =num +1
        while left in nums:
            nums[left] =False
            currentLength += 1
            left -=1
        while right in nums:
            nums[right] = False
            currentLength +=1
            right +=1
            if currentLength > longestLength:
                longestLength = currentLength
                bestRange = [left +1, right -1]
    return bestRange

my_range =[1,11,3,0,15,5,2,4,10,7,12,6]
print(largestRange(my_range))

