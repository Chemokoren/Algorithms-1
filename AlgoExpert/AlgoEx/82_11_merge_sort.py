"""
Merge Sort 
"""

# O(nlog(n)) time | O(nlog(n)) space
def mergeSort(array):
    if len(array) == 1:
        return array
    middleIdx = len(array) // 2
    leftHalf = array[:middleIdx]
    rightHalf=array[middleIdx:]

    return mergeSortedArrays(mergeSort(leftHalf), mergeSort(rightHalf))

def mergeSortedArrays(leftHalf, rightHalf):
    sortedArrays =[None] * (len(leftHalf)+len(rightHalf))
    k = i = j = 0
    while i < len(leftHalf) and j < len(rightHalf):
        if leftHalf[i] < rightHalf[j]:
            sortedArrays[k] =leftHalf[i]
            i +=1
        else:
            sortedArrays[k] =rightHalf[j]
            j += 1
        k += 1
    while i< len(leftHalf):
        sortedArrays[k] = leftHalf[i]
        i += 1
        k += 1

    while j< len(rightHalf):
        sortedArrays[k] = rightHalf[j]
        j += 1
        k += 1
    return sortedArrays


'''
approach 2
'''
# O(nlog(n)) time | O(n) space
def mergeSortTwo(array):
    if len(array) <= 1:
        return array
    auxiliaryArray = array[:]
    mergeSortHelper(array, 0, len(array)-1, auxiliaryArray)
    return array

def mergeSortHelper(mainArray, startIdx, endIdx, auxiliaryArray):
    if startIdx == endIdx:
        return
    middleIdx = (startIdx + endIdx) // 2
    mergeSortHelper(auxiliaryArray, startIdx, middleIdx, mainArray)
    mergeSortHelper(auxiliaryArray, middleIdx +1, endIdx, mainArray)
    doMerge(mainArray, startIdx, middleIdx, endIdx, auxiliaryArray)

def doMerge(mainArray, startIdx, middleIdx, endIdx, auxilliaryArray):
    k = startIdx
    i = startIdx
    j = middleIdx +1
    while i <= middleIdx  and j <= endIdx:
        if auxilliaryArray[i] <= auxilliaryArray[j]:
            mainArray[k] = auxilliaryArray[i]
            i += 1
        else:
            mainArray[k] = auxilliaryArray[j]
            j += 1
        k += 1

    while i <= middleIdx:
        mainArray[k] = auxilliaryArray[i]
        i += 1
        k += 1

    while j <= endIdx:
        mainArray[k] = auxilliaryArray[j]
        j += 1
        k += 1


# driver code

my_array =[8,5,2,9,5,6,3]

print(mergeSortTwo(my_array))