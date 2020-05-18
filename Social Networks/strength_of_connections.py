# Let's make a character-to-character graph
# Note that if an edge is added multiple times, the strength increases
import time
time1 = time.time()
charG ={}
def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] ={}
    (G[node1])[node2] =1
    if node2 not in G:
        G[node2] ={}
        (G[node2])[node1] =1
    return G

for char1 in characters:
    for book in marvelG[char1]:
        for char2 in marvelG[book]:
            make_link(charG, char1, char2)
time2 =time.time()
print( "time to compute strengths: ", time2-time1)

# Get highest k strengths.
time1 =time.time()
k= 10
heap =[]
for char1 in characters:
    for char2 in charG[char1]:
        #avoid duplicates by only including pairs where the character
        #number of the first is less than that of the second
        if characters[char1] <characters[char2]:
            if len(heap)< k:
                insert_heap(heap, (charG[char1][char2],(char1,char2)))
            elif charG[char1][char2] > val(heap[0]):


