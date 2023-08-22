# O(nd) time | O(n) space
def numberOfWaysToMakeChange(n,denoms):
    ways =[0 for amount in range(n +1)]
    ways[0] = 1
    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]
    return ways[n]


def change(amount, coins):
    if (len(coins) == 0):
        return 0
    f =[0 for amount in range(amount +1)]
    # f[0] = amount + 1
    f[0] = 1 # This is the base case
    for coin in coins:
        for value in range(1,amount+1):
            if (coin <= value):
                f[value] += f[value - coin]
    return f[amount]



# amount =10
# denominations =[1,5,10,25]
amount =5
denominations =[1,2,5]

# print(numberOfWaysToMakeChange(amount,denominations))
print(change(amount,denominations))
