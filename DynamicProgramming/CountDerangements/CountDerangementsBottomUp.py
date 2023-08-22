class CountDerangementsBottomUp:

    def __init(self, set_size):
        self.set_size = set_size
        self.sub_solutions = [-1] * (set_size + 1)
        for n in range(1, set_size + 1):
            if n == 0:
                self.sub_solutions[n] = 1
            elif n == 1:
                self.sub_solutions[n] = 0
            else:
                self.sub_solutions[n] = (n - 1) * (self.sub_solutions[n - 1]) + self.sub_solutions[n - 2]

    def count_derangements(self):
        return self.sub_solutions[self.set_size]


# for i in range(1, 64):
# for j in range(1, 11):
#     n = CountDerangementsBottomUp(j).count_derangements()
#     print("Derangements in set size {} -> {} ".format(j, n))

# time complexity of O(n) and a space complexity of O(n), 
def count_derangements(n):
    if n == 0:
        return 1
    elif n == 1:
        return 0
    else:
        sub_solution = [0] * (n + 1)
        sub_solution[0] = 1
        sub_solution[1] = 0
        for i in range(2, n+1):
            sub_solution[i] = (i-1) * (sub_solution[i-1] + sub_solution[i-2])
        return sub_solution[n]
    
for j in range(1, 11):
    n = count_derangements(j)
    print("Derangements in set size {} -> {} ".format(j, n))