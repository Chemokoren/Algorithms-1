class Node:
    def __init__(self,data):
        self.data =data
        self.prev =None
        self.next =None

class BinaryTree:
    def __init__(self):
        self.head =None

    def push(self,new_node):
        # create new node
        latest_node =Node(new_node)
        latest_node.next =self.head

        # check if head is not empty
        if self.head != None:
            # set prev of the new head to None
            self.head.prev =latest_node

        self.head =latest_node

    # append two circular doubly linked lists and return the new list
    def append(self, node_one, node_two):
        if node_one == None:
            return node_two
        if node_two == None:
            return node_one

        a_last_node = node_one.prev
        b_last_node = node_two.prev

        # join the two to make them connected and circular
        self.joinNodes(a_last_node,b_last_node)
        self.joinNodes(b_last_node,a_last_node)

        return a_last_node

    def joinNodes(self, node_one, node_two):
        node_one.next = node_two
        node_two.prev =node_one


    def treeToList(self,root):
        if (root ==None):
            return None
        leftList =self.treeToList(root.prev)
        rightList =self.treeToList(root.next)

        leftList =self.append(leftList,root)
        leftList =self.append(leftList, rightList)
        return leftList

    def printNodes(self,node):
        while(node is not None):
            print(node.data)
            node =node.next


testBinaryToCircular = BinaryTree()

testBinaryToCircular.push(1)
testBinaryToCircular.push(2)
testBinaryToCircular.push(3)
testBinaryToCircular.push(4)
testBinaryToCircular.printNodes(testBinaryToCircular.head)
