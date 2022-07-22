"""
Alternate Sorting

Given an array of integers, print the array in such a way that the first element is first
maximum and second element is first minimum etc.

Input : arr[] = {7, 1, 2, 3, 4, 5, 6}
Output : 7 1 6 2 5 3 4

Input : arr[] = {1, 6, 9, 4, 3, 7, 8, 2}
Output : 9 1 8 2 7 3 6 4

A simple solution is to first print maximum element, then minimum, then second maximum 
etc. Time complexity of this approach is O(n^2)

An efficient solution involves:
1. Sort input array using a O(nLogn) algorithm
2. We maintain two pointers, one from beginning and one from end in sorted array. We 
alternatively print elements pointed by two pointers and move them toward each other

Time Complexity: O(n Log n) 
Auxiliary Space : O(1)

"""

# function to print alternate sorted values
def alternateSort(arr):
    n =len(arr)

    arr.sort()

    # printing the last eleent of array first and then first element and then second last
    # element etc.
    i =0
    j = n-1

    while (i < j):

        print(arr[j], end=" ")
        j -=1
        print(arr[i], end=" ")
        i += 1
    # If the total element in array is odd then print the last middle element
    if(n % 2 != 0):
        print(arr[i])



alternateSort([1, 12, 4, 6, 7, 10])






print("\n my tests \n")

'''
my tests

Time complexity: O(n) if O(max_function is constant) else O(n^2) if O(max) is O(n)
Space complexity: O(n)

'''
def my_tests(arr):
    final_arr =[]
    
    for i in range(len(arr)):

        if(arr and max(arr)):
            final_arr.append(max(arr))
            arr.remove(max(arr))

        if ( arr and min(arr)):
            final_arr.append(min(arr))
            arr.remove(min(arr))
    return final_arr
    

print("Expected:[7,1,6,2,5,3,4],Actual:", my_tests([7, 1, 2, 3, 4, 5, 6]))
print("Expected:[12,1,10,4,7,6],Actual:", my_tests([1, 12, 4, 6, 7, 10]))




def my_tests_two(arr):
    arr.sort()

    final_arr =[]

    start = 0
    end = len(arr)-1

    bool_val =True
    while start <= end:
        if(bool_val):
            final_arr.append(arr[end])
            end -=1
            bool_val=False
        else:
            final_arr.append(arr[start])
            start +=1
            bool_val=True
    
    return final_arr

print("Expected:[7,1,6,2,5,3,4],Actual:", my_tests_two([7, 1, 2, 3, 4, 5, 6]))
print("Expected:[12,1,10,4,7,6],Actual:", my_tests_two([1, 12, 4, 6, 7, 10]))