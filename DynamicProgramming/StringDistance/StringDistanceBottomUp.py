class StringDistanceBottomUp:
    def __init__(self, str_A, str_B):
        self.str_A =str_A
        self.str_B = str_B
        self.dist =[[]] * (len(str_A) + 1)
        for a in range(len(str_A) + 1):
            self.dist[a] = [-1] * (len(str_B) + 1)
            for b in range(len(str_B) + 1):
                if a == 0:
                    self.dist[a][b] =b
                elif b == 0:
                    self.dist[a][b] =a
                else:
                    replace_cost = 0  if self.str_A[a - 1] == self.str_B[b - 1] else 1
                    cost_delete =self.dist[a - 1] [b] + 1
                    cost_insert = self.dist[a][b - 1] + 1
                    cost_replace = self.dist[a - 1][b -1] + replace_cost
                    min_cost =min(cost_delete,cost_insert, cost_replace)
                    self.dist[a][b] =min_cost
            print(self.dist[a])

    def distance(self):
        return self.dist[len(self.str_A)][len(self.str_B)]

# dist =StringDistanceBottomUp("TodayIsSaturday", "TomorrowIsSunday")
dist = StringDistanceBottomUp("Saturday", "Sundays")
print(dist.distance())


print("############ optimization ############")

class StringDistanceBottomUpOpt:
    def __init__(self, str_A, str_B):
        self.str_A = str_A
        self.str_B = str_B
        self.dist = [[-1] * (len(str_B) + 1) for _ in range(len(str_A) + 1)]
        for a in range(len(str_A) + 1):
            self.dist[a][0] = a
        for b in range(len(str_B) + 1):
            self.dist[0][b] = b
        for a in range(1, len(str_A) + 1):
            for b in range(1, len(str_B) + 1):
                replace_cost = 0 if self.str_A[a - 1] == self.str_B[b - 1] else 1
                cost_delete = self.dist[a - 1][b] + 1
                cost_insert = self.dist[a][b - 1] + 1
                cost_replace = self.dist[a - 1][b - 1] + replace_cost
                self.dist[a][b] = min(cost_delete, cost_insert, cost_replace)
            print(self.dist[a])
    def distance(self):
        return self.dist[len(self.str_A)][len(self.str_B)]

# dist = StringDistanceBottomUpOpt("TodayIsSaturday", "TomorrowIsSunday")
dist = StringDistanceBottomUp("Saturday", "Sundays")
print(dist.distance())
