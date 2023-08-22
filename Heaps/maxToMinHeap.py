# implementation program to convert min Heap to max Heap

# to heapify a subtree with root at given index
def heapifyToMax(_array, i, n):
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i
    if l < n and _array[l] > _array[i]:
        largest = l
    if r < n and _array[r] > _array[largest]:
        largest = r
    if largest != i:
        _array[i], _array[largest] = _array[largest], _array[i]
        heapifyToMax(_array, largest, n)


# This function basically builds max heap
def buildMaxHeap(_arr, n):
    # Start from bottommost and rightmost
    # internal mode and heapify all
    # internal modes in bottom up way
    for i in range(int((n - 2) / 2), -1, -1):
        heapifyToMax(_arr, i, n)


# function to print an array given the size of the array
def printArray(_arr, size):
    for i in range(size):
        print(_arr[i], end=" ")
    print()


# main method to test max to min heap implementation
if __name__ == '__main__':
    #  Min Heap array representation
    # _arr = [3, 5, 9, 6, 8, 20, 10, 12, 18, 9]
    # _arr = [9, 4, 7, 1, -2, 6, 5]
    _arr = [1, 4, 5, 6, 7, 9]
    n = len(_arr)

    print("Min Heap _array : ")
    printArray(_arr, n)

    buildMaxHeap(_arr, n)

    print("Max Heap array : ")
    printArray(_arr, n)