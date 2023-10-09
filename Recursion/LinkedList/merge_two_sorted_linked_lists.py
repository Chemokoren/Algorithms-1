class Node:

    def __init__(self, val, next=None) -> None:
        self.val  = val
        self.next = next

    def set_next(self, node):
        self.next =node

    def get_next(self):
        return self.next

def merge_sorted_lls(A:Node, B: Node):
    if A == None: return B
    if B == None: return A

    if A.val < B.val:
        
        A.next= merge_sorted_lls(A.next, B)
        return A
    else:
        B.next= merge_sorted_lls(A, B.next)
        return B
def print_node(node):
    cur = node
    while cur:
        print(cur.val, end="-->")
        cur = cur.get_next()
    print()

node1 =Node(1)
node2 =Node(8)
node3 =Node(22)
node4 =Node(40)


node1.set_next(node2)
node2.set_next(node3)
node3.set_next(node4)



new_node1 = Node(4)
new_node2 = Node(11)
new_node3 = Node(16)
new_node4 = Node(20)

new_node1.set_next(new_node2)
new_node2.set_next(new_node3)
new_node3.set_next(new_node4)

print_node(merge_sorted_lls(new_node1, node1))
