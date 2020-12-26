# O(n^2) time | O(1) space
def insertionSort(array):
    for i in range(1,len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            swap(j, j - 1, array)
            j -=1
        return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]



print(insertionSort([8,5,2,9,5,6,3]))

print("################# version 2 of insertion sort ####################")

def insertionSort(arr):

	# Traverse through 1 to len(arr)
	for i in range(1, len(arr)):

		key = arr[i]

		# Move elements of arr[0..i-1], that are greater than key, to one position ahead
		# of their current position
		j = i-1
		while j >= 0 and key < arr[j] :
				arr[j + 1] = arr[j]
				j -= 1
		arr[j + 1] = key


# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
for i in range(len(arr)):
	print ("% d" % arr[i])
