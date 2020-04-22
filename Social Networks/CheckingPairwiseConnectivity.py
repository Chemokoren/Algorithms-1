def mark_component(G, node, marked):
    marked[node] = True
    total_marked = 1
    for neighbor in G[node]:
        if neighbor not in marked:
            total_marked += mark_component(G, neighbor, marked)
    return total_marked

def check_connection(G, v1, v2):
    marked = {}
    mark_component(G, v1, marked)
    return v2 in marked
