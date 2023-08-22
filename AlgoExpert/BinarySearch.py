# O(log(n)) time | O(log(n)) space
def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) -1)

def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1
    middle =(left+right) //2
    potentialMatch =array[middle]
    if target == potentialMatch:
        return [middle,array[middle]]
    elif target < potentialMatch:
        return binarySearchHelper(array, target, left, middle -1)
    else:
        return binarySearchHelper(array, target, middle+1, right)


# iterative approach
# O(log(n)) time | O(1) space
def binarySearch1(array, target):
    return binarySearchHelper(array, target, 0, len(array -1))

def binarySearchHelperIterative(array, target, left, right):
    while left <= right:
        middle =(left+right) //2
        potentialMatch = array[middle]
        if target == potentialMatch:
            return middle
        elif target < potentialMatch:
            right = middle -1
        else:
            left =middle +1
    return -1

my_array =[0,1,21,33,45,45,61,71,72,73]

print(binarySearch(my_array,33))

def binary_search(arr, val):
	start =0
	end =len(arr)-1
	
	while start <= end:
		mid = (start + end) // 2
		
		if val ==arr[mid]:
			return arr[mid]
		elif arr[mid] > val:
			end = mid -1
		elif arr[mid] < val:
			start = mid + 1
	return False
		
my_array =[0,1,21,33,45,45,61,71,72,73]
print(binary_search(my_array, 0))