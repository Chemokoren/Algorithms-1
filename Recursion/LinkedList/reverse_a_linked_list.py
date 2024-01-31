"""

"""
class Node:
    def __init__(self, val, next=None) -> None: #node: Node
        self.val =val
        self.next =next

    def set_next(self, node): # node: Node
        self.next = node

    def get_next(self):
        return self.next

def reverseList(head: Node)->Node:
    if (head == None) or (head.next == None):
        return head
    p= reverseList(head.next)
    head.next.next =head
    head.next = None
    return p

def print_node(node:Node):

    cur = node
    while cur:
        print(cur.val, end="-->")
        cur = cur.get_next()
    print()

node1 =Node(1)
node2 =Node(2)
node3 =Node(3)
node4 =Node(4)
node5 =Node(5)

node1.set_next(node2)
node2.set_next(node3)
node3.set_next(node4)
node4.set_next(node5)

# before reversing
print_node(node1)

# after reversing
print_node(reverseList(node1))