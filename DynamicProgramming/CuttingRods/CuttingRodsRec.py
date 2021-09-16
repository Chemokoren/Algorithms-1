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
	
	
prices= [1,5, 8, 9, 10]
print(CuttingRodsRec(5, prices))