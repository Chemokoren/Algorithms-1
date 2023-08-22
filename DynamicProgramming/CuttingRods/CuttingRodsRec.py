"""
Given a rod of length n and prices P[i] for i=1, ..., n, where P[i] is the price of a
rod of length i. Find the maximum total revenue you can make by cutting and selling
the rod (Assume no cost for cutting the rod).
"""

def CuttingRodsRec(n, prices):
	if n == 0:
		return 0
		
	max_val =-1
	
	for i in range(0,n):
		temp = prices[n-i-1] +CuttingRodsRec(i, prices)
		if(temp >max_val):
			max_val = temp
			
	return max_val
	
	
def rod_cutting_recursive(n, prices):
    if n == 0:
        return 0
    max_revenue = -1
    for i in range(1, n+1):
        cut_revenue = prices[i-1] + rod_cutting_recursive(n-i, prices)
        max_revenue = max(max_revenue, cut_revenue)
    return max_revenue

prices= [1,5, 8, 9, 10]
print(rod_cutting_recursive(5, prices))