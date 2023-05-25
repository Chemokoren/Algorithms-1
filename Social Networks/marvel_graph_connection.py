"""
# Compute connection Strength

write a program to read the Marvel graph and put a strength value on each link. WHich link has the highest strength value?

# Lets make a character to character graph
# Note that if an edge is added multiple times, the strength increases
"""
time1 =time.time()
charG ={}
for char1 in characters:
    for book in marvelG[char1]:
        for char2 in marvelG[book]:
            make_link(charG, char1, char2)
time2 =time.time()
print "time to compute strengths: ", time2-time1

# Get highest k strengths.
time1 =time.time()
k=10
heap =[]
for char1 in characters:
    for char2 in charG[char1]:
        # avoid duplicates by only including pairs where the character
        # number of the first is less than that of the second
        if characters[char1] < characters[char2]:
            if len(heap) < k:
                insert_heap(heap,(charG[char1][char2],(char1,char2)))
            elif charG[char1][char2] > val(heap[0]);
            

