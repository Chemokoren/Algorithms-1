from collections import defaultdict

graph = [(1, 2), (2, 3), (3, 1)]
alist = defaultdict(list)
for e in graph:
    alist[e[0]].append(e[1])
    alist[e[1]].append(e[0])  # these edges are bidirectional
    for v in alist:
        print("%d -> %s" % (v, alist[v]))


def adj_list(graph):
    alist = {}
    for i in range(len(graph)):
        if graph[i][0] not in alist:
            alist[graph[i][0]] = [graph[i][1]]
        else:
            alist[graph[i][0]].append(graph[i][1])
        if graph[i][1] not in alist:
            alist[graph[i][1]] = [graph[i][0]]
        else:
            alist[graph[i][1]].append(graph[i][0])
        return alist

print('############################### the results ######################################')
print(adj_list(graph))
