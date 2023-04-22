class MaxSubArrayTopDown:
    def __init__(self,prices):
        self.prices = prices
        self.sub_solutions = [None] * len(prices)

    def max_sub_array(self):
        max_value = 0
        for j in range(len(self.prices)):
            max_value = max(max_value, self.max_sub_array_ending_at(j))
        return max_value

    def max_sub_array_ending_at(self, i):
        if self.sub_solutions[i] is not None:
            return self.sub_solutions[i]
        if i == 0:
            return self.prices[0]
        m = max(self.prices[i], self.max_sub_array_ending_at(i - 1) + self.prices[i])
        self.sub_solutions[i] =m
        return m

msa = MaxSubArrayTopDown([5, -4, 8, -10, -2, 4, -3, 2, 7, -8, 3, -5, 3])
print(msa.max_sub_array())

def MaxSubArrayTopDown1(prices):
    sub_solutions = [None] * len(prices)
    max_value = 0
    if len(prices) == 0:
            return 0
    sub_solutions[0]=prices[0] 
    for j in range(1,len(prices)):
        if sub_solutions[j] is not None:
            return sub_solutions[j]
        m = max(prices[j], (sub_solutions[j - 1] + prices[j]))
        sub_solutions[j] =m
        max_value = max(max_value, m)
    return max_value

print("#####################")
print(MaxSubArrayTopDown1([5, -4, 8, -10, -2, 4, -3, 2, 7, -8, 3, -5, 3]))
print(MaxSubArrayTopDown1([]))