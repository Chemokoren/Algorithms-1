def BestTimeToBuySellStockTopDown(i, prices):
    sub_solutions =[-1] *(i+1)
    
    if (i == 0):
        return 0
        
    max_val = BestTimeToBuySellStockTopDown(i-1,prices)
    
    for j in range(1,i+1):
        if sub_solutions[j] != -1:
            max_val =sub_solutions[j]
        max_val = max(max_val,prices[i - 1]-prices[j -1])
        sub_solutions[j] =max_val
    return max_val
	
prices = [7, 1, 5, 4, 6, 4]
# prices = [7, 6, 4, 3, 1]

# print(BestTimeToBuySellStockTopDown(5, prices))
print(BestTimeToBuySellStockTopDown(6, prices))