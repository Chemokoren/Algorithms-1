"""
Maximum triplet sum in array

Given an array, the task is to find the maximum trip sum in the array


Input : arr[] = {1, 2, 3, 0, -1, 8, 10} 
Output : 21
10 + 8 + 3 = 21

Input : arr[] = {9, 8, 20, 3, 4, -1, 0}
Output : 37
20 + 9 + 8 = 37

Naive approach: In this method, we smply run three-loop and one by one add three-element and 
compare with the previous sum if the of three-element is greater then store in  the previous sum

"""
# Time complexity: O(n^3) | Space complexity : O(1)
def maximum_triplet_sum_naive(arr):
    max_sum =-float("inf")
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                if (arr[i] + arr[j] + arr[k]) > max_sum:
                    max_sum =(arr[i] + arr[j] + arr[k]) 
    return max_sum


print("Naive Expected: 37, Actual", maximum_triplet_sum_naive([9, 8, 20, 3, 4, -1, 0]))
print("Naive Expected: 21, Actual", maximum_triplet_sum_naive([1, 2, 3, 0, -1, 8, 10]))


"""
Another approach

- In this, we first need to sort the whole array and after that when we add the last three-element
of the array then we find the maximum sum of triplets. 
 
Time complexity: O(nlogn) 
Space complexity: O(1)

Efficient approach

Scan the array and compute the Maximum, second maximum, and third maximum element present in the 
array and return the sum of its and it would be maximum sum.


"""
# Time complexity : O(n) | Space complexity : O(1)
def max_triplet_sum_eff(arr):
    n = len(arr)
    max_a =-float("inf")
    max_b =-float("inf")
    max_c =-float("inf")

    for i in range(0, n):

        # update maximum, second maximum and third maximum element
        if arr[i] > max_a:
            max_c = max_b
            max_b =max_a
            max_a =arr[i]
        # update second maximum and third maximum element
        elif arr[i] >max_b:
            max_c =max_b
            max_b = arr[i]
        # update third maximum element
        elif (arr[i] > max_c):
            max_c = arr[i]
    return (max_a + max_b + max_c)


print("Eff Expected: 37, Actual", max_triplet_sum_eff([9, 8, 20, 3, 4, -1, 0]))
print("Eff Expected: 21, Actual", max_triplet_sum_eff([1, 2, 3, 0, -1, 8, 10]))




'''
my tests
'''


def my_tests(arr):
    arr.sort(reverse=True)
    return sum(arr[0:3])

print("Expected: 37, Actual", my_tests([9, 8, 20, 3, 4, -1, 0]))
print("Expected: 21, Actual", my_tests([1, 2, 3, 0, -1, 8, 10]))

def my_tests_two(arr):
    arr.sort()
    return sum(arr[-3:])

print("Expected: 37, Actual", my_tests_two([9, 8, 20, 3, 4, -1, 0]))
print("Expected: 21, Actual", my_tests_two([1, 2, 3, 0, -1, 8, 10]))

def my_tests_three(arr):
    big, bigger =0,0

    biggest =arr[0]
    for i in range(1,len(arr)):
        
        if arr[i] > biggest:
            if biggest > bigger:
                if bigger > big:
                    big = bigger
                bigger =biggest
            biggest =arr[i]
        else:
            if arr[i] > bigger:
                if bigger > big:
                    big = bigger
                bigger =arr[i]
            else:
                if arr[i] > big:
                    big = arr[i]
            
    return (big + bigger + biggest)

print("Expected: 37, Actual", my_tests_three([9, 8, 20, 3, 4, -1, 0]))
print("Expected: 21, Actual", my_tests_three([1, 2, 3, 0, -1, 8, 10]))