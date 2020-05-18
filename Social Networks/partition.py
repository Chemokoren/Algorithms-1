#
# Write partition to return a new array with
# all values less then `v` to the left
# and all values greater then `v` to the right
#

L =[31,45,91,51,66,82,28,33,11,89,84,27,36]
def partition(L, v):
    P = []
    W = []
    for val in L:
        if val < v:
            P.append(val)
        if val > v:
            W.append(val)
    return P+[v]+W

print(partition(L,84))

