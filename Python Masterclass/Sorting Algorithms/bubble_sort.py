"""
What is Sorting?

- Sorting is the process of rearranging the items in a collection(e.g. an array) so that the items 
are in some kind of order.

Why do we need to learn this?
-Sorting is an incredibly common task, so it's good to know how it works
-There are many different ways to sort things, and different techniques have their own advantages 
and disadvantages

Objectives 
-implement bubble sort
-Understand why it is important to learn these simpler sorting algorithms

BubbleSort
-A sorting algorithm where the largest values bubble up to the top!

BubbleSort Pseudocode
- Start looping the end of the array towards the beginning
- Start an inner loop with a variable called j from the beginning until i -1
- If arr[j] is greater than arr[j+1], swap those two values!
- Return the sorted array

Time complexity of Bubble sort is O(N^2)

"""

def bubbleSort(arr):
    for i in range(len(arr), 0,-1):
        # for j in range(i-1):
        for j in range(len(arr)-1):
            print("1:",arr)
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] =arr[j+1], arr[j]
    return arr

# arr =[4,6,9,1,3,8,2]
arr =[8,1,2,3,4,5,6,7]
print(bubbleSort(arr))


'''
optimized bubblesort without swaps

'''

def bubbleSortOptimized(arr):

    no_swaps = None

    for i in range(len(arr), 0, -1):
        no_swaps = True
        print(arr)

        for j in range(i-1):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                no_swaps = False
        if(no_swaps):
            break
    return arr

print(" optimized bubblesort ")
print(bubbleSortOptimized([8,1,2,3,4,5,6,7]))
