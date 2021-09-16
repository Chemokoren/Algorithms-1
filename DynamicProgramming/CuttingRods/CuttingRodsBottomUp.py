
def CuttingRodsBottomUp(n, prices):
    R = [-1] *(n+1)
    R[0] = 0
    
    for i in range(1, n):
        max_val =-1
        for j in range(1, i):
            temp = prices[j-1] + R[i-j]
            if (temp > max_val):
                max_val=temp
    R[i] =max_val
	
	
    return R[n]

prices= [1,5, 8, 9, 10]

print(CuttingRodsBottomUp(5, prices))