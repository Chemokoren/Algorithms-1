"""
Find the element that appears once in an array where every other element appears twice

Given an array of integers. All numbers occur twice except one number which occurs once.

Find the the number in O(n) time & constant extra space.

Input:  ar[] = {7, 3, 5, 4, 5, 3, 4}
Output: 7 

One solution is to check every element if it appears once or not. Once an element with a single 
occurrence is found, return it. Time complexity of this solution is O(n^2).

A better solution is to use hashing
1. Traverse all elements and put them in a hash table. Element is used as key and the count of
occurrences is used as the value in the hash table.
2. Traverse the array again and print the element with count 1 in the hash table.
This solution works in O(n) time but requires extra space.

The best solution is to use XOR. XOR of all array elements gives us the number with a single 
occurrence. The idea is based on the following two facts.

1. XOR of a number with itself is 0
2. XOR of a number with 0 is number itself

Let us consider the above example.  
Let ^ be xor operator as in C and C++.

res = 7 ^ 3 ^ 5 ^ 4 ^ 5 ^ 3 ^ 4

Since XOR is associative and commutative, above 
expression can be written as:
res = 7 ^ (3 ^ 3) ^ (4 ^ 4) ^ (5 ^ 5)  
    = 7 ^ 0 ^ 0 ^ 0
    = 7 ^ 0
    = 7 

Time Complexity: O(n)
Auxiliary Space: O(1)
"""
def find_single(ar):

    res =ar[0]

    # Do XOR of all elements and return
    for i in range(1, len(ar)):
        res = res ^ ar[i]
    return res

print("XOR Expected:7, Actual:", find_single([7, 3, 5, 4, 5, 3, 4]))

"""
Another approach
- This is not an efficient approach but just another way to get the desired results. If we add 
each number once and multiply the sum by 2, we will get twice the sum of each element of the array
Then we will subtract the sum of the whole array from the twice_sum and get the required number
(which appears once in the array).

Array[] :[a,a,b,b,c,c,d]
Mathematical Equatio = 2*(a+b+c+d)-(a+a+b+b+c+c+d)

In more simple words: 2 *(sum_of_array_without_duplicates)-(sum_of_array)

let arr[] =[7, 3, 5,4,5,3,4]
Required no = 2 *(sum_of_array_without_duplicates) - (sum_of_array)
            = 2 *(7 +3 +5 + 4) - (7+3+5+4+5+3+4)
            = 2 * 19 - 31
            = 38 - 31
            = 7 (required answer)

As we know that set does not contain any duplicate element we will be using the set here.

Time Complexity: O(nlogn)
Auxiliary Space: O(n)
"""
def  single_number(nums):

    # applying the formula
    return 2 * sum(set(nums)) - sum(nums)

print("Expected:89, Actual:", single_number([15, 18, 16, 18, 16, 15, 89]))
print("Expected:2, Actual:", single_number([2, 3, 5, 4, 5, 3, 4]))


"""

Another approach
- This is an efficient approach for finding the single element in a list of duplicate elements.
In this approach, we are using binary search algorithm to find the single element in the list of
duplicate elements. Before that, we need to make sure if the array is sorted. The first step 
is to sort the array because binary search algorithm wont work if the array is not sorted.
Now let us move to binary search implementation.

There are two halfs that are created by the only single element present in the array which are
left half and right half. Now if there are duplications present in the left half then the 1st 
instance of the duplicate element in the left half is an even index and the 2nd instance is 
an odd index. The opposite of the left half happes in the right half(1st instance is odd index
and the second instance is even index). Now apply binary search algorithm:

1. The solution is to take two indexes of the array(low and high) where low points to 
array-index 0 and high points to array-index(array size-2). We take out the mid index from 
the values by (low+high) /2
2. Now check if the mid index value falls in the left half or the right half. If it falls in 
the left half then we change the low value to mid+1 and if it falls in the right half, then we 
change the high index to mid-1. To check it, we used a logic.
(if(arr[mid]==arr[mid^1]). If mid is an even number then mid^1 will be the next odd index, and if
the codition gets satisfied, then we say that we are in the left index, else we can say we 
are in the right half. But if mid is an odd index, then mid^1 takes us to mid-1 which is the 
previous even index, which gets equal means we are in the right half else left half.
3. This is done because the aim of this implementation is to find the single element in the list
of duplicates. It is only possible if low value is more than high value because at that moment low
will be pointing to the index that contains the single element in the array.
4. After the loop ends, we return the value with low index.

"""
# Time Complexity: O(nlogn) | Auxiliary Space: O(1)

def single_element_two(arr):
    arr.sort()
    n = len(arr)
    low = 0
    high= n-2
    mid = 0
    while(low <= high):
        mid =(low + high) // 2
        if(arr[mid] == arr[mid ^ 1]):
            low = mid + 1
        else:
            high = mid -1
    return arr[low]


print("22 Expected:89, Actual:", single_element_two([15, 18, 16, 18, 16, 15, 89]))
print("22 Expected:2, Actual:", single_element_two([2, 3, 5, 4, 5, 3, 4]))



'''

my tests 

'''
def my_tests(arr):
    dic ={}
    for i in range(len(arr)):
        dic[arr[i]] =dic.get(arr[i], 0) +1

    for key, val in dic.items():
        if val == 1:
            return key
    return -1

print("Expected:7, Actual:", my_tests([7, 3, 5, 4, 5, 3, 4]))



# Time Complexity: O(n) | Auxiliary Space: O(1)
def my_tests_two(arr):

    for i in range(len(arr)):
        if arr.count(arr[i]) ==1:
            return arr[i]

    return -1

print("Expected:7, Actual:", my_tests_two([7, 3, 5, 4, 5, 3, 4]))