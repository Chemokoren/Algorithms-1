"""
problem statement:

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one 
share of the stock), design an algorithm to find the maximum profit.

Examples:

input: [7, 1, 5, 3, 6, 4]

output: 5

max. difference = 6-1 = 5 (not 7-1, as selling price needs to be larger than buying price)

maximization problem - we want to maximize the amount of money that we can make.


"""


def BestTimeToBuySellStockRec(i, prices):
	if (i == 0):
		return 0
		
	max_val = BestTimeToBuySellStockRec(i-1,prices)
	
	for j in range(1,i+1):
		max_val = max(max_val,prices[i - 1]-prices[j -1])
		
	return max_val
	
prices = [7, 1, 5, 4, 6, 4]
# prices = [7, 6, 4, 3, 1]
# prices = [1, 2, 3, 4, 5]

# print(BestTimeToBuySellStockRec(6, prices))
print(BestTimeToBuySellStockRec(5, prices))