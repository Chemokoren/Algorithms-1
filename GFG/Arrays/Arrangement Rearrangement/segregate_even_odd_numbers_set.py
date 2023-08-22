"""
Segregate even and odd numbers

Given an array of integers, segregate even and odd numbers in the array. 
All the even numbers should present first, and then the odd numbers

Examples:  

Input: arr[] = 1 9 5 3 2 6 7 11
Output: 2 6 5 3 1 9 7 11

Input: arr[] = 1 3 2 4 7 6 9 10
Output:  2 4 6 10 7 1 9 3

Brute-Force Solution

As we need to maintain the order of elements then this can be done in the following steps :

Create a temporary array A of size n and an integer ind which will keep the index of 
elements inserted .
Initialize ind with zero and iterate over the original array and if even number is 
found then put that number at A[ind] and then increment the value of ind .
Again iterate over array and if an odd number is found then put it in A[ind] and then 
increment the value of ind.
Iterate over the temporary array A and copy its values in the original array.

Time complexity: O(n)
Auxiliary space: O(n) 

"""

def arrayEvenAndOdd(arr, n):

    ind =0
    a =[0 for i in range(n)]

    for i in range(n):
        if(arr[i] % 2 == 0):
            a[ind] = arr[i]
            ind +=1

    for i in range(n):
        if (arr[i] % 2 !=0):
            a[ind]=arr[i]
            ind +=1
    
    for i in range(n):
        print(a[i], end=" ")

    print()

arr = [ 1, 3, 2, 4, 7, 6, 9, 10 ]
n = len(arr)
 
# Function call
arrayEvenAndOdd(arr, n)

print("\n Efficient Approach: \n")
"""
Efficient Approach:

The optimization for above approach is based on Lomuto’s Partition Scheme 

Maintain a pointer to the position before first odd element in the array.
Traverse the array and if even number is encountered then swap it with the first odd element.
Continue the traversal.

Time Complexity : O(n) 
Auxiliary Space : O(1)

"""

print("ddddddddddddddddddddddddd")
def arrayEvenAndOdd(arr,n):
    i = -1
    j= 0
    while (j!=n):
        if (arr[j] % 2 ==0):
            i = i+1
 
            # Swapping even and odd numbers
            arr[i],arr[j] = arr[j],arr[i]
             
        j = j+1
     
    # Printing segregated array
    for i in arr:
        print (str(i) + " " ,end='')

if __name__=='__main__':
    arr = [ 1 ,3, 2, 4, 7, 6, 9, 10]
    n = len(arr)
    arrayEvenAndOdd(arr,n)


# time complexity: O(n)
# space complexity: O(1)
def segregate_even_odd_updated(arr):
	i =0
	j =len(arr)-1
	
	while i<j:
		if arr[i] %2 ==0 and arr[j] % 2 !=0:
			i = i+1
			j = j-1
		elif (arr[i] % 2==0 and arr[j] %  2 ==0):
			i = i +1
		elif (arr[i] % 2 !=0 and arr[j] %  2 !=0):
			j = j - 1
			
		elif (arr[i] % 2 !=0 and arr[j] %  2 ==0):
			arr[i],arr[j] =arr[j],arr[i]
			i = i+1
			j = j-1
	return arr
			
print("attttttttttttttt")	 
print("expected:[2, 6, 5, 3, 1, 9, 7, 11], actual:", segregate_even_odd_updated([1, 9, 5, 3, 2, 6, 7, 11]))
print("expected:[2, 4 ,6 ,10, 7, 1, 9, 3], actual:", segregate_even_odd_updated([1, 3, 2, 4, 7, 6, 9, 10]))
	