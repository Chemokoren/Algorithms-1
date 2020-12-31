class CountDerangementsBottomUp:

    def __init(self, set_size):
        self.set_size = set_size
        self.sub_solutions = [-1] * (set_size + 1)
        for n in range(1, set_size + 1):
            if n == 1:
                self.sub_solutions[n] = 0
            elif n == 2:
                self.sub_solutions[n] = 1
            else:
                self.sub_solutions[n] = (n - 1) * (self.sub_solutions[n - 1]) + self.sub_solutions[n - 2]

    def count_derangements(self):
        return self.sub_solutions[self.set_size]


# for i in range(1, 64):
for j in range(1, 11):
    n = CountDerangementsBottomUp(j).count_derangements()
    print("Derangements in set size {} -> {} ".format(j, n))
