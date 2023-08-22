"""
Sort an array containing 1 to n values

You have been given an array which contain 1 to n element, your task is to sort this array
in an efficient way and without replace with 1 to n numbers.


Native approach:
-Sort this array with the use of any type of sorting method. It takes O(n(logn)) minimum
time.

Efficient approach
------------------
- Replace every element with it's position. It takes O(n) efficient time and give you the
sorted array.

Time Complexity: O(n)

Space Complexity: O(1)

"""
# program to sort an array of numbers in range from 1 to n.

def sortit(arr):
    n = len(arr)
    for i in range(n):
        arr[i] = i+1

    return arr
 
# print(sortit([10, 7, 9, 2, 8, 3, 5, 4, 6, 1 ]))

print("Expected:, Actual:[2, 5, 7, 8, 10, 12, 14] ", sortit([14, 12, 7, 2, 10, 5, 8]))











print("\n my tests \n")
'''

my tests

'''

def merge_sort_origi(arr):

    if len(arr) > 1:
        m = len(arr)//2

        left_arr = arr[: m]
        right_arr= arr[m+1:]

       # Sorting the first half
        merge_sort_origi(left_arr)
  
        # Sorting the second half
        merge_sort_origi(right_arr)

        i = 0
        j = 0
        k = 0
        
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k]=left_arr[i]
                i +=1
            else:
                arr[k]=right_arr[j]
                j +=1
            k +=1

        
        while i < len(left_arr):
            arr[k]=left_arr[i]
            i +=1
            k +=1

        while j < len(right_arr):
            arr[k] +=right_arr[j]
            j +=1
            k +=1

        return arr


# def merge(arr1, arr2):

#     i = 0
#     j = 0
#     final_arr=[0] *(len(arr1) +len(arr2))
#     k =0
    
#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] < arr2[j]:
#             final_arr[k]=arr1[i]
#             i +=1
#             k +=1
#         elif (arr2[j] < arr1[i]):
#             final_arr[k]=arr2[j]
#             j +=1
#             k +=1

    
#     while i < len(arr1):
#         final_arr[k]=arr1[i]
#         i +=1
#         k +=1

#     while j < len(arr2):
#         final_arr[k] +=arr1[j]
#         j +=1
#         k +=1

#     return final_arr

print("Expected: [1 2 3 4 5 6 7 8 9 10], Actual:", merge_sort_origi([10, 7, 9, 2, 8, 3, 5, 4, 6, 1]))
print("Expected: [5 6 7 11 12 13], Actual:", merge_sort_origi([12, 11, 13, 5, 6, 7]))
