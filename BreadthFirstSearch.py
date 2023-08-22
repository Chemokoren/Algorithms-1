import csv
import time

def make_link(G, node1, node2):
    G[node1] ={}
    (G[node1])[node2] =1
    G[node2] ={}
    (G[node2])[node1] =1
    return G

"""
creates an empty dictionary G, then iterates through each line of the CSV file and adds the corresponding 
edge to G using the make_link function.
returns a dictionary representing the graph
"""
def read_graph(filename):
    # reads an undirected graph in csv format. Each line is an edge
    tsv =csv.reader(open(filename), delimiter='\t')
    G = {}
    for(node1, node2) in tsv: make_link(G, node1,node2)
    return G
#read the marvel comics graph
marvelG =read_graph("uniq_edges.tsv")


"""
The path function takes a graph G and two nodes v1 and v2, and returns the shortest path between the two 
nodes using a BFS algorithm. 

It initializes a dictionary distance_from_start to store the distance from v1 to each node visited, and a
list open_list containing the nodes to be visited.
 
It also initializes the distance from v1 to itself as 0, and adds v1 to the open list. It then enters a
loop that continues until open_list is empty.

In each iteration of the loop, the first node current in open_list is removed, and the distance from v1 
to each of its neighbors is calculated and stored in distance_from_start. 

If a neighbor is the target node v2, the function returns the path from v1 to v2. Otherwise, the neighbor
is added to open_list to be visited later.

If the target node v2 is not found, the function returns False.
The code sets the variables from_node and to_node to the values "A" and "ZZZAX", respectively, and then 
calls the path function with the marvelG graph and the two nodes as arguments. 

The resulting shortest path is printed to the console.

"""
def path(G, v1, v2):
    distance_from_start ={}
    open_list =[v1]
    distance_from_start[v1] =[v1]
    # path_from_start[v1] =[v1]
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            if neighbor not in distance_from_start:
                distance_from_start[neighbor] =distance_from_start[current] + [neighbor]
                if neighbor == v2:
                    return distance_from_start[v2]
                open_list.append(neighbor)
    return False
from_node ="A"
to_node="ZZZAX"
print(path(marvelG,from_node,to_node))

"""
code provided in the above won't work with the sample data provided, as the nodes in the CSV 
file are letters, not integers. To make it work with letters, you can modify the code as follows
"""
def make_link(G, node1, node2):
    G[node1] = {}
    G[node1][node2] = 1
    G[node2] = {}
    G[node2][node1] = 1
    return G

def read_graph(filename):
    # reads an undirected graph in csv format. Each line is an edge
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header
        G = {}
        for row in reader:
            node1, node2 = row
            make_link(G, node1, node2)
        return G

# read the graph from the CSV file
G = read_graph('uniq_edges.csv')

# print the graph
print(G)

