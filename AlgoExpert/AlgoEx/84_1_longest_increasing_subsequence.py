# O(n^2) time | O(n) space
from typing import Sequence


def longestIncreasingSubsequence(array):
    sequences =[None for x in array]
    lengths =[1 for x in array]
    maxLengthIdx = 0
    for i in range(len(array)):
        currentNum = array[i]
        for j in range(0, i):
            otherNum = array[j]
            if otherNum < currentNum and lengths[j] + 1 >= lengths[i]:
                lengths[i] = lengths[j] + 1
                sequences[i] = j

        if lengths[i] >= lengths[maxLengthIdx]:
            maxLengthIdx = i
    return buildSequence(array, sequences, maxLengthIdx)

def buildSequence(array, sequences, currentIdx):
    sequence =[]
    while currentIdx is not None:
        sequence.append(array[currentIdx])
        currentIdx = sequences[currentIdx]
    return list(reversed(sequence))


# O(nlog(n)) time | O(n) space
def longestIncreasingSubsequence(array):
    sequences =[None for x in array]
    indices =[None for x in range(len(array)+1)]
    length = 0

    for i, num in enumerate(array):
        newLength = binarySearch(1, length, indices, array, num)
        sequences[i] = indices[newLength - 1]
        indices[newLength] = i
        length = max(length, newLength)
    return buildSequence(array, sequences, indices[length])

def binarySearch(startIdx, endIdx, indices, array, num):
    if startIdx > endIdx:
        return startIdx
    middleIdx =(startIdx + endIdx) // 2
    if array[indices[middleIdx]] < num:
        startIdx = middleIdx + 1
    else:
        endIdx = middleIdx - 1
    return binarySearch(startIdx, endIdx, indices, array, num)

def buildSequence(array, sequences, currentIdx):
    sequence =[]
    while currentIdx is not None:
        sequence.append(array[currentIdx])
        currentIdx = sequences[currentIdx]
    return list(reversed(sequence))