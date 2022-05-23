"""
Rearrange an array in order - smallest, largest, 2nd smallest, 2nd largest, 
3rd smallest, 3rd largest

Input : arr[] = [5, 8, 1, 4, 2, 9, 3, 7, 6]
Output :arr[] = {1, 9, 2, 8, 3, 7, 4, 6, 5}

Input : arr[] = [1, 2, 3, 4]
Output :arr[] = {1, 4, 2, 3}


A simple solution is to first find the smallest element, swap it with first element.
Then find largest element, swap it with second element and so on.
Time complexity of this solution is O(n^2).


An efficient solution is to use sorting

1. Sort the elements of array. 
2. Take two variables say i and j and point them to the first and last index of
the array respectively. 
3. Now run a loop and store the elements in the array one by one by incrementing i 
and decrementing j.
Let’s take an array with input 5, 8, 1, 4, 2, 9, 3, 7, 6 and sort them so the array 
to become 1, 2, 3, 4, 5, 6, 7, 8, 9.
Now take two variables say i and j and point them to the first and last index of
the array respectively, run a loop and store value into new array by incrementing 
i and decrementing j.
We get final result as 1 9 2 8 3 7 4 6 5. 


Time Complexity : O(n Log n) 
Auxiliary Space : O(n)

"""

def rearrangeArray(arr, n):

    # sorting the array elements
    arr.sort()

    # To store modified array
    tempArr =[0] * (n+1)

    # adding numbers from sorted array to new array accordingly
    ArrIndex = 0

    # Traverse from beginning and end simultaneously
    i = 0
    j = n-1

    while(i <=n // 2 or j > n // 2):
        tempArr[ArrIndex] = arr[i]
        ArrIndex = ArrIndex + 1
        tempArr[ArrIndex] = arr[j]
        ArrIndex = ArrIndex + 1
        i = i + 1
        j = j - 1

    # Modifying  original array
    for i in range(0, n):
        arr[i] = tempArr[i]

arr = [ 5, 8, 1, 4, 2, 9, 3, 7, 6 ]
n = len(arr)
rearrangeArray(arr, n)
 
for i in range(0, n) :
    print( arr[i], end = " ")


'''
test
'''
def swapElements(arr):
	arr.sort()
	i = 0
	j =len(arr)
	# while i < j:
	while(i <=n // 2 or j > n // 2):
		temp =arr.pop()
		arr.insert(i+1,temp)
		i =i + 2
		j =j - 1
	return arr

arr=[5, 8, 1, 4, 2, 9, 3, 7, 6]
# arr=[1, 2, 3, 4]

print("aaa:", swapElements(arr))