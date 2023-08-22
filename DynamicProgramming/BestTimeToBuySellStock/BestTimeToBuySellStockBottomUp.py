'''
time complexity: O(n^2)
'''

def BestTimeToBuySellStockBottomUp(n, prices):
    R = [-1] * (n)
    
    R[0] = 0
    for i in range(1,n):
        R[i] =R[i-1]
        for j in range(0,i,1):
            R[i] = max(R[i],prices[i]-prices[j])
    return R[n-1]


'''
optimization solution: O(n)
'''
def BestTimeToBuySellStockBottomUp1(n, prices):
    sub_solution = [-1] * (n)
    
    sub_solution[0] = 0
    min_val =prices[0]

    for i in range(1,n-1):
        min_val = min(min_val,prices[i])
        sub_solution[i] = max(sub_solution[i-1],prices[i]-min_val)
    return sub_solution[n-1]

	
prices = [7, 1, 5, 4, 6, 4]
# prices = [7, 6, 4, 3, 1]

# print(BestTimeToBuySellStockTopDown(5, prices))
print(BestTimeToBuySellStockBottomUp1(6, prices))

