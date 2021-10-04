"""
Branch Sums 

write a function that takes in the root node of a binary tree and return
a list of all the branch sums in this binary tree.
[15,16,18,10,11]

Branch sum - sum of all the values in a particular branch in the binary tree
Branch - is a path in a binary tree  that starts at the root node and ends in one of the leaf
nodes.
"""

class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.left  = None
        self.right = None
    
    def insert(self,data):
        if self.value:
            if data < self.value:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            if data > self.value:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.value = Node(data)

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.value)
        if self.right:
            self.right.printTree()


# O(n) time | O(n) space
def branchSums(root):
    sums =[]
    recursiveBranchSums(root,0, sums)
    return sums

def recursiveBranchSums(node, runningSum, sums):
    if node is None:
        return

    newRunningSum = runningSum + node.value

    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return

    recursiveBranchSums(node.left, newRunningSum, sums)
    recursiveBranchSums(node.right, newRunningSum, sums)


tree = Node(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.insert(7)
tree.insert(8)
tree.insert(9)
tree.insert(10)
tree.printTree()

my_tree =tree
print("branch sums is: ", branchSums(tree))
    
    

