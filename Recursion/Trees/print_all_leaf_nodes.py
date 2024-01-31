class Node:

    def __init__(self, val, left=None, right=None) -> None:
        self.val  =val
        self.left =left
        self.right = right

def print_leaves(root: Node):
    if not root:
        return
    if not root.left and not root.right:
        print(root.val, end="-->")
        return

    if root.left:
        print_leaves(root.left)
    if root.right:
        print_leaves(root.right)
    

n = Node(100)
n.left=Node(80)
n.right=Node(120)
n.left.left=Node(50)
n.left.right=Node(100)
n.right.left=Node(110)
n.right.right=Node(140)

n.left.left.left=Node(30)
n.left.left.right=Node(60)
n.left.right.left=Node(85)
n.left.right.right=Node(95)
n.right.left.left=Node(108)
n.right.left.right=Node(115)
n.right.right.right=Node(150)

print_leaves(n)