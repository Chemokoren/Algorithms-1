"""
Given an array of n elements, create a new array which is a rotation of given array and hamming distance between both the arrays is maximum. 
Hamming distance between two arrays or strings of equal length is the number of positions at which the corresponding character(elements) are different.
Note: There can be more than one output for the given input. 
Examples: 

Input :  1 4 1
Output :  2
Explanation:  
Maximum hamming distance = 2.
We get this hamming distance with 4 1 1 
or 1 1 4 

Input :  N = 4
         2 4 8 0
Output :  4
Explanation: 
Maximum hamming distance = 4
We get this hamming distance with 4 8 0 2.
All the places can be occupied by another digit.
Other possible solutions are 8 0 2 4 and 0 2 4 8.  

Method #1: 

Create another array which is double the size of the original array, such that 
the elements of this new array (copy array) are just the elements of the 
original array repeated twice in the same sequence. Example, if the original array 
is 1 4 1, then the copy array is 1 4 1 1 4 1. 
Now, iterate through the copy array and find hamming distance with every shift 
(or rotation). So we check 4 1 1, 1 1 4, 1 4 1, choose the output for which 
the hamming distance is maximum. 

Time Complexity : O(n*n)

"""
# code to find another array such that the hamming distance from the original array is max
# return the max hamming distance of a rotation

def maxHamming(arr, n):
    #arr[] to brr[] two times so that we can traverse through all rotations.
    brr =[0] * (2*n+1)
    for i in range(n):
        brr[i] =arr[i]
    for i in range(n):
        brr[n+1] = arr[i]
    # we know hamming distance with 0 rotation would be 0
    maxHam =0

    # we try other rotations one by one and compute Hamming distance of every rotation
    for i in range(1,n):
        currHam = 0
        k = 0
        for j in range(i, i+n):
            if brr[j] != arr[k]:
                currHam += 1
                k = k+1

        # we can never get more than n
        if currHam == n:
            return n
        maxHam =max(maxHam,currHam)
    return maxHam

arr = [2, 4, 6, 8]
n = len(arr)
print(maxHamming(arr, n))


"""
Method #2: 



We can find the maximum hamming distance using a different approach by taking advantage 
of list-comprehension in python. In this method, we divide the job in 3 separate functions.

hamming_distance(x : list, y : list): This method returns the hamming distance for two
list passed as parameters. The idea is to count the positions at which elements are different
at the same index in two lists x and y where x is the original array taken in input and y 
is one of it rotations. Initialize a variable count from 0. Run loop from starting index 0 
to last index (n-1) where n is the length of the list. For each iteration check if element 
of x and element at index i (0<=i<=n-1) is same or not. If they are same, increment the counter.
After loop is completed, return the count(by definition this is the hamming distance for given 
arrays or strings)
rotate_by_one(arr : list): This method rotates the array (passed in argument ) in anti-clockwise
direction by 1 position. For e.g. if array [1,1,4,4] is passed, this method returns
[1,4,4,5,1]. The idea is to copy the 1st element of the array and save it in a variable (say x).
Then iterate the array from 0 to n-2 and copy every i+1 th value at ith position. 
Now assign x to last index.
max_hamming_distance(arr : list): This method finds the maximum hamming distance for a given 
array and it’s rotations. Follow below steps in this method. We copy this array in a new array
(say a) and initialize a variable max. Now, after every n rotations we get the original array.
So we need to find hamming distance for original array with it’s n-1 rotations and store 
the current maximum in a variable(say max). Run loop for n-1 iterations. For each iteration, 
we follow below steps:
Get the next rotation of arr by calling method ‘rotate_by_one’.
Call method hamming distance() and pass original array (a) and current rotation of a (arr) and 
store the current hamming distance returned in a variable (say curr_h_dist).
Check if value of curr_h_dist is greater than value of max. If yes, assign value of 
curr_h_dist to max_h.
Repeat steps 1-3 till loop terminates.
Return maximum hamming distance (max_h)

"""

# code to find maximum of an array with it's rotations
import time

# Function hamming distance to find the hamming distance for two lists/strings
def hamming_distance(x: list, y: list):
    # initialize count
    count =0

    # Run loop for size of x (or y) as both as same length
    for i in range(len(x)):
        # check if corresponding elements at same index are not equal
        if(x[i] != y[i]):
            # Incre,ent the count every time above condition satisfies
            count +=1

    # return the hamming distance for given pair of lists or strings
    return count

# Function to rotate the given array in anti-clockwise direction by 1
def rotate_by_one(arr: list):
    # store 1st element in a variable
    x =arr[0]

    # update each ith elment (0<=i<n-2) with it's next value
    for i in range(0,len(arr)-1):
        arr[i] =arr[i+1]

    # assign 1st element to the last index
    arr[len(arr)-1] = x

# Function max_hamming distance to find the maximum hamming distance for given array
def max_hamming_distance(arr: list):
    # Initialize a variable to store maximum hamming distance
    max_h =-1000000000
    
    # store size of the given array in a variable n
    n = len(arr)

    # Initialize a new array
    a =[]
    
    # Initialize a new array
    a =[]

    # Copy the original array in new array
    for i in range(n):
        a.append(arr[i])

    # Run loop for i=0 to i=n-1 for n-1 rotations
    for i in range(1,n):
        # Find the next rotation
        rotate_by_one(arr)
        print("Array after %d rotation : " % (i), arr)

        # store hamming distance of cirrent rotation with original array
        curr_h_dist = hamming_distance(a, arr)
        print("Hamming Distance with %d rotations: %d" %(i, curr_h_dist))


        # check if current hamming distance is greater than max hamming distance
        if curr_h_dist > max_h:

            # if yes, assign value of current hamming distance  to max hamming distance
            max_h = curr_h_dist

        print('\n')
    # return maximum hamming distance
    return max_h

if __name__ == '__main__':
   
    arr = [3, 0, 6, 4, 3]
    start = time.time()
    print('\n')
    print("Original Array : ", arr)
    print('\n')
    print("Maximum Hamming Distance: ", max_hamming_distance(arr))
    end = time.time()
    print(f"Execution Time = {end - start}")

