from Trees.TernarySearchTree.Node import Node
class TST(object):
    def __init__(self):
        self.rootNode =None

    def put(self, key, value):
        self.rootNode =self.putItem(self.rootNode, key, value, 0)

    def putItem(self, node, key, value, index):
        c =key[index]
        if node ==None:
            node =Node(c)

        if c < node.character:
            node.leftNode =self.putItem(node.leftNode,key, value, index)
        elif c >node.character:
            node.rightNode =self.putItem(node.rightNode, key, value, index)
        elif index < len(key) -1:
            node.middleNode =self.putItem(node.middleNode, key, value, index +1)
        else:
            node.value =value
        return node

    def get(self, key):
        node =self.getItem(self.rootNode, key, 0)
        if node ==None:
            return None
        return node.value

    def getItem(self, node, key, index):
        if node == None:
            return None
        c = key[index]
        if c < node.character:
            return self.getItem(node.leftNode, key, index)
        elif c > node.character:
            return self.getItem(node.rightNode, key, index)
        elif index < len(key) -1:
            return self.getItem(node.middleNode, key, index+1)
        else:
            return node
