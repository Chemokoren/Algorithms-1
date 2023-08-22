def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

connections = [('a', 'g'), ('a', 'd'), ('d', 'g'), ('g', 'c'), ('b', 'f'),
               ('f', 'e'), ('e', 'h')]

G = {}
for (x,y) in connections: make_link(G,x,y)

###################################################################
# Transversal...
#  Call this routine on nodes being visited for the first time
def mark_component(G, node, marked):
    marked[node] = True
    total_marked = 1
    for neighbor in G[node]:
        if neighbor not in marked:
            total_marked += mark_component(G, neighbor, marked)
    return total_marked

def list_component_sizes(G):
    marked = {}
    for node in G.keys():
        if node not in marked:
            print ("Component containing", node, ": ", mark_component(G, node, marked))

list_component_sizes(G)

#check pairwise connectivity
def check_connection(G, v1, v2):
    marked = {}
    mark_component(G,v1,marked)
    return v2 in marked

print(check_connection(G,'a','g'))
