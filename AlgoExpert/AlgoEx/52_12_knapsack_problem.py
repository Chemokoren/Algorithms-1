"""
Knapsack Problem
"""
# O(nc) time | O(nc) space
from typing import Sequence


def knapsackProblem(items, capacity):
    knapsackValues =[[0 for x in range(0, capacity+1)] for y in range(0,len(items)+1)]
    for i in range(1, len(items) + 1):
        currentWeight = items[i-1][1]
        currentValue = items[i-1][0]
        for c in range(0,capacity +1):
            if currentWeight > c:
                knapsackValues[i][c] =knapsackValues[i-1][c]
            else:
                knapsackValues[i][c] = max(knapsackValues[i-1][c],knapsackValues[i-1][c-currentWeight]+currentValue)

        return [knapsackValues[-1][-1],getKnapSackItems(knapsackValues,items)]

def getKnapSackItems(KnapsackValues, items):
    sequence =[]
    i = len(KnapsackValues) -1
    c = len(KnapsackValues[0]) -1

    while i > 0:
        if KnapsackValues[i][c] == KnapsackValues[i-1][c]:
            i -=1

        else:
            sequence.append(i-1)
            c -= items[i-1][1]
            i -= 1
        if c == 0:
            break
    return list(reversed(sequence))

my_capacities =[0,1,2,3,4,5,6,7,8,9,10]
my_items=[[1,2],[4,3],[5,6],[6,7]]

print(knapsackProblem(my_items,my_capacities))

