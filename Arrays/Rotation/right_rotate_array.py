"""
Given an array, rotate the array to the right by k steps where k is non-negative
Example 1:
input: nums =[1,2,3,4,5,6,7], k= 3
Output: [5,6,7,1,2,3,4]

Explanation:
rotate 1 steps to the right:[7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
[-1, -100, 3, 99], k=2

Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

"""

''' approach 1'''
# time complexity O(n)
def rotate_array(arr,k):
    n =len(arr)
    for j in range(k):
        temp = arr[n-1]
        for i in range(n-1, 0, -1):
            arr[i] = arr[i-1]
        arr[0] =temp


# nums, k =[1,2,3,4,5,6,7],3
nums, k =[-1, -100, 3, 99], 2
print("array before:", nums)
rotate_array(nums, k)
print("array after:", nums)

''' approach 2'''
# time complexity O(1)
def rotate_array2(arr,k):
    rotate_helper(arr,0,len(arr)-1)
    rotate_helper(arr,0,k-1)
    rotate_helper(arr,k,len(arr)-1)

def rotate_helper(arr, start, end):
    while start < end:
        arr[start],arr[end] = arr[end],arr[start]
        start +=1
        end -=1
    return arr

nums,k =[1,2,3,4,5,6,7],3
rotate_array2(nums,k)
print(nums)


