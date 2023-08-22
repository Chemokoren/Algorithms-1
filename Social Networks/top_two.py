#
# write a function, `top_two` that takes in a graph and a starting
# node and returns two paths, the first and second shortest paths,
# for all the other nodes in the graph.  You can assume that the
# graph is connected.
#

def top_two(graph, start):
    # your code here
    #
    # the result should be a dictionary, containing a mapping between
    # every node in the graph, except the start node, to a list.  The
    # list should contain two elements.  Each element should contain a
    # cost to get to that node and the path followed.  See the `test`
    # function for an example
    #
    pass

def test():
    graph = {'a':{'b':3, 'c':4, 'd':8},
             'b':{'a':3, 'c':1, 'd':2},
             'c':{'a':4, 'b':1, 'd':2},
             'd':{'a':8, 'b':2, 'c':2}}
    result = top_two(graph, 'a') # this is a dictionary
    b = result['b'] # this is a list
    b_first = b[0] # this is a list
    assert b_first[0] == 3 # the cost to get to 'b'
    assert b_first[1] == ['a', 'b'] # the path to 'b'
    b_second = b[1] # this is a list
    assert b_second[0] == 5 # the cost to get to 'b'
    assert b_second[1] == ['a', 'c', 'b']



