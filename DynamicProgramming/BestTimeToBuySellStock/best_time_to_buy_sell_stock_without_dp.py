"""
This problem can be solved using a simple approach known as "buy low, sell high". 

The idea is to find the lowest price to buy the stock and the highest price to sell it, 
which gives us the maximum profit.

Here's the algorithm to solve this problem:

    Initialize two variables, min_price and max_profit, to the first element of the array.
    Traverse the array from the second element to the last.
    For each element, calculate the difference between the current element and the min_price.
    If the difference is greater than the current max_profit, update max_profit.
    If the current element is less than min_price, update min_price to the current element.
    After traversing the whole array, return max_profit.


"""
def max_profit(prices):
    min_price = prices[0]
    max_profit = 0
    for price in prices[1:]:
        diff = price - min_price
        if diff > max_profit:
            max_profit = diff
        if price < min_price:
            min_price = price
    return max_profit

prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))

