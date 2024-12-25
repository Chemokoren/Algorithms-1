A=['red','green','blue','white','black']
print('original list:', A)
print('sorted list A:', sorted(A))
A.sort(key=len)
print('sorted list B:', A)