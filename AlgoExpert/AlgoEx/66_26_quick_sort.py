# O(nlog(n)) time | O(log(n)) space
def quickSort(array):
    quickSortHelper(array, 0, len(array) -1)
    return array

def quickSortHelper(array, startIdx, endIdx):
    if startIdx >= endIdx:
        return
    pivotIdx = startIdx
    leftIdx = startIdx + 1
    rightIdx = endIdx

    while rightIdx>= leftIdx:
        if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
            swap(leftIdx, rightIdx, array)
        if array[leftIdx] <=array[pivotIdx]:
            leftIdx +=1
        if array[rightIdx] >=array[pivotIdx]:
            rightIdx -=1
    swap(pivotIdx, rightIdx, array)

    leftSubArrayIsSmaller = rightIdx - 1 - startIdx < endIdx-(rightIdx +1)
    if leftSubArrayIsSmaller:
        quickSortHelper(array, startIdx, rightIdx-1)
        quickSortHelper(array, rightIdx +1, endIdx)
    else:
        quickSortHelper(array, rightIdx +1, endIdx)
        quickSortHelper(array, startIdx, rightIdx-1)

def swap(i, j, array):
    array[i],array[j] = array[j], array[i]


my_array =[8,5,2,9,5,6,3]

print(quickSort(my_array))
