"""
A set of n items, where item i has weight w[i] and value v[i], and a knapsack with capacity
w.

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

KnapsackProblemRec(4,9, weights,values)


