"""

A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.

For example, in array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.
Write a function:

def solution(A)

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, as explained in the example above.

Write an efficient algorithm for the following assumptions:

N is an odd integer within the range [1..1,000,000];
each element of array A is an integer within the range [1..1,000,000,000];
all but one of the values in A occur an even number of times.
"""

#function times out
def solution(A):
    for element in A:
        if(A.count(element) ==1 ):
            return element


# takes 2 minutes in total -OddOccurrencesInArray
def solution1(A):
   result = 0
   for number in A:
     result ^= number
   return result
#O(N)


#Big-O Calculation
def solution2(A):
    if len(A) == 1:
         return A[0]
    A = sorted(A)       # O(n*log(N) or N)
    for i in range(0 , len (A) , 2): # O(N)
         if i+1 == len(A):
             return A[i]
         if A[i] != A[i+1]:
             return A[i]
# O(N*log(N) or O(N))

# function to get unique values
# def unique(list1):
#     x = np.array(list1)
#     print(np.unique(x))
#
y = [9, 3, 9, 3, 9, 7,9];
print(solution1(y));


