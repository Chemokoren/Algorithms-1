#List of distinct two-digit values.
#Where will 84 be located in the sorted version

L =[31,45,91,51,66,82,28,33,11,89,84,27,36]

def rank(L, v):
    pos =0
    for val in L:
        if val < v:
            pos +=1
    return pos

print (rank(L,84))
