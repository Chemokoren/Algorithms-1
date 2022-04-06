"""
Tree Traversal 
- Breadth First Search
- Depth First Search
    - InOrder
    - PreOrder
    - PostOrder

BFS - Steps(Iteratively)

-create a queue(this can be an array) and a variable to store the values of 
nodes visited
-place the root node in the queue
-loop as long as there is anything in the queue
    - Dequeue a node from the queue and push the value of the node into the variable that
    stores the nodes
    - If there is a left property on the node dequeued - add  it to the queue
    - If there is a right property on the node dequeued -add it to the queue
-Return the variable that stores the values

DFS - InOrder

    -create a variable to store the values of nodes visited
    -store the root of the BST in a variable called current
    -write a helper function which accepts a node
        - if the node has a left property, call the helper function with the left property
        on the node
        -push the value of the to the variable that stores the values
        -if the node has a right property, call the helper function with the right property
        on the node
    -invoke the helper function with the current variable

    Sort items from smallest to the largest -inorder(Notice we get all nodes in the
    tree in their underlying order)

DFS - PostOrder

- Create a variable to store the values of nodes visited
- Store the root of the BST in a variable called current
- Write a helper function which accepts a node
    - If the node has a left property, call the helper function with the left property 
    on the node
    -If the node has a right property, call the helper function with the right property
    on the node
    -Push the value of the node to the variable that stores the values
    - Invoke the helper function with the current variable

DFS - PostOrder   

-Create a variable to store the values of nodes visited
-Store the root of the BST in a variable called current
-Write a helper function which accepts a node 
    - Push the value of the node to the variable that stores the values
    - If the node has a left property, call the helper function with the left property
    on the node
    - If the node has a right property, call the helper function with the right property 
    on the node
-Invoke the helper function with the current variable
-Return the array of values

RECAP
- Trees are non-linear data structures that contain a root and child nodes
- Binary Trees can have values of any type, but at most two children for each parent
- Binary search trees are a more specific version of binary trees where every node
to the left of a parent is less than it's value and every node to the right is greater.


"""

class Node:

    def __init__(self, value) -> None:
        self.value  = value
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self) -> None:
        self.root = None
      
    def insert_node_iterative(self, val):
        n = Node(val)
        if self.root == None:
            self.root=n
            # return
        current = self.root
        while(True):
            if(val == current.value): 
                return False
            
            if n.value > current.value:
                if current.right:
                    current = current.right
                current.right=n
            else:
                if current.left:
                    current = current.left
                current.left=n
    
    def contains(self, val):
        if self.root == None:
            return False
        current = self.root
        found = False
        while(current and not found):
            if val < current.value:
                current = current.left
            elif val > current.value:
                current = current.right
            else:
                return True
        return False


    def bfsUp(self):
        queue =[self.root]
        visited =[]

        while (queue):
            val = queue.pop(0)
            visited.append(val.value)
            
            # if val.left:
            #     queue.append(val.left)

            if val.right:
                queue.append(val.right)

            print("aa:", visited)
        return visited

    def bfs(self):
        queue =[]
        visited =[]

        queue.append(self.root)

        while (len(queue) > 0):
            val = queue.pop(0)
            visited.append(val.value)
            
            if val.left:
                queue.append(val.left)
            if val.right:
                queue.append(val.right)

        return visited

    def DFSPreOrder(self):
        visited =[]
        
        def helper(node):
            visited.append(node.value)
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
        helper(self.root)
        return visited
  
    def DFSInOrderUpdated(self):
        visited =[]
        
        def helper(node):
            if node.left:
                helper(node.left)
            visited.append(node.value)
            if node.right:
                helper(node.right)
        helper(self.root)
        return visited
    
    def DFSPostOrder(self):
        visited =[]
        
        def helper(node):
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
            visited.append(node.value)
        helper(self.root)
        return visited

    def DFSInOrder(self):
        queue =[]
        visited =[]

        node = self.root
        queue.append(node)

        while queue:
            node = queue.pop()

            if node.left:
                queue.append(node.left)
                self.DFSInOrder()
            visited.append(node)
            if node.right:
                queue.append(node.right)
                self.DFSInOrder()

        return visited

    '''
    DFS - PreOrder

    Can be used to "export" a tree structure so that it is easily reconstructed or copied
    - i.e. flatten the tree & recreate it

    '''



#       10
#   5       13

# 2   7  11    16

tree = BinarySearchTree()
tree.insert_node_iterative(10)
tree.insert_node_iterative(5)
tree.insert_node_iterative(13)
tree.insert_node_iterative(2)
tree.insert_node_iterative(7)
tree.insert_node_iterative(11)
tree.insert_node_iterative(16)

print(tree.DFSInOrderUpdated())
# print(tree.contains(16))
