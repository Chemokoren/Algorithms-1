class MaxSubArrayBottomUp:
    def __init__(self, prices):
        self.prices = prices
        self.sub_solutions =[None] * len(prices)

        for i in range(len(self.prices)):
            if i == 0:
                self.sub_solutions[i] = self.prices[0]
            else:
                self.sub_solutions[i] = max(self.prices[i], self.sub_solutions[i - 1] + self.prices[i])

    def max_sub_array(self):
        max_value = 0
        for j in range(len(self.prices)):
            max_value = max(max_value, self.sub_solutions[j])
        return max_value

msa = MaxSubArrayBottomUp([5, -4, 8, -10, -2, 4, -3, 2, 7, -8, 3, -5, 3])
print(msa.max_sub_array())


def max_sub_array_bottom_up(prices):
    sub_solutions =[None] * len(prices)
    max_value = 0

    for i in range(len(prices)):
        if i == 0:
            sub_solutions[i] = prices[0]
        else:
            sub_solutions[i] = max(prices[i], sub_solutions[i - 1] + prices[i])
            
        max_value = max(max_value, sub_solutions[i])
    return max_value

print(max_sub_array_bottom_up([5, -4, 8, -10, -2, 4, -3, 2, 7, -8, 3, -5, 3]))