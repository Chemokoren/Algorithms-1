"""
Tasks Details
Medium
1. CountNonDivisible
Calculate the number of elements of an array that are not divisors of each element.
Task Score
100%
Correctness
100%
Performance
100%
Task description
You are given an array A consisting of N integers.

For each number A[i] such that 0 ≤ i < N, we want to count the number of elements of the array that are not the divisors of A[i]. We say that these elements are non-divisors.

For example, consider integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 3
    A[4] = 6
For the following elements:

A[0] = 3, the non-divisors are: 2, 6,
A[1] = 1, the non-divisors are: 3, 2, 3, 6,
A[2] = 2, the non-divisors are: 3, 3, 6,
A[3] = 3, the non-divisors are: 2, 6,
A[4] = 6, there aren't any non-divisors.
Write a function:

def solution(A)

that, given an array A consisting of N integers, returns a sequence of integers representing the amount of non-divisors.

Result array should be returned as an array of integers.

For example, given:

    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 3
    A[4] = 6
the function should return [2, 4, 3, 2, 0], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..50,000];
each element of array A is an integer within the range [1..2 * N].
"""


A = [3, 1, 2, 3, 6]
def solution(A):
    my_list =[]
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i] % A[j] !=0:
                my_list.append(i)
    # mylist = list(dict.fromkeys(my_list))
    return my_list


def solution1(A):
 N=len(A)
 num_non_divisors=[0]*N
 if N<2:
  return num_non_divisors
 MaxVal=max(A)
#Trivial cases
 if MaxVal < 2:
     return num_non_divisors
 MinVal=min(A)
 if MinVal==MaxVal:
  return num_non_divisors
 Occur = [0] * (MaxVal + 1)
#Occurences of e in A
 for e in A:
      Occur[e]+=1
#Divisors of any element lower than MaxVal
 Divisors = [Occur[1]] * (MaxVal + 1)
#DejaVu to avoid counting them more than once
 DejaVu = [0] * (MaxVal + 1)

 for e in A:
     if e!=1 and DejaVu[e]==0:
      Divisors[e]+=Occur[e]
      DejaVu[e]+=1

 i = 2
 while (i * i <= MaxVal):
#We start at i x i to avoid counting 2 times multiples of the form k x i, where k<i.
   k =  i * i
   while (k <= MaxVal):
     Divisors[k] += Occur[i]
     if i * i < k: #equivalent k/i != i
     #Symmetric divisor
         Divisors[k] += Occur[int(k/i)];
     k += i
   i += 1
#Re-initialize DejaVu
 DejaVu = [0] * (MaxVal + 1)
 for i in range(0,len(A)):
    if not DejaVu[A[i]]:
     DejaVu[A[i]]=N-Divisors[A[i]]
    num_non_divisors[i]=DejaVu[A[i]]
 return num_non_divisors


print(solution(A))




"""
################################# Logic ####################################
First it counts the occurrences of each number in the array.

Then for each array element i it finds the number of its divisors in a range from 1 to sqrt(i), including the divisors which are the result of the division.

Finally it subtracts a total number of divisors for given element from a total number of elements in the array.
"""
