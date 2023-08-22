"""
Rearrange an array such that ‘arr[j]’ becomes ‘i’ if ‘arr[i]’ is ‘j’ | Set 1

Given an array of size n where all elements are distinct and in range from 0 to n-1, 
change contents of arr[] so that arr[i] = j is changed to arr[j] = i. 

Example 1:
Input: arr[]  = {1, 3, 0, 2};
Output: arr[] = {2, 0, 3, 1};
Explanation for the above output.
Since arr[0] is 1, arr[1] is changed to 0
Since arr[1] is 3, arr[3] is changed to 1
Since arr[2] is 0, arr[0] is changed to 2
Since arr[3] is 2, arr[2] is changed to 3

Example 2:
Input: arr[]  = {2, 0, 1, 4, 5, 3};
Output: arr[] = {1, 2, 0, 5, 3, 4};

Example 3:
Input: arr[]  = {0, 1, 2, 3};
Output: arr[] = {0, 1, 2, 3};

Example 4:
Input: arr[]  = {3, 2, 1, 0};
Output: arr[] = {3, 2, 1, 0};

A simple solution is to create a temporary array and one by one copy 'i' to 'temp[arr[i]]'
where i varies from 0 to n-1

The time complexity is O(n) and auxiliary space needed is O(n).

"""
# program to rearrange contents of arr[] such that arr[j] becomes j if arr[i] is j
# A simple method to rearrange 'arr[0..n-1]' so that 'arr[j]' becomes 'i' if 'arr[i]' is 'j'

def rearrangeNaive(arr):
	new_arr=[0] * len(arr)
	for i in range(len(arr)):
		val = arr[i]
		new_arr[val] =i
	for i in range(len(new_arr)):
		arr[i] =new_arr[i]
	return arr
	
print("\n########################## rearrangeNaive ##########################\n")
print("expected:,actual:[3,2,1,0]",rearrangeNaive([3,2,1,0]))
print("expected:,actual:[0,1,2,3]",rearrangeNaive([0,1,2,3]))
print("expected:,actual:[2,0,3,1]",rearrangeNaive([1,3,0,2]))
print("expected:,actual:[1,2,0,5,3,4]",rearrangeNaive([2,0,1,4,5,3])) 



"""

Can we solve this in O(n) time and O(1) auxiliary space? 

The idea is based on the fact that the modified array is basically a permutation of the input array. 
We can find the target permutation by storing the next item before updating it.

Let us consider array ‘{1, 3, 0, 2}’ for example. We start with i = 0, arr[i] is 1. So we go to arr[1] and 
change it to 0 (because i is 0). Before we make the change, we store the old value of arr[1] as the old value 
is going to be our new index i. In the next iteration, we have i = 3, arr[3] is 2, so we change arr[2] to 3.
Before making the change we store next i as old value of arr[2]. 

The below code gives idea about this approach. 

// This function works only when output is a permutation with one cycle.

def rearrangeUtil(arr, n):

    // 'val' is the value to be stored at 'arr[i]'
    val = 0;   // The next value is determined using current index
    i = arr[0];  // The next index is determined using current value

    // While all elements in cycle are not processed
    while (i != 0):

        // Store value at index as it is going to be used as next index
        new_i = arr[i];

        // Update arr[]
        arr[i] = val;

        // Update value and index for next iteration
        val = i;
        i = new_i;

    arr[0] = val;  // Update the value at arr[0]


The above function doesn’t work for inputs like {2, 0, 1, 4, 5, 3}; as there are two cycles. 
One cycle is (2, 0, 1) and other cycle is (4, 5, 3). 
How to handle multiple cycles with the O(1) space constraint? 
The idea is to process all cycles one by one. To check whether an element is processed or not,
we change the value of processed items arr[i] as -arr[i]. Since 0 can not be made negative,
we first change all arr[i] to arr[i] + 1. In the end, we make all values positive and 
subtract 1 to get old values back. 
 
The time complexity of this method seems to be more than O(n) at first look. 
If we take a closer look, we can notice that no element is processed more than a 
constant number of times.


"""

# program to rearrange contents of arr such that arr[j] becomes j if arr[i] is j

# A utility function to rearrange elements in the cycle starting at arr[i]. This function
# assume values in arr be from 1 to n. It changes arr[j-1] to i+1 if arr[i-1] is j+1
def rearrangeUtil(arr, n, i):
    # 'val' is the value to be stored at 'arr[i]', the next value is determined using 
    # current index
    val =-(i + 1)

    # The next index is determined using cirrent index
    i = arr[i] - 1

    # while all elements in cycle are not processed 
    while(arr[i] > 0):
        # store value at index as it is going to be as next index
        new_i =arr[i] -1

        # update arr
        arr[i] =val

        # update value and index for next iteration
        val =-(i + 1)
        i =new_i

# A space efficient method to rearange 'arr[0..n-1' so that 'arr[j]' becomes 'i' if 'arr[i]'
# is 'j'

def rearrange(arr, n):
    # increment all values by 1, so that all elements can be made negative 
    # to mark them as visited
    for i in range(n):
        arr[i] += 1

    # process all cycles
    for i in range(n):
        # process cycle starting arr[i] if this cycle is not already processed
        if(arr[i] > 0):
            rearrangeUtil(arr, n, i)

    
    # change sing and values of arr to get the orginal values back, i.ie., values in range
    # from 0 to n-1

    for i in range(n):
        arr[i] = (-arr[i]) -1

# A utility function to to print contents of arr[0..n-1]
def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()

arr = [ 2, 0, 1, 4, 5, 3 ]
n = len(arr)
 
print(" \n Given array is ")
printArray(arr, n)
 
rearrange(arr, n)
 
print("Modified array is ")
printArray(arr, n)



"""
Another Method: 

The idea is to store each element’s new and old value as quotient and remainder of n, 
respectively (n being the size of the array). 
For example, Suppose an element’s new value is 2, the old value is 1 and n is 3, 
then the element’s value is stored as 1 + 2*3 = 7. We can retrieve its old value by
7%3 = 1 and its new value by 7/3 = 2. 
"""

# A simple method to rearrange 'arr[0..n-1]' so that 'arr[j]' becomes 'i' if 'arr[i]' is 'j'

def rearrange(arr, n):
    for i in range(n):
        # retrieving old value and storing the new one 
        arr[arr[i] % n] += i * n

    for i in range(n):
        # retrieving new value
        arr[i] //= n

     
def prArray(arr, n):
     
    for i in range(n):
        print(arr[i], end = " ")
    print()
 
# Driver code
arr = [2, 0, 1, 4, 5, 3]
n = len(arr)
 
print("Given array is : ")
prArray(arr, n)
 
rearrange(arr, n)
 
print("Modified array is :")
prArray(arr, n)