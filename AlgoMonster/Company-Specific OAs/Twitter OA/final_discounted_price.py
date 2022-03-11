"""
(OA) 2021 | Final Discounted Price

You own an online shop. You have n items that you are selling, and for each item i (starting from zero)
, you are selling that item for prices[i] dollars.

One day, you decided to close the shop soon, but before you do that, you decided to do one last sale.
The sale works as follows: starting from the first item, for each item, you look at the prices of the 
items until you find an item that has a price less than or equal to the original item. 
If you successfully find such item, you reduce the price of the original item by the price of the 
item you found. Otherwise, no discounts are offered for that item.

Assuming that you sold out all your items during the sale, how much money do you make from the sale?

Parameter

    prices: A list of integers indicating the original prices of each item.

Result

    An integer representing the total revenue during the sale.

Examples
Example 1:

Input: prices = [2, 3, 1, 2]

Output: 6

Explanation: For item 0 and item 1, item 2 is the first item with less than or equal pricing, so item
0 and item 1 are discounted by 1. For item 2 and item 3, there are no items after them with less or 
equal pricing, so no discounts are made. Therefore, the total revenue after discount is 
1 + 2 + 1 + 2 = 6 dollars.

Constraints

    1 <= n <= 10^5
    1 <= prices[i] <= 10^6
    The final result does not exceed integer limit (2,147,483,647).

"""

from typing import List

def final_revenue(prices: List[int]) -> int:
    return 0

if __name__ == '__main__':
    prices = [int(x) for x in input().split()]
    res = final_revenue(prices)
    print(res)