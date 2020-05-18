import csv
import time

def make_link(G, node1, node2):
    G[node1] ={}
    (G[node1])[node2] =1
    G[node2] ={}
    (G[node2])[node1] =1
    return G
def read_graph(filename):
    # reads an undirected graph in csv format. Each line is an edge
    tsv =csv.reader(open(filename), delimiter='\t')
    G = {}
    for(node1, node2) in tsv: make_link(G, node1,node2)
    return G
#read the marvel comics graph
marvelG =read_graph("uniq_edges.tsv")

def centrality(G, v):
    distance_from_start ={}
    open_list =[v]
    distance_from_start[v] =0
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            if neighbor not in distance_from_start:
                distance_from_start[neighbor] =distance_from_start[current] + 1
                open_list.append(neighbor)
    return (sum(distance_from_start.values())+0.0) /len(distance_from_start)

from_node ="A"
to_node="ZZZAX"
print (centrality(marvelG,from_node))

