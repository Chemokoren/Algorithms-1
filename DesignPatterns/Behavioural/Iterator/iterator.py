"""
defines how values in an objects can be iterated through

In python, just defining an array and iterating through using the in keyword uses the built
in listiterator. This way, we don't even have to index the array.

my_list =[1,2,3]
for n in my_list:
    print(n)
    
For more complex objects like binary search trees,  or linked list, we can define our own.


"""
class ListNode:
    
    def __init__(self, val):
        self.val = val
        self.next = None
        
class LinkedList:
    
    def __init__(self, head):
        self.head = head
        self.cur = None
        
    # Define Iterator
    def __iter__(self):
        self.cur = self.head
        return self
    
    # Iterate
    def __next__(self):
        if self.cur:
            val = self.cur.val
            self.cur = self.cur.next
            return val
        else:
            raise StopIteration
        
# Initialize LinkedList
head = ListNode(1)
head.next = ListNode(2)
head.next.next =ListNode(3)
myList = LinkedList(head)

# Iterate through LinkedList
for n in myList:
    print(n)
