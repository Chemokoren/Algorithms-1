"""
The derangement problem is the problem of finding the number of permutations of a set 
of n distinct objects such that no object appears in its original position.

The formula for the number of derangements is given by the following recursive relation:

D(n) = (n-1) [D(n-1) + D(n-2)]

with D(0) = 1 and D(1) = 0

"""

class CountDerangementsRec:
    def __init__(self, set_size):
        self.set_size =set_size

    def count_derangements(self):
        return self.count_derangements_rec(self.set_size)

    def count_derangements_rec(self,n):
        if n == 1:
            return 0
        if n == 2:
            return 1
        return (n - 1) * (self.count_derangements_rec(n - 1)) + self.count_derangements_rec(n - 2)

# for i in range(1, 64):
for i in range(1, 11):
    n = CountDerangementsRec(i).count_derangements()
    print("Derangements in set size {} -> {} ".format(i,n))