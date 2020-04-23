
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
        w =shortest_dist_node(dist_so_far)
        # lock it down !
        print ("lock", w, dist_so_far[w])
        final_dist[w] =dist_so_far[w]
        del dist_so_far[w]
        for x in G[w]:
            if x not in final_dist:
                if x not in dist_so_far:
                    dist_so_far[x] =final_dist[w] + G[w][x]
                elif final_dist[w] + G[w] [x] < dist_so_far[x]:
                    dist_so_far[x] =final_dist[w] + G[w][x]
        return final_dist
print (dijkstra(G,a))
