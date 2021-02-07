def heapSort(array):
    buildMaxHeap(array)
    for endIdx in reversed(range(1,len(array))):
        swap(0, endIdx, array)
        siftDown(0, endIdx -1, array)
    return array

def buildMaxHeap(array):
    firstParentIdx =(len(array) -1) // 2
    for currentIdx in reversed(range(firstParentIdx +1)):
        siftDown(currentIdx, len(array) -1, array)
def siftDown(currentidx, endIdx, heap):
    childOneIdx = currentidx * 2 +1
    while childOneIdx <=endIdx:
        childTwoIdx =currentidx *2 +2 if currentidx *2 +2 <=endIdx else -1
        if childTwoIdx > -1 and heap[childTwoIdx] > heap[childOneIdx]:
            idxToSwap =childTwoIdx
        else:
            idxToSwap =childOneIdx
        if heap[idxToSwap] > heap[currentidx]:
            swap(currentidx, idxToSwap, heap)
            currentidx =idxToSwap
            childOneIdx =currentidx * 2 +1
        else:
            return

def swap(i, j, array):
    array[i], array[j] =array[j], array[i]

my_array =[8,5,2,9,5,6,3]

print(heapSort(my_array))
