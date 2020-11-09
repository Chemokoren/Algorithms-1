import queue
q = queue.PriorityQueue()

q.put((10,'Hello World'))
q.put((15,'Mars'))
q.put((15,'Important'))

print(q.get())

text ="A A A A A A A B B B B B C C C C C C D D D"

d ={}
for word in text.split(" "):
    if word in d:
        d[word] =d[word]+1
    else:
        d[word] =1

pq = queue.PriorityQueue()
for word, number in d.iterms():
    pq.put(number, word)
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())