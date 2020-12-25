# O(n^2) time | O(1) space
def selectionSort(array):
    currentIdx =0
    while currentIdx < len(array) -1:
        smallestIdx =currentIdx
        for i in range(currentIdx + 1, len(array)):
            if array[smallestIdx] > array[i]:
                smallestIdx =i
            swap(currentIdx, smallestIdx, array)
        return array
def swap(i, j, array):
    array[i], array[j] =array[j], array[i]


my_array = [8,5,2,9,5,6,3]
print(selectionSort(my_array))

print("################### second implementation of selection sort ################")
import sys
A =[64,25,12,22,11]
# Traverse through all array elements
for i in range(len(A)):
    # Find the minimum element in remaining unsorted array
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx =j

        # swap the found minimum element with the first element
        A[i], A[min_idx] =A[min_idx], A[i]

# test code
for i in range(len(A)):
    print("%d" %A[i]),
