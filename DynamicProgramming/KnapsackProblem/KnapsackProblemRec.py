"""
Given a set of n items, where item i has weight w[i] and value v[i], and a knapsack with
capacity w.

suppose you are to pick a few elements from the n elements such that their weight is less
than or equal to w but their summed value is maximized (maximization problem)

Example:

w[1]=8, v[1]=10
w[2]=5, v[2]=12
w[3]=8, v[3]=21

optimum is to choose 1 of object 1, and 1 of object 2, for total weight of 2+5=7 and total
value is 10+12. This is the maximum possible value with 8 weight.

Approach 1:

Define R[j] to be the largest obtainable value for a knapsack with capacity j
R[j]=max(0, v[1]+R[j-w[1]], v[2]+R[j-w[2]], ..., v[n]+R[j-w[n]])
Base Case: R[j] = 0, j <= 0

Wrong Solution! Because we might pack more than once from the same item!
So, we have to change our definition of R to take this into consideration.

PSEUDOCODE

Let R[0..n, O..W] be a new 2D array all 0
for i= 1 to n:
    for j=1 to W:
        if(j-w[i] >= 0 and v[i]+R[i-1][j-w[i]] > R[i-1][j]):
                R[i][j] =v[i] + R[i-1][j-w[i]]

        else
                R[i][j] = R[i-1][j]

    Return R[n][W]

"""

def KnapsackProblemRec(n, W, w, v): # int n, W, vectors W & v
    R = (n+1, w+1)
    for i in range(1,n):
        for j in range(1,W,1):
            if(j-w[i] >= 0 and v[i-1]+R[i-1][j-w[i-1]] > R[i-1][j]):
                R[i][j] =v[i-1] + R[i-1] [j-w[i-1]]
            else:
                R[i][j] = R[i-1][j]

    return R[n][W]

weights =[5,4,6,3]
values =[10,40,30,50]

# KnapsackProblemRec(4,9, weights,values)


def knapsack_recursive(n, w, weights, values):
    # Base case
    if n == 0 or w == 0:
        return 0
  
    # If weight of the nth item is more than the capacity of the knapsack, it cannot be included
    if weights[n-1] > w:
        return knapsack_recursive(n-1, w, weights, values)

    # Recursive case
    else:
        # Maximum value of either including the nth item or not
        return max(values[n-1] + knapsack_recursive(n-1, w-weights[n-1], weights, values),
                   knapsack_recursive(n-1, w, weights, values))

print("ggg::", knapsack_recursive(4,9, weights,values))


# solution
def knapsack_problem(capacity, weights, profits, n):
    """
    capacity: size of the bag
    weights: items weight
    profits: profits of the given items
    n : number of weights
    """
    if(n ==0 or capacity ==0):
        return 0
    if(weights[n-1] > capacity):
        return knapsack_problem(capacity, weights, profits, n-1)
    else:
        return max(profits[n-1]+knapsack_problem(capacity-weights[n-1],\
            weights, profits, n-1), \
            knapsack_problem(capacity, weights, profits, n-1))
    
profits=[24, 18, 18, 10]
weights =[24, 10, 10, 7]
capacity=25
n =len(weights)

print("::",knapsack_problem(capacity, weights, profits, n))


"""
Example:

We can only take 2 kg of Fruits. How much do we take of each fruit to maximize our profit?

fruitname       weight(g)           profit/unit
avacado         170                 2.2
pomelo          1500                8
durian          1500                22
cucamelon       15                  0.26
lychee          20                  0.4
star apple      200                 1

# assumption
- we are taking whole fruits not fractions

Solution methods
- greedy approximation
- dynamic programming
- dominance relations

Greedy approximation
--------------------
Take the fruit with the highest profit that does not exceed the weight limit
- simple
- Not guaranteed to be optimial
"""
items=[('avocado', 2.2, 170), ('pomelo', 8, 1500), ('durian', 22, 1500), \
    ('cucamelo',0.26, 51), ('lychee',0.4, 20), ('star apple',1,200)]

def greedy_fruit(items, capacity):
    items =sorted(items, key=lambda item:item[1], reverse=True)
    chosen_fruits ={}
    profit=0
    
    for i in range(len(items)):
        name, value, weight = items[i]
        num_of_fruit =(capacity - capacity % weight) / weight
        chosen_fruits[name] = num_of_fruit
        capacity = capacity % weight
        profit += num_of_fruit * value
    return round(profit, 2), chosen_fruits


def greedy_fruit_dantzig(items, capacity):
    items =sorted(items, key=lambda item:item[1]/item[2], reverse=True)
    chosen_fruits ={}
    profit=0
    
    for i in range(len(items)):
        name, value, weight = items[i]
        num_of_fruit =(capacity - capacity % weight) / weight
        chosen_fruits[name] = num_of_fruit
        capacity = capacity % weight
        profit += num_of_fruit * value
    return round(profit, 2), chosen_fruits
        
    
print(greedy_fruit(items, 2000))
print(greedy_fruit_dantzig(items, 2000))

def dynamic_fruit(items, capacity):
    bag =[0 for i in range(capacity+1)]
    for i in range(capacity + 1):
        for j in range(len(items)):
            _, value, weight =items[j]
            if(weight < i):
                bag[i]= max(bag[i], bag[i-weight]+value)
    return round(bag[capacity])


print("dynamic::",dynamic_fruit(items, 2000))