"""
Postive elements at even and negative at odd positions (Relative order not maintained)

You have been given an array and you have to make a program to convert that array such that positive 
elements occur at even numbered places in the array and negative elements occur at odd numbered places 
in the array and negative elements occur at odd numbered places in the array. We have to do it in place.
There can be unequal number of positive and negative values and the extra values have to be left as it is.

Examples;

Input : arr[] = {1, -3, 5, 6, -3, 6, 7, -4, 9, 10}
Output : arr[] = {1, -3, 5, -3, 6, 6, 7, -4, 9, 10}

Input : arr[] = {-1, 3, -5, 6, 3, 6, -7, -4, -9, 10}
Output : arr[] = {3, -1, 6, -5, 3, -7, 6, -4, 10, -9}


"""

print("#################### even positive numbers & odd negatives #################### ")
def rearrange_even_positives_odd_negatives(arr):
	n =len(arr)
	for i in range(n-1):
		if( i % 2 == 0 and arr[i] <0 and arr[i+1] > 0):
			arr[i], arr[i+1] =arr[i+1], arr[i]
			
		if( i % 2 !=0 and arr[i] >0 and arr[i+1] < 0):
			arr[i],arr[i+1] =arr[i+1], arr[i]
	return arr

print("expected:[1, -3, 5, -3, 6, 6, 7, -4, 9, 10], actual:", rearrange_even_positives_odd_negatives([1, -3, 5, 6, -3, 6, 7, -4, 9, 10]))
print("expected:[3, -1, 6, -5, 3, -7, 6, -4, 10, -9], actual:", rearrange_even_positives_odd_negatives([-1, 3, -5, 6, 3, 6, -7, -4, -9, 10]))

'''
Approach 1:

The idea is to use Hoare's partition process of QuickSort.
We take two pointers positive and negative. We then set the positive pointer at start of the array and the
negative pointer at 1st position of the array.

We move positive pointer two steps forward till it finds a negative element. Similaryly, we move negative
pointer forward by two places till it finds a positive value at its position.

If the positive and negative pointers are in the array then we will swap the values at these indexes 
otherwise we will stop executing the process.

'''

def rearrange_arr(a):
    size = len(a)
    
    positive = 0
    negative =1

    while(True):
        # move forward the positive pointer till negative number not encountered
        while(positive < size and a[positive] >=0):
            positive = positive + 2

        # move forward the negative pointer till positive number not encoutered
        while(negative < size and a[negative] <=0):
            negative = negative + 2


        # swap array elements to fix their position
        if(positive < size and negative < size):
            a[positive],a[negative] = a[negative],a[positive]

        # break from the while loop when any index exceeds the size of  the array
        else:
            break
    return a

print("Approach I\n")
print("expected:[1, -3, 5, -3, 6, 6, 7, -4, 9, 10], actual:", rearrange_arr([1, -3, 5, 6, -3, 6, 7, -4, 9, 10]))
print("expected:[3, -1, 6, -5, 3, -7, 6, -4, 10, -9], actual:", rearrange_arr([-1, 3, -5, 6, 3, 6, -7, -4, -9, 10]))


'''
Explanation:

arr[] = {1, -3, 5, 6, -3, 6, 7, -4, 9, 10} 

We declare two variables positive and negative positive points to zeroth position and negative points to 
first position
positive = 0 and negative =1
In the first iteration, positive will move 4 places to fifth position as a[4] is less than zero and positive=4
Negative will move 2 places and will point to fourht position as a[3] > 0
we will swap positive and negative position values as they are less than size of array.
After first iteration, the array becomes arr[] = {1, -3, 5, -3, 6, 6, 7, -4, 9, 10}
Now positive points at fourht position and negative points at third position in second iteration the positive
value will move 6 places and its value will be more than the size of the array.

The negative pointer will move two steps forward and it will point to 5th position As the positive pointer
value becomes greater than the array size we will not perform any swap operation and break out of the while
loop.
The final output will be 
arr[] = {1, -3, 5, -3, 6, 6, 7, -4, 9, 10}


An example where relative order is not maintained: 
{ -1, -2, -3, -4, -5, 6, 7, 8 }; 

Approach II:
-------------

The idea is to find a positive/negative element which is in incorrect place(i.e positive at odd and negative
at even place) and then find the element of oppositive sign which is also in incorrect position in the
remaining array and then swap these two elements.



'''

def printArray(a):
    for i in a:
        print(i, end =" ")
    print()

arr = [1, -3, 5, 6, -3, 6, 7, -4, 9, 10]
n =len(arr)
# before modification
printArray(arr)

for i in range(n):
    if(arr[i] >= 0 and i % 2 ==1):

        # out of order positive element
        for j in range(i +1, n):
            if(arr[j] < 0 and j % 2 == 0):

                # find out of order negative element in remaining array
                arr[i],arr[j] =arr[j], arr[i]
                break
    elif(arr[i] < 0 and i%2 ==0):
        # out of order negative element
        for j in range(i+1, n):

            #find out of order positive element in remaining array
            if(arr[j] >=0 and j%2 ==1):
                arr[i], arr[j] = arr[j],arr[i]
            break

print("Approach II \n")
printArray(arr)
