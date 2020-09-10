words ='Nitume is dedicated to offer its clients an out of this world online shopping experience. Nitume timely delivers products of high quality to its customers. Furthermore, vendors access a wider market and have the opportunity to access data analytics from a single dashboard at their discretion to make informed business decisions'
counts=dict()
words.split()
for word in words:
    counts[word] =counts.get(word,0)+1
print('Counts', counts)


bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)


lst = []
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=False)
print(lst)

print( sorted( [ (v,k) for k,v in counts.items() ], reverse=True ) )
