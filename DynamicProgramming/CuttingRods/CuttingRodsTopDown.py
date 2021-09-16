def CuttingRodsTopDown(n, prices):
    s =[-1] * (n+1)
    
    if n == 0:
        s[0]= 0
        
    max_val =-1
    
    for i in range(0,n):
        if(s[i] != -1):
            max_val = s[i]
        temp = prices[n-i-1 ] + CuttingRodsTopDown(i, prices)
        
        if(temp >max_val):
            max_val = temp
        s[i] =max_val
    
        
    return max_val
	
	
prices= [1, 5, 8, 9, 10]
print(CuttingRodsTopDown(5, prices))