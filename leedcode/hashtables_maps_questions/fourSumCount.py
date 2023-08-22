"""
Given four lists A,B,C,D of integer values compute how many
tuples (i,j,k,l) there are such that   A[i] +B[j] + C[k] + D[l]
is zero. In other words, we want to find 4 indices such that the
summation of elements at those indices sum up to zero.



Solution:
Find pair of numbers that sum up to some number x in arrays 
A and B

Find pair of numbers in the other 2 arrays that sum up to -x 
in arrays C and D
"""
class Solution:
    def fourSumCount(self, A: int,B: int,C:int, D: int):
        m ={}
        ans = 0

        for i in range(0, len(A)):
            x = A[i]
            for j in range(0, len(B)):
                y = B[j]
                if(x+y not in m):
                    m[x+y] = 0
                m[x+y] +=1

        for i in range(0, len(C)):
            x = C[i]
            for j in range(0, len(D)):
                y = D[j]
                target =-(x+y)
                if(target in m):
                    ans += m[target]

        return ans

A   =[1,2]
B   =[-2,-1]
C   =[-1,2]
D   =[0,2]

sol = Solution()
print(sol.fourSumCount(A,B,C,D))