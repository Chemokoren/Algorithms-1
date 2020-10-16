def dfs(node):
    node.visited =True
    print("%s ->" % node.name)

    for n in node.adjacenciesList:
        if not n.visited:
            dfs(n)