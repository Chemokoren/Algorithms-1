def linearsearch(A, key):
    position =0
    flag =False
    while position < len(A) and not flag:
        if A[position] ==key:
            flag =True
        else:
            position = position + 1
    return flag

def linearsearch1(A, key):
    for position in A:
        if position ==key:
            return True
    return False
A =[84,21,47,96,15]
found =linearsearch1(A,96)
print('Element 9 is present: ', found)
