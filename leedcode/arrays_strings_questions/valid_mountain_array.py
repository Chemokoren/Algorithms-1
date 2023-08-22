"""

"""

class Solution:
    def validMountainArray(self, A:int)->bool:
        # no mountain if Array A is less than 3
        if(len(A) < 3):
            return False
        
        i = 1
        # check if there is an increasing trend
        while (i <len(A) and A[i] >A[i-1]):
            i +=1

        # return false if the position of i remained at 1 or is at the of the array
        if(i==1 or i==len(A)):
            return False

        # check for a decreasing trend
        while(i<len(A) and A[i] < A[i-1]):
            i += 1
        
        # if after ascertaining the existence of both an increasing & decreasing trend, 
        # return  true if we are at the end, otherwise return false
        return i ==len(A)

# my_vals =[0,3,5,3, 2, 1]
my_vals =[1, 2, 3, 5, 3, 0]
sol = Solution()
print(sol.validMountainArray(my_vals))