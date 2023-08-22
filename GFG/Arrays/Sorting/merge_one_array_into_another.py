"""
Merge an array of size n into another array of size m+n

There are two sorted arrays. First one is of size m+n containing only m elements. Another
one is of size n and contains n elements. Merge these two arrays into the first array
of size m+n such that the output is sorted.
input: array with m+n elements (mPlusN[])

[2, None, 7, None, None, 10, None]

NA=> Value is not filled/available array mPlusN[]. There should be n such array blocks.
Input: array with n elements(N[])

[5, 8, 12, 14]


Output: N[] merged into mPlusN[] (Modified mPlusN[]) 
[2, 5, 7, 8, 10, 12, 14]

Algorithm:

Let first array be mPlusN[] and other array be N[]
- Move m elements of mPlusN[] to end.
- Start from nth element of mPlusN[] and 0th element of N[] and merge them into
mPlusN[].

"""
# Python program to Merge an array of
# size n into another array of size m + n

NA = -1

# Function to move m elements
# at the end of array mPlusN[]


def moveToEnd(mPlusN, size):

	i = 0
	j = size - 1
	for i in range(size-1, -1, -1):
		if (mPlusN[i] != NA):

			mPlusN[j] = mPlusN[i]
			j -= 1

# Merges array N[]
# of size n into array mPlusN[]
# of size m+n


def merge(mPlusN, N, m, n):

	i = n # Current index of i/p part of mPlusN[]
	j = 0 # Current index of N[]
	k = 0 # Current index of output mPlusN[]
	while (k < (m+n)):

		# Take an element from mPlusN[] if
		# a) value of the picked
		# element is smaller and we have
		# not reached end of it
		# b) We have reached end of N[] */
		if ((j == n) or (i < (m+n) and mPlusN[i] <= N[j])):

			mPlusN[k] = mPlusN[i]
			k += 1
			i += 1

		else: # Otherwise take element from N[]

			mPlusN[k] = N[j]
			k += 1
			j += 1

# Utility that prints
# out an array on a line


def printArray(arr, size):

	for i in range(size):
		print(arr[i], " ", end="")

	print()


# Driver function to
# test above functions

# Initialize arrays
mPlusN = [2, 8, NA, NA, NA, 13, NA, 15, 20]
N = [5, 7, 9, 25]
n = len(N)

m = len(mPlusN) - n

# Move the m elements
# at the end of mPlusN
moveToEnd(mPlusN, m+n)

# Merge N[] into mPlusN[]
merge(mPlusN, N, m, n)

# Print the resultant mPlusN
printArray(mPlusN, m+n)


print("\n my tests \n")
'''

my tests 

'''
def my_tests(arr1, arr2):

    start = 1
    end = len(arr1)-1
    index = 1
    for i in range(1,end):
        if arr1[index] == None:
            index +=1
        if arr1[start] != None:
            start +=1
        arr1[start], arr1[index] = arr1[index], arr1[start]

    for i in range(len(arr2)):
        arr1[start] =arr2[i]
        start +=1
    arr1.sort()
    return arr1


print("Expected: [2, 5, 7, 8, 10, 12, 14], Actual: ", my_tests([2, None, 7, None, None, 10, None], [5, 8, 12, 14]))