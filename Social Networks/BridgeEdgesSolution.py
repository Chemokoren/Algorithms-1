#
# First some utility functions
#

def make_link(G, node1, node2, r_or_g):
    # modified make_link to apply
    # a color to the edge instead of just 1
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = r_or_g
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = r_or_g
    return G

def get_children(S, root, parent):
    """returns the children from following the
    green edges"""
    return [n for n, e in S[root].items()
            if ((not n == parent) and
                (e == 'green'))]

def get_children_all(S, root, parent):
    """returns the children from following
    green edges and the children from following
    red edges"""
    green = []
    red = []
    for n, e in S[root].items():
        if n == parent:
            continue
        if e == 'green':
            green.append(n)
        if e == 'red':
            red.append(n)
    return green, red

#################

def create_rooted_spanning_tree(G, root):
    # use DFS from the root to add edges and nodes
    # to the tree.  The first time we see a node
    # the edge is green, but after that its red
    open_list = [root]
    S = {root:{}}
    while len(open_list) > 0:
        node = open_list.pop()
        neighbors = G[node]
        for n in neighbors:
            if n not in S:
                # we haven't seen this node, so
                # need to use a green edge to connect
                # it
                make_link(S, node, n, 'green')
                open_list.append(n)
            else:
                # we have seen this node,
                # but, first make sure that
                # don't already have the edge
                # in S
                if node not in S[n]:
                    make_link(S, node, n, 'red')
    return S

##################

def _post_order(S, root, parent, val, po):
    children = get_children(S, root, parent)
    for c in children:
        val = _post_order(S, c, root, val, po)
    po[root] = val
    return val + 1

def post_order(S, root):
    po = {}
    _post_order(S, root, None, 1, po)
    return po


##################

def _number_descendants(S, root, parent, nd):
    # number of descendants is the
    # sum of the number of descendants of a nodes
    # children plus one
    children = get_children(S, root, parent)
    nd_val = 1
    for c in children:
        # recursively calculate the number of descendants
        # for the children
        nd_val += _number_descendants(S, c, root, nd)
    nd[root] = nd_val
    return nd_val

def number_of_descendants(S, root):
    nd = {}
    _number_descendants(S, root, None, nd)
    return nd


#
# Since highest and lowest post order will follow
# a similar method, I only wrote one method
# that can be used for both
#
def _general_post_order(S, root, parent, po, gpo, comp):
    green, red = get_children_all(S, root, parent)
    val = po[root]
    for c in green:
        # recursively find the low/high post order value of the children
        test = _general_post_order(S, c, root, po, gpo, comp)
        # and save the low/highest one
        if comp(val, test):
            val = test
    for c in red:
        test = po[c]
        # and also look at the direct children
        # from following red edges
        # and save the low/highest one if needed
        if comp(val, test):
            val = test
    gpo[root] = val
    return val

def lowest_post_order(S, root, po):
    lpo = {}
    _general_post_order(S, root, None, po, lpo, lambda x, y: x > y)
    return lpo

def highest_post_order(S, root, po):
    hpo = {}
    _general_post_order(S, root, None, po, hpo, lambda x, y: x < y)
    return hpo

#
# Now put everything together
#

def bridge_edges(G, root):
    S = create_rooted_spanning_tree(G, root)
    po = post_order(S, root)
    nd = number_of_descendants(S, root)
    lpo = lowest_post_order(S, root, po)
    hpo = highest_post_order(S, root, po)
    bridges = []
    open_list = [(root, None)]
    # walk down the tree and see which edges are
    # tree edges
    while len(open_list) > 0:
        node, parent = open_list.pop()
        for child in get_children(S, node, parent):
            # all of these edges are automatically green (get_children only
            # follows green edges)
            # so only need to check the other two conditions
            if hpo[child] <= po[child] and lpo[child] > (po[child] - nd[child]):
                bridges.append((node, child))
            open_list.append((child, node))
    return bridges
