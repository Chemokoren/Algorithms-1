"""

Insertion Sort
- Builds up the sort by gradually creating a larger left half which is always sorted
(We are taking one element at a time and inserting it in the correct spot)
[5,3,4,1,2]
[3,5,4,1,2]
[3,4,5,1,2]
[1,3,4,5,2]
[1,2,3,4,5]

### we are taking an element and inserting it in the correct spot
Insertion Sort Pseudocode
- Start by picking the second element in the array
- Now compare the second element with the one before it and swap if necessary.
- Continue to the next element and if it is in the incorrect order, iterate through the sorted portion(i.e.
the left side) to place the element in the correct place.
- Repeat until the array is sorted.
"""

def insertionSort(arr):

    for i in range(len(arr)):
        for j in range(1, len(arr)):
            if(arr[j]<arr[j-1]):
                arr[j],arr[j-1] = arr[j-1], arr[j]

    return arr

print("expected:[1,2,3,4,5], actual: ", insertionSort([5,3,4,1,2]))

def insertionSortUpdated(arr):
    for i in range(1, len(arr)):
        current_val = arr[i]
        k = i-1
        #for(var j=i-1;j>=- and arr[j] >current_val;j--)
        for j in range(k, j-=1):
            arr[j+1] = arr[j]
        arr[j+1] = current_val
        print(arr)
    return arr

print(insertionSortUpdated(2,1,9,7,6))

