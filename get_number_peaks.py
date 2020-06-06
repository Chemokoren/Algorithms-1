"""
Task description
A non-empty array A consisting of N integers is given.

A peak is an array element which is larger than its neighbours. More precisely, it is an index P such that 0 < P < N − 1 and A[P − 1] < A[P] > A[P + 1].

For example, the following array A:

    A[0] = 1
    A[1] = 5
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2
has exactly four peaks: elements 1, 3, 5 and 10.

You are going on a trip to a range of mountains whose relative heights are represented by array A, as shown in a figure below. You have to choose how many flags you should take with you. The goal is to set the maximum number of flags on the peaks, according to certain rules.



Flags can only be set on peaks. What's more, if you take K flags, then the distance between any two flags should be greater than or equal to K. The distance between indices P and Q is the absolute value |P − Q|.

For example, given the mountain range represented by array A, above, with N = 12, if you take:

two flags, you can set them on peaks 1 and 5;
three flags, you can set them on peaks 1, 5 and 10;
four flags, you can set only three flags, on peaks 1, 5 and 10.
You can therefore set a maximum of three flags in this case.

Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the maximum number of flags that can be set on the peaks of the array.

For example, the following array A:

    A[0] = 1
    A[1] = 5
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2
the function should return 3, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..400,000];
each element of array A is an integer within the range [0..1,000,000,000].
"""

A = [1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]


def solution(A):
    number_picks = 0
    for i in range(1, len(A) - 1):
        if A[i] > A[i + 1] and A[i] > A[i - 1]:
            number_picks = number_picks + 1
    return number_picks - 1

#solution 2

import math
def solution1(A):
 N=len(A)
#Trivial cases
 if N<3:
    return 0
 Flags_Idx=[]

 for p in range(1,N-1):
     if A[p-1]<A[p] and A[p]>A[p+1] :
         Flags_Idx.append(p)

 if len(Flags_Idx)==0:
    return 0
 if len(Flags_Idx)<=2:
     return len(Flags_Idx)
 Start_End_Flags=Flags_Idx[len(Flags_Idx)-1]-Flags_Idx[0]
#Maximum number of flags N is such that Start_End_Flags/(N-1)>=N
#After solving a second degree equation we obtain the maximal value of N
 num_max_flags=math.floor(1.0+math.sqrt(4*Start_End_Flags+1.0))/2.0

#Set the current number of flags to its total number
 len_flags=len(Flags_Idx)
 min_peaks=len(Flags_Idx)
 p=0

#Compute the minimal number of flags by checking each indexes
#and comparing to the maximal theorique value num_max_flags
 while p<len_flags-1:
    add = 1
#Move to the next flag until the condition Flags_Idx[p+add]-Flags_Idx[p]>=min(num_max_flags,num_flags)
    while Flags_Idx[p+add]-Flags_Idx[p]<min(num_max_flags,min_peaks):
         min_peaks-=1
         if p+add<len_flags-1:
          add+=1
         else:
             p=len_flags
             break
    p+=add

 if num_max_flags==min_peaks:
  return min_peaks
#Bisect the remaining flags : check the condition
#for flags in [min_peaks,num_max_flags]
 num_peaks=min_peaks
 for nf in range (min_peaks,int(num_max_flags)+1):
  cnt=1
  p=0
  while p<len_flags-1:
    add = 1
    while Flags_Idx[p+add]-Flags_Idx[p]<nf:
         if p+add<len_flags-1:
          add+=1
         else:
             cnt-=1
             p=len_flags
             break
    p+=add
    cnt+=1
  num_peaks=max(min(cnt,nf),num_peaks)
 return num_peaks

print(solution1(A))
