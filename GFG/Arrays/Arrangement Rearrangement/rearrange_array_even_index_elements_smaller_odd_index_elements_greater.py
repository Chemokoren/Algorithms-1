"""
Rearrange array such that even index elements are smaller and odd index elements are greater

Given an array, rearrange the array such that:
1. If index i is even, arr[i] <= arr[i+1]
2. If index i is odd, arr[i] >= arr[i+1]

Note : There can be multiple answers.
Examples:  

Input  : arr[] = {2, 3, 4, 5} 
Output : arr[] = {2, 4, 3, 5}
Explanation : Elements at even indexes are
smaller and elements at odd indexes are greater
than their next elements

Note : Another valid answer
is arr[] = {3, 4, 2, 5}

Input  :arr[] = {6, 4, 2, 1, 8, 3}
Output :arr[] = {4, 6, 1, 8, 2, 3}

This problem is similar to sort an array in wave form.

A simple solution is to sort the array in descreasing order, then starting from 
second element, swap the adjacent elements.
An efficient solution is to iterate over the array and swap the elements as per the given
condition
If we have an array of length n, then we iterate from index 0 to n-2 and check  the given
condition.
At any point of time if i is even and arr[i] > arr[i+1], then we swap arr[i] and arr[i+1].

Time Complexity :O(n)

Auxiliary Space: O(1)



"""

def rearrangeVal(arr):
	n =len(arr)
	for i in range(n-1):
		if( i % 2 == 0 and arr[i] > arr[i+1]):
			arr[i], arr[i+1] =arr[i+1], arr[i]
			
		if( i % 2 !=0 and arr[i] < arr[i+1]):
			arr[i],arr[i+1] =arr[i+1], arr[i]
	return arr
	
print("expected:[2, 4, 3, 5], actual:", rearrangeVal([2, 3, 4, 5]))
print("expected:[4, 6, 1, 8, 2, 3], actual:", rearrangeVal([6, 4, 2, 1, 8, 3]))


print("\n positive elements at even and negative at odd positions: \n")
"""
positive elements at even and negative at odd positions (relative order not maintained)

You have been given an array and you have to make a program to convert that array such 
that positive elements occur at even numbered places in the array and negative elements 
occur at odd numbered places in the array. We have to do it in place.
There can be unequal number of positive and negative values and the extra values have
to left as it is.

Examples:  

Input : arr[] = {1, -3, 5, 6, -3, 6, 7, -4, 9, 10}
Output : arr[] = {1, -3, 5, -3, 6, 6, 7, -4, 9, 10}

Input : arr[] = {-1, 3, -5, 6, 3, 6, -7, -4, -9, 10}
Output : arr[] = {3, -1, 6, -5, 3, -7, 6, -4, 10, -9}

The idea is to use Hoare's partion process of Quick Sort
We take two pointers positive and negative. We set the positive pointer at start of the array
 and negative pointer at 1st position of the array.

 We move positive pointer two steps forward till it finds a negative element.

 Similarly, we move negative pointer forward by two places till it finds a positive value
 at its position.

 If the positive and negative pointers are in the array then we will swap the values
 at these indexes otherwise we will stop executing the process.


 *************************Explanation**************************:

 Lets explain the working of the code on the first example 
arr[] = {1, -3, 5, 6, -3, 6, 7, -4, 9, 10} 
We declare two variables positive and negative positive points to zeroth position and negative points to first position 
positive = 0 negative = 1 
In the first iteration positive will move 4 places to fifth position as a[4] is less than zero and positive = 4. 
Negative will move 2 places and will point to fourth position as a[3]>0 
we will swap positive and negative position values as they are less than size of array. 
After first iteration the array becomes arr[] = {1, -3, 5, -3, 6, 6, 7, -4, 9, 10}
Now positive points at fourth position and negative points at third position 
In second iteration the positive value will move 6 places and its value will 
more than the size of the array. 

The negative pointer will move two steps forward and it will point to 5th position 
As the positive pointer value becomes greater than the array size we will not perform any swap operation and break out of the while loop. 
The final output will be 
arr[] = {1, -3, 5, -3, 6, 6, 7, -4, 9, 10}

An example where relative order is not maintained: 
{ -1, -2, -3, -4, -5, 6, 7, 8 };


"""

def rearrange(a, size):

    positive = 0
    negative = 1

    while(True):
        # Move forward the positive pointer till negative number not encountered
        while( positive < size and a[positive] >= 0):
            positive = positive + 2

        # move forward the negative pointer till positive number not encountered
        while( negative < size and a[negative] <= 0):
            negative = negative + 2

        # swap array elements to fix their position
        if(positive < size and negative < size):
            temp =a[positive]
            a[positive] =a[negative]
            a[negative] =temp

        # break from the while loop when any index exceeds the size of the array
        else:
            break

arr =[ 1, -3, 5, 6, -3, 6, 7, -4, 9, 10 ]
n = len(arr)
 
rearrange(arr, n)
for i in range(0, n) :
    print(arr[i], end = " ")


"""
Another Approach :- 
The idea is to find a positive/negative element which is in incorrect place
(i.e. positive at odd and negative at even place) and the then find the element of opposite 
sign which is also in incorrect position in the remaining array and then swap these
two elements. 

"""

def printArray(a, n):
    for i in a:
        print(i, end=" ")
    print()

arr = [1, -3, 5, 6, -3, 6, 7, -4, 9, 10]
n = len(arr)

# before modification
print("\n original array:")
printArray(arr, n)

for i in range(n):
    if(arr[i] >= 0 and i % 2 == 1):
        # out of order positive element
        for j in range(i+1, n):
            if(arr[j] < 0 and j % 2==0):
                # find out of order negative element in remaining array
                arr[i], arr[j] = arr[j], arr[i]
                break
    elif (arr[i] < 0 and i % 2 == 0):

        # our of order negative element
        for j in range(i + 1, n):
            if(arr[j] >=0 and j % 2 == 1):
                
                # find out of order positive element remaining array
                arr[i], arr[j] =arr[j], arr[i]
                break

print("\n modified array: ")
printArray( arr, n)
