# List of node centrality values from example graph

L = [2, 3, 2, 3, 2, 4]


def mean(L):
    total = 0
    for i in range(len(L)):
        total += L[i]
    return (0.0 + total) / len(L)
print (mean(L))

# print(0.0+ (int(sum(L))) /(int(len(L))))
