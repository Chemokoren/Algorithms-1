"""
Sort an array of 0s, 1s and 2s | Ductch National Flag problem

Given an array[] consisting only 0s, 1s and 2s. The task is to write a function that sorts the
given array. The functions should put all 0s first, then all 1s and all 1s in last.

This problem is also the same as the famous "Dutch National Flag problem". The problem was proposed
by Edsger Dijkstra. The problem is as follows:

- Given N balls of colour red, white or blue arranged in a line in random order. You have to 
arrange all the balls such that the balls with the same colours are adjacent with the order of
the balls, with the order of colours being red, white and blue(i.e., all red coloured balls come
first then white coloured balls and then blue coloured balls).

nput: {0, 1, 2, 0, 1, 2}
Output: {0, 0, 1, 1, 2, 2}

Input: {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1}
Output: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2}

Approach

- The problem was posed with three colors, '0', '1', '2'. The array is divided into four sections
    a[1..Lo-1] zeroes (red)
    a[Lo..Mid-1] ones (white)
    a[Mid..Hi] unknown
    a[Hi+1..N] twos (blue)
    If the ith element is 0 then swap the element to the low range, thus shrinking the unknown range.
    Similarly, if the element is 1 then keep it as it is but shrink the unknown range.
    If the element is 2 then swap it with an element in high range.

    Algorithm:
    1. Keep three indices low =1, mid =1, and high =N and there are four ranges, 1 to low(the range
    containing 0), low to mid(tge rabge containing 1), mid to high(the range containing uknown
    elements) and high to N( the range containing 2).
    2. Travere the array from start to end and mid is less than high.(Loop counter is i)
    3. if the element is 0 then swap the element with the element at index low and update 
    low = low + 1 and mid = mid + 1
    4. If the element is 1 then update mid = mid + 1
    5. If the element is 2 then swap the element with the element at index high and update 
    high = high -1 and update i=i-1. As the swapped element is not processed
    6. print the array


"""

# Time Complexity: O(n) | Space complexity : O(1)
def sort012(a):
    arr_size =len(a)

    lo = 0
    hi = arr_size -1
    mid = 0
    while mid <= hi:
        if a[mid] == 0:
            a[lo], a[mid] = a[mid], a[lo]
            lo = lo + 1
            mid = mid + 1
        elif a[mid] == 1:
            mid = mid + 1
        else:
            a[mid], a[hi] = a[hi], a[mid]
            hi = hi -1
    return a

print("Expected:, Actual:", sort012([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]))

"""
Method 2

-Count the number of 0s, 1s and 2s in the given array. Then store all the 0s in the beginning
followed by all the 1s then all the 2s.

    Algorithm: 
        - Keep three counter c0 to count 0s, c1 to count 1s and c2 to count 2s
        - Traverse through the array and increase the count of c0 if the element is 0,increase 
        the count of c1 if the element is 1 and increase the count of c2 if the element is 2
        - Now again traverse the array and replace first c0 elements with 0, next c1 elements 
        with 1 and next c2 elements with 2.
"""

# Time Complexity: O(n)| Space Complexity : O(1)
def sortArr(arr):
    cnt0 = 0
    cnt1 = 0
    cnt2 = 0

    n = len(arr)

    for i in range(n):
        if arr[i] == 0:
            cnt0 +=1
        elif arr[i] == 1:
            cnt1 +=1
        elif arr[i] ==2:
            cnt2 +=1
    
    # update the array
    i = 0

    # store all the 0s in the beginning
    while (cnt0 > 0):
        arr[i] = 0
        i +=1
        cnt0 -=1
    # store all the 1s
    while(cnt1 > 0):
        arr[i] = 1
        i +=1
        cnt1 -=1

    # store all the 1s
    while(cnt2 > 0):
        arr[i] = 2
        i +=1
        cnt2 -=1
    return arr

print("sortArr Expected:[0, 0, 1, 1, 2, 2], Actual:",sortArr([0, 1, 2, 0, 1, 2]))
print("sortArr Expected:[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2], Actual:",sortArr([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]))








'''
my tests
'''

# time complexity : O(n), space complexity: O(n)
def my_tests(arr):
    res =[]
    for i in range(len(arr)):
        if(arr[i] ==0):
            res.append(arr[i])
    
    for i in range(len(arr)):
        if arr[i] ==1:
            res.append(arr[i])

    for i in range(len(arr)):
        if arr[i] ==2:
            res.append(arr[i])

    return res


print("Expected:[0, 0, 1, 1, 2, 2], Actual:",my_tests([0, 1, 2, 0, 1, 2]))
print("Expected:[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2], Actual:",my_tests([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]))

def my_tests_two(arr):
    res =[]
    for i in arr:
        if(i ==0):
            res.append(i)
            arr.remove(i)
    
    for i in arr:
        if i ==1:
            res.append(i)
            arr.remove(i)
    res.extend(arr)

    return res



# print("Expected:[0, 0, 1, 1, 2, 2], Actual:",my_tests_two([0, 1, 2, 0, 1, 2]))
print("Expected:[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2], Actual:",my_tests_two([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]))