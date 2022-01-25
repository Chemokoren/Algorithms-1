"""
Depth First Search

O(v) space - because of the array we return and it is going to have length v, where we would
have a tree with one gigantic branch we would have v frames on the call stack used up

Expected output: [ABEFIJCDGKH]
"""
'''
                         A
                       / | \
                      B  C  D
                    /  \   /  \
                    E   F G   H
                        /\ \
                       I  J k   

'''
# create a tree
class Tree:
    def __init__(self,value) -> None:
        self.value = value
        self.left = None
        self.right = None

    def insertNode(self,data):
        if self.value:
            if data < self.value:
                if self.left is None:
                    self.left =Tree(data)
                else:
                    self.left.insertNode(data)
            if data > self.value:
                if self.right is None:
                    self.right =Tree(data)
                else:
                    self.right.insertNode(data)
        else:
            self.value = Tree(data)

    def printTree(self):
        if self.left:
            return self.left.printTree()
        print(self.value)
        if self.right:
            return self.right.printTree()


class Node:
    def __init__(self,name) -> None:
        self.children =[]
        self.name=name

    def addChild(self, name):
        self.children.append(Node(name))

    # O(v + e) time 
    # O(v) space because of the v frames in the callstack in case of a tree with a long
    # gigantic branch. Also because of the array returned.
    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array


# build tree
# tree = Tree("A")
# tree.insertNode("B")
# tree.insertNode("C")
# tree.insertNode("D")
# tree.insertNode("E")
# tree.insertNode("F")
# tree.insertNode("G")
# tree.insertNode("H")
# tree.insertNode("I")
# tree.insertNode("J")
# tree.printTree()


my_array=[]
sol = Node("A")
sol.addChild("B")
sol.addChild("C")
sol.addChild("D")
sol.addChild("E")
sol.addChild("F")
sol.addChild("G")
sol.addChild("H")
sol.addChild("I")
sol.addChild("J")
print(sol.depthFirstSearch(my_array))
