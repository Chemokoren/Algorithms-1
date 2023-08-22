class CountDerangementsOpt:
    def __init__(self,set_size):
        self.set_size =set_size
        self.solution_n, solution_n_minus_1, solution_n_minus_2 =0,0,0
        for n in range(1, set_size+1):
            if n == 1:
                self.solution_n =0
            elif n == 2:
                self.solution_n =1
            else:
                self.solution_n =(n - 1) * (solution_n_minus_1 + solution_n_minus_2)
            solution_n_minus_2 =solution_n_minus_1
            solution_n_minus_1 = self.solution_n
    def count_derangements(self):
        return self.solution_n

# for i in range(1,64):
# # for i in range(1,11):
#     n = CountDerangementsOpt(i).count_derangements()
#     print("Derangements in set size {} -> {} ".format(i,n))
    
"""
we can optimize the bottom-up approach to further reduce the space complexity from O(n) to
O(1).

The current bottom-up approach uses an array dp of size n+1 to store the results of 
subproblems. However, since we only need the values of dp[i-1] and dp[i-2] to
compute dp[i], we can use two variables to store these values instead of an entire array.
This reduces the space complexity to O(1).

"""
            
def count_derangements(n):
    if n == 0:
        return 1
    elif n == 1:
        return 0
    else:
        initial = 1
        prev = 0
        result = 0
        for i in range(1, n+1):
            result = (i-1) * (initial + prev)
            prev, initial = initial, result
        return result

    
for i in range(1,11):
    n = count_derangements(i)
    print("{} -> {} ".format(i,n))
    
"""
Another variation
"""
def count_derangements1(n):
    if n == 0:
        return 1
    elif n == 1:
        return 0
    else:
        prev_prev_count = 1
        prev_count = 0
        current_count = 0
        for i in range(2, n+1):
            current_count = (i-1) * (prev_prev_count + prev_count)
            prev_prev_count = prev_count
            prev_count = current_count
        return current_count
print("variation::", count_derangements1(5))
for i in range(1,11):
    n = count_derangements1(i)
    print("{} -> {} ".format(i,n))
    