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

def rod_cutting_tp(n, prices):
    sub_solutions =[-1]*(n+1)
    
    sub_solutions[0]=0
    max_revenue = -1
    
    for i in range(1, n+1):
        if sub_solutions[i] !=-1:
            return sub_solutions[i]
        cut_revenue = prices[i-1] + rod_cutting_tp(n-i, prices)
        max_revenue = max(max_revenue, cut_revenue)
        sub_solutions[i] =max_revenue
    return sub_solutions[n]

prices= [1,5, 8, 9, 10]
print(rod_cutting_tp(5, prices))


"""
The line cache[n] = max_revenue is outside the for loop in the top-down optimized 
version of rod_cutting_recursive because we only want to store the maximum revenue for
the current rod length n, not for each possible cut i.

If we were to put the line cache[n] = max_revenue inside the for loop, we would end up 
caching the maximum revenue for every possible cut length i, which would be unnecessary 
and would take up more memory.

By placing cache[n] = max_revenue outside the for loop, we ensure that only the maximum 
revenue for the entire rod length n is cached, which is what we need for the 
optimization to work.
"""
def rod_cutting_recursive(n, prices, cache={}):
    if n == 0:
        return 0
    if n in cache:
        return cache[n]
    max_revenue = -1
    for i in range(1, n+1):
        cut_revenue = prices[i-1] + rod_cutting_recursive(n-i, prices, cache)
        max_revenue = max(max_revenue, cut_revenue)
    cache[n] = max_revenue
    return cache[n]

prices= [1,5, 8, 9, 10]
print(rod_cutting_recursive(5, prices))