"""
HeapSort - is a comparison based sorting technique where we first build Max Heap and 
then swaps the rot element with last element(size times) and maintains the heap 
property each time to finally make sorted.

program for implementation of iterative heap sort

function build max heap where value of each child is always smaller 
than value of their parent

Here, both function buildMaxHeap and heapSort runs in O(nlogn) time.
So, overall time complexity is O(nlogn)

"""

def buildMaxHeap(arr, n):
    for i in range(n):
        # if child is bigger than parent
        if arr[i] > arr[int((i-1)/2)]:
            j = i

            # swap child and parent until parent is smaller
            while(arr[j] > arr[int((j-1) / 2)]):
                (arr[j], arr[int((j-1)/2)]) = (arr[int((j-1)/2)],arr[j])
                j =int((j -1) / 2)

def heapSort(arr, n):
    buildMaxHeap(arr,n)
    for i in range(n-1, 0, -1):
        # swap value of first indexed with last indexed
        arr[0], arr[i] = arr[i], arr[0]

        # maintaining heap property after each swapping
        j, index = 0, 0

        while True:
            index = 2*j + 1

            # if left child is smaller than right child point index variable to right child
            if(index <(i -1) and arr[index] < arr[index + 1]):
                index +=1

            # if parent is smaller than child then swapping parent with child having 
            # higher value
            if index < i and arr[j] < arr[index]:
                arr[j], arr[index] = arr[index],arr[j]

            j =index
            if index >= i:
                break
if __name__ =='__main__':
    arr= [10,20,15,17,9,21]
    n =len(arr)

    print("Given array: ")
    for i in range(n):
        print(arr[i], end=" ")

    print()

    heapSort(arr,n)

    # print array after sorting
    print("sorted array: ")

    for i in range(n):
        print(arr[i], end=" ")