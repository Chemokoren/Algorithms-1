class Node:

    def __init__(self) -> None:
        pass
# Set<Node> visited
def dfs(node: Node, visited: set, goal: int):

    if node == None:
        return False
    
    if node.val == goal:
        return True
    for neighbor in node.getNeighbors():
        if (visited.contains(neighbor)): continue
        visited.add(neighbor)

        isFound = dfs(neighbor, visited, goal)

        if (isFound): return True
    return False
    