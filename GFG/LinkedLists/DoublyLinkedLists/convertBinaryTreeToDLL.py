# program to convert a binary tree to DLL
class Node:
    def __init__(self, data):
        self.data =data
        self.left =self.right =None

class BinaryTree:
    """
    A simple recursive function to convert a given Binary Tree to DLL
    root --> Root of Binary Tree
    head --> Pointer to head node of DLL created
    """

    root, head =None, None

    def BToDll(self, root: Node):
        if root is None:
            return
        # recursively convert right subtree
        self.BToDll(root.right)

        # insert root into DLL
        root.right =self.head

        # change left pointer of previous head
        if self.head is not None:
            self.head.left =root

        # change head of DLL
        self.head =root

        # recursively convert left subtree
        self.BToDll(root.left)

    @staticmethod
    def print_list(head: Node):
        print('Extracted DLL:')
        while head is not None:
            print(head.data, end =' ')
            head =head.right


# Driver program to test above function
if __name__ == '__main__':
    """
    Constructing below tree
            5
        // \\
        3 6
        // \\ \\
        1 4 8
    // \\ // \\
    0 2 7 9
    """
    tree = BinaryTree()
    tree.root = Node(5)
    tree.root.left = Node(3)
    tree.root.right = Node(6)
    tree.root.left.left = Node(1)
    tree.root.left.right = Node(4)
    tree.root.right.right = Node(8)
    tree.root.left.left.left = Node(0)
    tree.root.left.left.right = Node(2)
    tree.root.right.right.left = Node(7)
    tree.root.right.right.right = Node(9)

    tree.BToDll(tree.root)
    tree.print_list(tree.head)
