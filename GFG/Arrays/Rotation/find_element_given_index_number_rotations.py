"""
Find element at a given index after a number of rotations

An array consisting of N integers is given. There are several Right Circular Rotations 
of range[L..R] that we perform. After performing these rotations, we need to find element
at a given index.

        ranges[] = { {0, 2}, {0, 3} }
        index : 1
Output : 3
Explanation : After first given rotation {0, 2}
                arr[] = {3, 1, 2, 4, 5}
              After second rotation {0, 3} 
                arr[] = {4, 3, 1, 2, 5}
After all rotations we have element 3 at given
index 1. 

Method : Brute-force The brute force approach is to actually rotate the array 
for all given ranges, finally return the element in at given index in the modified array.

Method : Efficient We can do offline processing after saving all ranges. 
Suppose, our rotate ranges are : [0..2] and [0..3] 
We run through these ranges from reverse.
After range [0..3], index 0 will have the element which was on index 3. 
So, we can change 0 to 3, i.e. if index = left, index will be changed to right. 
After range [0..2], index 3 will remain unaffected.
So, we can make 3 cases : 
If index = left, index will be changed to right. 
If index is not bounds by the range, no effect of rotation. 
If index is in bounds, index will have the element at index-1.
Below is the implementation : 


For better explanation:-

10 20 30 40 50



Index: 1

Rotations: {0,2} {1,4} {0,3}

Answer: Index 1 will have 30 after all the 3 rotations in the order {0,2} {1,4} {0,3}.

We performed {0,2} on A and now we have a new array A1.

We performed {1,4} on A1 and now we have a new array A2.

We performed {0,3} on A2 and now we have a new array A3.

Now we are looking for the value at index 1 in A3.

But A3 is {0,3} done on A2.

So index 1 in A3 is index 0 in A2.

But A2 is {1,4} done on A1.

So index 0 in A2 is also index 0 in A1 as it does not lie in the range {1,4}.

But A1 is {0,2} done on A.

So index 0 in A1 is index 2 in A.

On observing it, we are going deeper into the previous rotations staring 
from the latest rotation.

{0,3}

|

{1,4}

|



{0,2}

This is the reason we are processing the rotations in reverse order.

Please note that we are not rotating the elements in the reverse order, 
just processing the index from reverse.

Because if we actually rotate in reverse order, we might get a completely 
different answer as in case of rotations the order matters. 


"""

# code to rotate an array and answer the index query

# Function to compute the element at a given index
def findElement(arr, ranges, rotations, index):
    for i in range(rotations -1, -1, -1):
        # Range[left ...right]
        left =ranges[i][0]
        right =ranges[i][1]

        # Rotation will not have any effect
        if( left <= index and right >= index):
            if(index == left):
                index =right
            else:
                index =index -1

    # Returning new element
    return arr[index]

arr = [ 1, 2, 3, 4, 5 ]
 
# No. of rotations
rotations = 2
 
# Ranges according to 0-based indexing
ranges = [ [ 0, 2 ], [ 0, 3 ] ]
 
index = 1
 
print(findElement(arr, ranges, rotations, index))


