# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

# approach 1

def get_next_nodes(edges, cur_node):
    connected_edges = [x for x in edges
                       if cur_node in x]
    if connected_edges:
        a, b = connected_edges[0]
        next_node = b if a == cur_node else a
        edges.remove(connected_edges[0])
        return [cur_node] + get_next_nodes(edges, next_node)
    return []

def take_tour(graph):
    start_node = graph[0][0]
    critical_edges = []
    nodes = []
    for edge in graph:
        if start_node in edge and len(critical_edges) < 2:
            critical_edges.append(edge)
        else:
            nodes.append(edge)

    second_node = critical_edges[0][1]
    stops = [start_node] + get_next_nodes(nodes, second_node)

    a, b = critical_edges[1]
    stops += [a] if b == start_node else [b]
    return stops + [start_node]

# approach -2
def take_tour(graph, node_start=None, cycle_only=True):
    if len(graph) == 0:
        if node_start is None:
            return []
        return [node_start]

    node_start = graph[0][0] if node_start is None else node_start

    for chosen_edge in [x for x in graph if node_start in x]:
        (node_a, node_b) = chosen_edge
        path = take_tour([e for e in graph if e != chosen_edge],
                         node_b if node_start == node_a else node_a,
                         cycle_only=False)
        if path is not False and (not cycle_only or node_start == path[-1]):
            return [node_start] + path
    return False

""" extra work can be done on the correct -approach 2"""
"""
If you are looking for some other simple exercise, here are 2 easy to medium questions that are left open and that could be answered in one go:

how would you modify take_tour to return a list of all possible tour/paths ?
and would you be able to transform take_tour in an iterator of all possible tour/paths ? (a clever iterator that would compute next path only upon request).

"""
