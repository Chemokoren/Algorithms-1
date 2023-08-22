"""
Example 1:
input: nums =[1,2,3,4,5,6,7], k= 3
Output: [4,5,6,7,1,2,3]

Explanation:
rotate 1 steps to the left:[2,3,4,5,6,7,1]
rotate 2 steps to the left: [3,4,5,6,7,1,2]
rotate 3 steps to the left: [4,5,6,7,1,2,3]

Example 2:
input: [-1, -100, 3, 99], k=2
output: [3,99,-1,-100]

Explanation
rotate 1 steps to the left:[-100,3,99,-1]
rotate 1 steps to the left:[3,99,-1,-100]

"""

''' approach 1 '''
# time complexity O(n)
def left_rotate_array(arr,k=3):
    for i in range(k):
        temp=arr[0]
        for i in range(len(arr)-1):
            arr[i] =arr[i+1]
        arr[len(arr)-1] =temp

nums =[1,2,3,4,5,6,7]
print("before:", nums)
left_rotate_array(nums)
print("before:", nums)


''' approach 2  -Reversal Algorithm for array rotation '''
# arr - array, k - is the rotation factor
print(" aproach 2")
def left_rotate_array_2(arr,k):
    left_rotate_helper(arr, 0, len(arr)-1)
    left_rotate_helper(arr, 0, k)
    left_rotate_helper(arr, k+1, len(arr)-1)
    return arr

def left_rotate_helper(arr, start, end):
    while start< end:
        arr[start], arr[end] =arr[end], arr[start]
        start +=1
        end -=1
    return arr

nums,k =[1,2,3,4,5,6,7],3

print(left_rotate_array_2(nums,k))

print(" ####################### reverse algorithm ###################### ")
# reversal algorithm
# A = n-k
# B = k
def reversal_algo(arr,k):
    n =len(arr)
    A = n-k
    B = k
    reversal_helper(arr,0,A-1)
    reversal_helper(arr,A,n-1)
    reversal_helper(arr,0,n-1)
    return arr

def reversal_helper(arr, start, end):
    while start < end:
        arr[start], arr[end]= arr[end], arr[start]
        start += 1
        end -=1
    return arr



arr =['a','b','c','d','e','f','g']
n =len(arr)
k =2
print(reversal_algo(arr,k))