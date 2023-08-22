"""
Equilibrium index of an array

Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal
to the sum of elements at higher indexes. For example, in an array A:

    Input: A[] = {-7, 1, 5, 2, -4, 3, 0} 
    Output: 3 
    3 is an equilibrium index, because: 
    A[0] + A[1] + A[2] = A[4] + A[5] + A[6]

    Input: A[] = {1, 2, 3} 
    Output: -1 

Write a function int equilibrium(int[] arr, int n);that given a sequence arr[] of size n, returns
an equilibrium index(if any) or -1 if no equilibrium indexes exist.

Method 1: Simple but inefficient
- Use two loops. Outer loop iterates through all the element and inner loop finds out whether the
current index picked by the outer loop is equilibrium index or not. Time complexity of this 
solution is O(n^2).

Time Complexity: O(n^2)

Auxiliary Space: O(1)

"""
# function to find the equilibrium index
def equilibrium(arr):
    leftsum = 0
    rightsum = 0
    n = len(arr)

    # check for indexes one by one until an equilibrium index is found
    for i in range(n):
        leftsum = 0
        rightsum = 0

        # get left sum
        for j in range(i):
            leftsum += arr[j]

        # get right sum
        for j in range(i + 1, n):
            rightsum += arr[j]

        # if leftsum and rightsum are same, then we are done
        if leftsum == rightsum:
            return i
    return -1

print("Expected: 3, Actual:", equilibrium([-7, 1, 5, 2, -4, 3, 0]))

"""

Method 2: Tricky and efficient
The idea is to get the total sum of the array first. Then iterate through the array and keep 
updating the left sum which is initialized as zero. In the loop, we can get the right sum by
subtracting the elements one by one. 

1) Initialize leftsum  as 0
2) Get the total sum of the array as sum
3) Iterate through the array and for each index i, do following.
    a)  Update sum to get the right sum.  
           sum = sum - arr[i] 
       // sum is now right sum
    b) If leftsum is equal to sum, then return current index. 
       // update leftsum for next iteration.
    c) leftsum = leftsum + arr[i]
4) return -1 
// If we come out of loop without returning then
// there is no equilibrium index

Time Complexity: O(n)

Auxiliary Space: O(1)
"""


def equilibrium(arr):
    total_sum =sum(arr)
    left_sum = 0
    for i, num in enumerate(arr):
        # total_sum is now right sum for index i
        total_sum -= num
        if left_sum == total_sum:
            return i
        left_sum += num
        # if no equilibrium index found, then return -1
    return -1

print("EQ Expected:3, Actual:", equilibrium([-7, 1, 5, 2, -4, 3, 0]))
print("EQ Expected:-1, Actual:", equilibrium([1, 2, 3]))

"""
Method 3: This is a quite simple and straightforward method. The idea is to take the prefix sum
of the array twice. Once from the front end of array and another from the back of array.

After taking both prefix sums run a loop and check for some i if both the prefix sum from one
array is equal to prefix sum from the second array then that point can be considered as the
Equilibrium point.

Time Complexity: O(n)

Auxiliary Space : O(n)
"""
# function to find the equilibrium index
def equilibrium_two(arr):
    left_sum =[]
    right_sum =[]

    # Iterate from 0 to len(arr)
    for i in range(len(arr)):

        # if it is not 0
        if(i):
            left_sum.append(left_sum[i-1] + arr[i])
            right_sum.append(right_sum[i-1]+arr[len(arr)-1-i])
        else:
            left_sum.append(arr[i])
            right_sum.append(arr[len(arr)-1])
    # Iterate from 0 to len(arr)
    for i in range(len(arr)):
        if(left_sum[i] == right_sum[len(arr)-1-i]):
            return (i)
    # if no equilibrium index found, then return -1
    return -1

print("EQ2 Expected:3, Actual:", equilibrium_two([-7, 1, 5, 2, -4, 3, 0]))
print("EQ2 Expected:-1, Actual:", equilibrium_two([1, 2, 3]))

"""
Method 4:– Using binary search

    To handle all the testcase, we can use binary search algorithm.

    1.calculate the mid and then create left sum and right sum around mid

    2.if left sum is greater than right sum, move to left until it become equal or less than 
    right sum

    3. else if right sum is greater than left, move right until it become equal or less than left 
    sum.

    4. finally we compare two sums if they are equal we got mid as index else its -1

"""

# Time Complexity: O(n) | Auxiliary Space: O(1)
def find(arr):
    n = len(arr)
    mid = n//2
    left_sum =  0
    right_sum = 0

    # calculation sum to left of mid
    for i in range(mid):
        left_sum += arr[i]

    # calculating sum to right of mid
    for i in range(n-1, mid, -1):
        right_sum += arr[i]

    # if right_sum > left_sum
    if(right_sum > left_sum):

        # we keep moving right until right_sum becomes equal or less than left_sum
        while(right_sum > left_sum and mid < n-1):
            right_sum -= arr[mid + 1]
            left_sum += arr[mid]
            mid += 1
    
    else:
        # we keep moving right until left_sum become equal or less than right_sum
        while(left_sum > right_sum and mid > 0):
            right_sum += arr[mid]
            left_sum -= arr[mid - 1]
            mid -= 1
    # check if both sum become equal
    if(right_sum == left_sum):
        return mid 
    return -1

print("BSQ Expected:, Actual:", find([ 1, 1, 1, -1, 1, 1, 1 ]))

# def binary_search_eq(arr):
#     start =0
#     end =len(arr)-1
    
#     mid =(start+end)//2

#     while start <= end:

#         print("aaaa", sum(arr[:mid+1]),sum(arr[mid:]))
        
#         if sum(arr[:mid+1]) == sum(arr[mid:]):
#             return mid
#         elif sum(arr[:mid+1]) > sum(arr[mid:]):
#             mid -=1
#         elif sum(arr[:mid+1]) < sum(arr[mid:]):
#             mid +=1
#         else:
#             return -1
#     return -1

# # print(" BSQ Expected:3, Actual:", binary_search_eq([-7, 1, 5, 2, -4, 3, 0]))
# print(" BSQ Expected:-1, Actual:", binary_search_eq([1, 2, 3]))



def my_tests(arr):
    start = 0
    end =len(arr)-1
    mid =(start + end) //2

    if sum(arr[:mid]) == sum(arr[mid+1:]):
        return mid
    return -1

print("Expected:3, Actual:", my_tests([-7, 1, 5, 2, -4, 3, 0]))
print("Expected:-1, Actual:", my_tests([1, 2, 3]))