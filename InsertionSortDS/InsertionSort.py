class InsertionSort(object):
    def insertionSort(self,arr):
        for i in range(len(arr)):
            current =arr[i]
            j = i-1
            while j>=0 and arr[j] >current:
                arr[j+1] =arr[j]
                j =j -1
            arr[j+1] =current
        return arr


# Python program for implementation of Insertion Sort

# Function to do insertion sort
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
            arr[j+1] = key
    return arr


# Driver code to test above
arr = [12, 11, 13, 5, 6]
# insertionSort(arr)
# print ("Sorted array is:")
# for i in range(len(arr)):
# 	print ("%d" %arr[i])

# This code is contributed by Mohit Kumra

print(insertionSort(arr))


