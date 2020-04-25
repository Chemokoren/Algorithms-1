def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] ={}
    (G[node1])[node2] =1
    if node2 not in G:
        G[node2] ={}
        (G[node2])[node1] =1
    return G
(a,b,c,d,e,f,g) =('A', 'B', 'C', 'D', 'E', 'F', 'G')

triples =((a,c,3),(c,b,10),(a,b,15),(d,b,9),(a,d,4),(d,f,7),(d,e,3),(e,g,1),(e,f,5),(f,g,2),(b,f,1))

G ={}

for(i,j,k) in triples:
    make_link(G,i,j,k)

def shortest_dist_node(dist):
    best_node ='undefined'
    best_value =1000000
    for v in dist:
        if v in dist:
            if dist[v] < best_value:
                (best_node,best_value) =(v, dist[v])
    return best_node

def dijkstra(G, v):
    dist_so_far ={}
    dist_so_far[v] =0
    final_dist ={}
    while len(final_dist) <len(G):
        w = shortest_dist_node(dist_so_far)
        # lock it down !
        print ("lock", w, dist_so_far[w])
        final_dist[w] =dist_so_far[w]
        del dist_so_far[w]
        for x in G[w]:
            if x not in final_dist:
                if x not in dist_so_far:
                    dist_so_far[x] = final_dist[w] + G[w][x]
                elif final_dist[w] + G[w] [x] < dist_so_far[x]:
                    dist_so_far[x] =final_dist[w] + G[w][x]
        return final_dist
print (dijkstra(G,a))
