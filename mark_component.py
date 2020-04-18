# Rewrite `mark_component` to not use recursion
# and instead use the `open_list` data structure
# discussed in lecture
#

#initial mark_component using recursion
# def mark_component(G, node, marked):
#     marked[node] = True
#     total_marked = 1
#     for neighbor in G[node]:
#         if neighbor not in marked:
#             total_marked += mark_component(G, neighbor, marked)
#     return total_marked

# rewritten component not using open_list
"""
Similar to breadth first search, the main difference between DFS and BFS is the order in which nodes are removed from the open list.
"""
def mark_component(G, node, marked):
    open_list = [node]
    total_marked = 1
    marked[node] = True
    while len(open_list) > 0:
        node = open_list.pop()
        for neighbor in G[node]:
            if neighbor not in marked:
                open_list.append(neighbor)
                marked[neighbor] = True
                total_marked += 1
    return total_marked

#########
# Code for testing
#
def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def test():
    test_edges = [(1, 2), (2, 3), (4, 5), (5, 6)]
    G = {}
    for n1, n2 in test_edges:
        make_link(G, n1, n2)
    marked = {}
    assert mark_component(G, 1, marked) == 3
    assert 1 in marked
    assert 2 in marked
    assert 3 in marked
    assert 4 not in marked
    assert 5 not in marked
    assert 6 not in marked

test()
