class Node:

    def __init__(self) -> None:
        pass
# Set<Node> visited
def dfs(node: Node, visited: set, goal: int):

    if node == None:
        return False
    
    if node.val == goal:
        return True
    
    