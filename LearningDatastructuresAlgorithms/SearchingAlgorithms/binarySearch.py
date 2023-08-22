"""
Iterative Binary Search
"""
def IterativeBinarySearch(nums, val):
    left = 0
    right = len(nums)-1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < val:
            left = mid +1
        elif nums[mid] > val:
            right = mid -1
        elif nums[mid] == val:
            return nums[mid]
    return -1



"""
Recursive Binary Search

"""

def recursiveBinarySearch(nums, left, right, val):

    while(left <= right):
        mid = (left + right) // 2
        if(nums[mid] < val):
            return recursiveBinarySearch(nums, left+1, right, val)
        elif(nums[mid] > val):
            return recursiveBinarySearch(nums, left, right-1, val)
        elif(nums[mid]==val):
            return nums[mid]
    return -1


A =[15, 21, 47, 84, 96 ]
val =21
left = 0
right =len(A)-1
print("recursive binary search: ",recursiveBinarySearch(A,left, right, val))  
print("iterative binary search: ",IterativeBinarySearch(A, val)) 

