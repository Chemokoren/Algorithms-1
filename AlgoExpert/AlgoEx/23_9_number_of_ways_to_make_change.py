"""
number of ways to make change given the target number and the denominations

general formula:

if denom <= amount:
    ways[amount] += ways[amount-denom]

"""

# O(nd) time where n is the target amount and d the number of denominations | O(n) space
def numberOfWaysToMakeChange(n, denoms):
    ways =[0 for amount in range(n+1)]
    ways[0] = 1

    for denom in denoms:
        for amount in range(1,n+1):
            if denom <= amount:
                ways[amount] += ways[amount- denom]

    return ways[n]

target =10
denominations =[1,5,10,25]

# target =9
# denominations =[5]
print(numberOfWaysToMakeChange(target, denominations))