import sys
class Node(object):

    def __init__(self, name):
        self.name =name
        self.visited =False
        self.adjacenciesList =[]
        self.predecessor =None
        self.minDistance =sys.maxsize