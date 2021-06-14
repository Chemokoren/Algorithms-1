"""
Rearrange an array such that arr[i] =i

# Given an array of elements of length N, 
# ranging from 0 to N-1. All elements may not be present in the array. 
# If the element is not present then there will be -1
present in the array. Rearrange the array such that A[i] =i and if i is not present, 
display -1 at that place

Input : arr = {-1, -1, 6, 1, 9, 3, 2, -1, 4, -1}
Output : [-1, 1, 2, 3, 4, -1, 6, -1, -1, 9]

Input : arr = {19, 7, 0, 3, 18, 15, 12, 6, 1, 8,
              11, 10, 9, 5, 13, 16, 2, 14, 17, 4}
Output : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
         11, 12, 13, 14, 15, 16, 17, 18, 19]

Approach: Naive
1. Navigate the numbers from 0 to n-1
2. Now navigate through the array.
3. if (i == a[j]), then replace the element at i position with a[j] position
4. If there is any element in which -1 is used instead of the number then 
it will be replace automatically
5. Now, iterate through the array and check if(a[i]!=i), if its true then replace
a[i] with -1

Time Complexity: O(n^2)
"""

# Function to transform the array
def fixArray(ar, n):
    # Iterate over the array
    for i in range(n):
        for j in range(n):

            # check if  any ar[j] exists such that ar[j] is equal to i
            if (ar[j] == i):
                ar[j],ar[i] =ar[i], ar[j]

    # Iterate over array
    for i in range(n):
        
        # if not present
        if(ar[i] != i):
            ar[i] =-1

    # print the output
    print("Array after rearranging")

    for i in range(n):
        print(ar[i], end=" ")

ar = [ -1, -1, 6, 1, 9, 3, 2, -1, 4, -1 ]
# ar = [ 1, 2, 3, 4, 5 ]
n = len(ar)

# Function Call
print(fixArray(ar, n))

print("Approach 2:\n")
"""
Approach 2:

1. Navigate through the array.
2. check if a[i] =-1, if yes then ignore it.
3. if a[i]!=-1, check if element a[i] is at its correct position(i=A[i]). 
If yes then ignore it.
4. if a[i]!=-1 and element a[i] is not at its correct position (i != A[i]) 
then place it to its correct position, but there are two conditions:
1) Either A[i] is vacate, means A[i] =-1, then just put A[i]=i
2) OR A[i] is not vacate, means A[i] =x, then int y=x put A[i]=i. Now, we need to place y
to its correct place, so repeat from step 3
"""

# program for rearrange an array such that arr[i] =i

def fix(A, len):
    for i in range(0, len):
        if(A[i] != -1 and A[i] != i):
            x = A[i]

            # check if desired place is not vacate
            while(A[x] != -1 and A[x] !=x):
                # store the value from desired place
                y = A[x]

                # place the x to its correct position
                A[x] =x

                # now y will become x, now search the place for x
                x = y

            # place the x to its correct position
            A[x] =x

            # check if the while loop hasn't set the correct value at A[i]
            if(A[i] != i):
                # if not the put -1 at the vacated place
                A[i] =-1

A = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
 
fix(A, len(A))
 
for i in range(0, len(A)):
    print(A[i], end=' ')

print("Approach 3: HashSet")
"""
Approach 3: Using HashSet
1) Store all the numbers present in the array into a HashSet 
2) Iterate through the length of the array, if the corresponding position element 
is present in the HashSet, then set A[i] = i, else A[i] = -1
"""

# program for rearranging an array such that arr[i] = i
def fixHash(A):
    s =set()

    # storing all the values in the Set
    for i in range(len(A)):
        s.add(A[i])

    for i in range(len(A)):
        # check for item if present in set
        if i in s:
            A[i] =i
        else:
            A[i] =-1
    return A

if __name__ == "__main__":
    A = [-1, -1, 6, 1, 9,3, 2, -1, 4,-1]
    print(fixHash(A))

print("\n Approach 4: \n")

"""
Approach 4:  Swap elements in Array
1) iterate through elements in an array
2) if arr[i] >= 0 && arr[i] !=i, put arr[i] at i(swap arr[i] with arr[arr[i]])

Time Complexity: O(n)
"""

# program for rearranging an array such that arr[i] =i
if __name__=='__main__':
    arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
    n = len(arr)
    i =0
    while i < n:
        if(arr[i] >=0 and arr[i] != i):
            arr[arr[i]], arr[i] = arr[i],arr[arr[i]]
        else:
            i += 1

    for i in range(n):
        print(arr[i], end=" ")



