# class StringDistanceOpt:
#     def __init__(self, str_A, str_B):
#         self.str_A =str_A
#         self.str_B = str_B

#         self.dist_read =[-1] * (len(str_B) + 1)
#         self.dist_write =[-1] * (len(str_B) + 1)

#         for a in range(len(str_A) + 1):
#             for b in range(len(str_B) + 1):
#                 if a == 0:
#                     self.dist_write[b] =b
#                 elif b== 0:
#                     self.dist_write[b] = a
#                 else:
#                     replace_cost =0 if self.str_A[a - 1] == self.str_B[b - 1] else 1
#                     cost_delete =self.dist_read[b] + 1
#                     cost_insert =self.dist_write[b - 1] + 1
#                     cost_replace =self.dist_read[b -1] + replace_cost
#                     min_cost =min(cost_delete, cost_insert, cost_replace)
#                     self.dist_write[b] = min_cost(self.dist_read, self.dist_write)
#                     print(self.dist_read)

#     def distance(self):
#         return self.dist_read[len(self.str_B)]

# # dist =StringDistanceBottomUp("TodayIsSaturday", "TomorrowIsSunday")
# dist = StringDistanceOpt("Saturday", "Sundays")
# print(dist.distance())


print("##################### Optimized #####################")
class StringDistanceBottomUpOptimized:
    def __init__(self, str_A, str_B):
        self.str_A = str_A
        self.str_B = str_B
        self.prev_row = list(range(len(str_B) + 1))
        self.curr_row = [0] * (len(str_B) + 1)
        for a in range(1, len(str_A) + 1):
            self.curr_row[0] = a
            for b in range(1, len(str_B) + 1):
                replace_cost = 0 if self.str_A[a - 1] == self.str_B[b - 1] else 1
                cost_delete = self.prev_row[b] + 1
                cost_insert = self.curr_row[b - 1] + 1
                cost_replace = self.prev_row[b - 1] + replace_cost
                self.curr_row[b] = min(cost_delete, cost_insert, cost_replace)
            self.prev_row, self.curr_row = self.curr_row, self.prev_row

    def distance(self):
        return self.prev_row[-1]

dist = StringDistanceBottomUpOptimized("TodayIsSaturday", "TomorrowIsSunday")
print(dist.distance())