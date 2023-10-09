"""
                                        100
                                    /            \
                                  80               120
                                /     \          /      \   
                              50        90      110       140
                            /    \     /   \       \        \
                           30     60  85   95      115      150

call stack
insertNode(null, 108) # return node 108
insertNode(110, 108)
insertNode(120, 108)
insertNode(100, 108)
"""
class Node:

    def __init__(self, val, left=None, right=None) -> None:
        self.val  =val
        self.left =left
        self.right = right

    def preorder(self, troot):
        if troot:
            print(troot.vl,end="-->")
            self.preorder(troot.val.left)
            self.preorder(troot.val.right)
    
        

class BST:

    def __init__(self) -> None:
        self.root = None
        
    def insert_value_in_bst(self,head, val):
        new_node =Node(val)
        if head is None:
            head = new_node
        else:
            if val > head.val:
                head.right =self.insert_value_in_bst(head.right, val)
            elif val < head.val:
                head.left = self.insert_value_in_bst(head.left, val)
        return head
    
    def preorder(self):
        if self.root:
            print(self.root,end="-->")
            self.preorder(self.root.left)
            self.preorder(self.root.right)

    
bst =BST()
node =Node(1)
node.left=Node(2)
node.right=Node(3)
# bst.insert_value_in_bst(node, 1)
# bst.insert_value_in_bst(node, 2)
# bst.insert_value_in_bst(node, 3)
node.preorder()

