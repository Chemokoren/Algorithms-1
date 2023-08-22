d ={'a':10,'b':1,'c':22}
t=sorted(d.items())
print(t)
for k, v in sorted(d.items()):
	print(k,v)


print("#########################################")

c ={'a':10,'b':1,'c':22}
tmp =list()
for k, v in c.items():
	tmp.append((v,k))
print(tmp)
tmp =sorted(tmp, reverse=True)
print(tmp)
print("top 2 in the list")
for val, key in tmp[:2]:
	print(key,val)

#List comprehension creates a dynamic list. In this case, we make a list of reversed tuples and then sort it.
print(sorted([(v,k) for k,v in c.items()], reverse=True))