
def CuttingRodsBottomUp(n, prices):
    R = [-1] *(n+1)
    R[0] = 0
    
    for i in range(1, n):
        max_val =-1
        for j in range(1, i):
            temp = prices[j-1] + R[i-j]
            if (temp > max_val):
                max_val=temp
    R[i] =max_val
	
	
    return R[n]

prices= [1,5, 8, 9, 10]

print(CuttingRodsBottomUp(5, prices))

"""
The bottom-up solution works by computing the optimal revenue for progressively longer rod
lengths, starting from a rod of length 1 and building up to the desired length n. 
The solution uses a list revenue to store the maximum revenue that can be obtained for
each rod length up to n.

The outer loop of the function iterates over each rod length from 1 to n. For each rod 
length i, the function computes the maximum revenue that can be obtained by trying all 
possible cuts of length j from 1 to i, and adding the price of the cut prices[j - 1] to 
the maximum revenue that can be obtained from the remaining rod length i - j (which is 
stored in the revenue list). The maximum revenue over all possible cuts is then stored 
in the revenue list for the current rod length i.

After the outer loop has finished, the function returns the maximum revenue that can be 
obtained for a rod of length n, which is stored in the last element of the revenue list.

The time complexity of the bottom-up solution is O(n^2), since we need to compute the
optimal revenue for each rod length up to n, and for each rod length, we need to try all
possible cuts up to that length. The space complexity is also O(n), since we need to 
store the maximum revenue for each rod length up to n.

"""
def rod_cutting_bottom_up(n, prices):
    revenue = [0] * (n + 1)
    for i in range(1, n + 1):
        max_revenue = -1
        for j in range(1, i + 1):
            max_revenue = max(max_revenue, prices[j - 1] + revenue[i - j])
        revenue[i] = max_revenue
    return revenue[n]

print(rod_cutting_bottom_up(5, prices))